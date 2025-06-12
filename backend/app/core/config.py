import os
from typing import List, Optional
from pydantic import BaseSettings, Field
from functools import lru_cache

class Settings(BaseSettings):
    # API Settings
    api_title: str = "AI Code Review Assistant"
    api_version: str = "1.0.0"
    api_description: str = "An AI-powered code review system"
    
    # Server Settings
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    
    # Database Settings
    database_url: str = Field(..., env="DATABASE_URL")
    
    # AI/ML Settings
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_model: str = "gpt-4"
    max_tokens: int = 2000
    temperature: float = 0.3
    
    # GitHub Settings
    github_app_id: str = Field(..., env="GITHUB_APP_ID")
    github_app_private_key: str = Field(..., env="GITHUB_APP_PRIVATE_KEY")
    github_webhook_secret: Optional[str] = Field(None, env="GITHUB_WEBHOOK_SECRET")
    
    # Security Settings
    secret_key: str = Field(default="your-secret-key-change-in-production", env="SECRET_KEY")
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"
    
    # CORS Settings
    allowed_origins: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # Rate Limiting
    rate_limit_requests: int = 100
    rate_limit_period: int = 3600  # 1 hour
    
    # Code Analysis Settings
    max_file_size: int = 1024 * 1024  # 1MB
    supported_languages: List[str] = [
        "python", "javascript", "typescript", "java", "csharp", 
        "cpp", "go", "rust", "php", "ruby", "swift", "kotlin"
    ]
    
    # Vulnerability Database
    sonarqube_url: Optional[str] = Field(None, env="SONARQUBE_URL")
    sonarqube_token: Optional[str] = Field(None, env="SONARQUBE_TOKEN")
    
    # Redis Settings (for caching and queues)
    redis_url: str = Field(default="redis://localhost:6379", env="REDIS_URL")
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

