import { apiRequest, getAuthToken } from './api';
import { patientDocuments } from '@/data/demoData';
import type { PatientDocument } from '@/types';

export async function getDocuments(patientId: string): Promise<PatientDocument[]> {
  try {
    return await apiRequest<PatientDocument[]>(`/patients/${patientId}/documents`, { token: getAuthToken() });
  } catch {
    return patientDocuments[patientId] ?? [];
  }
}

export async function uploadDocument(patientId: string, file: File): Promise<PatientDocument> {
  const formData = new FormData();
  formData.append('file', file);
  return apiRequest<PatientDocument>(`/patients/${patientId}/documents`, {
    method: 'POST',
    body: formData,
    headers: {},
    token: getAuthToken(),
  });
}
