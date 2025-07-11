from sqlalchemy.orm import Session
from app.models.dogovor import Dogovor
from app.schemas.dogovor import DogovorCreate, DogovorUpdate
from datetime import date

def get_all_dogovori(db: Session):
    return db.query(Dogovor).all()

def get_dogovor_by_id(db: Session, id: int):
    return db.query(Dogovor).filter(Dogovor.id == id).first()

def create_dogovor(db: Session, data: DogovorCreate):
    new = Dogovor(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def update_dogovor(db: Session, id: int, data: DogovorUpdate):
    record = db.query(Dogovor).filter(Dogovor.id == id).first()
    if not record:
        return None
    for field, value in data.dict().items():
        setattr(record, field, value)
    db.commit()
    db.refresh(record)
    return record

def delete_dogovor(db: Session, id: int):
    record = db.query(Dogovor).filter(Dogovor.id == id).first()
    if record:
        db.delete(record)
        db.commit()
    return record

def get_expiring_contracts(db: Session, date_from: date, date_to: date):
    return db.query(Dogovor).filter(
        Dogovor.ddo >= date_from,
        Dogovor.ddo <= date_to,
        Dogovor.isprekrat == 0
    ).all()
