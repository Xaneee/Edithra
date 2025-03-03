# Deployment Settings
import os

DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///Edithra/database/gamesync.db")

def get_database_config():
    return {"url": DATABASE_URL}




