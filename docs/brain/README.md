# TILA brain (agent memory)

Agents do not remember previous chats. This folder is the durable **development** memory.

Architecture decisions (ADRs) live in [`../decisions/`](../decisions/), not here.

## Layout

| Path | Purpose |
|------|---------|
| `roadmap.md` | Phase status for the product |
| `gaps.md` | Known gaps, risks, stale notes |
| `task-history/<slug>.md` | Append-only log per feature |
| `task-history/_TEMPLATE.md` | Copy when starting a feature |
| `../stories/<slug>/` | Deep plans, HANDOFF, Q&A for large features |

## Context loading

Before coding, resolve docs via [`../context-routing.json`](../context-routing.json) (see `.agents/skills/tila-context/SKILL.md`). Do not load the entire `docs/` tree.

## Workflow

1. `/StartTask <slug>` — routing + brain + create/read task-history
2. `/MakePlan` → human approve → `/ImplementPlan` → `/ReviewCode` → `/TestCode`
3. `/Handoff` — append task-history; update roadmap/gaps; ADRs under `docs/decisions/`

## Rules

- Task-history is **append-only** (except first create from template).
- Key by **feature slug** (`auth-login`, `rag-ingest`), not chat id.
- Corrections: when a human overrides the AI, record old value, new value, rationale.
- Skills: `.agents/skills/tila-memory/SKILL.md`, `.agents/skills/tila-context/SKILL.md`.
