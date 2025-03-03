# Tests for Cloud Storage Upload
from Edithra.backend.cloud_storage import upload_to_cloud

def test_upload():
    """Tests if a file can be uploaded to cloud storage."""
    result = upload_to_cloud("test_file.txt", "/tmp/test_file.txt")
    assert "s3.amazonaws.com" in result




