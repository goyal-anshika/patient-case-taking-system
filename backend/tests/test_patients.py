from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register_user():
    response = client.post(
        "/api/auth/register",
        json={
            "full_name": "Test Doctor",
            "email": "testdoctor@example.com",
            "password": "TestDoctor@123",
            "role": "doctor",
        },
    )

    assert response.status_code in [200, 400]