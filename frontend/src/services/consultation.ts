import { apiRequest, getAuthToken } from './api';
import type { Consultation } from '@/types';

export async function saveConsultation(consultation: Consultation): Promise<Consultation> {
  return apiRequest<Consultation>(`/consultations/${consultation.patientId}`, {
    method: 'PUT',
    body: consultation,
    token: getAuthToken(),
  });
}

export async function completeConsultation(consultation: Consultation): Promise<Consultation> {
  return saveConsultation({ ...consultation, status: 'completed' });
}
