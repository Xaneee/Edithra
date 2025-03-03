# WebSocket Chat Server Tests
from fastapi.testclient import TestClient
from Edithra.backend.chat_server import app

client = TestClient(app)

def test_websocket_chat():
    """Tests WebSocket chat functionality."""
    with client.websocket_connect("/ws/chat") as websocket:
        websocket.send_text("Hello, world!")
        response = websocket.receive_text()
        assert response == "Hello, world!"




