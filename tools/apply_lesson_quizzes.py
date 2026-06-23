"""Insert Quick Check sections into lesson en.md / ru.md, and hash quizzes.

Two modes:
  python tools/apply_lesson_quizzes.py          # idempotent insert from quizzes/*.json
  python tools/apply_lesson_quizzes.py --hash    # print canonical quiz hashes (no writes)

The quiz hash is the schema-v2 contract used by the markdown->DB sync job (plan 05):
sha256 of the normalized "## Quick Check" / "## Проверь себя" section body, first 12 hex.
See documents/plans/lesson-schema-v2.md.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUIZ_DIR = Path(__file__).with_name("quizzes")

EN_ANCHORS = ("What's Next",)
RU_ANCHORS = ("Дальше", "Что дальше")

QUIZ_HEADINGS = ("## Quick Check", "## Проверь себя")


def insert_before_anchor(text: str, anchor: str, block: str) -> str:
    marker = f"## {anchor}"
    if marker not in text:
        return text
    needle = f"---\n\n{marker}"
    if needle in text:
        return text.replace(needle, f"---\n\n{block}\n\n{marker}", 1)
    return text.replace(marker, f"{block}\n\n{marker}", 1)


def load_quizzes() -> dict[str, dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    for path in sorted(QUIZ_DIR.glob("*.json")):
        merged.update(json.loads(path.read_text(encoding="utf-8")))
    return merged


def extract_quiz_section(text: str) -> str | None:
    """Return the quiz section body (heading excluded) up to the next `## ` or EOF."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if any(line.strip() == h for h in QUIZ_HEADINGS):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return "\n".join(lines[start:end])


def normalize(section: str) -> str:
    """CRLF->LF, strip trailing whitespace per line, strip leading/trailing blanks."""
    body = section.replace("\r\n", "\n").replace("\r", "\n")
    stripped = [ln.rstrip() for ln in body.split("\n")]
    return "\n".join(stripped).strip("\n")


def quiz_hash(section: str) -> str:
    return hashlib.sha256(normalize(section).encode("utf-8")).hexdigest()[:12]


def iter_lesson_files():
    for path in sorted(ROOT.glob("course-*/**/lesson-*-*/")):
        for lang in ("en", "ru"):
            md = path / f"{lang}.md"
            if md.exists():
                yield md, lang


def run_hash() -> None:
    count = 0
    missing = 0
    for md, _lang in iter_lesson_files():
        section = extract_quiz_section(md.read_text(encoding="utf-8"))
        rel = md.relative_to(ROOT)
        if section is None:
            print(f"NO QUIZ: {rel}")
            missing += 1
            continue
        print(f"{quiz_hash(section)}  {rel}")
        count += 1
    print(f"\nHashed {count} quizzes, {missing} files without a quiz section.")


def run_apply() -> None:
    quizzes = load_quizzes()
    updated = 0
    skipped = 0

    for lesson_slug, langs in quizzes.items():
        for course in ("course-1-python-basics", "course-2-web-apps"):
            matches = list(ROOT.glob(f"{course}/**/{lesson_slug}/en.md"))
            if matches:
                lesson_dir = matches[0].parent
                break
        else:
            print(f"MISSING DIR: {lesson_slug}")
            continue

        for lang, anchors in (("en", EN_ANCHORS), ("ru", RU_ANCHORS)):
            path = lesson_dir / f"{lang}.md"
            if not path.exists():
                print(f"MISSING FILE: {path}")
                continue
            text = path.read_text(encoding="utf-8")
            if any(h in text for h in QUIZ_HEADINGS):
                skipped += 1
                continue
            block = langs[lang]
            new_text = text
            for anchor in anchors:
                if f"## {anchor}" in new_text:
                    new_text = insert_before_anchor(new_text, anchor, block)
                    break
            if new_text == text:
                print(f"NO ANCHOR: {path}")
                continue
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            section = extract_quiz_section(new_text)
            digest = quiz_hash(section) if section else "??"
            print(f"OK: {path.relative_to(ROOT)}  (quiz {digest})")

    print(f"\nUpdated {updated} files, skipped {skipped} (already had quiz).")


def main() -> None:
    if "--hash" in sys.argv[1:]:
        run_hash()
    else:
        run_apply()


if __name__ == "__main__":
    main()
