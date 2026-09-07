/**
 * Base API client for MediKiosk backend integration.
 *
 * All backend calls go through this module. In production, set VITE_API_BASE_URL
 * to your FastAPI backend URL. Until then, services fall back to demo data.
 *
 * NEVER put API keys, secrets, or credentials in frontend code.
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '';

export class ApiError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
  }
}

interface RequestOptions {
  method?: string;
  body?: unknown;
  headers?: Record<string, string>;
  token?: string | null;
}

export async function apiRequest<T>(
  path: string,
  { method = 'GET', body, headers = {}, token }: RequestOptions = {}
): Promise<T> {
  if (!API_BASE_URL) {
    throw new ApiError('Backend not configured — using demo data', 503);
  }

  const finalHeaders: Record<string, string> = {
    'Content-Type': 'application/json',
    ...headers,
  };

  if (token) {
    finalHeaders['Authorization'] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    method,
    headers: finalHeaders,
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    throw new ApiError('Something went wrong. Please try again.', response.status);
  }

  return response.json() as Promise<T>;
}

export function getAuthToken(): string | null {
  return localStorage.getItem('medikiosk_token');
}

export function setAuthToken(token: string): void {
  localStorage.setItem('medikiosk_token', token);
}

export function clearAuthToken(): void {
  localStorage.removeItem('medikiosk_token');
}
