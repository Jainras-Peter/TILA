# TILA brain (agent memory)

Agents do not remember previous chats. This folder is the durable memory.

## Layout

| Path | Purpose |
|------|---------|
| `roadmap.md` | Phase status for the product |
| `gaps.md` | Known gaps, risks, stale notes |
| `decisions/ADR-*.md` | Architecture Decision Records |
| `task-history/<slug>.md` | Append-only log per feature |
| `task-history/_TEMPLATE.md` | Copy when starting a feature |
| `../stories/<slug>/` | Deep plans, HANDOFF, Q&A for large features |

## Workflow

1. `/StartTask <slug>` — load agent docs + roadmap/gaps + task-history
2. `/MakePlan` → human approve → `/ImplementPlan` → `/ReviewCode` → `/TestCode`
3. `/Handoff` — append task-history; update roadmap/gaps/ADRs

## Rules

- Task-history is **append-only** (except first create from template).
- Key by **feature slug** (`auth-login`, `notebook-crud`), not chat id.
- Corrections: when a human overrides the AI, record old value, new value, rationale.
- Skill: `.agents/skills/tila-memory/SKILL.md`.
