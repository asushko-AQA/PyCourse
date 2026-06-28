from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint_reports_db_ok(app_db_url: str) -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["db"]["ok"] is True
    assert payload["db"]["journal_mode"] == "wal"
