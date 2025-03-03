# User Authentication System (JWT + OAuth)
import os
import jwt
import datetime
import bcrypt
from fastapi import HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer
from Edithra.database.db_connection import get_db_connection
from fastapi import APIRouter
router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY", "mock_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_token(data: dict):
    """Generates a JWT token"""
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Security(oauth2_scheme)):
    """Verifies a JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def hash_password(password: str):
    """Hashes a password using bcrypt"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str):
    """Verifies a password hash"""
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_user(username: str, password: str):
    """Creates a new user in the database"""
    conn = get_db_connection()
    cur = conn.cursor()
    hashed_password = hash_password(password)
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    cur.close()
    conn.close()




