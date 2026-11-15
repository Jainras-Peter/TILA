import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { map } from 'rxjs';

import { AuthService } from '../services/auth.service';

export const guestGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.ready()) {
    return auth.isAuthenticated() ? router.createUrlTree(['/dashboard']) : true;
  }

  return auth.initialize().pipe(
    map((user) => (user ? router.createUrlTree(['/dashboard']) : true)),
  );
};
