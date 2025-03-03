from fastapi import APIRouter
import os
from ..config import GPU_SCALING_API_KEY

router = APIRouter(prefix="/gpu", tags=["gpu"])

@router.get("/status")
def gpu_status():
    return {"status": "GPU Scaling Active", "current_load": os.getenv("GPU_LOAD", "N/A")}



