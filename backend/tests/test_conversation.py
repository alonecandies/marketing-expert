import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    email = "convuser@example.com"
    password = "testpass123"
    client.post("/auth/signup", json={"email": email, "password": password})
    resp = client.post("/auth/login", json={"email": email, "password": password})
    return resp.json()["access_token"]

def test_conversation_flow():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    # Start conversation
    resp = client.post("/conversations/start", headers=headers)
    assert resp.status_code == 200
    conv_id = resp.json()["conversation_id"]
    # Send message
    resp = client.post(f"/conversations/{conv_id}/message", headers=headers, json={"role": "user", "content": "Hello"})
    assert resp.status_code == 200
    # AI chat
    resp = client.post(f"/ai/chat/{conv_id}", headers=headers)
    assert resp.status_code == 200
    assert "response" in resp.json()
