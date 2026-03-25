from __future__ import annotations

from pathlib import Path

def download_video(*, url: str, out_path: Path, cookies: Path | None = None) -> Path:
    """Download a video using yt-dlp.

    Notes:
    - Facebook often requires cookies or a logged-in session.
    - If download fails, try exporting cookies from your browser and pass them via yt-dlp.
      (This project intentionally keeps the flow simple and does not manage cookies itself.)
    """

    out_path = out_path.expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from yt_dlp import YoutubeDL  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "yt-dlp is required. Install with: pip install -e ."
        ) from e

    ydl_opts: dict = {
        "outtmpl": str(out_path),
        "merge_output_format": "mp4",
        "noplaylist": True,
        "retries": 10,
        "fragment_retries": 10,
        "continuedl": True,
        "quiet": False,
        "no_warnings": False,
    }

    if cookies is not None:
        cookiefile = cookies.expanduser().resolve()
        if not cookiefile.exists():
            raise FileNotFoundError(cookiefile)
        ydl_opts["cookiefile"] = str(cookiefile)

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if not out_path.exists():
        # yt-dlp may choose a different extension; try to locate the downloaded file.
        candidates = sorted(out_path.parent.glob(out_path.stem + ".*"))
        for c in candidates:
            if c.is_file():
                return c
        raise FileNotFoundError(out_path)

    return out_path
