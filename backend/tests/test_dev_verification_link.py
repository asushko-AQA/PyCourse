"""DEV/console-only verification-link helper (Railway smoke testing)."""

from __future__ import annotations

import re

from app.core.config import Settings, get_settings
from app.main import app

GOOD_PASSWORD = "snakes123"


def _token_from_link(text_body: str) -> str:
    match = re.search(r"token=([^\s&]+)", text_body)
    assert match, f"no token in email body:\n{text_body}"
    return match.group(1)


def test_dev_verification_link_hidden_when_not_console(client):
    smtp_settings = Settings(
        database_url="sqlite://",
        email_backend="smtp",
        verify_url_template="http://testserver/en/auth/verify?token={token}",
    )
    app.dependency_overrides[get_settings] = lambda: smtp_settings

    resp = client.get("/auth/dev/verification-link", params={"email": "any@example.com"})
    assert resp.status_code == 404
    assert resp.json()["detail"]["code"] == "not_found"


def test_dev_verification_link_returns_latest_active_token(client, mailer, test_settings):
    register = client.post(
        "/auth/register",
        json={"email": "smoke@example.com", "password": GOOD_PASSWORD},
    )
    assert register.status_code == 201

    expected_token = _token_from_link(mailer.last.text_body)
    expected_url = test_settings.build_verify_url(expected_token)

    resp = client.get("/auth/dev/verification-link", params={"email": "smoke@example.com"})
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body == {
        "email": "smoke@example.com",
        "verify_url": expected_url,
        "token": expected_token,
    }
