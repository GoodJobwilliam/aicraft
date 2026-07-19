"""
Pytest fixtures and configuration.
"""
from pathlib import Path
from typing import Generator
from unittest.mock import AsyncMock, patch

import pytest
from core.config import Settings
from core.client import APIClient


@pytest.fixture
def settings() -> Settings:
    """Test settings with safe defaults."""
    return Settings(
        app_env="testing",
        debug=False,
        log_level="DEBUG",
        api_base_url="http://test.example.com",
        data_dir=Path("/tmp/.cli-starter-test/data"),
        config_dir=Path("/tmp/.cli-starter-test/config"),
    )


@pytest.fixture
def api_client(settings: Settings) -> Generator[APIClient, None, None]:
    """Test API client that doesn't make real HTTP calls."""
    client = APIClient(settings)
    with patch.object(client, "_get_client", return_value=AsyncMock()):
        yield client
