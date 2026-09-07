import { apiRequest, getAuthToken } from './api';
import { conversationMessages, aiSummaries } from '@/data/demoData';
import type { AiSummary, ConversationMessage } from '@/types';

export async function getConversation(patientId: string): Promise<ConversationMessage[]> {
  try {
    return await apiRequest<ConversationMessage[]>(`/cases/${patientId}/conversation`, { token: getAuthToken() });
  } catch {
    return conversationMessages[patientId] ?? conversationMessages.p001;
  }
}

export async function sendResponse(
  patientId: string,
  response: { text: string; mode: 'voice' | 'text'; language: 'en' | 'hi' }
): Promise<ConversationMessage> {
  return apiRequest<ConversationMessage>(`/cases/${patientId}/responses`, {
    method: 'POST',
    body: response,
    token: getAuthToken(),
  });
}

export async function getAiSummary(patientId: string): Promise<AiSummary> {
  try {
    return await apiRequest<AiSummary>(`/cases/${patientId}/summary`, { token: getAuthToken() });
  } catch {
    return aiSummaries[patientId] ?? aiSummaries.p001;
  }
}
