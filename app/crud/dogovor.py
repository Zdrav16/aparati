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

def extend_dogovor(db: Session, dog_id: int, new_dot: date, new_ddo: date):
    existing = db.query(Dogovor).filter(Dogovor.id == dog_id).first()
    if not existing:
        return None
    
    # Генериране на нов номер на договор (може да се промени по твоя логика)
    new_dog_no = db.query(Dogovor).order_by(Dogovor.dog_no.desc()).first()
    new_dog_no = (new_dog_no.dog_no + 1) if new_dog_no else 1

    new_dogovor = Dogovor(
        dog_no=new_dog_no,
        kasa_no=existing.kasa_no,
        nfirma=existing.nfirma,
        dot=new_dot,
        ddo=new_ddo,
        price=existing.price,
        company=existing.company,
        bulstat=existing.bulstat,
        company_address=existing.company_address,
        company_grad=existing.company_grad,
        obekt=existing.obekt,
        obekt_address=existing.obekt_address,
        obekt_grad=existing.obekt_grad,
        company_tel=existing.company_tel,
        company_mol=existing.company_mol,
        fp=existing.fp,
        isprekrat=0
    )
    db.add(new_dogovor)
    db.commit()
    db.refresh(new_dogovor)
    return new_dogovor
