from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from app.database import get_db
from app.schemas.dogovor import DogovorCreate, DogovorOut, DogovorUpdate
from app.crud import dogovor as crud

router = APIRouter(
    prefix="/dogovor",
    tags=["Договори"]
)

@router.get("/", response_model=List[DogovorOut])
def list_dogovori(db: Session = Depends(get_db)):
    return crud.get_all_dogovori(db)

@router.get("/{dogovor_id}", response_model=DogovorOut)
def get_dogovor(dogovor_id: int, db: Session = Depends(get_db)):
    record = crud.get_dogovor_by_id(db, dogovor_id)
    if not record:
        raise HTTPException(status_code=404, detail="Договорът не е намерен.")
    return record

@router.post("/", response_model=DogovorOut)
def create_dogovor(data: DogovorCreate, db: Session = Depends(get_db)):
    return crud.create_dogovor(db, data)

@router.put("/{dogovor_id}", response_model=DogovorOut)
def update_dogovor(dogovor_id: int, data: DogovorUpdate, db: Session = Depends(get_db)):
    updated = crud.update_dogovor(db, dogovor_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Договорът не е намерен.")
    return updated

@router.delete("/{dogovor_id}")
def delete_dogovor(dogovor_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_dogovor(db, dogovor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Договорът не съществува.")
    return {"detail": "Договорът е изтрит успешно."}

@router.get("/expiring/", response_model=List[DogovorOut])
def get_expiring_dogovori(
    from_date: date = Query(..., description="Начална дата"),
    to_date: date = Query(..., description="Крайна дата"),
    db: Session = Depends(get_db)
):
    return crud.get_expiring_contracts(db, from_date, to_date)
