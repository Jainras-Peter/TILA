#!/usr/bin/env node
/**
 * Cursor `stop` hook: lint/typecheck files the agent changed.
 * Failures become a followup_message so the agent can fix them.
 */
import { existsSync } from "node:fs"
import { spawnSync } from "node:child_process"
import path from "node:path"

const root = process.cwd()
const tilaRoot = existsSync(path.join(root, "API"))
  ? root
  : existsSync(path.join(root, "TILA", "API"))
    ? path.join(root, "TILA")
    : root

const git = (args) =>
  spawnSync("git", args, { cwd: tilaRoot, encoding: "utf8" }).stdout.split("\n").filter(Boolean)

const changed = new Set([
  ...git(["diff", "--name-only", "HEAD"]),
  ...git(["ls-files", "--others", "--exclude-standard"]),
])

const problems = []

const pyFiles = [...changed].filter(
  (file) =>
    (file.startsWith("API/app/") || file.startsWith("API/tests/")) &&
    file.endsWith(".py") &&
    existsSync(path.join(tilaRoot, file)),
)

const ruffBin = path.join(tilaRoot, "API", "venv", "bin", "ruff")
if (pyFiles.length > 0 && existsSync(ruffBin)) {
  const result = spawnSync(ruffBin, ["check", ...pyFiles.map((f) => path.join(tilaRoot, f))], {
    cwd: path.join(tilaRoot, "API"),
    encoding: "utf8",
    timeout: 100_000,
  })
  if (result.status !== 0) {
    problems.push(`ruff failed:\n${`${result.stdout ?? ""}${result.stderr ?? ""}`.trim()}`)
  }
}

const webLintFiles = [...changed].filter(
  (file) =>
    file.startsWith("Web/src/") &&
    /\.(ts|html)$/.test(file) &&
    existsSync(path.join(tilaRoot, file)),
)

const eslintBin = path.join(tilaRoot, "Web", "node_modules", ".bin", "eslint")
if (webLintFiles.length > 0 && existsSync(eslintBin)) {
  const rels = webLintFiles.map((f) => path.relative(path.join(tilaRoot, "Web"), f))
  const result = spawnSync(
    eslintBin,
    ["--max-warnings=0", ...rels],
    {
      cwd: path.join(tilaRoot, "Web"),
      encoding: "utf8",
      timeout: 120_000,
    },
  )
  if (result.status !== 0) {
    problems.push(`eslint failed:\n${`${result.stdout ?? ""}${result.stderr ?? ""}`.trim()}`)
  }
}

const tsFiles = webLintFiles.filter((f) => f.endsWith(".ts"))
const tscBin = path.join(tilaRoot, "Web", "node_modules", ".bin", "tsc")
if (tsFiles.length > 0 && existsSync(tscBin)) {
  const result = spawnSync(tscBin, ["-p", "tsconfig.app.json", "--noEmit"], {
    cwd: path.join(tilaRoot, "Web"),
    encoding: "utf8",
    timeout: 120_000,
  })
  if (result.status !== 0) {
    problems.push(`tsc failed:\n${`${result.stdout ?? ""}${result.stderr ?? ""}`.trim()}`)
  }
}

if (problems.length > 0) {
  process.stdout.write(
    JSON.stringify({
      followup_message: `Checks failed on files you changed. Fix them, then stop:\n\n${problems.join("\n\n")}`,
    }),
  )
}

process.exit(0)
