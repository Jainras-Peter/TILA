from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any


@dataclass
class LLMAttemptLog:
    """Execution audit log for an individual LLM invocation attempt."""
    provider: str
    model: str
    attempt_number: int
    status: str  # "success", "failed", "timeout"
    latency_ms: float
    error: Optional[str] = None


@dataclass
class LLMResponse:
    """Standardized normalized response object returned by LLM Gateway."""
    text: str
    provider_used: str
    model_used: str
    is_fallback: bool = False
    attempts: List[LLMAttemptLog] = field(default_factory=list)
    total_latency_ms: float = 0.0
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
