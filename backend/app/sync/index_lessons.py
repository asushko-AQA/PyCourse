from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass, field
from pathlib import Path
import sys

from sqlmodel import Session

from app.core.config import sqlite_path_from_url
from app.core.db import get_engine, reset_engine
from app.repositories.lesson_repo import LessonRepo
from app.sync.discovery import CourseRecord, discover_catalog


@dataclass(slots=True)
class SyncStats:
    created: int = 0
    updated: int = 0
    unchanged: int = 0


@dataclass(slots=True)
class SyncResult:
    courses: SyncStats = field(default_factory=SyncStats)
    blocks: SyncStats = field(default_factory=SyncStats)
    lessons: SyncStats = field(default_factory=SyncStats)
    issues: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.issues


def _bump(stats: SyncStats, action: str) -> None:
    if action == "created":
        stats.created += 1
    elif action == "updated":
        stats.updated += 1
    else:
        stats.unchanged += 1


def _ensure_db_parent(database_url: str) -> None:
    path = sqlite_path_from_url(database_url)
    if path is None:
        return
    parent = Path(path).parent
    parent.mkdir(parents=True, exist_ok=True)


def _diff_existing(repo: LessonRepo, courses: list[CourseRecord]) -> list[str]:
    issues: list[str] = []
    expected_courses = {course.id: course for course in courses}
    expected_blocks = {block.id: block for course in courses for block in course.blocks}
    expected_lessons = {
        lesson.id: lesson
        for course in courses
        for block in course.blocks
        for lesson in block.lessons
    }

    for row in repo.list_courses():
        expected = expected_courses.get(row.id)
        if expected is None:
            issues.append(f"extra course in DB: {row.id}")
            continue
        if (
            row.slug != expected.slug
            or row.title != expected.title
            or row.path != expected.path
            or row.order_index != expected.order_index
            or row.content_hash != expected.content_hash
        ):
            issues.append(f"course drift: {row.id}")
    for expected in expected_courses.values():
        if repo.get_course(expected.id) is None:
            issues.append(f"missing course in DB: {expected.id}")

    for row in repo.list_blocks():
        expected = expected_blocks.get(row.id)
        if expected is None:
            issues.append(f"extra block in DB: {row.id}")
            continue
        if (
            row.course_id != expected.course_id
            or row.slug != expected.slug
            or row.title != expected.title
            or row.path != expected.path
            or row.order_index != expected.order_index
            or row.content_hash != expected.content_hash
        ):
            issues.append(f"block drift: {row.id}")
    for expected in expected_blocks.values():
        if repo.get_block(expected.id) is None:
            issues.append(f"missing block in DB: {expected.id}")

    for row in repo.list_lessons():
        expected = expected_lessons.get(row.id)
        if expected is None:
            issues.append(f"extra lesson in DB: {row.id}")
            continue
        if (
            row.course_id != expected.course_id
            or row.block_id != expected.block_id
            or row.slug != expected.slug
            or row.title != expected.title
            or row.path != expected.path
            or row.order_index != expected.order_index
            or row.quiz_hash != expected.quiz_hash
            or row.homework_ref != expected.homework_ref
            or row.checker_ref != expected.checker_ref
            or row.content_hash != expected.content_hash
        ):
            issues.append(f"lesson drift: {row.id}")
    for expected in expected_lessons.values():
        if repo.get_lesson(expected.id) is None:
            issues.append(f"missing lesson in DB: {expected.id}")

    return issues


def run_sync(
    *,
    content_root: str | Path | None = None,
    database_url: str | None = None,
    check_only: bool = False,
) -> SyncResult:
    if database_url is not None:
        _ensure_db_parent(database_url)
        reset_engine(database_url)

    result = SyncResult()
    courses = discover_catalog(content_root)

    with Session(get_engine()) as session:
        repo = LessonRepo(session)
        if check_only:
            result.issues.extend(_diff_existing(repo, courses))
            return result

        for course in courses:
            action, _ = repo.upsert_course(
                course_id=course.id,
                slug=course.slug,
                title=course.title,
                path=course.path,
                order_index=course.order_index,
                content_hash=course.content_hash,
            )
            _bump(result.courses, action)
            for block in course.blocks:
                action, _ = repo.upsert_block(
                    block_id=block.id,
                    course_id=block.course_id,
                    slug=block.slug,
                    title=block.title,
                    path=block.path,
                    order_index=block.order_index,
                    content_hash=block.content_hash,
                )
                _bump(result.blocks, action)
                for lesson in block.lessons:
                    action, _ = repo.upsert_lesson(
                        lesson_id=lesson.id,
                        course_id=lesson.course_id,
                        block_id=lesson.block_id,
                        slug=lesson.slug,
                        title=lesson.title,
                        path=lesson.path,
                        order_index=lesson.order_index,
                        quiz_hash=lesson.quiz_hash,
                        homework_ref=lesson.homework_ref,
                        checker_ref=lesson.checker_ref,
                        content_hash=lesson.content_hash,
                    )
                    _bump(result.lessons, action)

    return result


def _build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Sync markdown lesson metadata into the backend database.")
    parser.add_argument("--check", action="store_true", help="Check for drift without writing.")
    parser.add_argument("--root", type=str, default=None, help="Content root path (defaults to repo root).")
    parser.add_argument("--database-url", type=str, default=None, help="Override DATABASE_URL for this run.")
    return parser


def _print_stats(result: SyncResult, check_only: bool) -> None:
    if check_only:
        if result.ok:
            print("Sync check: OK (no drift)")
            return
        print("Sync check: DRIFT DETECTED")
        for issue in result.issues:
            print(f"- {issue}")
        return

    print(
        "Courses: created={0} updated={1} unchanged={2}".format(
            result.courses.created, result.courses.updated, result.courses.unchanged
        )
    )
    print(
        "Blocks: created={0} updated={1} unchanged={2}".format(
            result.blocks.created, result.blocks.updated, result.blocks.unchanged
        )
    )
    print(
        "Lessons: created={0} updated={1} unchanged={2}".format(
            result.lessons.created, result.lessons.updated, result.lessons.unchanged
        )
    )


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    result = run_sync(content_root=args.root, database_url=args.database_url, check_only=args.check)
    _print_stats(result, args.check)
    if args.check and not result.ok:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

