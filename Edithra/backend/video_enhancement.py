# AI Video Enhancement
import cv2
import numpy as np
import torch
from moviepy.editor import VideoFileClip
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def enhance_video(video_path, output_path):
    """Processes video using AI for enhancements."""
    clip = VideoFileClip(video_path)
    new_clip = clip.fl_image(process_frame)
    new_clip.write_videofile(output_path, codec="libx264")
    
def process_frame(frame):
    """Applies AI processing to each frame."""
    results = model(frame)
    for r in results:
        if len(r.boxes) > 0:
            return cv2.putText(frame, "AI Enhanced", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    return frame




