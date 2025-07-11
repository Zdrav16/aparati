from sqlalchemy.orm import Session
from app.models.org import Org
from app.schemas.org import OrgCreate

def get_org(db: Session, org_id: int):
    return db.query(Org).filter(Org.id == org_id).first()

def get_orgs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Org).offset(skip).limit(limit).all()

def create_org(db: Session, org: OrgCreate):
    db_org = Org(**org.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

def delete_org(db: Session, org_id: int):
    db_org = db.query(Org).filter(Org.id == org_id).first()
    if db_org:
        db.delete(db_org)
        db.commit()
    return db_org

def update_org(db: Session, org_id: int, org: OrgCreate):
    db_org = db.query(Org).filter(Org.id == org_id).first()
    if db_org:
        for key, value in org.dict().items():
            setattr(db_org, key, value)
        db.commit()
        db.refresh(db_org)
    return db_org