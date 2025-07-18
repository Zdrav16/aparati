from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.demontaj import DemontajCreate, DemontajUpdate, DemontajOut
from app.crud import demontaj as crud

router = APIRouter(
    prefix="/demontaj",
    tags=["Демонтажи"]
)

@router.get("/", response_model=List[DemontajOut])
def list_demontaji(db: Session = Depends(get_db)):
    return crud.get_all_demontaji(db)

@router.get("/{demontaj_id}", response_model=DemontajOut)
def get_demontaj(demontaj_id: int, db: Session = Depends(get_db)):
    dem = crud.get_demontaj_by_id(db, demontaj_id)
    if not dem:
        raise HTTPException(status_code=404, detail="Записът не е намерен.")
    return dem

@router.post("/", response_model=DemontajOut)
def create_demontaj(data: DemontajCreate, db: Session = Depends(get_db)):
    return crud.create_demontaj(db, data)

@router.put("/{demontaj_id}", response_model=DemontajOut)
def update_demontaj(demontaj_id: int, data: DemontajUpdate, db: Session = Depends(get_db)):
    updated = crud.update_demontaj(db, demontaj_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Записът не е намерен.")
    return updated

@router.delete("/{demontaj_id}")
def delete_demontaj(demontaj_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_demontaj(db, demontaj_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Записът не е намерен.")
    return {"detail": "Записът е изтрит успешно."}
