# System Architecture

## Current Backend Architecture

Client
  ↓
FastAPI
  ↓
Authentication
  ↓
API Routes
  ↓
Service Layer
  ↓
SQLAlchemy
  ↓
PostgreSQL

## Current APIs

- Authentication
- Patients
- Consent
- Cases
- Case Responses
- Documents
- Consultations

## Future AI Layer

Patient Voice
  ↓
Speech-to-Text
  ↓
Clinical Conversation
  ↓
Structured Case Responses

Documents
  ↓
OCR
  ↓
Entity Extraction
  ↓
Structured Information

Case Data
  ↓
LLM + Clinical Ontology
  ↓
Structured Case Summary
  ↓
Doctor Review

## Future Health Data Layer

Internal Records
  ↓
FHIR Mapping
  ↓
ABDM Integration