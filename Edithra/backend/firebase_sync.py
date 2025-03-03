# Firebase Integration for Real-time Data Sync
import firebase_admin
from firebase_admin import credentials, db
import os

FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")

cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("FIREBASE_DATABASE_URL")})

def update_realtime_data(ref_path, data):
    """Updates data in Firebase Realtime Database."""
    ref = db.reference(ref_path)
    ref.set(data)
    return f"Data updated at {ref_path}"




