from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    return int(value) if value else default


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


def get_settings() -> Settings:
    return Settings()
