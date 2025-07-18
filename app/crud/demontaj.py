from sqlalchemy.orm import Session
from app.models.demontaj import Demontaj
from app.schemas.demontaj import DemontajCreate, DemontajUpdate

def get_all_demontaji(db: Session):
    return db.query(Demontaj).order_by(Demontaj.pdate.desc()).all()

def get_demontaj_by_id(db: Session, demontaj_id: int):
    return db.query(Demontaj).filter(Demontaj.id == demontaj_id).first()

def create_demontaj(db: Session, data: DemontajCreate):
    demontaj = Demontaj(**data.dict())
    db.add(demontaj)
    db.commit()
    db.refresh(demontaj)
    return demontaj

def update_demontaj(db: Session, demontaj_id: int, data: DemontajUpdate):
    record = db.query(Demontaj).filter(Demontaj.id == demontaj_id).first()
    if record:
        for field, value in data.dict().items():
            setattr(record, field, value)
        db.commit()
        db.refresh(record)
    return record

def delete_demontaj(db: Session, demontaj_id: int):
    record = db.query(Demontaj).filter(Demontaj.id == demontaj_id).first()
    if record:
        db.delete(record)
        db.commit()
    return record
