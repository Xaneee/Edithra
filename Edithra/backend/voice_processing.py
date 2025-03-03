# AI-Powered Voice Command System
import speech_recognition as sr
import pyttsx3

# Initialize speech recognition & text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def recognize_speech(audio_file):
    """Convert speech to text"""
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError:
            return "Speech recognition service unavailable"

def speak_text(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()




