from pydantic import BaseModel
from typing import Optional
from datetime import date

class SvidBase(BaseModel):
    nsvid: Optional[int] = None
    dsvid: date
    fd: Optional[str] = None
    fd_date: Optional[date] = None
    company: str
    company_address: str
    company_grad: str
    bulstat: str
    obekt: Optional[str] = None
    obekt_address: Optional[str] = None
    obekt_grad: Optional[str] = None
    mol: Optional[str] = None
    fp: Optional[str] = None
    dogno: Optional[int] = None
    kasa_no: Optional[str] = None
    dot: Optional[date] = None
    ddo: Optional[date] = None
    company_tel: Optional[str] = None
    cmodel: Optional[str] = None
    reshenie: Optional[str] = None
    rdate: Optional[date] = None
    dog_id: Optional[int] = None
    nfirma: Optional[int] = None
    czu: Optional[str] = None
    benz: Optional[str] = None
    deinost: Optional[str] = None
    isegn1: Optional[int] = 0
    niz: Optional[str] = None

class SvidCreate(SvidBase):
    pass

class SvidUpdate(SvidBase):
    pass

class SvidOut(SvidBase):
    id: int

    class Config:
        orm_mode = True
