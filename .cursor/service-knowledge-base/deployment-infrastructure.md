# Deployment / infrastructure

## Local development

| Command | Effect |
|---------|--------|
| `npm run setup` | Create Python 3.12 venv + install deps; npm install frontend |
| `npm run dev` | uvicorn :8000 + Angular :4200 (proxy `/api`, `/llm`) |
| `make dev` | Same as `npm run dev` |

Python pin: `API/.python-version` → `3.12`.

## Containers

`API/Dockerfile` and `docker-compose.yml` exist but are empty placeholders. Filling them (API + Mongo) is a tracked gap.

## Environments

- Backend secrets: `API/.env` (from `.env.example`)
- Frontend: `src/environments/environment*.ts`

## Observability (target)

Structured logging, request ids, health checks, LLM attempt logs (already on gateway responses). Full OTel/Sentry later.
