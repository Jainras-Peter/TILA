# Explain End-to-End Flow

Explain the requested functionality as an end-to-end flow using the actual TILA implementation. READ-ONLY.

## Rules

- Trace from start to finish using real source.
- Do not invent steps.
- For each step: trigger, what happens, data in/out, file, symbol, next step.

## Mermaid

Always include a Mermaid flowchart with real component/file names.

```mermaid
flowchart TD
    A[User Action] --> B[Angular Component]
    B --> C[FeatureService]
    C --> D[ApiService]
    D --> E[FastAPI Route]
    E --> F[Controller]
    F --> G[Service]
    G --> H[(Mongo / Gateway)]
    H --> G
    G --> F
    F --> D
    D --> B
```

Only include layers that participate.
