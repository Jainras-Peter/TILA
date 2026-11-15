# Repository structure

```text
TILA/
├── AGENTS.md / CLAUDE.md
├── package.json / Makefile / scripts/
├── docs/                    # vision, architecture, … + brain/
├── .cursor/                 # agent.md, rules, commands, hooks, knowledge base
├── .agents/skills/
├── API/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/v1/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── models/ schemas/ middleware/ dependencies/ core/
│   │   ├── ai/gateway/      # canonical LLM
│   │   ├── ai/rag/ embeddings/ vectorstores/ prompts/
│   │   ├── document_processing/
│   │   ├── factories/ storage/ workers/ utils/
│   ├── tests/
│   ├── pyproject.toml
│   └── .python-version
└── Web/
    ├── src/app/{core,features,layout,shared}/
    ├── proxy.conf.json
    └── package.json
```

Module AGENTS.md files live in `API/` and `Web/`.
