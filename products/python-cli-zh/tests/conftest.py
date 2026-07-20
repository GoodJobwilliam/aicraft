"""
pytest 测试夹具和配置。
"""
from pathlib import Path
from typing import Generator
from unittest.mock import AsyncMock, patch

import pytest
from core.config import Settings


@pytest.fixture
def settings() -> Settings:
    """测试用配置（安全的默认值）。"""
    return Settings(
        app_env="testing",
        debug=False,
        log_level="DEBUG",
        api_base_url="http://test.example.com",
        data_dir=Path("/tmp/.cli-zh-test/data"),
        config_dir=Path("/tmp/.cli-zh-test/config"),
    )
