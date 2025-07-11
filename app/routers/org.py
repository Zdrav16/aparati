from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.org import OrgBase, OrgCreate, OrgOut
from app.crud.org import get_org, get_orgs, create_org
from app.database import get_db
from typing import List

router = APIRouter(prefix="/orgs", tags=["orgs"])

@router.get("/", response_model=List[OrgOut])
def read_orgs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_orgs(db, skip=skip, limit=limit)

@router.get("/{org_id}", response_model=OrgOut)
def read_org(org_id: int, db: Session = Depends(get_db)):
    db_org = get_org(db, org_id=org_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Org not found")
    return db_org

@router.post("/", response_model=OrgOut)
def create_new_org(org: OrgCreate, db: Session = Depends(get_db)):
    return create_org(db, org)