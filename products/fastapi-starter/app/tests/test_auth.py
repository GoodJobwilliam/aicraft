"""Integration tests for authentication endpoints."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_success(client: AsyncClient) -> None:
    """POST /api/v1/auth/register should return 201 and user data."""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "alice@example.com",
            "password": "SecurePass123!",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "alice@example.com"
    assert "id" in data
    assert "password" not in data
    assert data["is_active"] is True


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient) -> None:
    """POST /api/v1/auth/register with existing email -> 409."""
    payload = {
        "email": "bob@example.com",
        "password": "SecurePass123!",
    }
    await client.post("/api/v1/auth/register", json=payload)

    response = await client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 409
    assert "already registered" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient) -> None:
    """POST /api/v1/auth/login returns access + refresh tokens."""
    email = "login-test@example.com"
    password = "SecurePass123!"

    await client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password},
    )

    response = await client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient) -> None:
    """POST /api/v1/auth/login with wrong password -> 401."""
    email = "wrong-pw@example.com"
    await client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": "CorrectPass1!"},
    )

    response = await client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": "WrongPass1!"},
    )
    assert response.status_code == 401
    assert "invalid" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_login_nonexistent_user(client: AsyncClient) -> None:
    """POST /api/v1/auth/login with unregistered email -> 401."""
    response = await client.post(
        "/api/v1/auth/login",
        json={
            "email": "ghost@example.com",
            "password": "SomePass123!",
        },
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_refresh_token_success(client: AsyncClient) -> None:
    """POST /api/v1/auth/refresh with valid refresh token -> 200."""
    email = "refresh-ok@example.com"
    password = "SecurePass123!"

    await client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password},
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": password},
    )
    tokens = login_resp.json()

    response = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": tokens["refresh_token"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


@pytest.mark.asyncio
async def test_refresh_with_access_token_fails(
    client: AsyncClient,
) -> None:
    """POST /api/v1/auth/refresh with an access token -> 401."""
    email = "bad-refresh@example.com"
    password = "SecurePass123!"

    await client.post(
        "/api/v1/auth/register",
        json={"email": email, "password": password},
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": password},
    )
    tokens = login_resp.json()

    response = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": tokens["access_token"]},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_refresh_invalid_token(client: AsyncClient) -> None:
    """POST /api/v1/auth/refresh with a garbage token -> 401."""
    response = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": "not-a-real-jwt-token"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_me_authenticated(
    client: AsyncClient, registered_user: dict
) -> None:
    """GET /api/v1/auth/me returns the current user's profile."""
    headers = {
        "Authorization": f"Bearer {registered_user['access_token']}"
    }
    response = await client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == registered_user["email"]
    assert "id" in data
    assert "password" not in data


@pytest.mark.asyncio
async def test_get_me_unauthenticated(client: AsyncClient) -> None:
    """GET /api/v1/auth/me without a token -> 401."""
    response = await client.get("/api/v1/auth/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_me_invalid_token(client: AsyncClient) -> None:
    """GET /api/v1/auth/me with a malformed token -> 401."""
    headers = {"Authorization": "Bearer invalid-token"}
    response = await client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == 401
