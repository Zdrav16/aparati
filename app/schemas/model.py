from pydantic import BaseModel
from typing import Optional
from datetime import date

class ModelBase(BaseModel):
    cmodel: str
    reshenie: Optional[str] = None
    rdate: Optional[date] = None

class ModelCreate(ModelBase):
    pass

class ModelUpdate(ModelBase):
    pass

class ModelOut(ModelBase):
    id: int

    class Config:
        orm_mode = True
