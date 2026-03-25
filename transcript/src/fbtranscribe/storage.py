from __future__ import annotations

from pathlib import Path

from fbtranscribe.config import Settings, get_settings


def object_name_for_job(job_id: str, file_name: str) -> str:
    return f"jobs/{job_id}/{file_name}"


def object_uri(bucket: str, object_name: str) -> str:
    return f"s3://{bucket}/{object_name}"


def upload_job_artifacts(job_id: str, out_dir: Path, settings: Settings | None = None) -> dict[str, str]:
    settings = settings or get_settings()
    if not settings.object_storage_enabled:
        return {}

    try:
        from minio import Minio
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("minio dependency is required for object storage uploads") from exc

    client = Minio(
        settings.s3_endpoint,
        access_key=settings.s3_access_key,
        secret_key=settings.s3_secret_key,
        secure=settings.s3_secure,
    )

    if not client.bucket_exists(settings.s3_bucket):
        client.make_bucket(settings.s3_bucket)

    uploaded: dict[str, str] = {}
    candidates = [
        out_dir / "transcript.txt",
        out_dir / "transcript.srt",
        out_dir / "transcript.cleaned.txt",
        out_dir / "transcript.final.txt",
        out_dir / "summary.json",
    ]

    for path in candidates:
        if not path.exists() or not path.is_file():
            continue
        object_name = object_name_for_job(job_id, path.name)
        client.fput_object(settings.s3_bucket, object_name, str(path))
        uploaded[path.name] = object_uri(settings.s3_bucket, object_name)

    return uploaded