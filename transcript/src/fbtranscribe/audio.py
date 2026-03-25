from __future__ import annotations

import subprocess
from pathlib import Path


def chunk_audio_from_video(
    *,
    video_path: Path,
    chunks_dir: Path,
    segment_seconds: int,
    sample_rate: int = 16000,
) -> list[Path]:
    """Create fixed-length audio chunks from a video using ffmpeg.

    Produces mono WAV chunks suitable for speech-to-text.
    If chunks already exist, returns them (resume-friendly).
    """

    video_path = video_path.expanduser().resolve()
    if not video_path.exists():
        raise FileNotFoundError(video_path)

    chunks_dir = chunks_dir.expanduser().resolve()
    chunks_dir.mkdir(parents=True, exist_ok=True)

    existing = sorted(chunks_dir.glob("chunk_*.wav"))
    if existing:
        return existing

    out_pattern = chunks_dir / "chunk_%03d.wav"

    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-y",
        "-i",
        str(video_path),
        "-vn",
        "-ac",
        "1",
        "-ar",
        str(sample_rate),
        "-f",
        "segment",
        "-segment_time",
        str(segment_seconds),
        "-reset_timestamps",
        "1",
        str(out_pattern),
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            "ffmpeg failed while chunking audio.\n"
            f"Command: {' '.join(cmd)}\n\n"
            f"STDERR:\n{proc.stderr}"
        )

    chunks = sorted(chunks_dir.glob("chunk_*.wav"))
    if not chunks:
        raise RuntimeError("No chunks were produced; check input video and ffmpeg output.")
    return chunks
