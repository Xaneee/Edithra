# Security Configuration
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
HASHING_ALGORITHM = "HS256"

def get_secret_key():
    return SECRET_KEY




