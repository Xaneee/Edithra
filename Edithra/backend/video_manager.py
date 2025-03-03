from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import cv2
from moviepy.editor import VideoFileClip
from ultralytics import YOLO

router = APIRouter()
model = YOLO("yolov8n.pt")

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video file")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    detected_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame)

        for r in results:
            if len(r.boxes) > 0:
                out.write(frame)
                detected_frames += 1

    cap.release()
    out.release()
    return {"detected_highlights": detected_frames, "output_path": output_path}

@router.post("/process-video/")
async def process_uploaded_video(file: UploadFile = File(...)):
    try:
        video_path = f"Edithra/uploads/{file.filename}"
        os.makedirs("Edithra/uploads", exist_ok=True)

        with open(video_path, "wb") as buffer:
            buffer.write(await file.read())

        output_path = video_path.replace(".mp4", "_output.mp4")
        result = process_video(video_path, output_path)

        os.remove(video_path)
        return {"message": "Video processed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


