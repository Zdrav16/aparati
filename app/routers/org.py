from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.org import OrgBase, OrgCreate, OrgOut
from app.crud.org import get_org, get_orgs, create_org, update_org, delete_org  # <-- Добавено
from app.database import get_db
from typing import List
from app.schemas.org import OrgCreate, OrgUpdate, OrgOut

router = APIRouter(prefix="/org", tags=["Организации"])

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


@router.put("/{org_id}", response_model=OrgOut)
def update_existing_org(org_id: int, org: OrgUpdate, db: Session = Depends(get_db)):
    updated = update_org(db, org_id, org)
    if not updated:
        raise HTTPException(status_code=404, detail="Org not found for update")
    return updated

# ✅ DELETE заявка
@router.delete("/{org_id}")
def delete_existing_org(org_id: int, db: Session = Depends(get_db)):
    deleted = delete_org(db, org_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Org not found for deletion")
    return {"detail": "Организацията беше изтрита успешно."}
