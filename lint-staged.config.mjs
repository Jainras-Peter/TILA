import path from "node:path"
import { fileURLToPath } from "node:url"

const root = path.dirname(fileURLToPath(import.meta.url))
const quote = (file) => `"${file.replaceAll('"', '\\"')}"`

export default {
  "Web/src/**/*.{ts,html}": (files) => {
    if (files.length === 0) return []
    const rels = files.map((f) => path.relative(path.join(root, "Web"), f))
    return [
      `npm --prefix Web exec eslint --fix --max-warnings=0 ${rels.map(quote).join(" ")}`,
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
