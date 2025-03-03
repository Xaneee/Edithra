# Firebase Sync Tests
from Edithra.backend.firebase_sync import update_realtime_data

def test_update_realtime_data():
    """Tests Firebase real-time database sync (Mock)."""
    result = update_realtime_data("/test", {"message": "Hello, Firebase!"})
    assert "Data updated at" in result




