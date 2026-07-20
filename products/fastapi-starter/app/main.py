"""FastAPI Starter — Application factory."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.config import settings
from app.core.exceptions import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan — startup / shutdown hooks."""
    # ── Startup ──────────────────────────────────────────────────
    # e.g. verify DB connectivity, warm cache, etc.
    yield
    # ── Shutdown ──────────────────────────────────────────────────
    # e.g. close connections, flush metrics.


def create_app() -> FastAPI:
    """Build and return a configured FastAPI application instance."""
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Register routers
    app.include_router(api_router, prefix="/api/v1")

    # Register custom exception handlers
    register_exception_handlers(app)

    # Health check
    @app.get("/health", tags=["system"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
