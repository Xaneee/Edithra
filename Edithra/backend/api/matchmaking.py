from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.leaderboard import Leaderboard

router = APIRouter(prefix="/matchmaking", tags=["matchmaking"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/skill-based/{user_id}")
def skill_based_matchmaking(user_id: int, db: Session = Depends(get_db)):
    player = db.query(Leaderboard).filter(Leaderboard.id == user_id).first()
    
    if not player:
        return {"message": "Player not found"}
    
    # Find similar skill level players
    matched_players = db.query(Leaderboard).filter(
        Leaderboard.score.between(player.score - 50, player.score + 50)
    ).limit(5).all()
    
    return {"matched_players": matched_players}


