from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from fbtranscribe.audio import chunk_audio_from_video
from fbtranscribe.downloader import download_video
from fbtranscribe.transcribe import (
    BackendConfig,
    Segment,
    transcribe_chunks,
)
from fbtranscribe.writer import write_srt, write_text


@dataclass(frozen=True)
class PipelinePaths:
    out_dir: Path
    video_path: Path
    chunks_dir: Path
    state_dir: Path
    transcript_txt: Path
    transcript_srt: Path


def _paths(out_dir: Path) -> PipelinePaths:
    out_dir = out_dir.resolve()
    return PipelinePaths(
        out_dir=out_dir,
        video_path=out_dir / "input_video.mp4",
        chunks_dir=out_dir / "chunks",
        state_dir=out_dir / "state",
        transcript_txt=out_dir / "transcript.txt",
        transcript_srt=out_dir / "transcript.srt",
    )


def run_pipeline(
    *,
    url: str | None,
    input_video: Path | None,
    out_dir: Path,
    cookies: Path | None,
    language: str,
    segment_seconds: int,
    backend: str,
    model: str,
    device: str,
    compute_type: str,
    whisper_cpp_bin: Path | None,
    whisper_cpp_model: Path | None,
    keep_video: bool,
) -> None:
    paths = _paths(out_dir)
    paths.out_dir.mkdir(parents=True, exist_ok=True)
    paths.chunks_dir.mkdir(parents=True, exist_ok=True)
    paths.state_dir.mkdir(parents=True, exist_ok=True)

    if input_video is None:
        assert url is not None
        video_path = download_video(url=url, out_path=paths.video_path, cookies=cookies)
    else:
        video_path = input_video.expanduser().resolve()
        if not video_path.exists():
            raise FileNotFoundError(video_path)

    chunks = chunk_audio_from_video(
        video_path=video_path,
        chunks_dir=paths.chunks_dir,
        segment_seconds=segment_seconds,
    )

    backend_cfg = BackendConfig(
        backend=backend,
        model=model,
        language=language,
        device=device,
        compute_type=compute_type,
        whisper_cpp_bin=whisper_cpp_bin,
        whisper_cpp_model=whisper_cpp_model,
    )

    segments: list[Segment] = transcribe_chunks(
        chunks=chunks,
        segment_seconds=segment_seconds,
        state_dir=paths.state_dir,
        cfg=backend_cfg,
    )

    write_text(segments=segments, out_path=paths.transcript_txt)
    if any(s.start is not None and s.end is not None for s in segments):
        write_srt(segments=segments, out_path=paths.transcript_srt)

    summary = {
        "backend": backend,
        "model": model,
        "language": language,
        "chunks": len(chunks),
        "segments": len(segments),
        "transcript_txt": str(paths.transcript_txt),
        "transcript_srt": str(paths.transcript_srt) if paths.transcript_srt.exists() else None,
    }
    (paths.out_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    if input_video is None and not keep_video:
        try:
            paths.video_path.unlink(missing_ok=True)
        except OSError:
            pass
