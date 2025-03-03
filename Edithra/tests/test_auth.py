# Unit Tests for Authentication System
from Edithra.backend.auth import hash_password, verify_password, create_token, verify_token

def test_password_hashing():
    """Tests password hashing and verification"""
    password = "securepassword"
    hashed = hash_password(password)
    assert verify_password(password, hashed)

def test_token_creation():
    """Tests JWT token creation and validation"""
    token = create_token({"user_id": 1})
    payload = verify_token(token)
    assert payload["user_id"] == 1




