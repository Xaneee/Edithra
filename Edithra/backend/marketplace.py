from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.marketplace import Marketplace

router = APIRouter(prefix="/marketplace", tags=["marketplace"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/buy")
def buy_item(user_id: int, item_id: int, db: Session = Depends(get_db)):
    purchase = Marketplace(user_id=user_id, item_id=item_id)
    db.add(purchase)
    db.commit()
    return {"message": "Item purchased"}


