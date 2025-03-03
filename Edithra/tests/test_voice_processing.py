# Voice Processing Tests
from Edithra.backend.voice_processing import recognize_speech, speak_text
import os

def test_recognize_speech():
    """Tests speech recognition function"""
    result = recognize_speech("test_audio.wav")
    assert isinstance(result, str)

def test_speak_text():
    """Tests text-to-speech function"""
    try:
        speak_text("Hello, this is a test")
        assert True
    except Exception:
        assert False




