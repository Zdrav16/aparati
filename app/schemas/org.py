from pydantic import BaseModel
from typing import Optional

class OrgBase(BaseModel):
    corg: str
    address: str
    ntown: int
    bulstat: str
    tel: Optional[str] = None
    mol: Optional[str] = None
    position: Optional[str] = None
    ntdd: Optional[int] = None
    isegn: Optional[int] = 0
    dds: Optional[int] = 1

class OrgCreate(OrgBase):
    pass

class OrgUpdate(OrgBase):
    pass

class OrgOut(OrgBase):
    id: int

    class Config:
        from_attributes = True
