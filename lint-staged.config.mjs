import path from "node:path"
import { fileURLToPath } from "node:url"

const root = path.dirname(fileURLToPath(import.meta.url))
const quote = (file) => `"${file.replaceAll('"', '\\"')}"`
const webRoot = path.join(root, "Web")

export default {
  "Web/src/**/*.{ts,html}": (files) => {
    if (files.length === 0) return []
    // Relative to Web/ — eslint must run with cwd=Web for config + paths.
    const rels = files.map((f) => path.relative(webRoot, f))
    // Direct binary (not `npm exec`) so --fix / --max-warnings reach eslint.
    return [
      `cd ${quote(webRoot)} && ./node_modules/.bin/eslint --fix --max-warnings=0 ${rels.map(quote).join(" ")}`,
    ]
  },
  "API/**/*.py": (files) => {
    if (files.length === 0) return []
    const abs = files.map(quote).join(" ")
    return [
      `API/venv/bin/ruff check --fix ${abs}`,
      `API/venv/bin/ruff format ${abs}`,
    ]
  },
}
