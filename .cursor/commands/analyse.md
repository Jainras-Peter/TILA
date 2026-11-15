# Analyse Task

Analyse the requested task end-to-end before making any implementation changes.

## Core Rule

This command is strictly READ-ONLY.

DO NOT create, modify, delete, rename, refactor, format, or configure files.

Purpose: understand the system and plan using existing TILA patterns (Python/FastAPI + Angular).

---

## 1. Understand the Task

Identify what must change, expected behaviour, what must stay unchanged, and whether frontend, backend, Mongo, AI/RAG, workers, or config are affected.

## 2. Load context

Read as needed:

- `AGENTS.md`
- Relevant `docs/*.md`
- `docs/brain/roadmap.md`, `docs/brain/gaps.md`
- `docs/brain/task-history/<feature-slug>.md` if it exists
- Module `API/AGENTS.md` / `Web/AGENTS.md`

Do not scan the whole repo unnecessarily.

## 3. Find Existing Patterns

Search for similar routes, services, components, schemas, tests. Prefer existing patterns over new ones. Gateway under `app/ai/gateway` is the best backend reference; landing/navbar for UI.

## 4. Trace the Flow

Only include layers that exist for this task:

Frontend: component → feature service → ApiService → HTTP  
Backend: route → middleware → controller → service → repository / gateway → response

## 5–9. Logic, files, pattern, impact, risks

For each important file: path, symbol, responsibility, why relevant. Identify closest pattern to copy. List blast radius, regressions, edge cases.

## 10. Implementation Plan

For each change: file, what changes, pattern followed, why, deps, tests. Do not invent files that are not in the repo structure.

## Output Format

### 1. Task Understanding
### 2. Relevant Project Structure
### 3. Existing Similar Implementation
### 4. Current End-to-End Flow
### 5. Existing Pattern
### 6. Relevant Files
### 7. Dependencies and Impact
### 8. Risks and Edge Cases
### 9. Recommended Implementation Plan
### 10. Validation Strategy

## Final Rule

STOP after the analysis. No code or config changes.
