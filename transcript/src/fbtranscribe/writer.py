from __future__ import annotations

from pathlib import Path

from fbtranscribe.transcribe import Segment


def write_text(*, segments: list[Segment], out_path: Path) -> None:
    out_path = out_path.expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    parts: list[str] = []
    for s in segments:
        txt = (s.text or "").strip()
        if txt:
            parts.append(txt)

    out_path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def write_srt(*, segments: list[Segment], out_path: Path) -> None:
    out_path = out_path.expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    cues = [s for s in segments if s.start is not None and s.end is not None]
    cues.sort(key=lambda s: (s.start or 0.0, s.end or 0.0))

    lines: list[str] = []
    idx = 1
    for s in cues:
        text = (s.text or "").strip()
        if not text:
            continue
        start = _format_srt_timestamp(float(s.start))
        end = _format_srt_timestamp(float(s.end))
        lines.append(str(idx))
        lines.append(f"{start} --> {end}")
        lines.append(text)
        lines.append("")
        idx += 1

    out_path.write_text("\n".join(lines), encoding="utf-8")


def _format_srt_timestamp(seconds: float) -> str:
    if seconds < 0:
        seconds = 0

    hh = int(seconds // 3600)
    seconds -= hh * 3600
    mm = int(seconds // 60)
    seconds -= mm * 60
    ss = int(seconds)
    ms = int(round((seconds - ss) * 1000))

    if ms >= 1000:
        ss += 1
        ms -= 1000
    if ss >= 60:
        mm += 1
        ss -= 60
    if mm >= 60:
        hh += 1
        mm -= 60

    return f"{hh:02d}:{mm:02d}:{ss:02d},{ms:03d}"
