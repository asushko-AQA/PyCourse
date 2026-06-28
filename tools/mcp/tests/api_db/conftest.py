from pathlib import Path
import sys

import pytest
from alembic import command
from alembic.config import Config
from sqlmodel import Session, create_engine

REPO_ROOT = Path(__file__).resolve().parents[4]
BACKEND_ROOT = REPO_ROOT / "backend"
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.core.db import reset_engine


def _sqlite_url(db_path: Path) -> str:
    return f"sqlite:///{db_path.as_posix()}"


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test_pycourse.db"


@pytest.fixture
def alembic_cfg(db_path: Path) -> Config:
    cfg = Config(str(BACKEND_ROOT / "alembic.ini"))
    cfg.set_main_option("script_location", str(BACKEND_ROOT / "alembic"))
    cfg.set_main_option("sqlalchemy.url", _sqlite_url(db_path))
    return cfg


@pytest.fixture
def migrated_db(alembic_cfg: Config, db_path: Path) -> Path:
    command.upgrade(alembic_cfg, "head")
    return db_path


@pytest.fixture
def session(migrated_db: Path) -> Session:
    engine = create_engine(_sqlite_url(migrated_db), connect_args={"check_same_thread": False})
    with Session(engine) as db:
        yield db


@pytest.fixture
def app_db_url(migrated_db: Path) -> str:
    url = _sqlite_url(migrated_db)
    reset_engine(url)
    return url
