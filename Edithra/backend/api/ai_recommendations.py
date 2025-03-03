from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import redis
import json
from backend.database.db_setup import SessionLocal

router = APIRouter(prefix="/ai", tags=["ai"])
redis_client = redis.Redis(host="localhost", port=6379, db=0)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/recommendations/{user_id}")
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    cache_key = f"recommendations:{user_id}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    recommendations = {
        "user_id": user_id,
        "recommended_games": ["Game A", "Game B", "Game C"],
        "tips": "Try focusing on strategy and quick reflexes."
    }

    redis_client.setex(cache_key, 3600, json.dumps(recommendations))
    return recommendations



