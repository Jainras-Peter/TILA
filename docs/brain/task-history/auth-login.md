---
slug: auth-login
status: in-progress
started-at: 2026-11-15T12:20:00+05:30
last-phase: implement
product: TILA
branches: []
---

## Goal

Dry-run of /StartTask: scaffold auth login for TILA (not implemented yet).

## Notes

### YYYY-MM-DD — started

- Context loaded from roadmap/gaps.
- Next: `/MakePlan`

<!-- Append new dated sections below. Do not rewrite earlier sections. -->

### 2026-11-15 — implemented (FastAPI Users)

- Chose FastAPI Users + Beanie + MongoDB Atlas (not Better Auth / Node sidecar).
- CookieTransport + DatabaseStrategy; Argon2; username login; CSRF + explicit CORS.
- Angular: landing CTAs → login/register; auth guards; dashboard shell with hardcoded widgets; sidebar profile + sign-out.
- ADR: `docs/brain/decisions/ADR-0003-fastapi-users-cookie-db.md`.
- User pastes Atlas URI into `API/.env` as `MONGODB_URI`.
- Out of scope still: forgot/reset password, email verify.
