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
    logger.info(f"[SEARCH] eik={eik}, kasa_no={kasa_no}, name={name}")

    all_aparati = db.query(aparati.Aparat.kasa_no).all()
    all_kasa_nos = [a[0] for a in all_aparati]
    logger.info(f"[ВСИЧКИ KASA_NO В БАЗАТА] {all_kasa_nos}")

    query = db.query(
        org.Org.corg.label("firm_name"),
        org.Org.bulstat.label("eik"),
        aparati.Aparat.cobekt.label("object_name"),
        aparati.Aparat.address.label("object_address"),
        aparati.Aparat.kasa_no.label("kasa_no"),
        org.Org.tel.label("firm_tel")
    ).join(org.Org, aparati.Aparat.norg == org.Org.id)

    if eik:
        query = query.filter(org.Org.bulstat == eik)
        logger.info(f"[FILTER] bulstat == {eik}")
    elif kasa_no:
        normalized = kasa_no.replace(" ", "").strip().lower()
        query = query.filter(
            func.lower(func.replace(func.trim(aparati.Aparat.kasa_no), " ", "")) == normalized
        )
        logger.info(f"[FILTER] kasa_no normalized == {normalized}")
    elif name:
        query = query.filter(org.Org.corg.ilike(f"%{name}%"))
        logger.info(f"[FILTER] name ILIKE %{name}%")
    else:
        return []

    results = query.all()
    logger.info(f"[SEARCH RESULT] {results}")

    return [
        {
            "firm_name": r.firm_name,
            "eik": r.eik,
            "object_name": r.object_name,
            "object_address": r.object_address,
            "kasa_no": r.kasa_no,
            "firm_tel": r.firm_tel,
        }
        for r in results
    ]
