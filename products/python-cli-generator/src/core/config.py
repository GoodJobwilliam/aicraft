"""
Application configuration via Pydantic Settings.

Reads from environment variables and/or .env file.
"""
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment / .env file.

    All fields have sensible defaults. Override via environment variables
    or a `.env` file in the project root.
    """

    # App
    app_name: str = "CLI Starter"
    app_env: str = "development"  # development | staging | production
    debug: bool = True

    # API
    api_base_url: str = "https://api.example.com"
    api_timeout: int = 30
    api_max_retries: int = 3

    # Logging
    log_level: str = "INFO"  # DEBUG | INFO | WARNING | ERROR | CRITICAL
    log_json: bool = False  # Set True for JSON log output (production)

    # Paths
    data_dir: Path = Path.home() / ".cli-starter" / "data"
    config_dir: Path = Path.home() / ".cli-starter" / "config"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    def is_production(self) -> bool:
        return self.app_env == "production"
