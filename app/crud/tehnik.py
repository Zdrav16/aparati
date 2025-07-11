from sqlalchemy.orm import Session
from app.models.tehnik import Tehnik
from app.schemas.tehnik import TehnikCreate, TehnikUpdate

def get_all_tehnici(db: Session):
    return db.query(Tehnik).order_by(Tehnik.ctehnik).all()

def get_tehnik_by_id(db: Session, tehnik_id: int):
    return db.query(Tehnik).filter(Tehnik.id == tehnik_id).first()

def create_tehnik(db: Session, data: TehnikCreate):
    new = Tehnik(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def update_tehnik(db: Session, tehnik_id: int, data: TehnikUpdate):
    record = db.query(Tehnik).filter(Tehnik.id == tehnik_id).first()
    if record:
        for field, value in data.dict().items():
            setattr(record, field, value)
        db.commit()
        db.refresh(record)
    return record

def delete_tehnik(db: Session, tehnik_id: int):
    record = db.query(Tehnik).filter(Tehnik.id == tehnik_id).first()
    if record:
        db.delete(record)
        db.commit()
    return record
