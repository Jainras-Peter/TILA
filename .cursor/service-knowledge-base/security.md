# Security

- Never commit `.env` or API keys.
- Password hashing and JWT/session logic belong in `app/core/security.py` + auth service (scaffold).
- Protected routes use auth dependencies (`app/dependencies/auth.py`).
- Resource ownership: every user-owned query includes `userId` from the authenticated principal — never trust client-supplied owner alone.
- CORS is permissive in early local `main.py`; tighten for production.
- Frontend stores tokens only via the approved auth service patterns; prefer httpOnly cookies when session design lands.
- Do not log secrets, raw tokens, or full prompt/PII dumps in production logs.
- Rate limiting middleware is planned under `app/middleware/rate_limit.py`.
