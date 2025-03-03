# AI-Powered Game Analytics Module
import pandas as pd
import json

class GameAnalytics:
    """Processes and analyzes game data for insights."""
    
    def __init__(self, data_file="Edithra/data/game_data.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self):
        """Loads game data from JSON file."""
        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        """Saves updated game data to JSON file."""
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def record_event(self, player_id, event_type, details):
        """Logs an in-game event with AI-enhanced tracking."""
        event = {
            "player_id": player_id,
            "event_type": event_type,
            "details": details
        }
        self.data.append(event)
        self.save_data()

    def generate_report(self):
        """Generates AI-driven game performance reports."""
        df = pd.DataFrame(self.data)
        if df.empty:
            return "No data available."

        event_counts = df["event_type"].value_counts().to_dict()
        return {
            "total_events": len(df),
            "event_breakdown": event_counts
        }




