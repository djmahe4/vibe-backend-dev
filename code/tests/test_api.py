from fastapi.testclient import TestClient

from app.main import create_app


def test_health() -> None:
    client = TestClient(create_app())
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_docs_disabled_by_default() -> None:
    client = TestClient(create_app())
    response = client.get("/docs")
    assert response.status_code == 404


def test_login_and_protected_flow() -> None:
    client = TestClient(create_app())
    login = client.post(
        "/api/v1/auth/token",
        json={"username": "admin", "password": "ChangeThisNow!123"},
    )
    assert login.status_code == 200
    token = login.json()["access_token"]

    protected = client.post(
        "/api/v1/vibe/intent",
        json={"intent": "Generate a typed endpoint for tenant metrics"},
        headers={"Authorization": "Bearer " + token},
    )
    assert protected.status_code == 200
    assert "security_notes" in protected.json()


def test_invalid_login() -> None:
    client = TestClient(create_app())
    response = client.post(
        "/api/v1/auth/token",
        json={"username": "admin", "password": "wrong-password-000"},
    )
    assert response.status_code == 401
