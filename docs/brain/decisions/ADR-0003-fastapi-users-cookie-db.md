# ADR-0003: FastAPI Users with CookieTransport + DatabaseStrategy

## Status

Accepted — 2026-11-15

## Context

TILA needs username/password signup and login for an Angular SPA, with revocable sessions, MongoDB Atlas as the system of record, and no separate Node auth service. Better Auth was considered but is Node-only; FastAPI Users fits the Python API.

## Decision

- Use **FastAPI Users** with **Beanie** on MongoDB Atlas.
- Auth transport: **CookieTransport** (HTTP-only cookie `tilaauth`).
- Auth strategy: **DatabaseStrategy** with Beanie `AccessToken` documents (logout deletes the token row — immediate revocation).
- Password hashing: Argon2 via FastAPI Users `PasswordHelper`.
- Login identifier: application **username** (custom `UserManager.authenticate`), not email.
- CSRF: `starlette-csrf` double-submit cookie + Angular `withXsrfConfiguration`.
- CORS: explicit origins only; `cookie_secure` true when `ENVIRONMENT=production` (HTTPS required in production).
- Do **not** mount forgot-password or email-verify routers in this MVP.

## Consequences

- Auth user/token documents follow FastAPI Users / Beanie field names (`hashed_password`, `token`, `user_id`, …) — an intentional exception to TILA camelCase for other collections.
- Stock Beanie access-token adapter stores the opaque token string (not a hash). Accept for MVP; harden Atlas network access; revisit hashing later if needed.
- Domain APIs resolve the current user via `current_active_user` / `app/dependencies/auth.py`.
