from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    email = "topupuser@example.com"
    password = "testpass123"
    client.post("/auth/signup", json={"email": email, "password": password})
    resp = client.post("/auth/login", json={"email": email, "password": password})
    return resp.json()["access_token"]

def test_topup():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    # Top up credits
    resp = client.post("/auth/topup", headers=headers, json={"amount": 50})
    assert resp.status_code == 200
    data = resp.json()
    assert data["credits"] >= 50
