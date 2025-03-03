# Text-to-Speech Tests
from Edithra.backend.text_to_speech import text_to_speech
import os

def test_text_to_speech():
    """Tests text-to-speech function."""
    output_file = text_to_speech("Hello, this is a test.")
    assert os.path.exists(output_file)




