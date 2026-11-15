/**
 * Non-blocking preflight for `npm run dev`.
 * Warns about missing venv, .env, or frontend node_modules, then exits 0
 * so the API and web servers still start.
 */
import { existsSync } from "node:fs"
import { join, dirname } from "node:path"
import { fileURLToPath } from "node:url"

const root = join(dirname(fileURLToPath(import.meta.url)), "..")
const warnings = []

const checks = [
  {
    path: join(root, "API", "venv", "bin", "uvicorn"),
    message: "Backend venv missing. Run: npm run setup:api",
  },
  {
    path: join(root, "API", ".env"),
    message: "API/.env missing. Copy from .env.example and add API keys.",
  },
  {
    path: join(root, "Web", "node_modules"),
    message: "Frontend node_modules missing. Run: npm run setup:web",
  },
  {
    path: join(root, "node_modules", "concurrently"),
    message: "Root concurrently missing. Run: npm install (from TILA/)",
  },
]

for (const check of checks) {
  if (!existsSync(check.path)) warnings.push(check.message)
}

if (warnings.length > 0) {
  console.error("")
  console.error("────────────────────────────────────────────────────────────")
  console.error(" Dev preflight warnings (servers will still try to start):")
  for (const warning of warnings) {
    console.error(`  - ${warning}`)
  }
  console.error("────────────────────────────────────────────────────────────")
  console.error("")
}

process.exit(0)
