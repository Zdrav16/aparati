from pydantic import BaseModel

class AparatiBase(BaseModel):
    kasa_no: str | None = None
    fp: str | None = None
    nmodel: int | None = None
    cobekt: str | None = None
    address: str | None = None
    ntown: int | None = None
    telefon: str | None = None
    aparat_imsi: str | None = None
    aparat_tel: str | None = None
    norg: int | None = None
    dn: str | None = None

class AparatiCreate(AparatiBase):
    pass

class AparatiOut(AparatiBase):
    id: int
    class Config:
        orm_mode = True