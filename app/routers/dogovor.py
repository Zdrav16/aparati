from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import date

from app.database import get_db
from app.schemas.dogovor import DogovorCreate, DogovorOut, DogovorUpdate
from app.crud import dogovor as crud

router = APIRouter(
    prefix="/dogovor",
    tags=["Договори"]
)

class ExtendDogovorIn(BaseModel):
    new_dot: date
    new_ddo: date

@router.get("/", response_model=List[DogovorOut])
def list_dogovori(db: Session = Depends(get_db)):
    return crud.get_all_dogovori(db)

@router.get("/{dog_id}", response_model=DogovorOut)
def get_dogovor(dog_id: int, db: Session = Depends(get_db)):
    record = crud.get_dogovor_by_id(db, dog_id)
    if not record:
        raise HTTPException(status_code=404, detail="Договорът не е намерен.")
    return record

@router.post("/", response_model=DogovorOut)
def create_dogovor(data: DogovorCreate, db: Session = Depends(get_db)):
    return crud.create_dogovor(db, data)

@router.put("/{dog_id}", response_model=DogovorOut)
def update_dogovor(dog_id: int, data: DogovorUpdate, db: Session = Depends(get_db)):
    updated = crud.update_dogovor(db, dog_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Договорът не е намерен.")
    return updated

@router.delete("/{dog_id}")
def delete_dogovor(dog_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_dogovor(db, dog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Договорът не съществува.")
    return {"detail": "Договорът е изтрит успешно."}

@router.post("/extend/{dog_id}", response_model=DogovorOut)
def extend_dogovor_endpoint(dog_id: int, data: ExtendDogovorIn, db: Session = Depends(get_db)):
    new_dog = crud.extend_dogovor(db, dog_id, new_dot=data.new_dot, new_ddo=data.new_ddo)
    if not new_dog:
        raise HTTPException(status_code=404, detail="Договорът не е намерен.")
    return new_dog
