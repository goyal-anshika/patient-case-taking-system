from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.voice_conversation import router as voice_conversation_router
from .config import settings
from .routes import voice_conversation
from .routes import (
    auth,
    patients,
    consents,
    cases,
    case_responses,
    documents,
    consultations,
    speech,
    conversation,
    ocr,
    summarization,
    ai_pipeline,
    ai_case,
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
app.include_router(speech.router)
app.include_router(conversation.router)
app.include_router(ocr.router)
app.include_router(summarization.router)
app.include_router(ai_pipeline.router)
app.include_router(ai_case.router)
app.include_router(voice_conversation_router)
app.include_router(voice_conversation.router)


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