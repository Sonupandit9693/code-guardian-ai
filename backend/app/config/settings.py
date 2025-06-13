# backend/app/config/settings.py
from pydantic_settings import BaseSettings
from typing import List, Optional
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Code Review Assistant"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/codereviewer"
    MONGODB_URL: str = "mongodb://localhost:27017/codereviewer"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_SECRET: str = "jwt-secret-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 3600
    
    # GitHub Integration
    GITHUB_APP_ID: Optional[str] = None
    GITHUB_PRIVATE_KEY: Optional[str] = None
    GITHUB_WEBHOOK_SECRET: Optional[str] = None
    GITHUB_CLIENT_ID: Optional[str] = None
    GITHUB_CLIENT_SECRET: Optional[str] = None
    
    # AI Services
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_ORG_ID: Optional[str] = None
    
    # External Services
    SONARQUBE_URL: Optional[str] = None
    SONARQUBE_TOKEN: Optional[str] = None
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # CORS
    ALLOWED_HOSTS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # Application
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()