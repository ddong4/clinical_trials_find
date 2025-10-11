import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.api.studies import router as studies_router
from app.core.config import settings
from app.models.extraction import (
    TranscriptExtractionRequest,
    TranscriptExtractionResponse,
)
from app.services.extraction import TranscriptExtractionService
from app.services.gemini import GeminiService

logger = logging.getLogger(__name__)

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

app.include_router(studies_router)

@app.get("/")
async def root():
    return {"message": "Welcome to StudyBridge API"}

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


@app.post("/extract", response_model=TranscriptExtractionResponse)
async def extract_medical_info(request: TranscriptExtractionRequest):
    """Extract structured medical information from a transcript"""
    try:
        extraction_service = TranscriptExtractionService()
        extraction = await extraction_service.extract_from_transcript(request.transcript)
        
        return TranscriptExtractionResponse(
            extraction=extraction,
            success=True,
            message="Extraction completed successfully"
        )
    except Exception as e:
        logger.error(f"Error in extract endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Extraction failed: {str(e)}")
    
@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
