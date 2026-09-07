import { apiRequest, getAuthToken } from './api';
import { patients, getCaseData } from '@/data/demoData';
import type { CaseData, Patient } from '@/types';

export async function getPatients(): Promise<Patient[]> {
  try {
    return await apiRequest<Patient[]>('/patients', { token: getAuthToken() });
  } catch {
    return patients;
  }
}

export async function getPatientCase(patientId: string): Promise<CaseData> {
  try {
    return await apiRequest<CaseData>(`/patients/${patientId}/case`, { token: getAuthToken() });
  } catch {
    return getCaseData(patientId);
  }
}

export async function createPatient(patient: Omit<Patient, 'id'>): Promise<Patient> {
  return apiRequest<Patient>('/patients', {
    method: 'POST',
    body: patient,
    token: getAuthToken(),
  });
}
