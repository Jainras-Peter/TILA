# Security

- Never commit `.env` or API keys.
- Auth is **FastAPI Users** with **CookieTransport** + **DatabaseStrategy** (Beanie `users` + `accessTokens`). Wiring lives in `app/core/users.py`; config in `app/core/config.py`.
- Passwords are hashed with **Argon2** (FastAPI Users `PasswordHelper`).
- Protected routes use `current_active_user` via `app/dependencies/auth.py`.
- Resource ownership: every user-owned query includes `userId` from the authenticated principal — never trust client-supplied owner alone.
- CORS uses explicit `CORS_ORIGINS` with credentials. Production must serve HTTPS and set `ENVIRONMENT=production` so auth cookies are `Secure`.
- CSRF: `starlette-csrf` double-submit cookie + Angular XSRF header (`csrftoken` / `x-csrftoken`).
- Frontend does not store bearer tokens in `localStorage`; session is the HTTP-only cookie.
- Do not log secrets, raw tokens, or full prompt/PII dumps in production logs.
- Rate limiting middleware is planned under `app/middleware/rate_limit.py`.
- Known gap: access tokens are stored as opaque strings by the library adapter (not hashed).
