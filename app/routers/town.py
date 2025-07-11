from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.town import TownCreate, TownOut, TownUpdate
from app.crud import town as crud_town

router = APIRouter(
    prefix="/town",
    tags=["Градове"]
)

@router.get("/", response_model=List[TownOut])
def list_towns(db: Session = Depends(get_db)):
    return crud_town.get_all_towns(db)

@router.get("/{town_id}", response_model=TownOut)
def get_town(town_id: int, db: Session = Depends(get_db)):
    town = crud_town.get_town_by_id(db, town_id)
    if not town:
        raise HTTPException(status_code=404, detail="Градът не е намерен.")
    return town

@router.post("/", response_model=TownOut)
def create_town(town: TownCreate, db: Session = Depends(get_db)):
    return crud_town.create_town(db, town)

@router.put("/{town_id}", response_model=TownOut)
def update_town(town_id: int, town_data: TownUpdate, db: Session = Depends(get_db)):
    updated = crud_town.update_town(db, town_id, town_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Градът не е намерен.")
    return updated

@router.delete("/{town_id}")
def delete_town(town_id: int, db: Session = Depends(get_db)):
    deleted = crud_town.delete_town(db, town_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Градът не е намерен.")
    return {"detail": "Градът е изтрит успешно."}
