from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.core.config import settings
from app.services.gemini import GeminiService

app = FastAPI(
    title="StudyBridge API",
    description="API for matching patients with clinical trials",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to StudyBridge API"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }

@app.get("/config")
async def get_config():
    """Debug endpoint to check configuration (hide sensitive data)"""
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "allowed_hosts": settings.allowed_hosts,
        "gemini_key_configured": settings.gemini_key is not None,
        "gemini_key_length": len(settings.gemini_key) if settings.gemini_key else 0
    }

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(request: PromptRequest):
    """Generate text using Gemini API"""
    try:
        service = GeminiService()
        # Convert prompt to messages format expected by generate_response
        messages = [{"content": request.prompt}]
        response = await service.generate_response(messages)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
