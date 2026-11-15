# Errors

## Client envelope

```json
{
  "success": false,
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "Document not found"
  }
}
```

Success responses stay domain-shaped (or wrap with `success: true` when introduced consistently). Do not leak stack traces or secrets.

## Backend

- Define domain exceptions in `app/core/exceptions.py`.
- Raise them from services/repositories.
- Map them in `app/middleware/error_handler.py` to HTTP status + envelope.
- Stable `code` strings: `SCREAMING_SNAKE` (`NOTEBOOK_NOT_FOUND`, `UNAUTHORIZED`).

| Kind | Typical status |
|------|----------------|
| Validation | 400 |
| Unauthorized | 401 |
| Forbidden | 403 |
| Not found | 404 |
| Conflict | 409 |
| Upstream / LLM | 502 |
| Unavailable | 503 |

## Frontend

`error.interceptor.ts` should surface `error.code` / `error.message` to feature services. Prefer user-safe messages in UI; log details only in development.
