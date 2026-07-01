"""Plan 07 verification: sign-in/sign-out/session bootstrap flow."""

from __future__ import annotations

import re

from sqlmodel import Session, select

from app.models.tables import SessionRow

GOOD_PASSWORD = "snakes123"


def _token_from_link(text_body: str) -> str:
    match = re.search(r"token=([^\s&]+)", text_body)
    assert match, f"no token in email body:\n{text_body}"
    return match.group(1)


def _register_and_verify(client, mailer, *, email: str = "kid@example.com") -> None:
    register = client.post("/auth/register", json={"email": email, "password": GOOD_PASSWORD})
    assert register.status_code == 201
    token = _token_from_link(mailer.last.text_body)
    verify = client.post("/auth/verify", json={"token": token})
    assert verify.status_code == 200


def test_signin_signout_auth_checkpoint(client, engine, mailer):
    _register_and_verify(client, mailer)

    sign_in = client.post(
        "/auth/sign-in",
        json={"email": "kid@example.com", "password": GOOD_PASSWORD},
    )
    assert sign_in.status_code == 200, sign_in.text
    set_cookie = sign_in.headers.get("set-cookie", "").lower()
    assert "httponly" in set_cookie
    assert "secure" in set_cookie
    assert "samesite=lax" in set_cookie

    session_ok = client.get("/auth/session")
    assert session_ok.status_code == 200
    assert session_ok.json()["user"]["email"] == "kid@example.com"

    sign_out = client.post("/auth/sign-out")
    assert sign_out.status_code == 204

    session_denied = client.get("/auth/session")
    assert session_denied.status_code == 401
    assert session_denied.json()["detail"]["code"] == "unauthorized"

    # Reusing an old cookie value must not restore access (server-side revoke).
    with Session(engine) as s:
        assert s.exec(select(SessionRow)).all() == []


def test_unverified_user_cannot_sign_in(client):
    client.post("/auth/register", json={"email": "not-verified@example.com", "password": GOOD_PASSWORD})
    resp = client.post(
        "/auth/sign-in",
        json={"email": "not-verified@example.com", "password": GOOD_PASSWORD},
    )
    assert resp.status_code == 403
    assert resp.json()["detail"]["code"] == "email_not_verified"


def test_rate_limit_after_repeated_bad_passwords(client, mailer):
    _register_and_verify(client, mailer, email="ratelimit@example.com")

    for _ in range(5):
        resp = client.post(
            "/auth/sign-in",
            json={"email": "ratelimit@example.com", "password": "wrongpass1"},
        )
        assert resp.status_code == 401
        assert resp.json()["detail"]["code"] == "invalid_credentials"

    blocked = client.post(
        "/auth/sign-in",
        json={"email": "ratelimit@example.com", "password": "wrongpass1"},
    )
    assert blocked.status_code == 429
    assert blocked.json()["detail"]["code"] == "too_many_attempts"
