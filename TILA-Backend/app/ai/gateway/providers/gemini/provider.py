import time
import json
import asyncio
import urllib.request
import urllib.error
from typing import Optional

try:
    import httpx
except ImportError:
    httpx = None

from app.ai.gateway.interfaces.llm_provider import LLMProvider
from app.ai.gateway.models.request import LLMRequest
from app.ai.gateway.models.response import LLMResponse, LLMAttemptLog
from app.ai.gateway.config import gateway_config
from app.ai.gateway.exceptions import LLMProviderAPIError, LLMTimeoutError


class GeminiProvider(LLMProvider):
    """Adapter implementation for Google Gemini LLM API."""

    @property
    def provider_name(self) -> str:
        return "gemini"

    async def generate(self, request: LLMRequest) -> LLMResponse:
        api_key = gateway_config.GEMINI_API_KEY
        if not api_key:
            raise LLMProviderAPIError(self.provider_name, "GEMINI_API_KEY is not configured.", status_code=401)

        raw_model = request.model or gateway_config.FALLBACK_LLM_MODEL
        model = raw_model.replace("models/", "")
        timeout = request.timeout or gateway_config.FALLBACK_LLM_TIMEOUT

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

        contents = []
        if request.system_prompt:
            contents.append({
                "role": "user",
                "parts": [{"text": f"System Instruction: {request.system_prompt}\n\n{request.prompt}"}]
            })
        else:
            contents.append({
                "role": "user",
                "parts": [{"text": request.prompt}]
            })

        payload = {
            "contents": contents,
            "generationConfig": {
                "temperature": request.temperature,
            }
        }
        if request.max_tokens:
            payload["generationConfig"]["maxOutputTokens"] = request.max_tokens

        start_time = time.perf_counter()

        if httpx is not None:
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.post(url, json=payload)
                    latency_ms = (time.perf_counter() - start_time) * 1000

                    if response.status_code != 200:
                        raise LLMProviderAPIError(self.provider_name, f"Gemini HTTP {response.status_code}: {response.text}", status_code=response.status_code)

                    data = response.json()
                    text_content = data["candidates"][0]["content"]["parts"][0]["text"]
                    attempt = LLMAttemptLog(
                        provider=self.provider_name,
                        model=model,
                        attempt_number=1,
                        status="success",
                        latency_ms=round(latency_ms, 2)
                    )
                    return LLMResponse(
                        text=text_content,
                        provider_used=self.provider_name,
                        model_used=model,
                        is_fallback=False,
                        attempts=[attempt],
                        total_latency_ms=round(latency_ms, 2),
                        metadata={"candidates": len(data.get("candidates", []))}
                    )
            except httpx.TimeoutException:
                raise LLMTimeoutError(self.provider_name, timeout_seconds=timeout)
            except httpx.RequestError as exc:
                raise LLMProviderAPIError(self.provider_name, f"Network request failed: {str(exc)}")
        else:
            def _http_post():
                json_data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(url, data=json_data, headers={"Content-Type": "application/json"}, method="POST")
                try:
                    with urllib.request.urlopen(req, timeout=timeout) as resp:
                        res_body = resp.read().decode("utf-8")
                        return resp.status, json.loads(res_body)
                except urllib.error.HTTPError as err:
                    res_body = err.read().decode("utf-8") if err.fp else str(err)
                    raise LLMProviderAPIError(self.provider_name, f"Gemini HTTP {err.code}: {res_body}", status_code=err.code)
                except TimeoutError:
                    raise LLMTimeoutError(self.provider_name, timeout_seconds=timeout)
                except urllib.error.URLError as err:
                    raise LLMProviderAPIError(self.provider_name, f"Network error: {str(err.reason)}")

            try:
                status_code, data = await asyncio.to_thread(_http_post)
                latency_ms = (time.perf_counter() - start_time) * 1000
                text_content = data["candidates"][0]["content"]["parts"][0]["text"]
                attempt = LLMAttemptLog(
                    provider=self.provider_name,
                    model=model,
                    attempt_number=1,
                    status="success",
                    latency_ms=round(latency_ms, 2)
                )
                return LLMResponse(
                    text=text_content,
                    provider_used=self.provider_name,
                    model_used=model,
                    is_fallback=False,
                    attempts=[attempt],
                    total_latency_ms=round(latency_ms, 2),
                    metadata={"candidates": len(data.get("candidates", []))}
                )
            except (LLMTimeoutError, LLMProviderAPIError):
                raise
            except Exception as exc:
                raise LLMProviderAPIError(self.provider_name, f"Request execution failed: {str(exc)}")
