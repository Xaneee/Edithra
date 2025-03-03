# AI-Driven Video Processing (Auto-Highlights, Smart Zoom, AI Thumbnail)
import cv2
import torch
import os
import numpy as np
from fastapi import UploadFile
from moviepy.editor import VideoFileClip
from ultralytics import YOLO

# Load AI Model (YOLO for Object & Action Detection)
model = YOLO("yolov8n.pt")

def extract_highlights(video_path: str, output_path: str):
    """Processes video to detect highlights and save a clipped version."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    highlight_frames = []
    
    for _ in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame)
        
        # Detect objects & actions, and mark highlight frames
        for r in results:
            if len(r.boxes) > 0:  # If objects detected
                highlight_frames.append(frame)
    
    for frame in highlight_frames:
        out.write(frame)
    
    cap.release()
    out.release()

def generate_thumbnail(video_path: str, thumbnail_path: str):
    """Extracts a thumbnail from the best highlight frame."""
    clip = VideoFileClip(video_path)
    best_frame_time = clip.duration / 2  # Pick a frame from the middle
    frame = clip.get_frame(best_frame_time)
    
    cv2.imwrite(thumbnail_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    return thumbnail_path




