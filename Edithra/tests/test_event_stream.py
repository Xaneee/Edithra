# Tests for AI Real-time Game Event Streaming
from fastapi.testclient import TestClient
from Edithra.backend.event_stream import app

client = TestClient(app)

def test_event_stream():
    """Tests event streaming API."""
    response = client.get("/stream")
    assert response.status_code == 200




