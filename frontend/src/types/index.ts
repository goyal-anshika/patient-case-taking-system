export type Language = 'en' | 'hi';

export type PatientStatus = 'waiting' | 'in-review' | 'ready' | 'in-consultation' | 'completed';
export type VerificationStatus = 'pending' | 'verified' | 'rejected';
export type OcrStatus = 'pending' | 'processing' | 'completed' | 'failed';
export type ConsultationStatus = 'not-started' | 'draft' | 'completed';

export type InfoSource = 'patient' | 'ai-extracted' | 'document' | 'doctor-entered' | 'ai-summary';

export type MessageType = 'system' | 'patient';
export type MessageMode = 'voice' | 'text';

export interface Patient {
  id: string;
  name: string;
  age: number;
  gender: 'Male' | 'Female' | 'Other';
  phone: string;
  patientId: string;
  checkInTime: string;
  status: PatientStatus;
  verification: VerificationStatus;
  chiefComplaint: string;
  consent: boolean;
  language: Language;
}

export interface ConversationMessage {
  id: string;
  type: MessageType;
  text: string;
  mode: MessageMode;
  timestamp: string;
  language: Language;
}

export interface ClinicalField {
  label: string;
  value: string;
  source: InfoSource;
  confidence?: number;
}

export interface ExtractedMedication {
  id: string;
  name: string;
  dose: string;
  frequency: string;
  duration: string;
  confidence: number;
  source: string;
}

export interface PatientDocument {
  id: string;
  filename: string;
  type: 'prescription' | 'lab-report' | 'medical-report' | 'consultation' | 'other';
  uploadDate: string;
  uploadedBy: string;
  ocrStatus: OcrStatus;
  thumbnail?: string;
  extractedMedications?: ExtractedMedication[];
  extractedFields?: { label: string; value: string; confidence: number }[];
}

export interface AiSummary {
  chiefComplaint: string;
  historyOfPresentIllness: string;
  previousHistory: string;
  medications: string[];
  allergies: string[];
  investigations: string[];
  confidence: number;
}

export interface PrescriptionEntry {
  id: string;
  medicine: string;
  dosage: string;
  frequency: string;
  duration: string;
  instructions: string;
}

export interface Consultation {
  id: string;
  patientId: string;
  status: ConsultationStatus;
  clinicalNotes: string;
  diagnosis: string;
  investigations: string[];
  prescriptions: PrescriptionEntry[];
  doctorRemarks: string;
  doctorName: string;
  date: string;
}

export interface CaseData {
  patient: Patient;
  conversation: ConversationMessage[];
  clinicalFields: ClinicalField[];
  documents: PatientDocument[];
  aiSummary: AiSummary;
  consultation: Consultation;
}

export interface DoctorInfo {
  name: string;
  specialisation: string;
  contact: string;
}

export interface Notification {
  id: string;
  type: 'new-patient' | 'verification' | 'ocr' | 'consultation' | 'system';
  title: string;
  message: string;
  time: string;
  read: boolean;
}
