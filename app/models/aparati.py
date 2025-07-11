from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Aparat(Base):
    __tablename__ = "aparati"

    id = Column(Integer, primary_key=True, index=True)
    kasa_no = Column(String(20))
    fp = Column(String(20))
    nmodel = Column(Integer, ForeignKey("model.id"))
    cobekt = Column(String(30))
    address = Column(String(30))
    ntown = Column(Integer, ForeignKey("town.id"))
    telefon = Column(String(20))
    aparat_imsi = Column(String(14))
    aparat_tel = Column(String(13))
    norg = Column(Integer, ForeignKey("org.id"))
    dn = Column(String(80))
