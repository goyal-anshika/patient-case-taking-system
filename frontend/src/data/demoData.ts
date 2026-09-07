import type {
  Patient,
  ConversationMessage,
  ClinicalField,
  PatientDocument,
  AiSummary,
  Consultation,
  Notification,
  CaseData,
  ExtractedMedication,
} from '@/types';

export const patients: Patient[] = [
  {
    id: 'p001',
    name: 'Ananya Sharma',
    age: 24,
    gender: 'Female',
    phone: '+91 98765 43210',
    patientId: 'MK-2026-001',
    checkInTime: '10:32 AM',
    status: 'ready',
    verification: 'verified',
    chiefComplaint: 'Headache',
    consent: true,
    language: 'en',
  },
  {
    id: 'p002',
    name: 'Rahul Verma',
    age: 35,
    gender: 'Male',
    phone: '+91 98220 11234',
    patientId: 'MK-2026-002',
    checkInTime: '10:45 AM',
    status: 'in-review',
    verification: 'pending',
    chiefComplaint: 'Lower back pain',
    consent: true,
    language: 'hi',
  },
  {
    id: 'p003',
    name: 'Priya Singh',
    age: 28,
    gender: 'Female',
    phone: '+91 99100 56789',
    patientId: 'MK-2026-003',
    checkInTime: '11:02 AM',
    status: 'waiting',
    verification: 'pending',
    chiefComplaint: 'Persistent cough',
    consent: true,
    language: 'en',
  },
  {
    id: 'p004',
    name: 'Arjun Mehta',
    age: 42,
    gender: 'Male',
    phone: '+91 98330 78901',
    patientId: 'MK-2026-004',
    checkInTime: '11:15 AM',
    status: 'in-consultation',
    verification: 'verified',
    chiefComplaint: 'Knee pain and swelling',
    consent: true,
    language: 'hi',
  },
  {
    id: 'p005',
    name: 'Neha Gupta',
    age: 31,
    gender: 'Female',
    phone: '+91 90220 33445',
    patientId: 'MK-2026-005',
    checkInTime: '11:30 AM',
    status: 'completed',
    verification: 'verified',
    chiefComplaint: 'Skin rash',
    consent: true,
    language: 'en',
  },
  {
    id: 'p006',
    name: 'Vikram Reddy',
    age: 50,
    gender: 'Male',
    phone: '+91 98450 66778',
    patientId: 'MK-2026-006',
    checkInTime: '11:48 AM',
    status: 'waiting',
    verification: 'pending',
    chiefComplaint: 'High blood pressure',
    consent: true,
    language: 'hi',
  },
  {
    id: 'p007',
    name: 'Sneha Patel',
    age: 26,
    gender: 'Female',
    phone: '+91 97110 22334',
    patientId: 'MK-2026-007',
    checkInTime: '12:05 PM',
    status: 'ready',
    verification: 'verified',
    chiefComplaint: 'Stomach ache',
    consent: true,
    language: 'en',
  },
];

export const conversationMessages: Record<string, ConversationMessage[]> = {
  p001: [
    { id: 'm1', type: 'system', text: "What is the main problem that brought you here today?", mode: 'text', timestamp: '10:32 AM', language: 'en' },
    { id: 'm2', type: 'patient', text: "I have a headache.", mode: 'voice', timestamp: '10:32 AM', language: 'en' },
    { id: 'm3', type: 'system', text: "Can you tell me where exactly the pain is?", mode: 'text', timestamp: '10:33 AM', language: 'en' },
    { id: 'm4', type: 'patient', text: "It's mostly in my forehead.", mode: 'voice', timestamp: '10:33 AM', language: 'en' },
    { id: 'm5', type: 'system', text: "When did the headache start?", mode: 'text', timestamp: '10:34 AM', language: 'en' },
    { id: 'm6', type: 'patient', text: "Yesterday evening.", mode: 'voice', timestamp: '10:34 AM', language: 'en' },
    { id: 'm7', type: 'system', text: "Does anything make it worse?", mode: 'text', timestamp: '10:35 AM', language: 'en' },
    { id: 'm8', type: 'patient', text: "It gets worse when I look at bright light.", mode: 'voice', timestamp: '10:35 AM', language: 'en' },
    { id: 'm9', type: 'system', text: "What makes it feel better?", mode: 'text', timestamp: '10:36 AM', language: 'en' },
    { id: 'm10', type: 'patient', text: "Resting in a dark room helps a little.", mode: 'voice', timestamp: '10:36 AM', language: 'en' },
    { id: 'm11', type: 'system', text: "Do you have any other symptoms like nausea, fever, or dizziness?", mode: 'text', timestamp: '10:37 AM', language: 'en' },
    { id: 'm12', type: 'patient', text: "I feel slightly nauseous.", mode: 'voice', timestamp: '10:37 AM', language: 'en' },
  ],
};

