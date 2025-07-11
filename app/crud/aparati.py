from sqlalchemy.orm import Session
from app.models.aparati import Aparat
from app.schemas.aparati import AparatCreate, AparatUpdate

def get_all_aparati(db: Session):
    return db.query(Aparat).all()

def get_aparat_by_id(db: Session, aparat_id: int):
    return db.query(Aparat).filter(Aparat.id == aparat_id).first()

def create_aparat(db: Session, data: AparatCreate):
    new_aparat = Aparat(**data.dict())
    db.add(new_aparat)
    db.commit()
    db.refresh(new_aparat)
    return new_aparat

def update_aparat(db: Session, aparat_id: int, data: AparatUpdate):
    aparat = db.query(Aparat).filter(Aparat.id == aparat_id).first()
    if aparat:
        for field, value in data.dict().items():
            setattr(aparat, field, value)
        db.commit()
        db.refresh(aparat)
    return aparat

def delete_aparat(db: Session, aparat_id: int):
    aparat = db.query(Aparat).filter(Aparat.id == aparat_id).first()
    if aparat:
        db.delete(aparat)
        db.commit()
    return aparat
