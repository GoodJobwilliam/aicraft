from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.database import get_session
from app.models import User
from app.schemas.auth import (
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    Token,
)
from app.schemas.user import UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(
    body: RegisterRequest,
    session: AsyncSession = Depends(get_session),
) -> User:
    """Create a new user account.

    Returns the created user (without password).
    """
    # Check for existing user
    result = await session.execute(
        select(User).where(User.email == body.email)
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    user = User(
        email=body.email,
        hashed_password=hash_password(body.password),
    )
    session.add(user)
    await session.flush()
    await session.refresh(user)
    return user


@router.post(
    "/login",
    response_model=Token,
    summary="Authenticate and receive tokens",
)
async def login(
    body: LoginRequest,
    session: AsyncSession = Depends(get_session),
) -> Token:
    """Authenticate with email + password and receive JWT tokens."""
    result = await session.execute(
        select(User).where(User.email == body.email)
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})

    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post(
    "/refresh",
    response_model=Token,
    summary="Refresh an expired access token",
)
async def refresh(
    body: RefreshRequest,
    session: AsyncSession = Depends(get_session),
) -> Token:
    """Issue a new access/refresh token pair using a valid refresh token."""
    try:
        payload = decode_token(body.refresh_token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
        )

    user_id: str | None = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    result = await session.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()

    if user is None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    new_refresh_token = create_refresh_token(data={"sub": str(user.id)})

    return Token(
        access_token=access_token, refresh_token=new_refresh_token
    )


@router.get(
    "/me",
    response_model=UserRead,
    summary="Get the currently authenticated user",
)
async def get_me(
    current_user: User = Depends(get_current_user),
) -> User:
    """Return the authenticated user's profile."""
    return current_user
