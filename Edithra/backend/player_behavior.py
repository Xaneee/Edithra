# Player Behavior Analysis
import json

def analyze_behavior(logs):
    """Analyzes player behavior patterns from game logs."""
    actions = [log["action"] for log in logs]
    action_counts = {action: actions.count(action) for action in set(actions)}
    
    return {
        "most_frequent_action": max(action_counts, key=action_counts.get),
        "action_distribution": action_counts
    }




