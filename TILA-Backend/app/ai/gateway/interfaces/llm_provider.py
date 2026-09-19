from abc import ABC, abstractmethod
from app.ai.gateway.models.request import LLMRequest
from app.ai.gateway.models.response import LLMResponse


class LLMProvider(ABC):
    """Abstract Base Class (Interface) for all LLM Provider Adapters in TILA Gateway."""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Returns unique identifier name of provider (e.g. 'groq', 'gemini', 'openai')."""
        pass

    @abstractmethod
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """
        Executes completion call using the provider's specific API / SDK,
        and returns a standardized, normalized LLMResponse.
        """
        pass
