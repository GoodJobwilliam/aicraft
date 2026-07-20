from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "FastAPI Starter"
    DEBUG: bool = False

    # Database
    DATABASE_URL: PostgresDsn = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/app"
    )

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    SECRET_KEY: str = "change-me-to-a-long-random-string"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, v: str) -> str:
        if v == "change-me-to-a-long-random-string":
            import warnings

            warnings.warn(
                "SECRET_KEY is set to the default value. "
                "Change it in production!",
                stacklevel=2,
            )
        return v


settings = Settings()
