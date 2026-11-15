import re
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_csrf import CSRFMiddleware

from app.ai.gateway.router import router as llm_gateway_router
from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.database import close_mongo_connection, connect_to_mongo


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()


settings = get_settings()

app = FastAPI(
    title="TILA - Teaching & Intelligent Learning Assistant API",
    description=(
        "Backend API for TILA, featuring LLM Gateway, RAG pipeline, document management, and chat."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CSRFMiddleware,
    secret=settings.auth_secret,
    sensitive_cookies={settings.auth_cookie_name},
    cookie_name=settings.csrf_cookie_name,
    cookie_secure=settings.is_production,
    cookie_samesite="lax",
    header_name=settings.csrf_header_name,
    required_urls=[
        re.compile(r".*/api/v1/auth/(register|cookie/login|cookie/logout)$"),
    ],
)

app.include_router(api_router, prefix="/api/v1")
app.include_router(llm_gateway_router)
app.include_router(llm_gateway_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
async def root():
    return {
        "app": "TILA Backend API",
        "status": "online",
        "llm_gateway_endpoint": "/llm",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
