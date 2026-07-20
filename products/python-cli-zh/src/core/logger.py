"""
结构化日志配置 — 使用 structlog 库。

开发环境：彩色控制台输出
生产环境：JSON 格式输出（便于日志采集系统处理）
"""
import structlog
from core.config import Settings


def setup_logging(settings: Settings) -> None:
    """
    配置 structlog。
    在应用启动时调用一次。
    """
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
    ]

    if settings.log_json or settings.is_production():
        # 生产环境：JSON 格式输出
        processors = shared_processors + [
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ]
    else:
        # 开发环境：彩色控制台输出
        processors = shared_processors + [
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    """获取配置好的日志记录器。"""
    return structlog.get_logger(name or __name__)
