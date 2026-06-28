from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///data/pycourse.db"
    frontend_origin: str = "http://localhost:3000"
    sqlite_busy_timeout_ms: int = 5000


@lru_cache
def get_settings() -> Settings:
    return Settings()


def sqlite_path_from_url(database_url: str) -> Path | None:
    if not database_url.startswith("sqlite:///"):
        return None
    raw_path = database_url.replace("sqlite:///", "", 1)
    return Path(raw_path)
