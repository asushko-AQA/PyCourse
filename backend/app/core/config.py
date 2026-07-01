from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///data/pycourse.db"
    frontend_origin: str = "http://localhost:3000"
    sqlite_busy_timeout_ms: int = 5000

    # --- Auth / registration (plan 06) ---
    # Minimum password length enforced at registration.
    password_min_length: int = 8
    # Lifetime of an email-verification token before it expires.
    email_verification_ttl_hours: int = 24
    # Frontend route that redeems a verification token. `{token}` is substituted
    # with the single-use token; the page then POSTs it back to /auth/verify.
    verify_url_template: str = "http://localhost:3000/en/auth/verify?token={token}"

    # --- Email delivery (plan 06) ---
    # "console" (dev: prints the link to logs) or "smtp" (production stub).
    email_backend: str = "console"
    email_from: str = "no-reply@pycourse.local"
    # SMTP settings — only used when email_backend == "smtp".
    smtp_host: str = "localhost"
    smtp_port: int = 587
    smtp_user: str | None = None
    smtp_password: str | None = None
    smtp_use_tls: bool = True

    # --- Session auth (plan 07) ---
    session_cookie_name: str = "pycourse_session"
    session_ttl_hours: int = 24 * 7
    signin_rate_limit_attempts: int = 5
    signin_rate_limit_window_seconds: int = 60

    def build_verify_url(self, token: str) -> str:
        if "{token}" in self.verify_url_template:
            return self.verify_url_template.format(token=token)
        sep = "&" if "?" in self.verify_url_template else "?"
        return f"{self.verify_url_template}{sep}token={token}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


def sqlite_path_from_url(database_url: str) -> Path | None:
    if not database_url.startswith("sqlite:///"):
        return None
    raw_path = database_url.replace("sqlite:///", "", 1)
    return Path(raw_path)
