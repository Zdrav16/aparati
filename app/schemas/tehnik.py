from pydantic import BaseModel

class TehnikBase(BaseModel):
    ctehnik: str
    egn: str

class TehnikCreate(TehnikBase):
    pass

class TehnikUpdate(TehnikBase):
    pass

class TehnikOut(TehnikBase):
    id: int

    class Config:
        orm_mode = True
