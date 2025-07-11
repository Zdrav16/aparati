from sqlalchemy import Column, Integer, String
from app.database import Base

class Town(Base):
    __tablename__ = "town"

    id = Column(Integer, primary_key=True, index=True)
    ctown = Column(String(30), unique=True)
