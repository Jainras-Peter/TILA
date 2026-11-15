from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.ai.gateway.router import router as llm_gateway_router

app = FastAPI(
    title="TILA - Teaching & Intelligent Learning Assistant API",
    description="Backend API for TILA, featuring LLM Gateway, RAG pipeline, document management, and chat.",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register LLM Gateway router (/llm and /api/v1/llm)
app.include_router(llm_gateway_router)
app.include_router(llm_gateway_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
async def root():
    return {
        "app": "TILA Backend API",
        "status": "online",
        "llm_gateway_endpoint": "/llm"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
