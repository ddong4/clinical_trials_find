from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file"""
    
    # API Keys
    gemini_key: Optional[str] = None
    
    # Application settings
    app_name: str = "StudyBridge API"
    debug: bool = False
    
    # CORS settings
    allowed_hosts: list[str] = ["*"]  # In production, specify actual domains
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # Case insensitive environment variables
        case_sensitive = False


# Create a global settings instance
settings = Settings()