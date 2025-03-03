# AI Content Generation (GPT API)
import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_text(prompt):
    """Generates text using OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an AI content assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)




