from collections.abc import Generator
from pathlib import Path

from sqlalchemy import event, text
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import get_settings, sqlite_path_from_url

_engine = None


def _build_engine(database_url: str):
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    engine = create_engine(database_url, connect_args=connect_args)
    _attach_sqlite_pragmas(engine)
    return engine


def _attach_sqlite_pragmas(engine) -> None:
    settings = get_settings()

    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, _connection_record):  # type: ignore[no-untyped-def]
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=WAL;")
        cursor.execute(f"PRAGMA busy_timeout={settings.sqlite_busy_timeout_ms};")
        cursor.close()


def get_engine():
    global _engine
    if _engine is None:
        _engine = _build_engine(get_settings().database_url)
    return _engine


def reset_engine(database_url: str) -> None:
    global _engine
    _engine = _build_engine(database_url)


def ensure_sqlite_parent_dir() -> None:
    path = sqlite_path_from_url(get_settings().database_url)
    if path is None:
        return
    parent = Path(path).parent
    parent.mkdir(parents=True, exist_ok=True)


def init_db() -> None:
    ensure_sqlite_parent_dir()
    SQLModel.metadata.create_all(get_engine())


def db_ping() -> dict[str, str | bool]:
    with Session(get_engine()) as session:
        session.exec(text("SELECT 1")).one()
        journal_mode_row = session.exec(text("PRAGMA journal_mode;")).one()
    try:
        journal_mode = journal_mode_row[0]
    except (TypeError, KeyError, IndexError):
        journal_mode = journal_mode_row
    return {"ok": True, "journal_mode": str(journal_mode).lower()}


def get_session() -> Generator[Session, None, None]:
    with Session(get_engine()) as session:
        yield session
