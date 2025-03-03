# AI Speech Synthesis
import pyttsx3

engine = pyttsx3.init()

def text_to_speech(text, output_file="output.mp3"):
    """Converts text into speech and saves it as an audio file."""
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file




