from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from app.sync.hashing import combined_content_hash, combined_quiz_hash, content_hash

COURSE_RE = re.compile(r"^course-\d+-")
BLOCK_RE = re.compile(r"^block-(\d+)-")
LESSON_RE = re.compile(r"^lesson-(\d+)-(\d+)-")
META_RE = re.compile(r"<!--\s*meta\b([\s\S]*?)-->", re.IGNORECASE)


@dataclass(slots=True)
class LessonRecord:
    id: str
    course_id: str
    block_id: str
    slug: str
    title: str
    path: str
    order_index: int
    quiz_hash: str | None
    homework_ref: str | None
    checker_ref: str | None
    content_hash: str


@dataclass(slots=True)
class BlockRecord:
    id: str
    course_id: str
    slug: str
    title: str
    path: str
    order_index: int
    content_hash: str | None
    lessons: list[LessonRecord]


@dataclass(slots=True)
class CourseRecord:
    id: str
    slug: str
    title: str
    path: str
    order_index: int
    content_hash: str | None
    blocks: list[BlockRecord]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def resolve_content_root(root: str | Path | None = None) -> Path:
    if root is not None:
        return Path(root).resolve()
    return _repo_root()


def _extract_id(value: str, pattern: re.Pattern[str], *, groups: int = 1) -> str | None:
    match = pattern.match(value)
    if match is None:
        return None
    if groups == 1:
        return match.group(1)
    return "-".join(match.group(index) for index in range(1, groups + 1))


def _extract_h1(markdown: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, flags=re.MULTILINE)
    if match is None:
        return "Untitled"
    return match.group(1).strip()


def _strip_prefix(title: str, kind: str) -> str:
    if kind == "lesson":
        return re.sub(r"^(Lesson|Урок)\s+[\d.]+\s*[:.]?\s*", "", title, flags=re.IGNORECASE).strip()
    if kind == "course":
        return re.sub(r"^Course\s+[\d.]+\s*[:.]?\s*", "", title, flags=re.IGNORECASE).strip()
    return re.sub(r"^Block\s+[\d.]+\s*[:.]?\s*", "", title, flags=re.IGNORECASE).strip()


def _read_text_or_none(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def _parse_meta(markdown: str) -> tuple[str | None, str | None]:
    match = META_RE.search(markdown)
    if match is None:
        return None, None

    homework_ref: str | None = None
    checker_ref: str | None = None
    for line in match.group(1).splitlines():
        kv = re.match(r"^\s*([a-zA-Z_]+)\s*:\s*(.+?)\s*$", line)
        if kv is None:
            continue
        key = kv.group(1).lower()
        value = kv.group(2).strip()
        if key == "homework":
            homework_ref = value
        elif key == "checker":
            checker_ref = value
    return homework_ref, checker_ref


def _sorted_dirs(parent: Path, pattern: re.Pattern[str]) -> list[Path]:
    return sorted([entry for entry in parent.iterdir() if entry.is_dir() and pattern.match(entry.name)], key=lambda x: x.name)


def _lesson_sort_key(slug: str) -> tuple[int, int]:
    match = LESSON_RE.match(slug)
    if match is None:
        return (99, 99)
    return (int(match.group(1)), int(match.group(2)))


def discover_catalog(root: str | Path | None = None) -> list[CourseRecord]:
    content_root = resolve_content_root(root)
    courses: list[CourseRecord] = []

    lesson_order_by_course: dict[str, int] = {}
    for course_index, course_dir in enumerate(_sorted_dirs(content_root, COURSE_RE)):
        course_id = _extract_id(course_dir.name, re.compile(r"^(course-\d+)"))
        if course_id is None:
            continue
        block_dirs = _sorted_dirs(course_dir, re.compile(r"^block-\d+-"))
        if not block_dirs:
            continue

        course_readme = _read_text_or_none(course_dir / "README.md")
        course_title = _strip_prefix(_extract_h1(course_readme or course_dir.name), "course")
        course_hash = content_hash(course_readme) if course_readme is not None else None

        blocks: list[BlockRecord] = []
        lesson_order_by_course.setdefault(course_id, 0)

        for block_dir in sorted(block_dirs, key=lambda p: int(BLOCK_RE.match(p.name).group(1))):  # type: ignore[union-attr]
            block_id = _extract_id(block_dir.name, re.compile(r"^(block-\d+)"))
            if block_id is None:
                continue
            block_num = _extract_id(block_dir.name, BLOCK_RE)
            block_order = int(block_num) if block_num is not None else 0

            block_readme = _read_text_or_none(block_dir / "README.md")
            block_title = _strip_prefix(_extract_h1(block_readme or block_dir.name), "block")
            block_hash = content_hash(block_readme) if block_readme is not None else None

            lessons: list[LessonRecord] = []
            lesson_dirs = sorted(_sorted_dirs(block_dir, re.compile(r"^lesson-\d+-\d+-")), key=lambda p: _lesson_sort_key(p.name))
            for lesson_dir in lesson_dirs:
                lesson_id = _extract_id(lesson_dir.name, re.compile(r"^(lesson-\d+-\d+)"))
                if lesson_id is None:
                    continue
                en_path = lesson_dir / "en.md"
                ru_path = lesson_dir / "ru.md"
                if not en_path.exists() or not ru_path.exists():
                    continue
                en_markdown = en_path.read_text(encoding="utf-8")
                ru_markdown = ru_path.read_text(encoding="utf-8")

                lesson_title = _strip_prefix(_extract_h1(en_markdown), "lesson")
                homework_ref, checker_ref = _parse_meta(en_markdown)
                rel_path = lesson_dir.relative_to(content_root).as_posix()

                lessons.append(
                    LessonRecord(
                        id=lesson_id,
                        course_id=course_id,
                        block_id=block_id,
                        slug=lesson_dir.name,
                        title=lesson_title,
                        path=rel_path,
                        order_index=lesson_order_by_course[course_id],
                        quiz_hash=combined_quiz_hash(en_markdown, ru_markdown),
                        homework_ref=homework_ref,
                        checker_ref=checker_ref,
                        content_hash=combined_content_hash(en_markdown, ru_markdown),
                    )
                )
                lesson_order_by_course[course_id] += 1

            block_rel_path = block_dir.relative_to(content_root).as_posix()
            blocks.append(
                BlockRecord(
                    id=block_id,
                    course_id=course_id,
                    slug=block_dir.name,
                    title=block_title,
                    path=block_rel_path,
                    order_index=block_order,
                    content_hash=block_hash,
                    lessons=lessons,
                )
            )

        courses.append(
            CourseRecord(
                id=course_id,
                slug=course_dir.name,
                title=course_title,
                path=course_dir.relative_to(content_root).as_posix(),
                order_index=course_index,
                content_hash=course_hash,
                blocks=blocks,
            )
        )

    return courses

