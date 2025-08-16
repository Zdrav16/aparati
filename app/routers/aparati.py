from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from app.database import get_db
from app.models.aparati import Aparat
from app.models.org import Org
from app.models.dogovor import Dogovor

router = APIRouter(prefix="/aparati", tags=["Апаратите"])

@router.get("/details")
def get_aparat_details(
    search_by: str,
    value: str,
    db: Session = Depends(get_db)
):
    # Подготовка на заявката
    query = db.query(Aparat)

    if search_by == "id":
        query = query.filter(Aparat.id == int(value))
    elif search_by == "kasa_no":
        query = query.filter(Aparat.kasa_no == value)
    elif search_by == "fp":
        query = query.filter(Aparat.fp == value)
    else:
        raise HTTPException(status_code=400, detail="Невалиден критерий за търсене")

    # Зареждане на всички свързани данни наведнъж
    aparat = query.options(
        selectinload(Aparat.firm)
        .selectinload(Org.dogovori)
        .selectinload(Dogovor.svid)
    ).first()

    if not aparat:
        raise HTTPException(status_code=404, detail="Апарат не е намерен.")
    if not aparat.firm:
        raise HTTPException(status_code=404, detail="Фирмата не е намерена.")

    org = aparat.firm
    dogovori = org.dogovori
    svidetelstva = []
    for dogovor in dogovori:
        svidetelstva.extend(dogovor.svid)

    return {
        "org": {
            "id": org.id,
            "corg": org.corg,
            "address": org.address,
            "bulstat": org.bulstat,
            "tel": org.tel,
            "mol": org.mol,
            "position": org.position,
            "ntdd": org.ntdd,
            "isegn": org.isegn,
            "dds": org.dds,
        },
        "aparat": {
            "id": aparat.id,
            "kasa_no": aparat.kasa_no,
            "fp": aparat.fp,
            "cobekt": aparat.cobekt,
            "address": aparat.address,
            "telefon": aparat.telefon,
            "aparat_imsi": aparat.aparat_imsi,
            "aparat_tel": aparat.aparat_tel,
            "dn": aparat.dn,
            "nmodel": aparat.nmodel,
            "ntown": aparat.ntown,
        },
        "dogovori": [
            {
                "id": d.id,
                "dog_no": d.dog_no,
                "dot": d.dot,
                "ddo": d.ddo,
                "price": str(d.price),
                "company": d.company,
                "company_tel": d.company_tel,
                "fp": d.fp,
                "isprekrat": d.isprekrat,
            }
            for d in dogovori
        ],
        "svidetelstva": [
            {
                "id": s.id,
                "nsvid": s.nsvid,
                "dsvid": s.dsvid,
                "fd": s.fd,
                "fd_date": s.fd_date,
                "company": s.company,
                "kasa_no": s.kasa_no,
                "dot": s.dot,
                "ddo": s.ddo,
                "cmodel": s.cmodel,
                "reshenie": s.reshenie,
                "rdate": s.rdate,
                "mol": s.mol,
            }
            for s in svidetelstva
        ]
    }
