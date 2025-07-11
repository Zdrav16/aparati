from sqlalchemy.orm import Session
from app.models.svid import Svid
from app.schemas.svid import SvidCreate, SvidUpdate

def get_all_svid(db: Session):
    return db.query(Svid).all()

def get_svid_by_id(db: Session, svid_id: int):
    return db.query(Svid).filter(Svid.id == svid_id).first()

def create_svid(db: Session, data: SvidCreate):
    svid = Svid(**data.dict())
    db.add(svid)
    db.commit()
    db.refresh(svid)
    return svid

def update_svid(db: Session, svid_id: int, data: SvidUpdate):
    record = db.query(Svid).filter(Svid.id == svid_id).first()
    if record:
        for field, value in data.dict().items():
            setattr(record, field, value)
        db.commit()
        db.refresh(record)
    return record

def delete_svid(db: Session, svid_id: int):
    record = db.query(Svid).filter(Svid.id == svid_id).first()
    if record:
        db.delete(record)
        db.commit()
    return record
