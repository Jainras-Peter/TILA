---
name: tila-context
description: Resolve and load only the TILA docs needed for a feature via docs/context-routing.json (Context Engineering).
---

# TILA context loading

Agents must not read every file under `docs/`. Use selective context.

## Resolve a route

1. Open `docs/context-routing.json`.
2. Match the feature **slug** to a route’s `slugs` array (preferred).
3. Else match **keywords** from the user request against route `keywords`.
4. If multiple match, pick the most specific (e.g. `rag` over `platform`).
5. If none match, load `default` only and ask which module applies.

## What to read

1. Always read `default` from the JSON.
2. Read that route’s `always` list (every path).
3. Read `optional` only when the task clearly needs UI/design or the listed module.
4. Read `docs/brain/task-history/<slug>.md` if it exists (or create via `/StartTask`).
5. Skim `docs/architecture/dependency-map.md` for blast radius (required when changing Auth, gateway, embeddings, workers, or shared core).
6. Optionally refresh `docs/architecture/dependency-map.generated.md` via `python3 scripts/scan-api-imports.py` before large API refactors.

## Output (in /StartTask or /MakePlan)

List **Context loaded** as the concrete paths you opened. Do not claim to have read the whole docs tree.

## Related

- Memory / handoff: `.agents/skills/tila-memory/SKILL.md`
- Index: `docs/README.md`
