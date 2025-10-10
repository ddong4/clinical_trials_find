"""
Service for extracting medical information from transcripts using Gemini AI
"""
import json
import logging
from typing import Any, Dict

from app.models.extraction import MedicalExtraction
from app.prompt.extract_keywords import PROMPT
from app.services.gemini import GeminiService

logger = logging.getLogger(__name__)


class TranscriptExtractionService:
    """Service for extracting structured medical data from transcripts"""
    
    def __init__(self):
        self.gemini_service = GeminiService()
    
    def _get_schema_example(self) -> Dict[str, Any]:
        """Get the JSON schema example for the prompt"""
        return {
            "diagnosis": "string - Primary diagnosis or 'Unknown' if not mentioned",
            "conditions": ["array of strings - medical conditions mentioned"],
            "symptoms": ["array of strings - symptoms described"],
            "medications": ["array of strings - current medications mentioned"],
            "age": "string or null - patient age if mentioned",
            "gender": "string or null - patient gender if mentioned",
            "medical_history": ["array of strings - relevant medical history"],
            "interventions": ["array of strings - treatments or interventions mentioned"],
            "keywords": ["array of strings - medical keywords for search"]
        }
    
    async def extract_from_transcript(self, transcript: str) -> MedicalExtraction:
        """
        Extract structured medical information from a transcript
        """
        try:
            # Prepare the prompt with schema and transcript
            schema_json = json.dumps(self._get_schema_example(), indent=2)
            formatted_prompt = PROMPT.format(schema_json, transcript)
            
            # Generate response using Gemini
            messages = [{"content": formatted_prompt}]
            response = await self.gemini_service.generate_response(messages)

            # Clean the response: remove leading/trailing code block markers
            cleaned_response = response.strip()
            if cleaned_response.startswith("```json"):
                cleaned_response = cleaned_response[7:]
            if cleaned_response.startswith("```"):
                cleaned_response = cleaned_response[3:]
            if cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[:-3]
            cleaned_response = cleaned_response.strip()

            # Parse JSON response
            try:
                extracted_data = json.loads(cleaned_response)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response: {e}")
                logger.error(f"Raw response: {response}")
                # Fallback to minimal extraction
                extracted_data = {
                    "diagnosis": "Unknown",
                    "conditions": [],
                    "symptoms": [],
                    "medications": [],
                    "age": None,
                    "gender": None,
                    "medical_history": [],
                    "interventions": [],
                    "keywords": []
                }

            # Ensure diagnosis is present
            if not extracted_data.get("diagnosis"):
                extracted_data["diagnosis"] = "Unknown"

            # Create and return MedicalExtraction object
            return MedicalExtraction(**extracted_data)
            
        except Exception as e:
            logger.error(f"Error extracting from transcript: {e}")
            # Return minimal fallback extraction
            return MedicalExtraction(
                diagnosis="Unknown",
                conditions=[],
                symptoms=[],
                medications=[],
                age=None,
                gender=None,
                medical_history=[],
                interventions=[],
                keywords=[]
            )