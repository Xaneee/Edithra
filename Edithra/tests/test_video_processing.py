# Video Processing Tests
from Edithra.backend.video_processing import extract_highlights, generate_thumbnail

def test_extract_highlights():
    """Tests highlight extraction function"""
    extract_highlights("test_video.mp4", "output_highlight.mp4")
    assert os.path.exists("output_highlight.mp4")

def test_generate_thumbnail():
    """Tests thumbnail generation function"""
    generate_thumbnail("test_video.mp4", "thumbnail.jpg")
    assert os.path.exists("thumbnail.jpg")




