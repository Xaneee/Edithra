# Text-to-Speech (TTS) using eSpeak
import os

def text_to_speech(text, output_file="output.wav"):
    """Converts text to speech using eSpeak."""
    command = f"espeak-ng '{text}' --stdout > {output_file}"
    os.system(command)
    return output_file




