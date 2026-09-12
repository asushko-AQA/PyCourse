from functools import lru_cache
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///data/pycourse.db"
    # Single origin (legacy) or comma-separated list, e.g.
    # "https://app.example.com,http://localhost:3000"
    frontend_origin: str = "http://localhost:3000"
    # Optional override; when set, replaces frontend_origin for CORS allowlist.
    cors_origins: str | None = None
    sqlite_busy_timeout_ms: int = 5000

    # --- Auth / registration (plan 06) ---
    # Minimum password length enforced at registration.
    password_min_length: int = 8
    # Lifetime of an email-verification token before it expires.
    email_verification_ttl_hours: int = 24
    # Frontend route that redeems a verification token. `{token}` is substituted
    # with the single-use token; optional `{lang}` defaults to "en" when omitted
    # from the call site. The page then POSTs the token back to /auth/verify.
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
    # False for local HTTP dev; set true in production (HTTPS).
    session_cookie_secure: bool = False

    @computed_field  # type: ignore[prop-decorator]
    @property
    def allowed_cors_origins(self) -> list[str]:
        raw = self.cors_origins if self.cors_origins is not None else self.frontend_origin
        origins = [part.strip() for part in raw.split(",") if part.strip()]
        return origins or ["http://localhost:3000"]

    def build_verify_url(self, token: str, *, lang: str = "en") -> str:
        if "{token}" in self.verify_url_template:
            return self.verify_url_template.format(token=token, lang=lang)
        base = (
            self.verify_url_template.format(lang=lang)
            if "{lang}" in self.verify_url_template
            else self.verify_url_template
        )
        sep = "&" if "?" in base else "?"
        return f"{base}{sep}token={token}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


def sqlite_path_from_url(database_url: str) -> Path | None:
    if not database_url.startswith("sqlite:///"):
        return None
    raw_path = database_url.replace("sqlite:///", "", 1)
    return Path(raw_path)
