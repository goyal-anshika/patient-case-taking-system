import { apiRequest, getAuthToken, setAuthToken, clearAuthToken } from './api';

export interface LoginCredentials {
  email: string;
  password: string;
  remember: boolean;
}

export interface AuthResponse {
  token: string;
  doctor: {
    name: string;
    specialisation: string;
    contact: string;
  };
}

export async function login(credentials: LoginCredentials): Promise<AuthResponse> {
  const response = await apiRequest<AuthResponse>('/auth/login', {
    method: 'POST',
    body: credentials,
  });
  setAuthToken(response.token);
  return response;
}

export function logout(): void {
  clearAuthToken();
}

export function isAuthenticated(): boolean {
  return Boolean(getAuthToken());
}
