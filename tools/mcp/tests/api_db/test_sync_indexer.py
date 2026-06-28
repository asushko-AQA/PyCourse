from __future__ import annotations

from pathlib import Path

from app.repositories.lesson_repo import LessonRepo
from app.sync.index_lessons import run_sync


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _build_fixture_content(root: Path) -> None:
    _write(
        root / "course-1-mini" / "README.md",
        "# Course 1: Mini Course\n\nShort summary.\n",
    )
    _write(
        root / "course-1-mini" / "block-1-start" / "README.md",
        "# Block 1: Start\n\nBlock summary.\n",
    )
    _write(
        root / "course-1-mini" / "block-1-start" / "lesson-1-1-hello" / "en.md",
        """# Lesson 1.1: Hello

<!-- meta
homework: starter/hello.py
checker: checker/hello
-->

## Quick Check

1. Is this a question?
- **a)** Yes
- **b)** No

<details><summary>Answers</summary>

1. **a)** Because yes.

</details>

## What's Next
""",
    )
    _write(
        root / "course-1-mini" / "block-1-start" / "lesson-1-1-hello" / "ru.md",
        """# Урок 1.1: Привет

## Проверь себя

1. Это вопрос?
- **a)** Да
- **b)** Нет

<details><summary>Ответы</summary>

1. **a)** Потому что да.

</details>

## Что дальше
""",
    )
    _write(
        root / "course-1-mini" / "block-1-start" / "lesson-1-2-next" / "en.md",
        """# Lesson 1.2: Next

## Quick Check

1. Next?
- **a)** Yes
- **b)** No

<details><summary>Answers</summary>

1. **a)** Yes.

</details>

## What's Next
""",
    )
    _write(
        root / "course-1-mini" / "block-1-start" / "lesson-1-2-next" / "ru.md",
        """# Урок 1.2: Далее

## Проверь себя

1. Дальше?
- **a)** Да
- **b)** Нет

<details><summary>Ответы</summary>

1. **a)** Да.

</details>

## Что дальше
""",
    )


def test_sync_is_idempotent_and_orders_lessons(session, app_db_url: str, tmp_path: Path) -> None:
    content_root = tmp_path / "content"
    _build_fixture_content(content_root)

    first = run_sync(content_root=content_root, database_url=app_db_url)
    assert first.courses.created == 1
    assert first.blocks.created == 1
    assert first.lessons.created == 2

    second = run_sync(content_root=content_root, database_url=app_db_url)
    assert second.courses.updated == 0
    assert second.blocks.updated == 0
    assert second.lessons.updated == 0
    assert second.lessons.unchanged == 2

    session.expire_all()
    lessons = LessonRepo(session).list_lessons()
    assert [lesson.order_index for lesson in lessons] == [0, 1]
    assert all(lesson.quiz_hash for lesson in lessons)


def test_sync_check_detects_drift_and_extra_rows(session, app_db_url: str, tmp_path: Path) -> None:
    content_root = tmp_path / "content"
    _build_fixture_content(content_root)
    run_sync(content_root=content_root, database_url=app_db_url)

    en_lesson = content_root / "course-1-mini" / "block-1-start" / "lesson-1-1-hello" / "en.md"
    en_lesson.write_text(en_lesson.read_text(encoding="utf-8").replace("Because yes.", "Changed."), encoding="utf-8")

    check_result = run_sync(content_root=content_root, database_url=app_db_url, check_only=True)
    assert not check_result.ok
    assert any("lesson drift: lesson-1-1" in issue for issue in check_result.issues)

    run_sync(content_root=content_root, database_url=app_db_url)
    fixed = run_sync(content_root=content_root, database_url=app_db_url, check_only=True)
    assert fixed.ok

    lesson_dir = content_root / "course-1-mini" / "block-1-start" / "lesson-1-2-next"
    for file_path in lesson_dir.glob("*"):
        file_path.unlink()
    lesson_dir.rmdir()

    missing_check = run_sync(content_root=content_root, database_url=app_db_url, check_only=True)
    assert not missing_check.ok
    assert any("extra lesson in DB: lesson-1-2" in issue for issue in missing_check.issues)

