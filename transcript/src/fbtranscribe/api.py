from __future__ import annotations

import uuid
from datetime import datetime
from uuid import UUID
from pathlib import Path

import psycopg
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, model_validator

from fbtranscribe.config import get_settings
from fbtranscribe.db import (
    build_dedupe_key,
    detect_platform,
    file_input_key,
    get_connection,
    normalize_url,
)

app = FastAPI(title="fbtranscribe API", version="0.1.0")


class JobCreateRequest(BaseModel):
    url: str | None = None
    input_video_path: str | None = None
    cookies_path: str | None = None
    language: str = "es"
    model: str = "small"
    backend: str = Field(default="faster-whisper", pattern="^(faster-whisper|whisper.cpp)$")
    segment_minutes: int = Field(default=30, ge=1, le=120)
    device: str = "cpu"
    compute_type: str = "int8"

    @model_validator(mode="after")
    def validate_source(self) -> "JobCreateRequest":
        if bool(self.url) == bool(self.input_video_path):
            raise ValueError("Provide exactly one of url or input_video_path.")
        return self


class JobResponse(BaseModel):
    id: UUID
    status: str
    dedupe_key: str
    requested_count: int
    requested_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None
    progress: float
    out_dir: str | None = None
    error_message: str | None = None
    source_url: str | None = None
    input_video_path: str | None = None
    transcript_txt_path: str | None = None
    transcript_srt_path: str | None = None


class JobArtifactsResponse(BaseModel):
    job_id: UUID
    out_dir: str
    transcript_txt_path: str | None = None
    transcript_srt_path: str | None = None
    transcript_clean_path: str | None = None
    summary_json_path: str | None = None
    chunks_dir: str | None = None
    state_dir: str | None = None
    object_prefix: str | None = None
    object_uris: dict[str, str] = Field(default_factory=dict)


def _upsert_video_source(cur: psycopg.Cursor, request: JobCreateRequest) -> tuple[str, str, str]:
    if request.url:
        normalized_url = normalize_url(request.url)
        platform = detect_platform(normalized_url)
        cur.execute(
            """
            insert into video_source (platform, original_url, normalized_url)
            values (%s, %s, %s)
            on conflict (normalized_url)
            do update set original_url = excluded.original_url
            returning id, normalized_url
            """,
            (platform, request.url, normalized_url),
        )
        row = cur.fetchone()
        assert row is not None
        return row["id"], normalized_url, request.url

    source_key = file_input_key(request.input_video_path or "")
    cur.execute(
        """
        insert into video_source (platform, original_url, normalized_url)
        values (%s, %s, %s)
        on conflict (normalized_url)
        do update set original_url = excluded.original_url
        returning id, normalized_url
        """,
        ("local-file", request.input_video_path, source_key),
    )
    row = cur.fetchone()
    assert row is not None
    return row["id"], source_key, request.input_video_path or ""


def _job_with_asset(cur: psycopg.Cursor, job_id: str) -> dict | None:
    cur.execute(
        """
        select
            j.id,
            j.status,
            j.dedupe_key,
            j.requested_count,
            j.requested_at,
            j.started_at,
            j.finished_at,
            j.progress,
            j.out_dir,
            j.error_message,
            j.source_url,
            j.input_video_path,
            a.txt_path as transcript_txt_path,
            a.srt_path as transcript_srt_path
        from transcription_job j
        left join transcript_asset a on a.job_id = j.id
        where j.id = %s
        """,
        (job_id,),
    )
    return cur.fetchone()


