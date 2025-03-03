# AI-Powered Real-time Game Event Streaming
import asyncio
from fastapi import FastAPI
from starlette.responses import StreamingResponse

app = FastAPI()
event_queue = asyncio.Queue()

async def event_generator():
    """Yields real-time game events."""
    while True:
        event = await event_queue.get()
        yield f"data: {event}\n\n"

@app.get("/stream")
async def stream():
    """Real-time event streaming endpoint."""
    return StreamingResponse(event_generator(), media_type="text/event-stream")

def publish_event(event_data):
    """Publishes a new event to the stream."""
    event_queue.put_nowait(event_data)




