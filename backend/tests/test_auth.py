import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_and_login():
    email = "testuser@example.com"
    password = "testpass123"
    # Signup
    resp = client.post("/auth/signup", json={"email": email, "password": password})
    assert resp.status_code == 200
    # Login
    resp = client.post("/auth/login", json={"email": email, "password": password})
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
