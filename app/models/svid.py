from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class Svid(Base):
    __tablename__ = "svid"

    id = Column(Integer, primary_key=True, index=True)
    dog_id = Column(Integer, ForeignKey("dogovor.id"))
    nfirma = Column(Integer, ForeignKey("org.id"))
    nsvid = Column(Integer)
    dsvid = Column(Date)
    fd = Column(String(30))
    fd_date = Column(Date)
    company = Column(String(100))
    company_address = Column(String(100))
    company_grad = Column(String(100))
    bulstat = Column(String(20))
    obekt = Column(String(50))
    obekt_address = Column(String(100))
    obekt_grad = Column(String(100))
    mol = Column(String(50))
    fp = Column(String(20))
    dogno = Column(Integer)
    kasa_no = Column(String(30))
    dot = Column(Date)
    ddo = Column(Date)
    company_tel = Column(String(30))
    cmodel = Column(String(100))
    reshenie = Column(String(50))
    rdate = Column(Date)
    czu = Column(String(30))
    benz = Column(String(30))
    deinost = Column(String(50))
    isegn1 = Column(Boolean)
    niz = Column(String(100))

    dogovor = relationship("Dogovor", back_populates="svid")
