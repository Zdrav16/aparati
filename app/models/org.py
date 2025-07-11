from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .town import Town
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    town = relationship('Town')