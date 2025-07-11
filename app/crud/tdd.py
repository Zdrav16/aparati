from sqlalchemy.orm import Session
from app.models.tdd import Tdd
from app.schemas.tdd import TddCreate, TddUpdate

def get_all_tdds(db: Session):
    return db.query(Tdd).order_by(Tdd.tddnap).all()

def get_tdd_by_id(db: Session, tdd_id: int):
    return db.query(Tdd).filter(Tdd.id == tdd_id).first()

def create_tdd(db: Session, data: TddCreate):
    tdd = Tdd(**data.dict())
    db.add(tdd)
    db.commit()
    db.refresh(tdd)
    return tdd

def update_tdd(db: Session, tdd_id: int, data: TddUpdate):
    tdd = db.query(Tdd).filter(Tdd.id == tdd_id).first()
    if tdd:
        for field, value in data.dict().items():
            setattr(tdd, field, value)
        db.commit()
        db.refresh(tdd)
    return tdd

def delete_tdd(db: Session, tdd_id: int):
    tdd = db.query(Tdd).filter(Tdd.id == tdd_id).first()
    if tdd:
        db.delete(tdd)
        db.commit()
    return tdd
