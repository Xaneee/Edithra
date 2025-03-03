# AI Text Generation Tests
from Edithra.backend.ai_text_generation import generate_text

def test_generate_text():
    """Tests AI-generated text (Mock)."""
    result = generate_text("Tell me a joke.")
    assert isinstance(result, str) and len(result) > 0




