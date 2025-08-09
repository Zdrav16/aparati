from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.aparati import Aparat
from app.models.org import Org
from app.models.dogovor import Dogovor
from app.models.svid import Svid

router = APIRouter(prefix="/aparati", tags=["Апаратите"])

@router.get("/{aparat_id}/details")
def get_aparat_details(aparat_id: int, db: Session = Depends(get_db)):
    aparat = db.query(Aparat).filter(Aparat.id == aparat_id).first()
    if not aparat:
        raise HTTPException(status_code=404, detail="Апарат не е намерен.")

    org = db.query(Org).filter(Org.id == aparat.norg).first()
    if not org:
        raise HTTPException(status_code=404, detail="Фирмата не е намерена.")

    dogovori = db.query(Dogovor).filter(Dogovor.kasa_no == aparat.kasa_no).all()
    svidetelstva = db.query(Svid).filter(Svid.kasa_no == aparat.kasa_no).all()

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
