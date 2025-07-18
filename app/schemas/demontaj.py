from pydantic import BaseModel
from typing import Optional
from datetime import date

class DemontajBase(BaseModel):
    pdate: Optional[date]
    dot: Optional[date]
    ddo: Optional[date]
    kasa_no: Optional[str]
    fp: Optional[str]
    norg: Optional[int]
    cfirma: Optional[str]
    mol: Optional[str]
    bulstat: Optional[str]
    isegn: Optional[int]
    fdread: Optional[str]
    reason: Optional[str]
    cmodel: Optional[str]
    reshenie: Optional[str]
    rdate: Optional[date]
    time: Optional[str]
    g1: Optional[str]
    g2: Optional[str]
    g3: Optional[str]
    g4: Optional[str]
    address: Optional[str]

class DemontajCreate(DemontajBase):
    pass

class DemontajUpdate(DemontajBase):
    pass

class DemontajOut(DemontajBase):
    id: int

    class Config:
        orm_mode = True
