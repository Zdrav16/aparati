from sqlalchemy.orm import Session
from app.models.town import Town
from app.schemas.town import TownCreate, TownUpdate

def get_all_towns(db: Session):
    return db.query(Town).order_by(Town.ctown).all()

def get_town_by_id(db: Session, town_id: int):
    return db.query(Town).filter(Town.id == town_id).first()

def create_town(db: Session, town: TownCreate):
    db_town = Town(**town.dict())
    db.add(db_town)
    db.commit()
    db.refresh(db_town)
    return db_town

def update_town(db: Session, town_id: int, town_data: TownUpdate):
    town = db.query(Town).filter(Town.id == town_id).first()
    if town:
        for field, value in town_data.dict().items():
            setattr(town, field, value)
        db.commit()
        db.refresh(town)
    return town

def delete_town(db: Session, town_id: int):
    town = db.query(Town).filter(Town.id == town_id).first()
    if town:
        db.delete(town)
        db.commit()
    return town
