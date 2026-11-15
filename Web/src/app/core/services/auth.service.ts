import { Injectable, computed, inject, signal } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, catchError, map, of, switchMap, tap, throwError } from 'rxjs';

import { AuthFeatureService } from '../../features/auth/services/auth-feature.service';
import { LoginRequest, RegisterRequest, User } from '../models/user.model';

interface ApiUser {
  id: string;
  email: string;
  username: string;
  name: string;
  is_active: boolean;
  is_superuser: boolean;
  is_verified: boolean;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly authApi = inject(AuthFeatureService);
  private readonly router = inject(Router);

  private readonly userSignal = signal<User | null>(null);
  private readonly readySignal = signal(false);

  readonly user = this.userSignal.asReadonly();
  readonly isAuthenticated = computed(() => this.userSignal() !== null);
  readonly ready = this.readySignal.asReadonly();

  /** Seed CSRF cookie, then load session if present. */
  initialize(): Observable<User | null> {
    return this.authApi.seedCsrf().pipe(
      catchError(() => of({ ok: false })),
      switchMap(() => this.refreshSession()),
    );
  }

  refreshSession(): Observable<User | null> {
    return this.authApi.getMe().pipe(
      map((apiUser) => this.mapUser(apiUser)),
      tap((user) => {
        this.userSignal.set(user);
        this.readySignal.set(true);
      }),
      catchError(() => {
        this.userSignal.set(null);
        this.readySignal.set(true);
        return of(null);
      }),
    );
  }

  registerAndLogin(payload: RegisterRequest): Observable<User> {
    return this.authApi.register(payload).pipe(
      switchMap(() =>
        this.login({ username: payload.username, password: payload.password }),
      ),
    );
  }

  login(payload: LoginRequest): Observable<User> {
    return this.authApi.login(payload).pipe(
      switchMap(() => this.refreshSession()),
      switchMap((user) => {
        if (!user) {
          return throwError(() => new Error('Session not established'));
        }
        return of(user);
      }),
    );
  }

  logout(): Observable<void> {
    return this.authApi.logout().pipe(
      catchError(() => of(undefined)),
      tap(() => {
        this.userSignal.set(null);
        void this.router.navigateByUrl('/');
      }),
      map(() => undefined),
    );
  }

  private mapUser(apiUser: ApiUser): User {
    return {
      id: apiUser.id,
      email: apiUser.email,
      username: apiUser.username,
      name: apiUser.name,
      isActive: apiUser.is_active,
      isSuperuser: apiUser.is_superuser,
      isVerified: apiUser.is_verified,
    };
  }
}
