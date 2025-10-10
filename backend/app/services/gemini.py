"""
Service for interacting with Google Gemini API
"""
import asyncio
import logging
import os
from functools import wraps
from typing import Any, Callable, Dict, List

from google import genai
from google.genai import types

from app.core.config import settings

# Set up logger
logger = logging.getLogger(__name__)


def retry_on_null_response(max_retries: int = 3, delay: float = 0.5):
    """Decorator to retry async functions when they return null/empty responses"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            retry_count = 0
            
            while retry_count < max_retries:
                try:
                    result = await func(*args, **kwargs)
                    
                    # Check if result is null or empty
                    if result and str(result).strip():
                        if retry_count > 0:
                            logger.info(f"Successfully generated response after {retry_count + 1} attempts")
                        return result
                    else:
                        retry_count += 1
                        logger.warning(f"Received null/empty response (attempt {retry_count}/{max_retries})")
                        if retry_count < max_retries:
                            logger.info(f"Retrying in {delay} seconds... (attempt {retry_count + 1}/{max_retries})")
                            await asyncio.sleep(delay)
                            continue
                        else:
                            logger.error("Maximum retries reached due to null/empty responses")
                            raise Exception("Received null or empty response after maximum retries")
                            
                except Exception as e:
                    retry_count += 1
                    logger.warning(f"API error on attempt {retry_count}/{max_retries}: {str(e)}")
                    if retry_count < max_retries:
                        logger.info(f"Retrying in {delay} seconds... (attempt {retry_count + 1}/{max_retries})")
                        await asyncio.sleep(delay)
                        continue
                    else:
                        logger.error(f"Maximum retries reached due to API errors: {str(e)}")
                        raise Exception(f"Failed to generate response after {max_retries} attempts: {str(e)}")
            
            # This should never be reached, but included for completeness
            raise Exception("Unexpected error in retry loop")
        return wrapper
    return decorator


class GeminiService:
    """Service for interacting with Google Gemini API"""
    
    def __init__(self):
        if not settings.gemini_key:
            raise ValueError("GEMINI_KEY environment variable is required")
        
        # Set the API key for the Google client (it expects GEMINI_API_KEY)
        os.environ["GEMINI_API_KEY"] = settings.gemini_key
        
        # The client automatically gets the API key from GEMINI_API_KEY environment variable
        self.client = genai.Client()
    
    @retry_on_null_response(max_retries=3, delay=0.5)
    async def generate_response(self, messages: List[Dict]) -> str:
        """
        Generate response using Gemini API
        """
        # Convert messages to a simple content string for now
        # TODO: use this as basis for transcript read
        content = messages[-1].get("content", "") if messages else ""
        
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=content,
            config=types.GenerateContentConfig(
                max_output_tokens=1024,
            ),
        )
        
        return response.text
    
    def is_configured(self) -> bool:
        """Check if the service is properly configured"""
        return settings.gemini_key is not None


# Example of how to use it in an endpoint
def get_gemini_service() -> GeminiService:
    """Dependency function to get configured Gemini service"""
    return GeminiService()
