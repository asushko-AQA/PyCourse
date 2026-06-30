"""Request/response models for the registration + verification flow (plan 06)."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)
    # COPPA gate: a self-declared "I am under 13" checkbox. When true the
    # guardian fields below are required (enforced in the service layer).
    is_minor: bool = False
    guardian_email: EmailStr | None = None
    parental_consent: bool = False


class RegisterResponse(BaseModel):
    user_id: str
    email: EmailStr
    verification_required: bool = True
    # Echoes whether parental consent was recorded, so the client can show the
    # right "check your (guardian's) email" copy.
    is_minor: bool = False


class VerifyRequest(BaseModel):
    token: str = Field(min_length=1)


class VerifyResponse(BaseModel):
    email: EmailStr
    email_verified_at: datetime
