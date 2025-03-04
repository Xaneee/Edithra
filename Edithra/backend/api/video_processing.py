# Video Processing API
from fastapi import APIRouter, UploadFile, File
import cv2
import os
from backend.ai_processing import AIProcessor

router = APIRouter()
ai_processor = AIProcessor()

@router.post("/process-video/")
async def process_video(file: UploadFile = File(...)):
    video_path = f"videos/{file.filename}"
    os.makedirs("videos", exist_ok=True)
    with open(video_path, "wb") as buffer:
        buffer.write(file.file.read())

    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = ai_processor.analyze_frame(frame)
        frames.append(results)

    cap.release()
    return {"message": "Processing complete", "frames_analyzed": len(frames)}




