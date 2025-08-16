from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, and_, select
from datetime import date
from typing import Optional
from app.database import get_db
from app.models import aparati, org, dogovor, svid

router = APIRouter(
    prefix="/reports",
    tags=["Справки"]
)

@router.get("/expiring-contracts")
def expiring_contracts(
    date_from: Optional[date] = Query(None, description="Начална дата на изтичане"),
    date_to: Optional[date] = Query(None, description="Крайна дата на изтичане"),
    model: Optional[str] = Query(None, description="Модел апарат"),
    active_only: bool = Query(False, description="Само активни договори"),
    db: Session = Depends(get_db)
):
    # Подзаявка за взимане на последно свидетелство за всеки kasa_no
    last_svid_subq = (
        select(svid.Svid.kasa_no, func.max(svid.Svid.fd).label("last_fd"))
        .group_by(svid.Svid.kasa_no)
        .subquery()
    )

    q = (
        db.query(
            org.Org.corg.label("firm_name"),
            org.Org.bulstat.label("eik"),
            org.Org.tel.label("firm_tel"),
            dogovor.Dogovor.ddo.label("end_date"),
            aparati.Aparat.kasa_no.label("kasa_no"),
            aparati.Aparat.nmodel.label("model"),
            svid.Svid.fd.label("fdrid")
        )
        .join(aparati.Aparat, aparati.Aparat.norg == org.Org.id)
        .join(dogovor.Dogovor, dogovor.Dogovor.kasa_no == aparati.Aparat.kasa_no)
        .outerjoin(
            last_svid_subq,
            last_svid_subq.c.kasa_no == aparati.Aparat.kasa_no
        )
        .outerjoin(
            svid.Svid,
            and_(
                svid.Svid.kasa_no == last_svid_subq.c.kasa_no,
                svid.Svid.fd == last_svid_subq.c.last_fd
            )
        )
    )

    # Филтри по дати
    if date_from and date_to:
        q = q.filter(dogovor.Dogovor.ddo.between(date_from, date_to))

    # Филтър по модел
    if model:
        q = q.filter(aparati.Aparat.nmodel == model)

    # Само активни договори
    if active_only:
        today = date.today()
        q = q.filter(
            dogovor.Dogovor.isprekrat == False,
            dogovor.Dogovor.ddo >= today
        )

    q = q.order_by(dogovor.Dogovor.ddo.asc())

    results = q.all()
    count = len(results)

    return {
        "count": count,
        "data": [
            {
                "firm_name": r.firm_name,
                "eik": r.eik,
                "firm_tel": r.firm_tel,
                "end_date": r.end_date,
                "kasa_no": r.kasa_no,
                "fdrid": r.fdrid,
                "model": r.model
            }
            for r in results
        ]
    }
