import { Routes } from '@angular/router';

import { authGuard } from './core/guards/auth.guard';
import { guestGuard } from './core/guards/guest.guard';
import { LoginPageComponent } from './features/auth/pages/login/login-page.component';
import { RegisterPageComponent } from './features/auth/pages/register/register-page.component';
import { DashboardHomeComponent } from './features/dashboard/pages/dashboard-home/dashboard-home.component';
import { LandingPageComponent } from './features/landing/landing-page.component';
import { AppShellComponent } from './layout/app-shell/app-shell.component';

export const routes: Routes = [
  {
    path: '',
    component: LandingPageComponent,
  },
  {
    path: 'auth/login',
    component: LoginPageComponent,
    canActivate: [guestGuard],
  },
  {
    path: 'auth/register',
    component: RegisterPageComponent,
    canActivate: [guestGuard],
  },
  {
    path: 'dashboard',
    component: AppShellComponent,
    canActivate: [authGuard],
    children: [
      {
        path: '',
        component: DashboardHomeComponent,
      },
    ],
  },
  {
    path: '**',
    redirectTo: '',
  },
];
