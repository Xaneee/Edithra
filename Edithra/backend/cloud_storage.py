# AI Cloud Storage Integration
import boto3
import os

S3_BUCKET = os.getenv("S3_BUCKET_NAME", "mock-bucket")
s3 = boto3.client("s3")

def upload_to_cloud(filename, file_path):
    """Uploads a file to cloud storage."""
    s3.upload_file(file_path, S3_BUCKET, filename)
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{filename}"




