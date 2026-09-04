from fastapi import FastAPI

from .config import settings
from .database import Base, engine

# Import models so SQLAlchemy registers them.
from .models import (
    Patient,
    Consent,
    PatientCase,
    CaseResponse,
    Document,
    Consultation,
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)


@app.get("/")
def root():
    return {
        "message": "Patient Case Taking System API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }