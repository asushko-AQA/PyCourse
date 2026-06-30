"""Plan 06 verification: register + email verification flow."""

from __future__ import annotations

import re
from datetime import timedelta

from sqlmodel import select

from app.models.tables import EmailVerificationToken, User, now_utc

GOOD_PASSWORD = "snakes123"


def _token_from_link(text_body: str) -> str:
    match = re.search(r"token=([^\s&]+)", text_body)
    assert match, f"no token in email body:\n{text_body}"
    return match.group(1)


def test_register_creates_user_token_and_sends_link(client, engine, mailer):
    resp = client.post("/auth/register", json={"email": "Kid@Example.com", "password": GOOD_PASSWORD})
    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert body["verification_required"] is True
    assert body["email"] == "kid@example.com"  # normalized

    # A token row exists and the dev console "sent" a link containing it.
    from sqlmodel import Session

    with Session(engine) as s:
        tokens = s.exec(select(EmailVerificationToken)).all()
        assert len(tokens) == 1
        user = s.exec(select(User)).one()

    assert len(mailer.sent) == 1
    assert mailer.last.to == "kid@example.com"
    assert _token_from_link(mailer.last.text_body) == tokens[0].token

    # Password is stored only as a hash, never plaintext.
    assert user.password_hash != GOOD_PASSWORD
    assert user.password_hash.startswith("$argon2")
    assert user.email_verified_at is None


def test_register_rejects_duplicate_email(client):
    payload = {"email": "dup@example.com", "password": GOOD_PASSWORD}
    assert client.post("/auth/register", json=payload).status_code == 201
    resp = client.post("/auth/register", json=payload)
    assert resp.status_code == 409
    assert resp.json()["detail"]["code"] == "email_already_registered"


def test_register_rejects_weak_password(client):
    # Too short.
    r1 = client.post("/auth/register", json={"email": "a@example.com", "password": "ab1"})
    assert r1.status_code == 422
    assert r1.json()["detail"]["code"] == "weak_password"

    # No digit.
    r2 = client.post("/auth/register", json={"email": "b@example.com", "password": "onlyletters"})
    assert r2.status_code == 422
    assert r2.json()["detail"]["code"] == "weak_password"

    # Common password.
    r3 = client.post("/auth/register", json={"email": "c@example.com", "password": "password1"})
    assert r3.status_code == 422


def test_verify_sets_email_verified_at(client, engine, mailer):
    client.post("/auth/register", json={"email": "verify@example.com", "password": GOOD_PASSWORD})
    token = _token_from_link(mailer.last.text_body)

    resp = client.post("/auth/verify", json={"token": token})
    assert resp.status_code == 200, resp.text
    assert resp.json()["email"] == "verify@example.com"

    from sqlmodel import Session

    with Session(engine) as s:
        user = s.exec(select(User)).one()
        token_row = s.exec(select(EmailVerificationToken)).one()
    assert user.email_verified_at is not None
    assert token_row.consumed_at is not None


def test_verify_via_get_link(client, mailer):
    client.post("/auth/register", json={"email": "link@example.com", "password": GOOD_PASSWORD})
    token = _token_from_link(mailer.last.text_body)
    resp = client.get("/auth/verify", params={"token": token})
    assert resp.status_code == 200


def test_reused_token_rejected(client, mailer):
    client.post("/auth/register", json={"email": "reuse@example.com", "password": GOOD_PASSWORD})
    token = _token_from_link(mailer.last.text_body)
    assert client.post("/auth/verify", json={"token": token}).status_code == 200
    second = client.post("/auth/verify", json={"token": token})
    assert second.status_code == 410
    assert second.json()["detail"]["code"] == "token_used"


def test_invalid_token_rejected(client):
    resp = client.post("/auth/verify", json={"token": "not-a-real-token"})
    assert resp.status_code == 404
    assert resp.json()["detail"]["code"] == "invalid_token"


def test_expired_token_rejected(client, engine, mailer):
    client.post("/auth/register", json={"email": "expired@example.com", "password": GOOD_PASSWORD})
    token = _token_from_link(mailer.last.text_body)

    from sqlmodel import Session

    with Session(engine) as s:
        row = s.exec(select(EmailVerificationToken)).one()
        row.expires_at = now_utc() - timedelta(hours=1)
        s.add(row)
        s.commit()

    resp = client.post("/auth/verify", json={"token": token})
    assert resp.status_code == 410
    assert resp.json()["detail"]["code"] == "token_expired"
