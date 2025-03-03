# AI-Powered Text Generation
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt, max_length=100):
    """Generates AI-powered text."""
    response = generator(prompt, max_length=max_length, num_return_sequences=1)
    return response[0]["generated_text"]




