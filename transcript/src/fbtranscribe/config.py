from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    return int(value) if value else default


def _bool_env(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://transcript_user:transcript_pass@localhost:5432/transcript_db",
    )
    jobs_root: Path = Path(os.getenv("JOBS_ROOT", "./data/jobs")).expanduser()
    worker_poll_seconds: int = _int_env("WORKER_POLL_SECONDS", 5)
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = _int_env("API_PORT", 8000)
    object_storage_enabled: bool = _bool_env("OBJECT_STORAGE_ENABLED", True)
    s3_endpoint: str = os.getenv("S3_ENDPOINT", "minio:9000")
    s3_access_key: str = os.getenv("S3_ACCESS_KEY", "minio")
    s3_secret_key: str = os.getenv("S3_SECRET_KEY", "minio12345")
    s3_bucket: str = os.getenv("S3_BUCKET", "transcripts")
    s3_secure: bool = _bool_env("S3_SECURE", False)


def get_settings() -> Settings:
    return Settings()
