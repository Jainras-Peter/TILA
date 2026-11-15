import os
from pathlib import Path
from dataclasses import dataclass, field


# Path to root .env file (TILA-Backend/.env)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


def _load_env_file():
    """Simple parser for root .env file if present."""
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("'\"")
                    if key not in os.environ:
                        os.environ[key] = value


_load_env_file()


@dataclass
class GatewayConfig:
    """Configuration for LLM Gateway, loading root .env settings and providing default gateway behavior."""

    # Root Level LLM Provider Selection & Models
    MAIN_LLM_PROVIDER: str = field(default_factory=lambda: os.getenv("MAIN_LLM_PROVIDER", "groq"))
    MAIN_LLM_MODEL: str = field(default_factory=lambda: os.getenv("MAIN_LLM_MODEL", "llama-3.3-70b-versatile"))
    FALLBACK_LLM_PROVIDER: str = field(default_factory=lambda: os.getenv("FALLBACK_LLM_PROVIDER", "gemini"))
    FALLBACK_LLM_MODEL: str = field(default_factory=lambda: os.getenv("FALLBACK_LLM_MODEL", "gemini-2.0-flash"))

    # API Keys
    GROQ_API_KEY: str = field(default_factory=lambda: os.getenv("GROQ_API_KEY", ""))
    GEMINI_API_KEY: str = field(default_factory=lambda: os.getenv("GEMINI_API_KEY", ""))
    OPENAI_API_KEY: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", ""))

    # Gateway Retry, Interval, and Timeout Settings (Configurable in Gateway)
    MAIN_LLM_RETRY_COUNT: int = field(default_factory=lambda: int(os.getenv("MAIN_LLM_RETRY_COUNT", "2")))
    MAIN_LLM_RETRY_INTERVAL: float = field(default_factory=lambda: float(os.getenv("MAIN_LLM_RETRY_INTERVAL", "2.0")))
    MAIN_LLM_TIMEOUT: float = field(default_factory=lambda: float(os.getenv("MAIN_LLM_TIMEOUT", "15.0")))

    FALLBACK_LLM_RETRY_COUNT: int = field(default_factory=lambda: int(os.getenv("FALLBACK_LLM_RETRY_COUNT", "1")))
    FALLBACK_LLM_RETRY_INTERVAL: float = field(default_factory=lambda: float(os.getenv("FALLBACK_LLM_RETRY_INTERVAL", "2.0")))
    FALLBACK_LLM_TIMEOUT: float = field(default_factory=lambda: float(os.getenv("FALLBACK_LLM_TIMEOUT", "15.0")))


# Singleton instance of GatewayConfig
gateway_config = GatewayConfig()
