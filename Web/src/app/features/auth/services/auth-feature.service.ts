import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable, map } from 'rxjs';

import { environment } from '../../../../environments/environment';
import { LoginRequest, RegisterRequest } from '../../../core/models/user.model';
import { ApiService } from '../../../core/services/api.service';

@Injectable({ providedIn: 'root' })
export class AuthFeatureService {
  private readonly api = inject(ApiService);
  private readonly http = inject(HttpClient);
  private readonly baseUrl = environment.apiBaseUrl;

  seedCsrf(): Observable<{ ok: boolean }> {
    return this.api.get<{ ok: boolean }>('/auth/csrf');
  }

  register(payload: RegisterRequest): Observable<Record<string, unknown>> {
    return this.api.post<Record<string, unknown>>('/auth/register', payload);
  }

  login(payload: LoginRequest): Observable<void> {
    const body = new URLSearchParams();
    body.set('username', payload.username);
    body.set('password', payload.password);
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });
    // 204 No Content — avoid JSON parse of empty body
    return this.http
      .post(`${this.baseUrl}/auth/cookie/login`, body.toString(), {
        headers,
        responseType: 'text',
      })
      .pipe(map(() => undefined));
  }

  logout(): Observable<void> {
    return this.http
      .post(`${this.baseUrl}/auth/cookie/logout`, null, { responseType: 'text' })
      .pipe(map(() => undefined));
  }

  getMe(): Observable<{
    id: string;
    email: string;
    username: string;
    name: string;
    is_active: boolean;
    is_superuser: boolean;
    is_verified: boolean;
  }> {
    return this.api.get('/users/me');
  }
}
