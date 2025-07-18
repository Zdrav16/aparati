from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.town import Town  # <-- коригирана импорта
from app.database import Base     # <-- използвай само един Base

class Org(Base):
    __tablename__ = 'org'

    id = Column(Integer, primary_key=True, autoincrement=True)
    corg = Column(String(100))
    address = Column(String(100))
    ntown = Column(Integer, ForeignKey('town.id'))
    bulstat = Column(String(20))
    tel = Column(String(30))
    mol = Column(String(50))
    position = Column(String(30))
    ntdd = Column(Integer)
    isegn = Column(Boolean)
    dds = Column(Boolean, default=True)

    town = relationship("Town", back_populates="orgs")
