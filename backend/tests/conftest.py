from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.api.deps import auth_service, db_session, email_sender
from app.core.config import Settings, get_settings
from app.main import app
from app.repositories.email_verification_repo import EmailVerificationTokenRepo
from app.repositories.user_repo import UserRepo
from app.services.auth_service import AuthService
from app.services.email.base import EmailMessage


class RecordingEmailSender:
    """Captures sent messages so tests can read the verification link."""

    def __init__(self) -> None:
        self.sent: list[EmailMessage] = []

    def send(self, message: EmailMessage) -> None:
        self.sent.append(message)

    @property
    def last(self) -> EmailMessage:
        return self.sent[-1]


@pytest.fixture(name="engine")
def engine_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture(name="session")
def session_fixture(engine):
    with Session(engine) as session:
        yield session


@pytest.fixture(name="test_settings")
def settings_fixture() -> Settings:
    return Settings(
        database_url="sqlite://",
        email_backend="console",
        verify_url_template="http://testserver/en/auth/verify?token={token}",
        email_verification_ttl_hours=24,
        password_min_length=8,
    )


@pytest.fixture(name="mailer")
def mailer_fixture() -> RecordingEmailSender:
    return RecordingEmailSender()


@pytest.fixture(name="client")
def client_fixture(engine, mailer, test_settings):
    def override_db_session():
        with Session(engine) as session:
            yield session

    def override_email_sender():
        return mailer

    def override_settings():
        return test_settings

    def override_auth_service():
        with Session(engine) as session:
            yield AuthService(
                users=UserRepo(session),
                tokens=EmailVerificationTokenRepo(session),
                email_sender=mailer,
                settings=test_settings,
            )

    app.dependency_overrides[db_session] = override_db_session
    app.dependency_overrides[email_sender] = override_email_sender
    app.dependency_overrides[get_settings] = override_settings
    app.dependency_overrides[auth_service] = override_auth_service

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
