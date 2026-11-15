import { HttpHeaders } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable, map } from 'rxjs';

import { LoginRequest, RegisterRequest } from '../../../core/models/user.model';
import { ApiService } from '../../../core/services/api.service';

@Injectable({ providedIn: 'root' })
export class AuthFeatureService {
  private readonly api = inject(ApiService);

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
    return this.api
      .postText('/auth/cookie/login', body.toString(), { headers })
      .pipe(map(() => undefined));
  }

  logout(): Observable<void> {
    return this.api.postText('/auth/cookie/logout', null).pipe(map(() => undefined));
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
