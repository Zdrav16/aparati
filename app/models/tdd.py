from sqlalchemy import Column, Integer, String
from app.database import Base

class Tdd(Base):
    __tablename__ = "tdd"

    id = Column(Integer, primary_key=True, index=True)
    tddnap = Column(String(20))         # Име на ТДД (например "ПАЗАРДЖИК")
    tddaddress = Column(String(100))    # Адрес на ТДД
