from fastapi.testclient import TestClient

from app.core.config import Settings, get_settings
from app.main import create_app


def test_allowed_cors_origins_parses_comma_separated_list():
    settings = Settings(
        cors_origins="https://app.example.com, http://localhost:3000",
    )
    assert settings.allowed_cors_origins == [
        "https://app.example.com",
        "http://localhost:3000",
    ]


def test_allowed_cors_origins_falls_back_to_frontend_origin():
    settings = Settings(frontend_origin="https://only-one.example")
    assert settings.allowed_cors_origins == ["https://only-one.example"]


def test_cors_origins_env_override(monkeypatch):
    monkeypatch.setenv("CORS_ORIGINS", "https://prod.example,https://staging.example")
    get_settings.cache_clear()
    try:
        settings = get_settings()
        assert settings.allowed_cors_origins == [
            "https://prod.example",
            "https://staging.example",
        ]
    finally:
        get_settings.cache_clear()


def test_cors_allows_configured_origin():
    settings = Settings(cors_origins="https://app.example.com")
    with TestClient(create_app(settings), base_url="https://app.example.com") as client:
        response = client.options(
            "/health",
            headers={
                "Origin": "https://app.example.com",
                "Access-Control-Request-Method": "GET",
            },
        )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "https://app.example.com"


def test_cors_rejects_unlisted_origin():
    settings = Settings(cors_origins="https://app.example.com")
    with TestClient(create_app(settings)) as client:
        response = client.options(
            "/health",
            headers={
                "Origin": "https://evil.example",
                "Access-Control-Request-Method": "GET",
            },
        )
    assert response.headers.get("access-control-allow-origin") != "https://evil.example"
