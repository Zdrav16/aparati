from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.model import ModelCreate, ModelUpdate, ModelOut
from app.crud import model as crud

router = APIRouter(
    prefix="/models",
    tags=["Модели апарати"]
)

@router.get("/", response_model=List[ModelOut])
def list_models(db: Session = Depends(get_db)):
    return crud.get_all_models(db)

@router.get("/{model_id}", response_model=ModelOut)
def get_model(model_id: int, db: Session = Depends(get_db)):
    model = crud.get_model_by_id(db, model_id)
    if not model:
        raise HTTPException(status_code=404, detail="Моделът не е намерен.")
    return model

@router.post("/", response_model=ModelOut)
def create_model(model_data: ModelCreate, db: Session = Depends(get_db)):
    return crud.create_model(db, model_data)

@router.put("/{model_id}", response_model=ModelOut)
def update_model(model_id: int, model_data: ModelUpdate, db: Session = Depends(get_db)):
    updated = crud.update_model(db, model_id, model_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Моделът не е намерен.")
    return updated

@router.delete("/{model_id}")
def delete_model(model_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_model(db, model_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Моделът не е намерен.")
    return {"detail": "Моделът е изтрит успешно."}
