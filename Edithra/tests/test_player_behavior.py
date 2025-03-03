# Player Behavior Analysis Tests
from Edithra.backend.player_behavior import analyze_behavior

def test_analyze_behavior():
    """Tests player behavior analysis function."""
    logs = [{"action": "jump"}, {"action": "shoot"}, {"action": "jump"}]
    result = analyze_behavior(logs)
    
    assert "most_frequent_action" in result and "action_distribution" in result




