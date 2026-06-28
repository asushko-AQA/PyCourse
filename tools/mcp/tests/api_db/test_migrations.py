from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect


EXPECTED_TABLES = {
    "achievements",
    "blocks",
    "courses",
    "email_verification_tokens",
    "external_identities",
    "lessons",
    "progress",
    "sessions",
    "star_events",
    "streak_snapshots",
    "submissions",
    "user_achievements",
    "users",
}


def _engine_for(db_path: Path):
    return create_engine(f"sqlite:///{db_path.as_posix()}", connect_args={"check_same_thread": False})


def test_upgrade_creates_all_expected_tables(alembic_cfg: Config, db_path: Path) -> None:
    command.upgrade(alembic_cfg, "head")
    inspector = inspect(_engine_for(db_path))
    tables = set(inspector.get_table_names())
    assert EXPECTED_TABLES.issubset(tables)

    lesson_columns = {c["name"] for c in inspector.get_columns("lessons")}
    assert "content_hash" in lesson_columns
    assert "quiz_hash" in lesson_columns
    assert "body" not in lesson_columns
    assert "content" not in lesson_columns


def test_downgrade_to_base_removes_schema(alembic_cfg: Config, db_path: Path) -> None:
    command.upgrade(alembic_cfg, "head")
    command.downgrade(alembic_cfg, "base")
    inspector = inspect(_engine_for(db_path))
    tables = set(inspector.get_table_names())
    assert EXPECTED_TABLES.isdisjoint(tables)
