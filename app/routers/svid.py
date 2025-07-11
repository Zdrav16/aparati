from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.svid import SvidCreate, SvidOut, SvidUpdate
from app.crud import svid as crud

router = APIRouter(
    prefix="/svid",
    tags=["Свидетелства"]
)

@router.get("/", response_model=List[SvidOut])
def list_svid(db: Session = Depends(get_db)):
    return crud.get_all_svid(db)

@router.get("/{svid_id}", response_model=SvidOut)
def get_svid(svid_id: int, db: Session = Depends(get_db)):
    record = crud.get_svid_by_id(db, svid_id)
    if not record:
        raise HTTPException(status_code=404, detail="Свидетелството не е намерено.")
    return record

@router.post("/", response_model=SvidOut)
def create_svid(data: SvidCreate, db: Session = Depends(get_db)):
    return crud.create_svid(db, data)

@router.put("/{svid_id}", response_model=SvidOut)
def update_svid(svid_id: int, data: SvidUpdate, db: Session = Depends(get_db)):
    updated = crud.update_svid(db, svid_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Свидетелството не е намерено.")
    return updated

@router.delete("/{svid_id}")
def delete_svid(svid_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_svid(db, svid_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Свидетелството не съществува.")
    return {"detail": "Свидетелството е изтрито успешно."}
