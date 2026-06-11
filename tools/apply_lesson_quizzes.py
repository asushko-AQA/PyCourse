"""One-shot helper: insert Quick Check sections into lesson en.md / ru.md files."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUIZ_DIR = Path(__file__).with_name("quizzes")

EN_ANCHORS = ("What's Next",)
RU_ANCHORS = ("Дальше", "Что дальше")


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


def main() -> None:
    quizzes = load_quizzes()
    updated = 0
    skipped = 0

    for lesson_slug, langs in quizzes.items():
        for course in ("course-1-python-basics", "course-2-web-apps"):
            matches = list(ROOT.glob(f"{course}/**/{lesson_slug}/en.md"))
            if not matches:
                continue
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
            if "## Quick Check" in text or "## Проверь себя" in text:
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
            print(f"OK: {path.relative_to(ROOT)}")

    print(f"\nUpdated {updated} files, skipped {skipped} (already had quiz).")


if __name__ == "__main__":
    main()
