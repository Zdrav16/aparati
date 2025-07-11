from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Dogovor(Base):
    __tablename__ = "dogovor"

    id = Column(Integer, primary_key=True, index=True)
    dog_no = Column(Integer)
    kasa_no = Column(String(20))
    nfirma = Column(Integer, ForeignKey("org.id"))
    dot = Column(Date)  # Дата на започване
    ddo = Column(Date)  # Дата на приключване
    price = Column(Integer)
    prekrat = Column(Date, nullable=True)  # Дата на прекратяване
    prichina = Column(String(50), nullable=True)
    company = Column(String(50))
    bulstat = Column(String(15))
    company_address = Column(String(50))
    company_grad = Column(String(30))
    obekt = Column(String(30))
    obekt_address = Column(String(30))
    obekt_grad = Column(String(30))
    company_tel = Column(String(20))
    company_mol = Column(String(50))
    fp = Column(String(20))
    isprekrat = Column(Integer, default=0)
