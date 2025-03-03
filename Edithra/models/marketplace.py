from sqlalchemy import Column, Integer
from ..database import Base

class Marketplace(Base):
    __tablename__ = "marketplace"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    item_id = Column(Integer)


