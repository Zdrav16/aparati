from sqlalchemy import Column, Integer, String
from app.database import Base

class Tehnik(Base):
    __tablename__ = "tehnik"

    id = Column(Integer, primary_key=True, index=True)
    ctehnik = Column(String(40))  # Име на техника
    egn = Column(String(10))      # ЕГН или ЛНЧ
