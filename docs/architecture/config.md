# Configuration

## Rule

**No `os.getenv` / `process.env` for application settings outside the central config module.**

Backend: `app/core/config.py` (pydantic-settings `Settings` loaded from `API/.env`).

Gateway today still loads keys in `app/ai/gateway/config.py`. New settings must go through core config; migrate gateway to read from core as a follow-up (see [../brain/gaps.md](../brain/gaps.md)).

## Env file

Copy `API/.env.example` → `.env`. Never commit `.env`.

| Variable | Purpose |
|----------|---------|
| `ENVIRONMENT` | `development` / `production` (production enables Secure cookies) |
| `PORT` | API port (default 8000) |
| `MAIN_LLM_PROVIDER` / `MAIN_LLM_MODEL` | Primary LLM |
| `FALLBACK_LLM_PROVIDER` / `FALLBACK_LLM_MODEL` | Fallback LLM |
| `GROQ_API_KEY` / `GEMINI_API_KEY` / `OPENAI_API_KEY` | Provider secrets |
| `MAIN_LLM_RETRY_*` / `FALLBACK_LLM_*` | Gateway resiliency |
| `MONGODB_URI` | MongoDB Atlas (or local) connection string |
| `MONGODB_DB_NAME` | Database name (default `tila`) |
| `AUTH_SECRET` | CSRF signing + FastAPI Users token secrets |
| `AUTH_COOKIE_MAX_AGE` | Session lifetime seconds (default 604800 = 7 days) |
| `AUTH_COOKIE_NAME` | HTTP-only auth cookie (default `tilaauth`) |
| `CSRF_COOKIE_NAME` / `CSRF_HEADER_NAME` | Double-submit CSRF (`csrftoken` / `x-csrftoken`) |
| `CORS_ORIGINS` | Comma-separated browser origins (e.g. `http://localhost:4200`) |

## Frontend

`src/environments/environment*.ts` — `apiBaseUrl: '/api/v1'`. Dev proxy: `proxy.conf.json` → API `:8000`. Auth uses credentialed cookies + CSRF header; no bearer token storage in `localStorage`.
