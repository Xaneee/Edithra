# AI-Driven Game Notifications
from fastapi import FastAPI
from Edithra.backend.event_stream import publish_event

app = FastAPI()

notifications = []

@app.post("/notify")
def send_notification(message: str):
    """Sends AI-generated game notifications."""
    notifications.append(message)
    publish_event(message)
    return {"status": "Notification sent", "message": message}

@app.get("/notifications")
def get_notifications():
    """Fetches the list of AI notifications."""
    return {"notifications": notifications}