export const clinicalFields: Record<string, ClinicalField[]> = {
  p001: [
    { label: 'Chief Complaint', value: 'Headache', source: 'patient' },
    { label: 'Location', value: 'Forehead', source: 'patient' },
    { label: 'Onset', value: 'Yesterday evening', source: 'patient' },
    { label: 'Duration', value: '1 day', source: 'patient' },
    { label: 'Character', value: 'Throbbing', source: 'patient' },
    { label: 'Aggravating Factors', value: 'Bright light', source: 'patient' },
    { label: 'Relieving Factors', value: 'Rest in dark room', source: 'patient' },
    { label: 'Associated Symptoms', value: 'Nausea', source: 'patient' },
    { label: 'Previous Medication', value: 'Paracetamol 500 mg', source: 'document', confidence: 0.92 },
  ],
};

export const extractedMedications: ExtractedMedication[] = [
  {
    id: 'med1',
    name: 'Paracetamol',
    dose: '500 mg',
    frequency: '2 times/day',
    duration: '5 days',
    confidence: 0.92,
    source: 'Uploaded prescription',
  },
];

export const patientDocuments: Record<string, PatientDocument[]> = {
  p001: [
    {
      id: 'doc1',
      filename: 'prescription_2026.pdf',
      type: 'prescription',
      uploadDate: '10:40 AM',
      uploadedBy: 'Patient',
      ocrStatus: 'completed',
      extractedMedications: extractedMedications,
      extractedFields: [
        { label: 'Date', value: '15 Aug 2026', confidence: 0.95 },
        { label: 'Doctor', value: 'Dr. K. Malhotra', confidence: 0.88 },
      ],
    },
    {
      id: 'doc2',
      filename: 'blood_test_report.pdf',
      type: 'lab-report',
      uploadDate: '10:42 AM',
      uploadedBy: 'Patient',
      ocrStatus: 'completed',
      extractedFields: [
        { label: 'Hemoglobin', value: '13.2 g/dL', confidence: 0.96 },
        { label: 'WBC Count', value: '6,800 /µL', confidence: 0.94 },
      ],
    },
  ],
};

export const aiSummaries: Record<string, AiSummary> = {
  p001: {
    chiefComplaint: 'Headache in the forehead region',
    historyOfPresentIllness:
      'Patient reports headache onset yesterday evening, described as throbbing in the forehead. Aggravated by bright light, partially relieved by resting in a dark room. Associated with mild nausea.',
    previousHistory: 'No significant past medical history reported.',
    medications: ['Paracetamol 500 mg (from previous prescription)'],
    allergies: ['No known allergies'],
    investigations: ['Blood test (recent — within normal limits)'],
    confidence: 0.85,
  },
};

export const consultations: Record<string, Consultation> = {
  p001: {
    id: 'c001',
    patientId: 'p001',
    status: 'not-started',
    clinicalNotes: '',
    diagnosis: '',
    investigations: [],
    prescriptions: [],
    doctorRemarks: '',
    doctorName: 'Dr. Aditya Rao',
    date: '2026-09-07',
  },
};

export const notifications: Notification[] = [
  {
    id: 'n1',
    type: 'new-patient',
    title: 'New patient ready for review',
    message: 'Ananya Sharma has completed check-in and verification.',
    time: '2 min ago',
    read: false,
  },
  {
    id: 'n2',
    type: 'verification',
    title: 'Patient verification completed',
    message: 'Sneha Patel verified their case information.',
    time: '8 min ago',
    read: false,
  },
  {
    id: 'n3',
    type: 'ocr',
    title: 'OCR processing completed',
    message: 'Blood test report for Ananya Sharma has been processed.',
    time: '15 min ago',
    read: true,
  },
  {
    id: 'n4',
    type: 'consultation',
    title: 'Consultation saved',
    message: 'Draft consultation for Arjun Mehta has been saved.',
    time: '25 min ago',
    read: true,
  },
];

export function getCaseData(patientId: string): CaseData {
  const patient = patients.find((p) => p.id === patientId) ?? patients[0];
  return {
    patient,
    conversation: conversationMessages[patientId] ?? conversationMessages.p001,
    clinicalFields: clinicalFields[patientId] ?? clinicalFields.p001,
    documents: patientDocuments[patientId] ?? [],
    aiSummary: aiSummaries[patientId] ?? aiSummaries.p001,
    consultation: consultations[patientId] ?? consultations.p001,
  };
}

export const dashboardStats = {
  todayPatients: 24,
  waiting: 7,
  inConsultation: 2,
  completed: 15,
};

export const weeklyPatientVolume = [
  { day: 'Mon', count: 18 },
  { day: 'Tue', count: 22 },
  { day: 'Wed', count: 28 },
  { day: 'Thu', count: 20 },
  { day: 'Fri', count: 24 },
  { day: 'Sat', count: 16 },
  { day: 'Sun', count: 12 },
];

export const consultationStatusData = {
  waiting: 7,
  inConsultation: 2,
  completed: 15,
};
