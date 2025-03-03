# AI Text Generation Tests
from Edithra.backend.text_generation import generate_text

def test_generate_text():
    """Tests AI text generation function."""
    result = generate_text("Hello, AI!")
    assert isinstance(result, str)




