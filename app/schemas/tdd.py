from pydantic import BaseModel
from typing import Optional

class TddBase(BaseModel):
    tddnap: Optional[str] = None
    tddaddress: Optional[str] = None

class TddCreate(TddBase):
    pass

class TddUpdate(TddBase):
    pass

class TddOut(TddBase):
    id: int

    class Config:
        orm_mode = True
