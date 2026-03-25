from __future__ import annotations

import argparse
import re
from pathlib import Path


LINE_FIXES: list[tuple[str, str]] = [
    ("questionarnos", "cuestionarnos"),
    ("argo plazo", "largo plazo"),
    ("prepare", "preparé"),
    ("Berlin", "Berlín"),
    ("union soviética", "Unión Soviética"),
    ("Fracazaron", "Fracasaron"),
    ("fucuyama", "Fukuyama"),
    ("Focuyama", "Fukuyama"),
    ("sepsteinianas", "epsteinianas"),
    ("abstinianas", "epsteinianas"),
    ("agrientas", "sangrientas"),
    ("naciones económicas", "sanciones económicas"),
    ("trisiones", "trillones"),
    ("misferio", "hemisferio"),
    ("deélectica", "dialéctica"),
    ("díalectica", "dialéctica"),
    ("jegeliano", "hegeliano"),
    ("JG", "Hegel"),
    ("plus valía", "plusvalía"),
    ("reistribuya", "redistribuya"),
    ("reivierta", "reinvierte"),
    ("aqué costo", "¿a qué costo?"),
    ("chines", "China es"),
    ("válga", "valga"),
    ("asalternativas", "las alternativas"),
    ("Que propuestas", "Qué propuestas"),
    ("escenadores", "senadores"),
    ("al ser el modelo chino, la otra alternativa, el modelo liberal capitalista de estadounidense",
     "al ser el modelo chino la otra alternativa al modelo liberal-capitalista estadounidense"),
    ("chines el único país", "China es el único país"),
    ("uno debería de tener", "uno debería tener"),
    ("la Unión soviética", "la Unión Soviética"),
]

LOWERCASE_WORDS = {
    "a", "al", "ante", "bajo", "cabe", "con", "contra", "de", "del", "desde", "durante",
    "e", "el", "en", "entre", "hacia", "hasta", "la", "las", "lo", "los", "o", "para",
    "por", "que", "se", "sin", "sobre", "su", "sus", "tras", "u", "un", "una", "uno", "y",
}

PROPER_NOUNS = {
    "Berlín", "Bill", "BRICS", "Brasil", "China", "Clintons", "Cuba", "Epstein", "Estados",
    "Fukuyama", "Gates", "Gramsci", "Hegel", "Harry", "Irak", "Irán", "Jeffrey", "Keynes",
    "Kissinger", "Latinoamérica", "Marx", "México", "Noruega", "Obama", "OTAN", "Occidente",
    "Rusia", "Sanders", "Sudáfrica", "Swift", "Trump", "Twitter", "Unión", "Venezuela",
    "Vietnam", "Walter", "Benjamin", "Cuba", "China", "Estados Unidos", "Francis Fukuyama",
}


def clean_line(line: str) -> str:
    text = " ".join(line.strip().split())
    if not text:
        return ""

    for old, new in LINE_FIXES:
        text = text.replace(old, new)

    text = re.sub(r"\b([YEOA])\b", lambda m: m.group(1).lower(), text)
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    text = re.sub(r"([¿¡])\s+", r"\1", text)

    if text and text[0].islower():
        text = text[0].upper() + text[1:]

    return text


def sentence_case(text: str) -> str:
    words = text.split()
    result: list[str] = []
    capitalize_next = True

    for word in words:
        bare = re.sub(r"^[¿¡\(\"']+|[.,;:?!\)\"']+$", "", word)
        leading = word[: len(word) - len(word.lstrip("¿¡(\"'"))]
        trailing_match = re.search(r"[.,;:?!\)\"']+$", word)
        trailing = trailing_match.group(0) if trailing_match else ""

        core = bare
        if not core:
            result.append(word)
            continue

        if capitalize_next or core in PROPER_NOUNS:
            core_out = core[0].upper() + core[1:]
        elif core.lower() in LOWERCASE_WORDS:
            core_out = core.lower()
        else:
            core_out = core.lower()

        rebuilt = f"{leading}{core_out}{trailing}"
        result.append(rebuilt)
        if trailing.endswith((".", "?", "!")):
            capitalize_next = True
        else:
            capitalize_next = False

    text = " ".join(result)
    text = text.replace("¿corea", "¿Corea")
    text = text.replace("¿y", "¿Y")
    return text


def polish_paragraph(paragraph: str) -> str:
    text = " ".join(paragraph.split())
    for old, new in LINE_FIXES:
        text = text.replace(old, new)

    text = text.replace(" .", ".")
    text = text.replace(" ,", ",")
    text = text.replace(" ;", ";")
    text = text.replace(" :", ":")
    text = text.replace(" ?", "?")
    text = text.replace(" !", "!")
    text = sentence_case(text)
    text = re.sub(r"\bfrancis fukuyama\b", "Francis Fukuyama", text, flags=re.IGNORECASE)
    text = re.sub(r"\bestados unidos\b", "Estados Unidos", text, flags=re.IGNORECASE)
    text = re.sub(r"\bteoría crítica\b", "teoría crítica", text, flags=re.IGNORECASE)
    return text.strip()


def to_paragraphs(lines: list[str], lines_per_paragraph: int = 6) -> str:
    cleaned = [clean_line(line) for line in lines]
    cleaned = [line for line in cleaned if line]

    paragraphs: list[str] = []
    current: list[str] = []
    for line in cleaned:
        current.append(line)
        if len(current) >= lines_per_paragraph or line.endswith((".", "?", "!", ":")):
            paragraphs.append(" ".join(current))
            current = []

    if current:
        paragraphs.append(" ".join(current))

    text = "\n\n".join(paragraphs)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def polish_text(lines: list[str], lines_per_paragraph: int = 10) -> str:
    base = to_paragraphs(lines, lines_per_paragraph=lines_per_paragraph)
    paragraphs = [p.strip() for p in base.split("\n\n") if p.strip()]
    polished = [polish_paragraph(p) for p in paragraphs]
    polished = [p for p in polished if p]
    return "\n\n".join(polished).strip() + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a cleaned transcript file without modifying the original transcript."
    )
    parser.add_argument("input_path", type=Path, help="Original transcript text file")
    parser.add_argument("output_path", type=Path, help="Path for the cleaned transcript")
    parser.add_argument(
        "--mode",
        choices=["clean", "polish"],
        default="clean",
        help="clean: light cleanup, polish: stronger formatting and paragraph polishing.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    input_path = args.input_path.expanduser().resolve()
    output_path = args.output_path.expanduser().resolve()

    lines = input_path.read_text(encoding="utf-8").splitlines()
    if args.mode == "polish":
        cleaned = polish_text(lines)
    else:
        cleaned = to_paragraphs(lines)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(cleaned, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())