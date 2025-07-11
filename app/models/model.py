from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True, index=True)
    cmodel = Column(String(30))           # Име на модела
    reshenie = Column(String(20))         # Решение/разрешение (пример: номер на разрешение)
    rdate = Column(Date)                  # Дата на решението
