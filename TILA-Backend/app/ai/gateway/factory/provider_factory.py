from typing import Dict, Type
from app.ai.gateway.interfaces.llm_provider import LLMProvider
from app.ai.gateway.providers.groq.provider import GroqProvider
from app.ai.gateway.providers.gemini.provider import GeminiProvider
from app.ai.gateway.providers.openai.provider import OpenAIProvider
from app.ai.gateway.exceptions import LLMProviderNotFoundError


class LLMProviderFactory:
    """Factory for registering and instantiating LLM Providers (Strategy Pattern)."""

    _providers: Dict[str, Type[LLMProvider]] = {
        "groq": GroqProvider,
        "gemini": GeminiProvider,
        "openai": OpenAIProvider,
    }

    @classmethod
    def register_provider(cls, name: str, provider_cls: Type[LLMProvider]) -> None:
        """Register a new LLM provider adapter dynamically."""
        cls._providers[name.lower().strip()] = provider_cls

    @classmethod
    def get_provider(cls, name: str) -> LLMProvider:
        """Instantiate and return the requested LLM provider instance."""
        clean_name = name.lower().strip()
        provider_cls = cls._providers.get(clean_name)
        if not provider_cls:
            raise LLMProviderNotFoundError(clean_name)
        return provider_cls()
