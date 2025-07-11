from pydantic import BaseModel

class TownBase(BaseModel):
    ctown: str

class TownCreate(TownBase):
    pass

class TownUpdate(TownBase):
    pass

class TownOut(TownBase):
    id: int

    class Config:
        orm_mode = True
