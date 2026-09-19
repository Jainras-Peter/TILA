try:
    from fastapi import APIRouter, Query, HTTPException, status
except ImportError:
    APIRouter = None

from typing import Optional
from app.ai.gateway.models.request import LLMRequest
from app.ai.gateway.models.response import LLMResponse
from app.ai.gateway.services.llm_service import LLMService
from app.ai.gateway.exceptions import LLMGatewayException

if APIRouter is not None:
    router = APIRouter(prefix="/llm", tags=["LLM Gateway"])
    llm_service = LLMService()

    @router.get("", summary="Test LLM Gateway (GET)")
    async def test_llm_get(
        prompt: str = Query("Hello TILA! Are you operational?", description="Prompt to test LLM completion"),
        system_prompt: Optional[str] = Query(None, description="Optional system prompt"),
        temperature: float = Query(0.7, ge=0.0, le=2.0),
    ):
        """
        Test endpoint to send a prompt to the LLM Gateway.
        Executes Main LLM provider with retries, falling back to Fallback provider if necessary.
        """
        try:
            request = LLMRequest(
                prompt=prompt,
                system_prompt=system_prompt,
                temperature=temperature,
            )
            resp = await llm_service.generate(request)
            return resp.to_dict()
        except LLMGatewayException as exc:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc))
        except Exception as exc:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(exc)}")

    @router.post("", summary="Test LLM Gateway (POST)")
    async def test_llm_post(request: LLMRequest):
        """
        POST endpoint to send a structured LLMRequest payload to the LLM Gateway.
        Returns normalized response and execution audit logs.
        """
        try:
            resp = await llm_service.generate(request)
            return resp.to_dict()
        except LLMGatewayException as exc:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc))
        except Exception as exc:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(exc)}")
else:
    router = None
