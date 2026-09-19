import unittest
import asyncio
from unittest.mock import patch

from app.ai.gateway.models.request import LLMRequest
from app.ai.gateway.models.response import LLMResponse, LLMAttemptLog
from app.ai.gateway.interfaces.llm_provider import LLMProvider
from app.ai.gateway.factory.provider_factory import LLMProviderFactory
from app.ai.gateway.services.llm_service import LLMService
from app.ai.gateway.config import gateway_config
from app.ai.gateway.exceptions import (
    LLMProviderNotFoundError,
    LLMProviderAPIError,
    LLMAllProvidersFailedError,
)


class MockSuccessProvider(LLMProvider):
    @property
    def provider_name(self) -> str:
        return "mock_success"

    async def generate(self, request: LLMRequest) -> LLMResponse:
        attempt = LLMAttemptLog(
            provider=self.provider_name,
            model=request.model or "mock-model",
            attempt_number=1,
            status="success",
            latency_ms=10.0,
        )
        return LLMResponse(
            text="Mock success output",
            provider_used=self.provider_name,
            model_used=request.model or "mock-model",
            is_fallback=False,
            attempts=[attempt],
            total_latency_ms=10.0,
        )


class MockFailingProvider(LLMProvider):
    @property
    def provider_name(self) -> str:
        return "mock_failing"

    async def generate(self, request: LLMRequest) -> LLMResponse:
        raise LLMProviderAPIError(self.provider_name, "Simulated transient 500 failure", status_code=500)


class MockPermanentFailingProvider(LLMProvider):
    @property
    def provider_name(self) -> str:
        return "mock_perm_failing"

    async def generate(self, request: LLMRequest) -> LLMResponse:
        raise LLMProviderAPIError(self.provider_name, "Model Not Found", status_code=404)


class TestLLMGateway(unittest.IsolatedAsyncioTestCase):

    async def test_provider_factory(self):
        LLMProviderFactory.register_provider("mock_success", MockSuccessProvider)
        provider = LLMProviderFactory.get_provider("mock_success")
        self.assertIsInstance(provider, MockSuccessProvider)

        with self.assertRaises(LLMProviderNotFoundError):
            LLMProviderFactory.get_provider("non_existent_provider")

    async def test_main_provider_success(self):
        LLMProviderFactory.register_provider("mock_success", MockSuccessProvider)

        with patch.object(gateway_config, "MAIN_LLM_PROVIDER", "mock_success"):
            service = LLMService()
            req = LLMRequest(prompt="Hello World")
            resp = await service.generate(req)

            self.assertEqual(resp.text, "Mock success output")
            self.assertEqual(resp.provider_used, "mock_success")
            self.assertFalse(resp.is_fallback)
            self.assertEqual(len(resp.attempts), 1)
            self.assertEqual(resp.attempts[0].status, "success")

    async def test_fallback_activation_on_transient_failure(self):
        """Transient 500 error will retry MAIN_LLM_RETRY_COUNT times before fallback."""
        LLMProviderFactory.register_provider("mock_failing", MockFailingProvider)
        LLMProviderFactory.register_provider("mock_success", MockSuccessProvider)

        with patch.object(gateway_config, "MAIN_LLM_PROVIDER", "mock_failing"), \
             patch.object(gateway_config, "FALLBACK_LLM_PROVIDER", "mock_success"), \
             patch.object(gateway_config, "MAIN_LLM_RETRY_COUNT", 1), \
             patch.object(gateway_config, "MAIN_LLM_RETRY_INTERVAL", 0.01):

            service = LLMService()
            req = LLMRequest(prompt="Testing Fallback")
            resp = await service.generate(req)

            self.assertEqual(resp.text, "Mock success output")
            self.assertEqual(resp.provider_used, "mock_success")
            self.assertTrue(resp.is_fallback)
            # 2 failed attempts on main (1 initial + 1 retry) + 1 success attempt on fallback = 3 total
            self.assertEqual(len(resp.attempts), 3)
            self.assertEqual(resp.attempts[0].provider, "mock_failing")
            self.assertEqual(resp.attempts[1].provider, "mock_failing")
            self.assertEqual(resp.attempts[2].provider, "mock_success")

    async def test_immediate_fallback_on_permanent_error(self):
        """Permanent 404/401 error should bypass retries instantly and trigger fallback on attempt 1."""
        LLMProviderFactory.register_provider("mock_perm_failing", MockPermanentFailingProvider)
        LLMProviderFactory.register_provider("mock_success", MockSuccessProvider)

        with patch.object(gateway_config, "MAIN_LLM_PROVIDER", "mock_perm_failing"), \
             patch.object(gateway_config, "FALLBACK_LLM_PROVIDER", "mock_success"), \
             patch.object(gateway_config, "MAIN_LLM_RETRY_COUNT", 5), \
             patch.object(gateway_config, "MAIN_LLM_RETRY_INTERVAL", 0.01):

            service = LLMService()
            req = LLMRequest(prompt="Testing Permanent Error Fast Fallback")
            resp = await service.generate(req)

            self.assertEqual(resp.text, "Mock success output")
            self.assertEqual(resp.provider_used, "mock_success")
            self.assertTrue(resp.is_fallback)
            # Permanent error: 1 attempt on main (retries bypassed!) + 1 attempt on fallback = 2 total!
            self.assertEqual(len(resp.attempts), 2)
            self.assertEqual(resp.attempts[0].provider, "mock_perm_failing")
            self.assertIn("[Permanent]", resp.attempts[0].error)
            self.assertEqual(resp.attempts[1].provider, "mock_success")

    async def test_all_providers_exhausted(self):
        LLMProviderFactory.register_provider("mock_failing", MockFailingProvider)

        with patch.object(gateway_config, "MAIN_LLM_PROVIDER", "mock_failing"), \
             patch.object(gateway_config, "FALLBACK_LLM_PROVIDER", "mock_failing"), \
             patch.object(gateway_config, "MAIN_LLM_RETRY_COUNT", 0), \
             patch.object(gateway_config, "FALLBACK_LLM_RETRY_COUNT", 0):

            service = LLMService()
            req = LLMRequest(prompt="Testing Double Failure")

            with self.assertRaises(LLMAllProvidersFailedError):
                await service.generate(req)


if __name__ == "__main__":
    unittest.main()
