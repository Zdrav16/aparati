from pydantic import BaseModel
from typing import Optional
from datetime import date

class DogovorBase(BaseModel):
    dog_no: int
    kasa_no: str
    nfirma: int
    dot: date
    ddo: date
    price: Optional[int] = 0
    prekrat: Optional[date] = None
    prichina: Optional[str] = None
    company: str
    bulstat: str
    company_address: str
    company_grad: str
    obekt: Optional[str] = None
    obekt_address: Optional[str] = None
    obekt_grad: Optional[str] = None
    company_tel: Optional[str] = None
    company_mol: Optional[str] = None
    fp: Optional[str] = None
    isprekrat: Optional[int] = 0

class DogovorCreate(DogovorBase):
    pass

class DogovorUpdate(DogovorBase):
    pass

class DogovorOut(DogovorBase):
    id: int

    class Config:
        orm_mode = True

# 🔹 нова схема за справка
class DogovorReportOut(BaseModel):
    firma_name: str
    bulstat: str
    tel: Optional[str] = None
    ddo: date
    kasa_no: str
    fdrid: Optional[str] = None
    model: Optional[str] = None

    class Config:
        orm_mode = True
