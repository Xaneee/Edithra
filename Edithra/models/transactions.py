from sqlalchemy import Column, Integer, String, Float
from Edithra.database.db_setup import Base

class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    amount = Column(Float)
    status = Column(String, default="pending")


