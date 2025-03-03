# Video Utilities for Editing & Thumbnail Generation
import cv2
from moviepy.editor import VideoFileClip

def extract_thumbnail(video_path, thumbnail_path):
    """Extracts a thumbnail from the video"""
    clip = VideoFileClip(video_path)
    best_frame_time = clip.duration / 2
    frame = clip.get_frame(best_frame_time)
    
    cv2.imwrite(thumbnail_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    return thumbnail_path




