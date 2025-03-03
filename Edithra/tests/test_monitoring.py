# Tests for System Monitoring
from Edithra.backend.monitoring import monitor_system

def test_monitoring():
    """Runs a short monitoring session to test logging."""
    monitor_system()
    with open("Edithra/logs/monitoring.log", "r") as file:
        assert "CPU:" in file.read()




