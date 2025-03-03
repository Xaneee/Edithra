# Tests for Logging System
from Edithra.backend.logger import log_event

def test_logging():
    """Tests if logs are being recorded properly."""
    log_event("info", "Test Log Entry")
    with open("Edithra/logs/app.log", "r") as file:
        assert "Test Log Entry" in file.read()




