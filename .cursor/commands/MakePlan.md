# Make Plan

Plan the requested task end-to-end before making any implementation changes. Cover happy path and edge cases so `/ImplementPlan` can execute without redesign.

## Core Rule

This command is strictly READ-ONLY.

DO NOT create, modify, delete, rename, refactor, format, or configure files.

Purpose: understand the system and produce an implementable plan using existing TILA patterns (Python/FastAPI + Angular).

---

## 1. Understand the Task

Identify what must change, expected behaviour, what must stay unchanged, and whether frontend, backend, Mongo, AI/RAG, workers, or config are affected.

## 2. Load context (selective)

Follow `.agents/skills/tila-context/SKILL.md` and `docs/context-routing.json`:

- Load `default` + matched route `always` (and `optional` when needed)
- Prefer `/StartTask` context if already loaded in this conversation
- Do not scan the whole `docs/` tree
- Module `API/AGENTS.md` / `Web/AGENTS.md` when touching that stack

Output a **Context loaded** list of paths.

## 3. Find Existing Patterns

Search for similar routes, services, components, schemas, tests. Prefer existing patterns over new ones. Gateway under `app/ai/gateway` is the best backend AI reference; landing/navbar/auth for UI.

## 4. Trace the Flow

Only include layers that exist for this task. Prefer `docs/architecture/data-flow.md` when Auth/Documents/RAG/Chat are involved.

Frontend: component → feature service → ApiService → HTTP  
Backend: route → middleware → controller → service → repository / gateway → response

## 5–9. Logic, files, pattern, impact, risks

For each important file: path, symbol, responsibility, why relevant. Identify closest pattern to copy.

## 7. Dependencies and Impact (required)

Cite `docs/architecture/dependency-map.md` (and `dependency-map.generated.md` if present) when touching Auth middleware, gateway, embeddings, workers, or shared core. List blast radius explicitly.

## 10. Edge Cases (required)

Enumerate concrete edge cases the plan must address, including as applicable:

- Auth / authorization / ownership (`userId` scope)
- Empty, null, missing, or malformed input
- Validation and error-envelope behaviour
- FE/BE contract mismatches (field names, enums)
- Mongo naming (`camelCase` fields; `SCREAMING_SNAKE` closed sets)
- Concurrency / idempotency / duplicate submits
- Not-found vs forbidden
- Loading / empty UI states
- LLM / gateway failures when AI is in scope

For each edge case: expected behaviour and which layer handles it.

## 11. Implementation Plan

For each change: file, what changes, pattern followed, why, deps, tests. Do not invent files that are not in the repo structure. Plan must be directly executable by `/ImplementPlan`.

## Output Format

### 1. Task Understanding
### 2. Context Loaded
### 3. Relevant Project Structure
### 4. Existing Similar Implementation
### 5. Current End-to-End Flow
### 6. Existing Pattern
### 7. Relevant Files
### 8. Dependencies and Impact
### 9. Risks
### 10. Edge Cases
### 11. Recommended Implementation Plan
### 12. Validation Strategy

## Final Rule

STOP after the plan. No code or config changes.
