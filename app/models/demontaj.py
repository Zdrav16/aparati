from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Demontaj(Base):
    __tablename__ = "demontaj"

    id = Column(Integer, primary_key=True, index=True)
    pdate = Column(Date)                  # Дата на протокола
    dot = Column(Date)                    # Дата на начало на договора (ако има)
    ddo = Column(Date)                    # Дата на край на договора
    kasa_no = Column(String(50))
    fp = Column(String(50))
    norg = Column(Integer)                # ID на фирмата (org.id)
    cfirma = Column(String(50))           # Име на фирмата (повтаря се)
    mol = Column(String(50))              # МОЛ
    bulstat = Column(String(50))
    isegn = Column(Integer, default=0)    # Има ли ЕГН
    fdread = Column(String(50))           # Последно четене на фискална памет
    reason = Column(String(150))          # Причина за демонтаж
    cmodel = Column(String(50))           # Модел на апарата
    reshenie = Column(String(20))         # Решение
    rdate = Column(Date)                  # Дата на решението
    time = Column(String(5))              # Час
    g1 = Column(String(12))
    g2 = Column(String(12))
    g3 = Column(String(12))
    g4 = Column(String(12))
    address = Column(String(100))         # Адрес на обекта
