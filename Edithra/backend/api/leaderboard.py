from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.leaderboard import Leaderboard

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_leaderboard(db: Session = Depends(get_db)):
    return db.query(Leaderboard).order_by(Leaderboard.score.desc()).limit(10).all()

@router.post("/update")
def update_leaderboard(username: str, score: float, db: Session = Depends(get_db)):
    player = db.query(Leaderboard).filter(Leaderboard.username == username).first()
    if player:
        player.score = score
    else:
        player = Leaderboard(username=username, score=score)
        db.add(player)
    db.commit()
    return {"message": "Score updated"}