def _artifact_path(path: Path) -> str | None:
    return str(path) if path.exists() else None


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/jobs", response_model=JobResponse)
def create_job(request: JobCreateRequest) -> JobResponse:
    with get_connection() as conn:
        with conn.transaction():
            with conn.cursor() as cur:
                video_source_id, source_key, source_value = _upsert_video_source(cur, request)
                dedupe_key = build_dedupe_key(
                    source_key=source_key,
                    language=request.language,
                    model=request.model,
                    backend=request.backend,
                    segment_minutes=request.segment_minutes,
                )

                cur.execute(
                    "select id from transcription_job where dedupe_key = %s",
                    (dedupe_key,),
                )
                existing = cur.fetchone()
                if existing:
                    cur.execute(
                        "update transcription_job set requested_count = requested_count + 1 where id = %s",
                        (existing["id"],),
                    )
                    cur.execute(
                        "insert into request_log (job_id) values (%s)",
                        (existing["id"],),
                    )
                    row = _job_with_asset(cur, existing["id"])
                    assert row is not None
                    return JobResponse(**row)

                job_id = str(uuid.uuid4())
                settings = get_settings()
                out_dir = str((settings.jobs_root / job_id).resolve())
                cur.execute(
                    """
                    insert into transcription_job (
                        id,
                        video_source_id,
                        source_url,
                        input_video_path,
                        cookies_path,
                        language,
                        model,
                        backend,
                        segment_minutes,
                        device,
                        compute_type,
                        dedupe_key,
                        status,
                        out_dir
                    ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'pending', %s)
                    """,
                    (
                        job_id,
                        video_source_id,
                        request.url,
                        request.input_video_path,
                        request.cookies_path,
                        request.language,
                        request.model,
                        request.backend,
                        request.segment_minutes,
                        request.device,
                        request.compute_type,
                        dedupe_key,
                        out_dir,
                    ),
                )
                cur.execute("insert into request_log (job_id) values (%s)", (job_id,))
                row = _job_with_asset(cur, job_id)
                assert row is not None
                return JobResponse(**row)


@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: str) -> JobResponse:
    with get_connection() as conn:
        with conn.cursor() as cur:
            row = _job_with_asset(cur, job_id)
            if row is None:
                raise HTTPException(status_code=404, detail="Job not found")
            return JobResponse(**row)


@app.get("/jobs/{job_id}/artifacts", response_model=JobArtifactsResponse)
def get_job_artifacts(job_id: str) -> JobArtifactsResponse:
    settings = get_settings()
    with get_connection() as conn:
        with conn.cursor() as cur:
            row = _job_with_asset(cur, job_id)
            if row is None:
                raise HTTPException(status_code=404, detail="Job not found")

            out_dir = Path(row["out_dir"])
            clean_path = out_dir / "transcript.final.txt"
            if not clean_path.exists():
                clean_path = out_dir / "transcript.cleaned.txt"

            object_uris: dict[str, str] = {}
            if settings.object_storage_enabled:
                if (out_dir / "transcript.txt").exists():
                    object_uris["transcript.txt"] = f"s3://{settings.s3_bucket}/jobs/{row['id']}/transcript.txt"
                if (out_dir / "transcript.srt").exists():
                    object_uris["transcript.srt"] = f"s3://{settings.s3_bucket}/jobs/{row['id']}/transcript.srt"
                if clean_path.exists():
                    object_uris[clean_path.name] = f"s3://{settings.s3_bucket}/jobs/{row['id']}/{clean_path.name}"
                if (out_dir / "summary.json").exists():
                    object_uris["summary.json"] = f"s3://{settings.s3_bucket}/jobs/{row['id']}/summary.json"

            return JobArtifactsResponse(
                job_id=row["id"],
                out_dir=str(out_dir),
                transcript_txt_path=_artifact_path(out_dir / "transcript.txt"),
                transcript_srt_path=_artifact_path(out_dir / "transcript.srt"),
                transcript_clean_path=_artifact_path(clean_path),
                summary_json_path=_artifact_path(out_dir / "summary.json"),
                chunks_dir=_artifact_path(out_dir / "chunks"),
                state_dir=_artifact_path(out_dir / "state"),
                object_prefix=(f"s3://{settings.s3_bucket}/jobs/{row['id']}" if settings.object_storage_enabled else None),
                object_uris=object_uris,
            )


@app.get("/jobs")
def list_jobs(limit: int = 20) -> list[JobResponse]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select
                    j.id,
                    j.status,
                    j.dedupe_key,
                    j.requested_count,
                    j.requested_at,
                    j.started_at,
                    j.finished_at,
                    j.progress,
                    j.out_dir,
                    j.error_message,
                    j.source_url,
                    j.input_video_path,
                    a.txt_path as transcript_txt_path,
                    a.srt_path as transcript_srt_path
                from transcription_job j
                left join transcript_asset a on a.job_id = j.id
                order by j.requested_at desc
                limit %s
                """,
                (limit,),
            )
            return [JobResponse(**row) for row in cur.fetchall()]


def main() -> int:
    settings = get_settings()
    uvicorn.run("fbtranscribe.api:app", host=settings.api_host, port=settings.api_port, reload=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())