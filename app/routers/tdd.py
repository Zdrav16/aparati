from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.tdd import TddCreate, TddUpdate, TddOut
from app.crud import tdd as crud

router = APIRouter(
    prefix="/tdd",
    tags=["ТДД (НАП)"]
)

@router.get("/", response_model=List[TddOut])
def list_tdds(db: Session = Depends(get_db)):
    return crud.get_all_tdds(db)

@router.get("/{tdd_id}", response_model=TddOut)
def get_tdd(tdd_id: int, db: Session = Depends(get_db)):
    tdd = crud.get_tdd_by_id(db, tdd_id)
    if not tdd:
        raise HTTPException(status_code=404, detail="ТДД не е намерена.")
    return tdd

@router.post("/", response_model=TddOut)
def create_tdd(data: TddCreate, db: Session = Depends(get_db)):
    return crud.create_tdd(db, data)

@router.put("/{tdd_id}", response_model=TddOut)
def update_tdd(tdd_id: int, data: TddUpdate, db: Session = Depends(get_db)):
    updated = crud.update_tdd(db, tdd_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="ТДД не е намерена.")
    return updated

@router.delete("/{tdd_id}")
def delete_tdd(tdd_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_tdd(db, tdd_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ТДД не е намерена.")
    return {"detail": "ТДД е изтрита успешно."}
