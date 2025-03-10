from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Edithra.database.db_setup import SessionLocal
from Edithra.models.friends import Friends
from Edithra.database.db_setup import Base

router = APIRouter(prefix="/friends", tags=["friends"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
def add_friend(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    friendship = Friends(user_id=user_id, friend_id=friend_id)
    db.add(friendship)
    db.commit()
    return {"message": "Friend added"}


class Friends(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    friend_id = Column(Integer)

