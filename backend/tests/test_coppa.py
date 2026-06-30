"""Plan 06 verification: COPPA / parental-consent gate for under-13 users."""

from __future__ import annotations

from sqlmodel import Session, select

from app.models.tables import User

GOOD_PASSWORD = "snakes123"


def test_minor_without_guardian_email_rejected(client):
    resp = client.post(
        "/auth/register",
        json={"email": "minor1@example.com", "password": GOOD_PASSWORD, "is_minor": True},
    )
    assert resp.status_code == 422
    assert resp.json()["detail"]["code"] == "parental_consent_required"


def test_minor_without_consent_rejected(client):
    resp = client.post(
        "/auth/register",
        json={
            "email": "minor2@example.com",
            "password": GOOD_PASSWORD,
            "is_minor": True,
            "guardian_email": "parent@example.com",
            "parental_consent": False,
        },
    )
    assert resp.status_code == 422
    assert resp.json()["detail"]["code"] == "parental_consent_required"


def test_minor_with_guardian_and_consent_ok(client, engine, mailer):
    resp = client.post(
        "/auth/register",
        json={
            "email": "minor3@example.com",
            "password": GOOD_PASSWORD,
            "is_minor": True,
            "guardian_email": "Parent@Example.com",
            "parental_consent": True,
        },
    )
    assert resp.status_code == 201, resp.text
    assert resp.json()["is_minor"] is True

    with Session(engine) as s:
        user = s.exec(select(User)).one()
    assert user.is_minor is True
    assert user.guardian_email == "parent@example.com"
    assert user.parental_consent is True
    assert user.parental_consent_at is not None

    # The confirmation email is addressed to the guardian, not the child.
    assert mailer.last.to == "parent@example.com"


def test_adult_registration_does_not_require_guardian(client, engine):
    resp = client.post(
        "/auth/register",
        json={"email": "adult@example.com", "password": GOOD_PASSWORD, "is_minor": False},
    )
    assert resp.status_code == 201
    with Session(engine) as s:
        user = s.exec(select(User)).one()
    assert user.is_minor is False
    assert user.parental_consent is False
