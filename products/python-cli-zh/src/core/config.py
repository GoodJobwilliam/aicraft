"""
应用配置管理 — 使用 Pydantic Settings 加载配置。

配置来源（优先级从高到低）：
1. 环境变量
2. .env 文件
3. 默认值
"""
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    应用配置。
    
    所有字段都有合理的默认值。通过环境变量或 .env 文件覆盖。
    """
    # 应用信息
    app_name: str = "CLI 中文模板"
    app_env: str = "development"  # development | staging | production
    debug: bool = True

    # API 配置
    api_base_url: str = "https://api.example.com"
    api_timeout: int = 30
    api_max_retries: int = 3

    # 日志配置
    log_level: str = "INFO"  # DEBUG | INFO | WARNING | ERROR | CRITICAL
    log_json: bool = False  # 生产环境建议设为 True

    # 路径配置
    data_dir: Path = Path.home() / ".cli-zh" / "data"
    config_dir: Path = Path.home() / ".cli-zh" / "config"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    def is_production(self) -> bool:
        """判断是否为生产环境。"""
        return self.app_env == "production"
