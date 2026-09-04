from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routes import (
    auth,
    patients,
    consents,
    cases,
    case_responses,
    documents,
    consultations,
)


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="Backend API for the Patient Case-Taking System",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(consents.router)
app.include_router(cases.router)
app.include_router(case_responses.router)
app.include_router(documents.router)
app.include_router(consultations.router)


@app.get("/")
def root():
    return {
        "message": "Patient Case Taking System API",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }