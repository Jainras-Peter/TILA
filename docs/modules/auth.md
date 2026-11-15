# Module: Auth

| | |
|--|--|
| **Status** | `partial` — MVP login/register + cookie sessions |
| **Dependency-map node** | `Auth` / `AuthMiddleware` |
| **ADRs** | [ADR-0003](../decisions/ADR-0003-fastapi-users-cookie-db.md) |

## Owned paths

| Area | Paths |
|------|--------|
| API | `API/app/core/security.py`, auth deps under `dependencies/`, FastAPI Users wiring, `api/v1` auth routes, Beanie `User` / `AccessToken` |
| Web | `Web/src/app/features/auth/`, `core/services/auth.service.ts`, auth/guest guards, CSRF/`withCredentials` on HTTP |

## Contracts

- Cookie session (`tilaauth`) + double-submit CSRF.
- Login identifier: **username** (not email) per ADR-0003.
- Protected APIs resolve user via `current_active_user` / `app/dependencies/auth.py`.
- Collections: `users`, `accessTokens` (library field names — auth exception to camelCase).

## Required context

- [../architecture/backend-architecture.md](../architecture/backend-architecture.md)
- [../architecture/errors.md](../architecture/errors.md)
- [../architecture/config.md](../architecture/config.md)
- [../architecture/dependency-map.md](../architecture/dependency-map.md)
- [../decisions/ADR-0003-fastapi-users-cookie-db.md](../decisions/ADR-0003-fastapi-users-cookie-db.md)

## Before you change this

- Auth middleware / cookie / CSRF changes affect **every protected endpoint** and Angular interceptors.
- Do not store bearer tokens in `localStorage` for the cookie strategy.
- Do not dual-write a second auth scheme without an ADR.
- Out of MVP: forgot-password, email verify, multi-device session UI (see [../brain/gaps.md](../brain/gaps.md)).
