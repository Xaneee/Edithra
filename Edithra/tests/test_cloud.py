# Cloud Storage Tests
from Edithra.backend.cloud_storage import upload_to_s3, upload_to_firebase

def test_upload_s3():
    """Tests AWS S3 file upload function"""
    result = upload_to_s3("test_file.txt")
    assert isinstance(result, str)

def test_upload_firebase():
    """Tests Firebase file upload function"""
    result = upload_to_firebase("test_file.txt")
    assert isinstance(result, str)




