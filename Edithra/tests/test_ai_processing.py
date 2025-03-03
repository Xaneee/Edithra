# AI Processing Tests
import cv2
from Edithra.backend.ai_processing import detect_objects

def test_detect_objects():
    """Tests object detection on a sample image"""
    frame = cv2.imread("test.jpg")
    results = detect_objects(frame)
    assert results is not None




