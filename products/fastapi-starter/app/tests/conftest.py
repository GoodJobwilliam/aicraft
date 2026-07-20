"""pytest fixtures for the FastAPI Starter test suite."""

import uuid

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.security import create_access_token
from app.database import get_session
from app.main import create_app
from app.models import User
from app.models.base import Base


@pytest_asyncio.fixture
async def db_engine():
    """Create a fresh SQLite in-memory database for each test session."""
    engine = create_async_engine("sqlite+aiosqlite://", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture
async def db_session(db_engine):
    """Provide an async session bound to the test database."""
    factory = async_sessionmaker(
        db_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with factory() as session:
        yield session


@pytest_asyncio.fixture
async def client(db_session):
    """Provide an httpx AsyncClient with the app's dependency overridden.

    The ``get_session`` dependency is swapped so that all requests
    use the test database session.
    """
    app = create_app()

    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session

    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport, base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def registered_user(client: AsyncClient) -> dict:
    """Register and return a user dict with email, password, and tokens."""
    email = f"test-{uuid.uuid4().hex[:8]}@example.com"
    password = "SecurePass123!"

    resp = await client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password},
    )
    assert resp.status_code == 201
    user = resp.json()

    tokens = await client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": password},
    )
    token_data = tokens.json()

    return {
        "id": user["id"],
        "email": email,
        "password": password,
        "access_token": token_data["access_token"],
        "refresh_token": token_data["refresh_token"],
    }
