# Cloud AI Configuration
import os
from dotenv import load_dotenv

load_dotenv()

CLOUD_AI_API = os.getenv("CLOUD_AI_API", "https://api.mock-cloud-ai.com/analyze")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "mock-bucket")




