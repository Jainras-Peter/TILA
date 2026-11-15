from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class LLMAttemptLog:
    """Execution audit log for an individual LLM invocation attempt."""

    provider: str
    model: str
    attempt_number: int
    status: str  # "success", "failed", "timeout"
    latency_ms: float
    error: str | None = None


@dataclass
class LLMResponse:
    """Standardized normalized response object returned by LLM Gateway."""

    text: str
    provider_used: str
    model_used: str
    is_fallback: bool = False
    attempts: list[LLMAttemptLog] = field(default_factory=list)
    total_latency_ms: float = 0.0
    metadata: dict[str, Any] | None = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
