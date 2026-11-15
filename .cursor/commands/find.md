# Find Root Cause

Investigate the reported issue and prove the root cause. Do NOT implement a fix unless the user explicitly asks after the investigation.

Evidence may include screenshots, errors, console/network, logs, or description.

## Goals

1. What is going wrong
2. Where
3. Why
4. What evidence proves it
5. Which code path produces it

## Method

1. Understand the report (treat screenshots as evidence, not sole truth).
2. Trace the real flow (Angular → ApiService → FastAPI → service → repository/gateway → response → UI).
3. Compare with a working similar path in the repo.
4. Identify the first divergence between expected and actual.
5. Prove with code references and, when possible, a minimal reproduction path.

## Output

### Symptom
### Expected vs Actual
### Failure point (file + symbol)
### Root cause
### Evidence
### Suggested fix direction (no implementation unless asked)
