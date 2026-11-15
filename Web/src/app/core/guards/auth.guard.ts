import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { map } from 'rxjs';

import { AuthService } from '../services/auth.service';

export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.ready()) {
    return auth.isAuthenticated() ? true : router.createUrlTree(['/auth/login']);
  }

  return auth.initialize().pipe(
    map((user) => (user ? true : router.createUrlTree(['/auth/login']))),
  );
};
