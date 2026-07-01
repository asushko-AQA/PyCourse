"""Password hashing and token generation (plan 06).

Passwords are hashed with Argon2id (memory-hard, the OWASP-recommended default).
Verification tokens are cryptographically random, URL-safe, and single-use.
No plaintext password is ever stored or logged.
"""

from __future__ import annotations

import secrets
import hashlib

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError

_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    """Return an Argon2id hash for `password` (includes salt + parameters)."""
    return _hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Return True if `password` matches the stored Argon2 hash."""
    try:
        return _hasher.verify(password_hash, password)
    except (VerifyMismatchError, InvalidHashError, ValueError):
        return False


def needs_rehash(password_hash: str) -> bool:
    """True if the hash was produced with outdated parameters."""
    try:
        return _hasher.check_needs_rehash(password_hash)
    except (InvalidHashError, ValueError):
        return True


def generate_verification_token() -> str:
    """A high-entropy, URL-safe, single-use email-verification token."""
    return secrets.token_urlsafe(32)


def generate_session_token() -> str:
    """A high-entropy opaque session token stored only in a cookie."""
    return secrets.token_urlsafe(32)


def hash_session_token(token: str) -> str:
    """Store only a deterministic hash of the opaque session token."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()
