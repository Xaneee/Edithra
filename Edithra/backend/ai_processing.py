from fastapi import APIRouter, UploadFile, File, HTTPException
import cv2
import torch
import numpy as np
from ultralytics import YOLO
import tempfile
import os

# Initialize FastAPI router
router = APIRouter()

# Load YOLOv8 model once (global scope for efficiency)
model = YOLO("yolov8n.pt")

def detect_objects(frame):
    """Detect objects in a video frame using YOLOv8"""
    results = model(frame)
    return results

def process_video(video_path, output_path):
    """Process video and extract highlight frames with AI"""
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError("Error: Could not open video file")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frame_count = 0
    detected_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        results = detect_objects(frame)

        for r in results:
            if len(r.boxes) > 0:
                out.write(frame)
                detected_frames += 1

    cap.release()
    out.release()
    
    return {"total_frames": frame_count, "detected_highlights": detected_frames, "output_path": output_path}

@router.post("/process-video/")
async def process_uploaded_video(file: UploadFile = File(...)):
    """API Endpoint: Upload a video and process it"""
    try:
        # Save uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
            temp_input.write(await file.read())
            input_path = temp_input.name
        
        output_path = input_path.replace(".mp4", "_output.mp4")

        # Process video with AI
        result = process_video(input_path, output_path)

        # Cleanup: Remove temp input video
        os.remove(input_path)

        return {"message": "Video processed successfully", "data": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


