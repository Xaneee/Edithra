# AI Speech Synthesis Tests
from Edithra.backend.speech_synthesis import text_to_speech

def test_text_to_speech():
    """Tests AI speech synthesis function."""
    result = text_to_speech("Testing speech synthesis", "test_output.mp3")
    assert result == "test_output.mp3"




