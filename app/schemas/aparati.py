from pydantic import BaseModel
from typing import Optional

class AparatBase(BaseModel):
    kasa_no: Optional[str] = None
    fp: Optional[str] = None
    nmodel: Optional[int] = None
    cobekt: Optional[str] = None
    address: Optional[str] = None
    ntown: Optional[int] = None
    telefon: Optional[str] = None
    aparat_imsi: Optional[str] = None
    aparat_tel: Optional[str] = None
    norg: Optional[int] = None
    dn: Optional[str] = None

class AparatCreate(AparatBase):
    pass

class AparatOut(AparatBase):
    id: int
    class Config:
        from_attributes = True

class AparatUpdate(BaseModel):
    kasa_no: Optional[str] = None
    fp: Optional[str] = None
    nmodel: Optional[int] = None
    cobekt: Optional[str] = None
    address: Optional[str] = None
    ntown: Optional[int] = None
    telefon: Optional[str] = None
    aparat_imsi: Optional[str] = None
    aparat_tel: Optional[str] = None
    norg: Optional[int] = None
    dn: Optional[str] = None
