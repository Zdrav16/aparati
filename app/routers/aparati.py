from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.aparati import AparatCreate, AparatOut, AparatUpdate
from app.crud import aparati as crud_aparati

router = APIRouter(
    prefix="/aparati",
    tags=["Апаратите"]
)

@router.get("/", response_model=List[AparatOut])
def get_all_aparati(db: Session = Depends(get_db)):
    return crud_aparati.get_all_aparati(db)

@router.get("/{aparat_id}", response_model=AparatOut)
def get_aparat(aparat_id: int, db: Session = Depends(get_db)):
    aparat = crud_aparati.get_aparat_by_id(db, aparat_id)
    if not aparat:
        raise HTTPException(status_code=404, detail="Апаратът не е намерен.")
    return aparat

@router.post("/", response_model=AparatOut)
def create_aparat(data: AparatCreate, db: Session = Depends(get_db)):
    return crud_aparati.create_aparat(db, data)

@router.put("/{aparat_id}", response_model=AparatOut)
def update_aparat(aparat_id: int, data: AparatUpdate, db: Session = Depends(get_db)):
    updated = crud_aparati.update_aparat(db, aparat_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Апаратът не е намерен за редакция.")
    return updated

@router.delete("/{aparat_id}")
def delete_aparat(aparat_id: int, db: Session = Depends(get_db)):
    deleted = crud_aparati.delete_aparat(db, aparat_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Апаратът не съществува.")
    return {"detail": "Апаратът е изтрит успешно."}