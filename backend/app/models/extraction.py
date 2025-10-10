"""
Pydantic models for medical transcript extraction
"""
from typing import List, Optional

from pydantic import BaseModel, Field


class TranscriptExtractionRequest(BaseModel):
    """Request model for transcript extraction"""
    transcript: str = Field(..., description="Medical visit transcript text")


class MedicalExtraction(BaseModel):
    """Medical information extracted from transcript"""
    # Primary diagnosis - required field
    diagnosis: str = Field(..., description="Primary diagnosis or 'Unknown' if not mentioned")
    
    # Additional medical information that could be useful for clinical trial matching
    conditions: List[str] = Field(default_factory=list, description="List of medical conditions mentioned")
    symptoms: List[str] = Field(default_factory=list, description="List of symptoms described")
    medications: List[str] = Field(default_factory=list, description="Current medications mentioned")
    age: Optional[str] = Field(None, description="Patient age if mentioned")
    gender: Optional[str] = Field(None, description="Patient gender if mentioned")
    medical_history: List[str] = Field(default_factory=list, description="Relevant medical history")
    interventions: List[str] = Field(default_factory=list, description="Treatments or interventions mentioned")
    keywords: List[str] = Field(default_factory=list, description="Medical keywords for search")


class TranscriptExtractionResponse(BaseModel):
    """Response model for transcript extraction"""
    extraction: MedicalExtraction
    success: bool = True
    message: str = "Extraction completed successfully"