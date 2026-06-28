from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

from app.sync.hashing import (
    combined_content_hash,
    combined_quiz_hash,
    extract_quiz_section,
    normalize_text,
    quiz_hash,
    quiz_hash_from_markdown,
)

REPO_ROOT = Path(__file__).resolve().parents[4]
SAMPLE_EN = (
    REPO_ROOT
    / "course-1-python-basics"
    / "block-1-meeting-your-computer"
    / "lesson-1-2-using-the-terminal"
    / "en.md"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_quiz_hash_helpers_follow_canonical_rules() -> None:
    md = "## Quick Check\r\n\r\n1. Q?   \r\n\r\n## What's Next\r\n"
    section = extract_quiz_section(md)
    assert section is not None
    assert normalize_text(section) == "1. Q?"
    assert quiz_hash(section) == quiz_hash("1. Q?   \n")
    assert quiz_hash_from_markdown(md) == quiz_hash(section)


def test_combined_hashes_are_stable() -> None:
    en = "line1\r\nline2  \r\n"
    ru = "строка1\r\nстрока2   \n"
    first = combined_content_hash(en, ru)
    second = combined_content_hash(en.replace("\r\n", "\n"), ru)
    assert first == second

    en_quiz = "## Quick Check\n\n1. Q?\n\n## What's Next\n"
    ru_quiz = "## Проверь себя\n\n1. В?\n\n## Что дальше\n"
    assert combined_quiz_hash(en_quiz, ru_quiz) is not None


def test_hash_matches_apply_lesson_quizzes_script_output() -> None:
    markdown = _read(SAMPLE_EN)
    expected = quiz_hash_from_markdown(markdown)
    assert expected is not None

    process = subprocess.run(
        [sys.executable, "tools/apply_lesson_quizzes.py", "--hash"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    relative = SAMPLE_EN.relative_to(REPO_ROOT).as_posix()
    script_hashes: dict[str, str] = {}
    for line in process.stdout.splitlines():
        match = re.match(r"^([0-9a-f]{12})\s+(.+)$", line.strip())
        if match is None:
            continue
        hash_value, file_path = match.groups()
        script_hashes[file_path.replace("\\", "/")] = hash_value

    assert relative in script_hashes
    assert script_hashes[relative] == expected

