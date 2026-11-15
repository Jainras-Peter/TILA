export interface User {
  id: string;
  email: string;
  username: string;
  name: string;
  isActive: boolean;
  isSuperuser: boolean;
  isVerified: boolean;
}

export interface RegisterRequest {
  email: string;
  password: string;
  username: string;
  name: string;
}

export interface LoginRequest {
  username: string;
  password: string;
}
