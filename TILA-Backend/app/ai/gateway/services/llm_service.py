import time
import asyncio
import logging
from typing import List

from app.ai.gateway.interfaces.llm_provider import LLMProvider
from app.ai.gateway.models.request import LLMRequest
from app.ai.gateway.models.response import LLMResponse, LLMAttemptLog
from app.ai.gateway.factory.provider_factory import LLMProviderFactory
from app.ai.gateway.config import gateway_config
from app.ai.gateway.exceptions import (
    LLMGatewayException,
    LLMAllProvidersFailedError,
    LLMTimeoutError,
    LLMProviderAPIError,
    classify_error_retryability,
)

logger = logging.getLogger("LLMService")


class LLMService:
    """
    Central LLM Gateway Service in TILA.
    Executes LLM requests using configured Main Provider with smart retry logic,
    and falls back to Fallback Provider upon failure.

    Smart Error Classification:
    - Transient Errors (429, 500, 502, 503, 504, Timeout, Connection): Retries main provider.
    - Permanent Errors (400, 401, 403, 404, Invalid Key, Invalid Model): Bypasses retries immediately and triggers fallback.
    """

    def __init__(self):
        self.config = gateway_config

    async def generate(self, request: LLMRequest) -> LLMResponse:
        total_start_time = time.perf_counter()
        attempt_logs: List[LLMAttemptLog] = []

        # 1. Main LLM Attempt Loop
        main_provider_name = self.config.MAIN_LLM_PROVIDER
        main_model_name = request.model or self.config.MAIN_LLM_MODEL
        main_retry_count = self.config.MAIN_LLM_RETRY_COUNT
        main_retry_interval = self.config.MAIN_LLM_RETRY_INTERVAL
        main_timeout = request.timeout or self.config.MAIN_LLM_TIMEOUT

        logger.info(f"LLM Gateway initiating request via Main Provider '{main_provider_name}' (Model: '{main_model_name}')")

        for attempt_idx in range(1 + main_retry_count):
            attempt_num = attempt_idx + 1
            attempt_start = time.perf_counter()

            try:
                provider = LLMProviderFactory.get_provider(main_provider_name)
                req_copy = request.model_copy()
                req_copy.model = main_model_name
                req_copy.timeout = main_timeout

                response = await provider.generate(req_copy)
                latency_ms = (time.perf_counter() - attempt_start) * 1000

                log_entry = LLMAttemptLog(
                    provider=main_provider_name,
                    model=main_model_name,
                    attempt_number=attempt_num,
                    status="success",
                    latency_ms=round(latency_ms, 2)
                )
                attempt_logs.append(log_entry)

                total_latency = (time.perf_counter() - total_start_time) * 1000
                response.attempts = attempt_logs
                response.total_latency_ms = round(total_latency, 2)
                response.is_fallback = False
                return response

            except Exception as exc:
                latency_ms = (time.perf_counter() - attempt_start) * 1000
                error_msg = str(exc)
                is_retryable = classify_error_retryability(exc)
                error_type = "Retryable" if is_retryable else "Permanent"

                logger.warning(f"Main Provider '{main_provider_name}' Attempt {attempt_num} failed ({error_type}): {error_msg}")

                attempt_logs.append(LLMAttemptLog(
                    provider=main_provider_name,
                    model=main_model_name,
                    attempt_number=attempt_num,
                    status="timeout" if isinstance(exc, LLMTimeoutError) else "failed",
                    latency_ms=round(latency_ms, 2),
                    error=f"[{error_type}] {error_msg}"
                ))

                if not is_retryable:
                    logger.info(f"Main Provider '{main_provider_name}' encountered permanent non-retryable error. Bypassing remaining {main_retry_count - attempt_idx} retries and switching to Fallback.")
                    break

                if attempt_idx < main_retry_count:
                    await asyncio.sleep(main_retry_interval)

        # 2. Fallback LLM Attempt Loop
        fallback_provider_name = self.config.FALLBACK_LLM_PROVIDER
        fallback_model_name = self.config.FALLBACK_LLM_MODEL
        fallback_retry_count = self.config.FALLBACK_LLM_RETRY_COUNT
        fallback_retry_interval = self.config.FALLBACK_LLM_RETRY_INTERVAL
        fallback_timeout = request.timeout or self.config.FALLBACK_LLM_TIMEOUT

        logger.warning(f"Initiating Fallback Provider '{fallback_provider_name}' (Model: '{fallback_model_name}').")

        for attempt_idx in range(1 + fallback_retry_count):
            attempt_num = attempt_idx + 1
            attempt_start = time.perf_counter()

            try:
                provider = LLMProviderFactory.get_provider(fallback_provider_name)
                req_copy = request.model_copy()
                req_copy.model = fallback_model_name
                req_copy.timeout = fallback_timeout

                response = await provider.generate(req_copy)
                latency_ms = (time.perf_counter() - attempt_start) * 1000

                log_entry = LLMAttemptLog(
                    provider=fallback_provider_name,
                    model=fallback_model_name,
                    attempt_number=attempt_num,
                    status="success",
                    latency_ms=round(latency_ms, 2)
                )
                attempt_logs.append(log_entry)

                total_latency = (time.perf_counter() - total_start_time) * 1000
                response.attempts = attempt_logs
                response.total_latency_ms = round(total_latency, 2)
                response.is_fallback = True
                return response

            except Exception as exc:
                latency_ms = (time.perf_counter() - attempt_start) * 1000
                error_msg = str(exc)
                is_retryable = classify_error_retryability(exc)
                error_type = "Retryable" if is_retryable else "Permanent"

                logger.error(f"Fallback Provider '{fallback_provider_name}' Attempt {attempt_num} failed ({error_type}): {error_msg}")

                attempt_logs.append(LLMAttemptLog(
                    provider=fallback_provider_name,
                    model=fallback_model_name,
                    attempt_number=attempt_num,
                    status="timeout" if isinstance(exc, LLMTimeoutError) else "failed",
                    latency_ms=round(latency_ms, 2),
                    error=f"[{error_type}] {error_msg}"
                ))

                if not is_retryable:
                    logger.info(f"Fallback Provider '{fallback_provider_name}' encountered permanent non-retryable error. Stopping execution.")
                    break

                if attempt_idx < fallback_retry_count:
                    await asyncio.sleep(fallback_retry_interval)

        # 3. Exhausted All Providers
        total_latency = (time.perf_counter() - total_start_time) * 1000
        error_details = "; ".join([f"[{a.provider} #{a.attempt_number} {a.status}]: {a.error}" for a in attempt_logs])
        logger.critical(f"LLM Gateway: All providers failed after {len(attempt_logs)} total attempts. Errors: {error_details}")
        
        raise LLMAllProvidersFailedError(
            f"All configured LLM providers failed. Attempt trace: {error_details}"
        )
