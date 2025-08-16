from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Aparat(Base):
    __tablename__ = "aparati"

    id = Column(Integer, primary_key=True, index=True)
    kasa_no = Column(String(30))
    fp = Column(String(30))
    nmodel = Column(Integer, ForeignKey("model.id"))
    cobekt = Column(String(50))
    address = Column(String(100))
    ntown = Column(Integer, ForeignKey("town.id"))
    telefon = Column(String(30))
    aparat_imsi = Column(String(20))
    aparat_tel = Column(String(20))
    norg = Column(Integer, ForeignKey("org.id"))
    dn = Column(String(100))

    firm = relationship("Org", back_populates="aparati")
