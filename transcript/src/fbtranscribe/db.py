from __future__ import annotations

import hashlib
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import psycopg
from psycopg.rows import dict_row

from fbtranscribe.config import get_settings


@contextmanager
def get_connection():
    settings = get_settings()
    conn = psycopg.connect(settings.database_url, row_factory=dict_row)
    try:
        yield conn
    finally:
        conn.close()


def normalize_url(url: str) -> str:
    parsed = urlparse(url.strip())
    query = [(key, value) for key, value in parse_qsl(parsed.query, keep_blank_values=True) if not key.lower().startswith("utm_")]
    normalized_path = parsed.path.rstrip("/") or "/"
    normalized = parsed._replace(
        scheme=parsed.scheme.lower(),
        netloc=parsed.netloc.lower(),
        path=normalized_path,
        params="",
        query=urlencode(query),
        fragment="",
    )
    return urlunparse(normalized)


def detect_platform(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if "facebook.com" in host or "fb.watch" in host:
        return "facebook"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    if "vimeo.com" in host:
        return "vimeo"
    return host or "unknown"


def file_input_key(path: str) -> str:
    return f"file://{Path(path).expanduser().resolve()}"


def build_dedupe_key(
    *,
    source_key: str,
    language: str,
    model: str,
    backend: str,
    segment_minutes: int,
) -> str:
    raw = "|".join([source_key, language, model, backend, str(segment_minutes)])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
