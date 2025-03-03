# Logging Configuration
import os
from dotenv import load_dotenv

load_dotenv()

LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "Edithra/logs/app.log")
MONITORING_INTERVAL = int(os.getenv("MONITORING_INTERVAL", 5))




