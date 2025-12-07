from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Robotics Textbook Platform"
    API_V1_STR: str = "/api/v1"
    
    # Gemini / Cohere
    GOOGLE_API_KEY: str | None = None
    COHERE_API_KEY: str | None = None
    GEMINI_MODEL: str = "gemini-2.0-flash-exp"
    EMBEDDING_MODEL: str = "text-embedding-004"
    
    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: str | None = None
    QDRANT_COLLECTION: str = "textbook_chunks"
    
    # Neon / Postgres
    # Neon / Postgres / SQLite
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    
    # Auth
    SECRET_KEY: str = "dev_secret_key_change_in_prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

settings = Settings()
