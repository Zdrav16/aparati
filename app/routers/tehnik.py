from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.tehnik import TehnikCreate, TehnikUpdate, TehnikOut
from app.crud import tehnik as crud

router = APIRouter(
    prefix="/tehnik",
    tags=["Техници"]
)

@router.get("/", response_model=List[TehnikOut])
def list_tehnici(db: Session = Depends(get_db)):
    return crud.get_all_tehnici(db)

@router.get("/{tehnik_id}", response_model=TehnikOut)
def get_tehnik(tehnik_id: int, db: Session = Depends(get_db)):
    tech = crud.get_tehnik_by_id(db, tehnik_id)
    if not tech:
        raise HTTPException(status_code=404, detail="Техникът не е намерен.")
    return tech

@router.post("/", response_model=TehnikOut)
def create_tehnik(data: TehnikCreate, db: Session = Depends(get_db)):
    return crud.create_tehnik(db, data)

@router.put("/{tehnik_id}", response_model=TehnikOut)
def update_tehnik(tehnik_id: int, data: TehnikUpdate, db: Session = Depends(get_db)):
    updated = crud.update_tehnik(db, tehnik_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Техникът не е намерен.")
    return updated

@router.delete("/{tehnik_id}")
def delete_tehnik(tehnik_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_tehnik(db, tehnik_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Техникът не е намерен.")
    return {"detail": "Техникът е изтрит успешно."}
