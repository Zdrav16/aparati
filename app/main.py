from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base


from app.routers import (
    aparati, org, dogovor, svid, demontaj,
    model, town, tehnik, tdd
)

app = FastAPI(title="Aparati Management API")

# CORS (ако UI е на друг порт)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # за тестова среда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация на всички routers
app.include_router(org.router)
app.include_router(aparati.router)
app.include_router(dogovor.router)
app.include_router(svid.router)
app.include_router(demontaj.router)
app.include_router(model.router)
app.include_router(town.router)
app.include_router(tehnik.router)
app.include_router(tdd.router)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)