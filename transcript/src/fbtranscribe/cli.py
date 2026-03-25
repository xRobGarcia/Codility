from __future__ import annotations

import argparse
from pathlib import Path

from fbtranscribe.pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="fbtranscribe",
        description="Download (optional), chunk audio, and transcribe long videos with resume support.",
    )

    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="Video URL (Facebook share link or direct).")
    src.add_argument("--input-video", type=Path, help="Path to an already-downloaded video file.")

    p.add_argument("--out-dir", type=Path, default=Path("out"), help="Output directory.")
    p.add_argument(
        "--cookies",
        type=Path,
        default=None,
        help="Path to a Netscape cookies.txt file for yt-dlp (often required for Facebook).",
    )
    p.add_argument("--language", default="es", help="Language code (e.g. es, en).")
    p.add_argument(
        "--segment-minutes",
        type=int,
        default=30,
        help="Chunk length in minutes (default: 30).",
    )

    p.add_argument(
        "--backend",
        choices=["faster-whisper", "whisper.cpp"],
        default="faster-whisper",
        help="Transcription backend.",
    )

    p.add_argument(
        "--model",
        default="small",
        help="Model size/name for the backend (e.g. tiny/base/small/medium/large-v3).",
    )

    p.add_argument(
        "--device",
        default="cpu",
        help="faster-whisper device (cpu/cuda). Ignored for whisper.cpp.",
    )

    p.add_argument(
        "--compute-type",
        default="int8",
        help="faster-whisper compute type (int8/float16/float32).",
    )

    p.add_argument(
        "--whisper-cpp-bin",
        type=Path,
        default=None,
        help="Path to whisper.cpp binary (e.g. ./whisper.cpp/main).",
    )
    p.add_argument(
        "--whisper-cpp-model",
        type=Path,
        default=None,
        help="Path to whisper.cpp model (e.g. ./whisper.cpp/models/ggml-base.bin).",
    )

    p.add_argument(
        "--keep-video",
        action="store_true",
        help="If downloading, keep the original video file (default: keep).",
    )

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    run_pipeline(
        url=args.url,
        input_video=args.input_video,
        out_dir=args.out_dir,
        cookies=args.cookies,
        language=args.language,
        segment_seconds=args.segment_minutes * 60,
        backend=args.backend,
        model=args.model,
        device=args.device,
        compute_type=args.compute_type,
        whisper_cpp_bin=args.whisper_cpp_bin,
        whisper_cpp_model=args.whisper_cpp_model,
        keep_video=args.keep_video,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
