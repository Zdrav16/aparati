# app/routers/org.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.org import OrgCreate, OrgOut
from app.crud import org as crud_org

router = APIRouter(
    prefix="/orgs",
    tags=["Организации"]
)

@router.get("/", response_model=List[OrgOut])
def get_all_orgs(db: Session = Depends(get_db)):
    return crud_org.get_orgs(db)

@router.get("/{org_id}", response_model=OrgOut)
def get_org(org_id: int, db: Session = Depends(get_db)):
    org = crud_org.get_org(db, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Организацията не е намерена.")
    return org

@router.post("/", response_model=OrgOut)
def create_org_view(data: OrgCreate, db: Session = Depends(get_db)):
    return crud_org.create_org(db, data)
