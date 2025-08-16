from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import aparati, org
from typing import Optional
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/search",
    tags=["Търсене"]
)

@router.get("/")
def search_aparati(
    eik: Optional[str] = Query(None),
    kasa_no: Optional[str] = Query(None),
    name: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(
        aparati.Aparat.id.label("aparat_id"),
        org.Org.id.label("firm_id"),
        org.Org.corg.label("firm_name"),
        org.Org.bulstat.label("eik"),
        aparati.Aparat.cobekt.label("object_name"),
        aparati.Aparat.address.label("object_address"),
        aparati.Aparat.kasa_no.label("kasa_no"),
        org.Org.tel.label("firm_tel")
    ).join(org.Org, aparati.Aparat.norg == org.Org.id)

    if eik:
        query = query.filter(org.Org.bulstat == eik)
    if kasa_no:
        normalized = kasa_no.replace(" ", "").strip().lower()
        query = query.filter(
            func.lower(func.replace(func.trim(aparati.Aparat.kasa_no), " ", "")) == normalized
        )
    if name:
        query = query.filter(org.Org.corg.ilike(f"%{name}%"))

    results = query.all()

    return [
        {
            "aparat_id": r.aparat_id,
            "firm_id": r.firm_id,
            "firm_name": r.firm_name,
            "eik": r.eik,
            "object_name": r.object_name,
            "object_address": r.object_address,
            "kasa_no": r.kasa_no,
            "firm_tel": r.firm_tel,
        }
        for r in results
    ]
