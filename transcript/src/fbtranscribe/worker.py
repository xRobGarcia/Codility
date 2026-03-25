from __future__ import annotations

import json
import logging
import time
from pathlib import Path

from fbtranscribe.config import get_settings
from fbtranscribe.db import get_connection
from fbtranscribe.pipeline import run_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger("fbtranscribe.worker")


def _fetch_next_job() -> dict | None:
    with get_connection() as conn:
        with conn.transaction():
            with conn.cursor() as cur:
                cur.execute(
                    """
                    with next_job as (
                        select id
                        from transcription_job
                        where status = 'pending'
                        order by requested_at asc
                        limit 1
                        for update skip locked
                    )
                    update transcription_job j
                    set status = 'processing',
                        progress = 5,
                        started_at = now(),
                        error_message = null
                    from next_job
                    where j.id = next_job.id
                    returning j.*
                    """
                )
                return cur.fetchone()


def _upsert_asset(job: dict) -> None:
    out_dir = Path(job["out_dir"])
    txt_path = out_dir / "transcript.txt"
    clean_path = out_dir / "transcript.final.txt"
    if not clean_path.exists():
        clean_path = out_dir / "transcript.cleaned.txt"
    srt_path = out_dir / "transcript.srt"
    summary_path = out_dir / "summary.json"

    transcript_text = txt_path.read_text(encoding="utf-8") if txt_path.exists() else None
    clean_text = clean_path.read_text(encoding="utf-8") if clean_path.exists() else None
    summary_json = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {}

    with get_connection() as conn:
        with conn.transaction():
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into transcript_asset (
                        job_id,
                        video_source_id,
                        language,
                        model,
                        backend,
                        transcript_text,
                        transcript_clean_text,
                        txt_path,
                        srt_path,
                        summary_json
                    ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb)
                    on conflict (job_id)
                    do update set
                        transcript_text = excluded.transcript_text,
                        transcript_clean_text = excluded.transcript_clean_text,
                        txt_path = excluded.txt_path,
                        srt_path = excluded.srt_path,
                        summary_json = excluded.summary_json,
                        updated_at = now()
                    """,
                    (
                        job["id"],
                        job["video_source_id"],
                        job["language"],
                        job["model"],
                        job["backend"],
                        transcript_text,
                        clean_text,
                        str(txt_path) if txt_path.exists() else None,
                        str(srt_path) if srt_path.exists() else None,
                        json.dumps(summary_json, ensure_ascii=False),
                    ),
                )
                cur.execute(
                    """
                    update transcription_job
                    set status = 'completed',
                        progress = 100,
                        finished_at = now()
                    where id = %s
                    """,
                    (job["id"],),
                )


def _mark_failed(job_id: str, message: str) -> None:
    with get_connection() as conn:
        with conn.transaction():
            with conn.cursor() as cur:
                cur.execute(
                    """
                    update transcription_job
                    set status = 'failed',
                        error_message = %s,
                        finished_at = now()
                    where id = %s
                    """,
                    (message[:4000], job_id),
                )


def process_job(job: dict) -> None:
    LOGGER.info("processing job=%s", job["id"])
    out_dir = Path(job["out_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    input_video = Path(job["input_video_path"]).expanduser() if job["input_video_path"] else None
    cookies = Path(job["cookies_path"]).expanduser() if job["cookies_path"] else None

    run_pipeline(
        url=job["source_url"],
        input_video=input_video,
        out_dir=out_dir,
        cookies=cookies,
        language=job["language"],
        segment_seconds=int(job["segment_minutes"]) * 60,
        backend=job["backend"],
        model=job["model"],
        device=job["device"],
        compute_type=job["compute_type"],
        whisper_cpp_bin=None,
        whisper_cpp_model=None,
        keep_video=True,
    )

    _upsert_asset(job)
    LOGGER.info("completed job=%s", job["id"])


def main() -> int:
    settings = get_settings()
    settings.jobs_root.mkdir(parents=True, exist_ok=True)
    LOGGER.info("worker started poll=%ss jobs_root=%s", settings.worker_poll_seconds, settings.jobs_root)

    while True:
        job = _fetch_next_job()
        if job is None:
            time.sleep(settings.worker_poll_seconds)
            continue

        try:
            process_job(job)
        except Exception as exc:
            LOGGER.exception("job failed job=%s", job["id"])
            _mark_failed(job["id"], str(exc))


if __name__ == "__main__":
    raise SystemExit(main())