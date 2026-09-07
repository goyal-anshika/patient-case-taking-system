from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    APP_NAME: str = "Patient Case Taking System"
    APP_ENV: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str
    SECRET_KEY: str

    OPENROUTER_API_KEY: str | None = None
    OPENROUTER_MODEL: str = "YOUR_MODEL_ID"
    
    SPEECH_PROVIDER: str = "mock"
    TTS_PROVIDER: str = "mock"
    
    OCR_PROVIDER: str = "paddleocr"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )
        
settings = Settings()

