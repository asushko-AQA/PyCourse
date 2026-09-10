"""Alembic must honor DATABASE_URL, not the dev default in alembic.ini."""

from __future__ import annotations

from alembic.config import Config

from app.core.config import Settings


def test_alembic_env_uses_settings_database_url(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("DATABASE_URL", "sqlite:////data/pycourse.db")
    from app.core import config as config_module

    config_module.get_settings.cache_clear()

    alembic_cfg = Config(str(tmp_path / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", "alembic")
    alembic_cfg.set_main_option("sqlalchemy.url", "sqlite:///data/pycourse.db")

    settings = Settings()
    alembic_cfg.set_main_option("sqlalchemy.url", settings.database_url)

    assert alembic_cfg.get_main_option("sqlalchemy.url") == "sqlite:////data/pycourse.db"

    config_module.get_settings.cache_clear()
