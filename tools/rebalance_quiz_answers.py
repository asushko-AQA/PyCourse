"""Spread correct Quick Check answers across a–d for Courses 1 and 2.

EN and RU get the same letter for each question. tools/quizzes/*.json is
rewritten from the markdown so it stays in lock-step.

Usage: python tools/rebalance_quiz_answers.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LETTERS = "abcd"
OPTION_RE = re.compile(r"^(\s*-\s+\*\*)([a-d])(\)\*\*\s*)(.*)$")
ANSWER_RE = re.compile(r"^(\s*)(\d+)(\.\s+\*\*)([a-d])(\)\*\*\s*)(.*)$")
QUIZ_HEADING = {"en": "## Quick Check", "ru": "## Проверь себя"}


def split_questions(lines: list[str]) -> tuple[list[str], list[list[str]], list[str]]:
    """Return (before first question, question chunks, from the answer block on).

    Only the Quick Check / Проверь себя section is touched.
    """
    quiz = next(
        i
        for i, line in enumerate(lines)
        if line.strip() in ("## Quick Check", "## Проверь себя")
    )
    start = next(i for i in range(quiz, len(lines)) if re.match(r"^\d+\.\s+", lines[i]))
    details = next(i for i in range(start, len(lines)) if lines[i].lower().startswith("<details"))
    head = lines[:start]
    body = lines[start:details]
    tail = lines[details:]
    chunks: list[list[str]] = []
    current: list[str] = []
    for line in body:
        if current and re.match(r"^\d+\.\s+", line):
            chunks.append(current)
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append(current)
    return head, chunks, tail


def option_indexes(chunk: list[str]) -> list[int]:
    return [i for i, line in enumerate(chunk) if OPTION_RE.match(line)]


def correct_letter(tail_lines: list[str], number: int) -> str:
    for line in tail_lines:
        m = ANSWER_RE.match(line)
        if m and int(m.group(2)) == number:
            return m.group(4)
    raise ValueError(f"no answer for question {number}")


def set_answer_letter(tail_lines: list[str], number: int, letter: str) -> None:
    for i, line in enumerate(tail_lines):
        m = ANSWER_RE.match(line)
        if m and int(m.group(2)) == number:
            tail_lines[i] = f"{m.group(1)}{m.group(2)}{m.group(3)}{letter}{m.group(5)}{m.group(6)}"
            return
    raise ValueError(f"no answer line for question {number}")


def retarget(chunk: list[str], tail: list[str], target: str) -> None:
    number = int(re.match(r"^(\d+)\.", chunk[0]).group(1))
    indexes = option_indexes(chunk)
    letters = []
    texts = []
    for i in indexes:
        m = OPTION_RE.match(chunk[i])
        letters.append(m.group(2))
        texts.append(m.group(4))
    current = correct_letter(tail, number)
    n = len(texts)
    if current not in letters[:n]:
        raise ValueError(f"Q{number} answer {current} not in options {letters}")
    src = letters.index(current)
    dst = LETTERS.index(target)
    # new slot i shows the old slot (i - dst + src) mod n
    order = [((i - dst + src) % n) for i in range(n)]
    for slot, i in enumerate(indexes):
        m = OPTION_RE.match(chunk[i])
        chunk[i] = f"{m.group(1)}{LETTERS[slot]}{m.group(3)}{texts[order[slot]]}"
    set_answer_letter(tail, number, target)


def assign_targets(counts: list[int], used: dict[str, int]) -> list[list[str]]:
    """Per-lesson letter lists. No letter more than ceil(n/2); course totals stay even."""
    plans = []
    for n in counts:
        cap = (n + 1) // 2
        plan = []
        for _ in range(n):
            choices = sorted(LETTERS, key=lambda L: (used[L], L))
            letter = next(L for L in choices if plan.count(L) < cap)
            plan.append(letter)
            used[letter] += 1
        plans.append(plan)
    return plans


def quiz_section(text: str, lang: str) -> str | None:
    heading = QUIZ_HEADING[lang]
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    body = "\n".join(lines[start:end]).strip("\n")
    return body + "\n"


def main() -> None:
    courses = ["course-1-python-basics", "course-2-web-apps"]
    for course in courses:
        lessons = sorted(Path(course).glob("block-*/lesson-*"))
        counts = []
        parsed = []
        for lesson in lessons:
            en = (lesson / "en.md").read_text(encoding="utf-8").splitlines()
            head, chunks, tail = split_questions(en)
            counts.append(len(chunks))
            parsed.append((lesson, head, chunks, tail))
        used = {L: 0 for L in LETTERS}
        plans = assign_targets(counts, used)
        print(course, dict(used), "questions", sum(counts))
        for (lesson, _head, chunks, tail), plan in zip(parsed, plans):
            for lang in ("en", "ru"):
                path = lesson / f"{lang}.md"
                lines = path.read_text(encoding="utf-8").splitlines()
                head, lang_chunks, lang_tail = split_questions(lines)
                if len(lang_chunks) != len(plan):
                    raise SystemExit(f"{path}: {len(lang_chunks)} questions, plan {len(plan)}")
                for chunk, letter in zip(lang_chunks, plan):
                    retarget(chunk, lang_tail, letter)
                out = head + [line for chunk in lang_chunks for line in chunk] + lang_tail
                path.write_text("\n".join(out) + "\n", encoding="utf-8")

    # Refresh quiz JSON from the markdown so the insert tool stays in sync.
    by_slug: dict[str, dict[str, str]] = {}
    for md in sorted(ROOT.glob("course-[12]*/block-*/lesson-*/en.md")):
        slug = md.parent.name
        by_slug[slug] = {
            "en": quiz_section(md.read_text(encoding="utf-8"), "en") or "",
            "ru": quiz_section((md.parent / "ru.md").read_text(encoding="utf-8"), "ru") or "",
        }
    quiz_dir = ROOT / "tools" / "quizzes"
    for path in sorted(quiz_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for slug, langs in data.items():
            if slug in by_slug and by_slug[slug]["en"] and by_slug[slug]["ru"]:
                data[slug] = by_slug[slug]
                changed = True
        if changed:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print("updated", path.name)


if __name__ == "__main__":
    main()
