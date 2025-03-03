# FastAPI Analytics API for Game Insights
from fastapi import FastAPI
from Edithra.backend.game_analytics import GameAnalytics

app = FastAPI()
analytics = GameAnalytics()

@app.get("/api/game-report")
def game_report():
    """Returns AI-generated game performance report."""
    return analytics.generate_report()




