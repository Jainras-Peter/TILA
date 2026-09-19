from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class LLMRequest:
    """Standardized request object for LLM calls across all providers."""
    prompt: str
    system_prompt: Optional[str] = None
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    model: Optional[str] = None
    timeout: Optional[float] = None
    extra_params: Optional[Dict[str, Any]] = field(default_factory=dict)

    def model_copy(self) -> "LLMRequest":
        return LLMRequest(
            prompt=self.prompt,
            system_prompt=self.system_prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            model=self.model,
            timeout=self.timeout,
            extra_params=self.extra_params.copy() if self.extra_params else {}
        )
