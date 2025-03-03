from sqlalchemy import Column, Integer, String, Float
from Edithra.database.db_setup import Base

class Leaderboard(Base):
    __tablename__ = "leaderboard"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    score = Column(Float, default=0.0)
    rank = Column(Integer)


