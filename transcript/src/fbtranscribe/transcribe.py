from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BackendConfig:
    backend: str  # faster-whisper | whisper.cpp
    model: str
    language: str
    device: str
    compute_type: str
    whisper_cpp_bin: Path | None = None
    whisper_cpp_model: Path | None = None


@dataclass(frozen=True)
class Segment:
    text: str
    start: float | None = None
    end: float | None = None


def transcribe_chunks(
    *,
    chunks: list[Path],
    segment_seconds: int,
    state_dir: Path,
    cfg: BackendConfig,
) -> list[Segment]:
    state_dir.mkdir(parents=True, exist_ok=True)

    if cfg.backend == "faster-whisper":
        return _transcribe_faster_whisper(
            chunks=chunks,
            segment_seconds=segment_seconds,
            state_dir=state_dir,
            cfg=cfg,
        )

    if cfg.backend == "whisper.cpp":
        return _transcribe_whisper_cpp(
            chunks=chunks,
            segment_seconds=segment_seconds,
            state_dir=state_dir,
            cfg=cfg,
        )

    raise ValueError(f"Unknown backend: {cfg.backend}")


def _chunk_state_path(state_dir: Path, chunk: Path) -> Path:
    return state_dir / (chunk.stem + ".json")


def _transcribe_faster_whisper(
    *,
    chunks: list[Path],
    segment_seconds: int,
    state_dir: Path,
    cfg: BackendConfig,
) -> list[Segment]:
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "Backend faster-whisper no está instalado o no es compatible con tu Python. "
            "Prueba: pip install -e '.[faster-whisper]' (si hay wheels), "
            "o usa --backend whisper.cpp."
        ) from e

    model = WhisperModel(cfg.model, device=cfg.device, compute_type=cfg.compute_type)

    all_segments: list[Segment] = []

    for idx, chunk in enumerate(chunks):
        state_path = _chunk_state_path(state_dir, chunk)
        if state_path.exists():
            data = json.loads(state_path.read_text(encoding="utf-8"))
            for s in data.get("segments", []):
                all_segments.append(
                    Segment(text=s["text"], start=s.get("start"), end=s.get("end"))
                )
            continue

        offset = idx * segment_seconds
        segs_for_chunk: list[dict] = []

        segments, _info = model.transcribe(
            str(chunk),
            language=cfg.language or None,
            vad_filter=True,
        )

        for s in segments:
            start = float(s.start) + offset
            end = float(s.end) + offset
            text = (s.text or "").strip()
            if not text:
                continue
            all_segments.append(Segment(text=text, start=start, end=end))
            segs_for_chunk.append({"text": text, "start": start, "end": end})

        state_path.write_text(
            json.dumps({"chunk": str(chunk), "segments": segs_for_chunk}, ensure_ascii=False)
            + "\n",
            encoding="utf-8",
        )

    return all_segments


def _transcribe_whisper_cpp(
    *,
    chunks: list[Path],
    segment_seconds: int,
    state_dir: Path,
    cfg: BackendConfig,
) -> list[Segment]:
    if cfg.whisper_cpp_bin is None or cfg.whisper_cpp_model is None:
        raise RuntimeError(
            "Para usar whisper.cpp debes pasar --whisper-cpp-bin y --whisper-cpp-model."
        )

    bin_path = cfg.whisper_cpp_bin.expanduser().resolve()
    model_path = cfg.whisper_cpp_model.expanduser().resolve()
    if not bin_path.exists():
        raise FileNotFoundError(bin_path)
    if not model_path.exists():
        raise FileNotFoundError(model_path)

    all_segments: list[Segment] = []

    for idx, chunk in enumerate(chunks):
        state_path = _chunk_state_path(state_dir, chunk)
        if state_path.exists():
            data = json.loads(state_path.read_text(encoding="utf-8"))
            for s in data.get("segments", []):
                all_segments.append(
                    Segment(text=s["text"], start=s.get("start"), end=s.get("end"))
                )
            continue

        offset = idx * segment_seconds
        out_prefix = state_dir / chunk.stem

        # We ask whisper.cpp to emit SRT and TXT; then we parse SRT lines and shift timestamps.
        cmd = [
            str(bin_path),
            "-m",
            str(model_path),
            "-f",
            str(chunk),
            "-l",
            cfg.language,
            "-osrt",
            "-otxt",
            "-of",
            str(out_prefix),
        ]

        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise RuntimeError(
                "whisper.cpp failed.\n"
                f"Command: {' '.join(cmd)}\n\n"
                f"STDERR:\n{proc.stderr}"
            )

        srt_path = Path(str(out_prefix) + ".srt")
        txt_path = Path(str(out_prefix) + ".txt")

        segs_for_chunk: list[dict] = []

        if srt_path.exists():
            segs = _parse_srt_segments(srt_path)
            for s in segs:
                start = (s.start or 0.0) + offset
                end = (s.end or 0.0) + offset
                text = s.text.strip()
                if not text:
                    continue
                all_segments.append(Segment(text=text, start=start, end=end))
                segs_for_chunk.append({"text": text, "start": start, "end": end})
        elif txt_path.exists():
            text = txt_path.read_text(encoding="utf-8").strip()
            if text:
                all_segments.append(Segment(text=text))
                segs_for_chunk.append({"text": text})
        else:
            raise RuntimeError(
                f"whisper.cpp did not produce {srt_path.name} nor {txt_path.name}."
            )

        state_path.write_text(
            json.dumps({"chunk": str(chunk), "segments": segs_for_chunk}, ensure_ascii=False)
            + "\n",
            encoding="utf-8",
        )

    return all_segments


def _parse_srt_segments(path: Path) -> list[Segment]:
    """Minimal SRT parser: returns one Segment per cue."""

    lines = path.read_text(encoding="utf-8").splitlines()
    segments: list[Segment] = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        # cue index
        if line.isdigit():
            i += 1
            if i >= len(lines):
                break
            time_line = lines[i].strip()
        else:
            time_line = line

        if "-->" not in time_line:
            i += 1
            continue

        start_s, end_s = [p.strip() for p in time_line.split("-->", 1)]
        start = _parse_srt_timestamp(start_s)
        end = _parse_srt_timestamp(end_s)

        i += 1
        text_lines: list[str] = []
        while i < len(lines) and lines[i].strip():
            text_lines.append(lines[i].strip())
            i += 1

        text = " ".join(text_lines).strip()
        segments.append(Segment(text=text, start=start, end=end))

        i += 1

    return segments


def _parse_srt_timestamp(ts: str) -> float:
    # Format: HH:MM:SS,mmm
    hhmm, ms = ts.split(",", 1)
    hh, mm, ss = hhmm.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss) + int(ms) / 1000.0
