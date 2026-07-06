from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    OLLAMA_MODEL: str             #This is ollama
    EMBEDDING_MODEL: str          # Embedding Model
    DATA_PATH: str
    CHROMA_PATH: str
    HOST: str = "0.0.0.0"
    PORT: int = 8000

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
