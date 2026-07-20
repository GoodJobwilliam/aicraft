import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.security import hash_password
from app.database import get_session
from app.models import User
from app.schemas.user import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/me",
    response_model=UserRead,
    summary="Get own profile",
)
async def read_current_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """Return the profile of the currently authenticated user."""
    return current_user


@router.put(
    "/me",
    response_model=UserRead,
    summary="Update own profile",
)
async def update_current_user(
    body: UserUpdate,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
) -> User:
    """Update email, password, or active status for the current user."""
    if body.email is not None:
        # Check uniqueness
        result = await session.execute(
            select(User).where(User.email == body.email)
        )
        existing = result.scalar_one_or_none()
        if existing and existing.id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already taken",
            )
        current_user.email = body.email

    if body.password is not None:
        current_user.hashed_password = hash_password(body.password)

    if body.is_active is not None:
        current_user.is_active = body.is_active

    await session.flush()
    await session.refresh(current_user)
    return current_user


@router.get(
    "/{user_id}",
    response_model=UserRead,
    summary="Get a user by ID",
)
async def read_user(
    user_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
) -> User:
    """Return a specific user by UUID (requires authentication)."""
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user
