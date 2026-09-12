"""Unit tests for Settings.build_verify_url template substitution."""

from __future__ import annotations

from app.core.config import Settings


def test_build_verify_url_with_fixed_lang_segment() -> None:
    settings = Settings(
        verify_url_template="http://localhost:3000/en/auth/verify?token={token}",
    )

    assert (
        settings.build_verify_url("abc123")
        == "http://localhost:3000/en/auth/verify?token=abc123"
    )


def test_build_verify_url_with_lang_placeholder_defaults_to_en() -> None:
    settings = Settings(
        verify_url_template="https://app.example.com/{lang}/auth/verify?token={token}",
    )

    assert (
        settings.build_verify_url("abc123")
        == "https://app.example.com/en/auth/verify?token=abc123"
    )


def test_build_verify_url_with_lang_placeholder_uses_explicit_lang() -> None:
    settings = Settings(
        verify_url_template="https://app.example.com/{lang}/auth/verify?token={token}",
    )

    assert (
        settings.build_verify_url("abc123", lang="ru")
        == "https://app.example.com/ru/auth/verify?token=abc123"
    )


def test_build_verify_url_fallback_appends_token_when_template_has_lang_only() -> None:
    settings = Settings(
        verify_url_template="https://app.example.com/{lang}/auth/verify",
    )

    assert (
        settings.build_verify_url("abc123", lang="ru")
        == "https://app.example.com/ru/auth/verify?token=abc123"
    )
