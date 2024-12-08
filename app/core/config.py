from pydantic_settings import BaseSettings
from typing import Optional, Dict, Any
from pydantic import validator

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Content Recommendation Engine"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: Optional[str] = None
    
    # Supabase Configuration
    SUPABASE_URL: Optional[str] = None
    SUPABASE_KEY: Optional[str] = None
    SUPABASE_JWT_SECRET: Optional[str] = None
    
    @validator("DATABASE_URL", pre=True)
    def assemble_db_url(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if v:
            return v
        if values.get("SUPABASE_URL") and values.get("SUPABASE_JWT_SECRET"):
            return f"postgresql://postgres:{values['SUPABASE_JWT_SECRET']}@db.{values['SUPABASE_URL']}.supabase.co:5432/postgres"
        return "postgresql://postgres:postgres@localhost:5432/recommendation_engine"
    
    # Redis Configuration
    REDIS_URL: Optional[str] = None
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None
    
    # MongoDB Configuration
    MONGODB_URI: Optional[str] = None
    MONGODB_DB_NAME: str = "recommendation_engine"
    
    # Auth
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Service URLs
    FRONTEND_URL: str = "http://localhost:3000"
    API_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings() 