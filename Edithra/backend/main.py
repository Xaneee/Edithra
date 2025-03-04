from fastapi import FastAPI
from Edithra.backend.api.ai_recommendations import router as ai_recommendations_router
from Edithra.backend.api.matchmaking import router as matchmaking_router
from Edithra.backend.api.video_processing import router as video_router
from Edithra.backend.api.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
import uvicorn

app = FastAPI(title="Edithra Backend", version="1.0")

# Include API routers
app.include_router(ai_recommendations_router)
app.include_router(matchmaking_router)
app.include_router(video_router)
app.include_router(auth_router)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logging.info("🚀 Edithra Backend is starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("🛑 Shutting down Edithra Backend...")

@app.get("/")
def read_root():
    return {"message": "Hello from Edithra Backend!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Default to 10000 for Render
    uvicorn.run(app, host="0.0.0.0", port=port)


