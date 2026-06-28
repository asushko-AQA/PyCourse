from __future__ import annotations

import hashlib

QUIZ_HEADINGS = ("## Quick Check", "## Проверь себя")


def normalize_text(value: str) -> str:
    body = value.replace("\r\n", "\n").replace("\r", "\n")
    stripped = [line.rstrip() for line in body.split("\n")]
    return "\n".join(stripped).strip("\n")


def short_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def extract_quiz_section(markdown: str) -> str | None:
    lines = markdown.splitlines()
    start = None
    for index, line in enumerate(lines):
        if any(line.strip() == heading for heading in QUIZ_HEADINGS):
            start = index + 1
            break
    if start is None:
        return None

    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return "\n".join(lines[start:end])


def quiz_hash(section: str) -> str:
    return short_sha256(normalize_text(section))


def quiz_hash_from_markdown(markdown: str) -> str | None:
    section = extract_quiz_section(markdown)
    if section is None:
        return None
    return quiz_hash(section)


def combined_quiz_hash(en_markdown: str, ru_markdown: str) -> str | None:
    en_section = extract_quiz_section(en_markdown)
    ru_section = extract_quiz_section(ru_markdown)
    if en_section is None or ru_section is None:
        return None
    payload = f"{normalize_text(en_section)}\n{normalize_text(ru_section)}"
    return short_sha256(payload)


def content_hash(markdown: str) -> str:
    return short_sha256(normalize_text(markdown))


def combined_content_hash(en_markdown: str, ru_markdown: str) -> str:
    payload = f"{normalize_text(en_markdown)}\n\0\n{normalize_text(ru_markdown)}"
    return short_sha256(payload)

