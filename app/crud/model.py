from sqlalchemy.orm import Session
from app.models.model import Model
from app.schemas.model import ModelCreate, ModelUpdate

def get_all_models(db: Session):
    return db.query(Model).order_by(Model.cmodel).all()

def get_model_by_id(db: Session, model_id: int):
    return db.query(Model).filter(Model.id == model_id).first()

def create_model(db: Session, model_data: ModelCreate):
    model = Model(**model_data.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def update_model(db: Session, model_id: int, model_data: ModelUpdate):
    model = db.query(Model).filter(Model.id == model_id).first()
    if model:
        for field, value in model_data.dict().items():
            setattr(model, field, value)
        db.commit()
        db.refresh(model)
    return model

def delete_model(db: Session, model_id: int):
    model = db.query(Model).filter(Model.id == model_id).first()
    if model:
        db.delete(model)
        db.commit()
    return model
