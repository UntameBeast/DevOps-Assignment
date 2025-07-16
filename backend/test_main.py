from fastapi.testclient import TestClient
import sys
import os

# Add backend directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app  # Now this will work

client = TestClient(app)

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_message():
    response = client.get("/api/message")
    assert response.status_code == 200
    assert "message" in response.json()
