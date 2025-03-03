# AI Game Analytics Tests
import json
from fastapi.testclient import TestClient
from Edithra.backend.api_game_analytics import app

client = TestClient(app)

def test_game_report():
    """Tests AI-powered game analytics API."""
    response = client.get("/api/game-report")
    assert response.status_code == 200
    assert "total_events" in response.json()




