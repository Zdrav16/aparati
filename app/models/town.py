from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Town(Base):
    __tablename__ = "town"

    id = Column(Integer, primary_key=True, index=True)
    ctown = Column(String(30), unique=True)
    orgs = relationship("Org", back_populates="town")
