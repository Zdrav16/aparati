from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class Dogovor(Base):
    __tablename__ = "dogovor"

    id = Column(Integer, primary_key=True, index=True)
    dog_no = Column(Integer)
    kasa_no = Column(String(30))
    nfirma = Column(Integer, ForeignKey("org.id"))
    dot = Column(Date)
    ddo = Column(Date)
    price = Column(Numeric(10, 2))
    prekrat = Column(Date)
    prichina = Column(String(100))
    company = Column(String(100))
    bulstat = Column(String(20))
    company_address = Column(String(100))
    company_grad = Column(String(100))
    obekt = Column(String(50))
    obekt_address = Column(String(100))
    obekt_grad = Column(String(100))
    company_tel = Column(String(30))
    company_mol = Column(String(50))
    fp = Column(String(30))
    isprekrat = Column(Boolean, default=False)

    firm = relationship("Org", back_populates="dogovori")
    svid = relationship("Svid", back_populates="dogovor")
