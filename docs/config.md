# Configuration

## Rule

**No `os.getenv` / `process.env` for application settings outside the central config module.**

Backend: `app/core/config.py` (target: pydantic-settings `Settings` loaded from `API/.env`).

Gateway today still loads keys in `app/ai/gateway/config.py`. New settings must go through core config; migrate gateway to read from core as a follow-up (see [brain/gaps.md](brain/gaps.md)).

## Env file

Copy `API/.env.example` → `.env`. Never commit `.env`.

| Variable | Purpose |
|----------|---------|
| `ENVIRONMENT` | `development` / `production` |
| `PORT` | API port (default 8000) |
| `MAIN_LLM_PROVIDER` / `MAIN_LLM_MODEL` | Primary LLM |
| `FALLBACK_LLM_PROVIDER` / `FALLBACK_LLM_MODEL` | Fallback LLM |
| `GROQ_API_KEY` / `GEMINI_API_KEY` / `OPENAI_API_KEY` | Provider secrets |
| `MAIN_LLM_RETRY_*` / `FALLBACK_LLM_*` | Gateway resiliency |
| `MONGODB_URI` | (planned) Mongo connection |

## Frontend

`src/environments/environment*.ts` — `apiBaseUrl: '/api/v1'`. Dev proxy: `proxy.conf.json`.
