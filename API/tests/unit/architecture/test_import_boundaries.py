"""AST-based architecture import boundaries for the FastAPI app.

Dependency direction (docs/backend.md, AGENTS.md):

  routes → controllers → services → repositories → database
  services may also call AI gateway interfaces (no FastAPI, no motor)
  LLM vendor SDKs only inside app/ai/gateway
"""

from __future__ import annotations

import ast
from pathlib import Path

APP_ROOT = Path(__file__).resolve().parents[3] / "app"

# fastapi-users mounts routers directly until a controller wrapper exists.
# Shrink this set — never grow it without an ADR.
ROUTE_ALLOWLIST = {
    "api/v1/auth.py",
    "api/v1/users.py",
}

CONFIG_GETENV_ALLOWLIST = {
    "core/config.py",
    "ai/gateway/config.py",  # temporary until fully on core config
}

LLM_VENDOR_PREFIXES = (
    "groq",
    "openai",
    "google.generativeai",
    "google.genai",
    "anthropic",
    "app.ai.llm",
)


def get_imports(file_path: Path) -> list[str]:
    tree = ast.parse(file_path.read_text(encoding="utf-8"))
    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    return imports


def iter_app_py_files() -> list[Path]:
    return sorted(
        p
        for p in APP_ROOT.rglob("*.py")
        if p.is_file() and "__pycache__" not in p.parts and p.stat().st_size > 0
    )


def rel(path: Path) -> str:
    return path.relative_to(APP_ROOT).as_posix()


def _matches_prefix(module: str, prefixes: tuple[str, ...]) -> bool:
    return any(module == p or module.startswith(p + ".") for p in prefixes)


def test_routes_only_depend_on_controllers_or_allowlisted_auth():
    """api/v1 route modules must import controllers, not services/repositories."""
    offenders: list[str] = []
    for path in iter_app_py_files():
        r = rel(path)
        if not r.startswith("api/v1/") or r.endswith("__init__.py") or r.endswith("router.py"):
            continue
        if r in ROUTE_ALLOWLIST:
            continue
        imports = get_imports(path)
        for mod in imports:
            if mod.startswith("app.services") or mod.startswith("app.repositories"):
                offenders.append(f"{r}: imports {mod}")
            if mod.startswith("app.controllers"):
                continue
    assert offenders == [], "Routes must go through controllers:\n" + "\n".join(offenders)


def test_controllers_must_not_import_repositories():
    offenders: list[str] = []
    for path in iter_app_py_files():
        r = rel(path)
        if not r.startswith("controllers/"):
            continue
        for mod in get_imports(path):
            if mod.startswith("app.repositories") or mod in {"motor", "motor.motor_asyncio"}:
                offenders.append(f"{r}: imports {mod}")
            if _matches_prefix(mod, ("motor",)):
                offenders.append(f"{r}: imports {mod}")
    assert offenders == [], "Controllers must not touch repositories/Mongo:\n" + "\n".join(
        offenders
    )


def test_services_must_not_import_fastapi():
    offenders: list[str] = []
    for path in iter_app_py_files():
        r = rel(path)
        if not r.startswith("services/"):
            continue
        for mod in get_imports(path):
            if mod == "fastapi" or mod.startswith("fastapi."):
                offenders.append(f"{r}: imports {mod}")
    assert offenders == [], "Services must not depend on FastAPI:\n" + "\n".join(offenders)


def test_only_repositories_import_motor():
    offenders: list[str] = []
    for path in iter_app_py_files():
        r = rel(path)
        for mod in get_imports(path):
            if not _matches_prefix(mod, ("motor",)):
                continue
            if r.startswith("repositories/") or r in {
                "core/database.py",
            }:
                continue
            offenders.append(f"{r}: imports {mod}")
    assert offenders == [], "Only repositories/core.database may import motor:\n" + "\n".join(
        offenders
    )


def test_llm_vendor_sdks_only_in_gateway():
    offenders: list[str] = []
    for path in iter_app_py_files():
        r = rel(path)
        in_gateway = r.startswith("ai/gateway/")
        for mod in get_imports(path):
            if _matches_prefix(mod, LLM_VENDOR_PREFIXES):
                if in_gateway and not mod.startswith("app.ai.llm"):
                    # gateway may use HTTP; still ban legacy app.ai.llm
                    if mod.startswith("app.ai.llm"):
                        offenders.append(f"{r}: imports legacy {mod}")
                    continue
                if in_gateway:
                    continue
                offenders.append(f"{r}: imports {mod}")
            if mod.startswith("app.ai.llm"):
                offenders.append(f"{r}: imports legacy {mod}")
    assert offenders == [], "LLM SDKs / legacy llm package only via gateway:\n" + "\n".join(
        offenders
    )


def test_os_getenv_only_in_allowlisted_config():
    offenders: list[str] = []
    for path in iter_app_py_files():
        r = rel(path)
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            # os.getenv(...)
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "getenv"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "os"
            ):
                if r not in CONFIG_GETENV_ALLOWLIST:
                    offenders.append(f"{r}: os.getenv")
            # from os import getenv; getenv(...)
            if isinstance(node, ast.ImportFrom) and node.module == "os":
                for alias in node.names:
                    if alias.name == "getenv" and r not in CONFIG_GETENV_ALLOWLIST:
                        offenders.append(f"{r}: from os import getenv")
    assert offenders == [], "os.getenv only in config allowlist:\n" + "\n".join(offenders)


def test_get_imports_handles_forms():
    sample = """
import motor
from motor import motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import fastapi
from app.services.x import Y
"""
    tree = ast.parse(sample)
    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    assert "motor" in imports
    assert "motor.motor_asyncio" in imports
    assert "fastapi" in imports
    assert "app.services.x" in imports
