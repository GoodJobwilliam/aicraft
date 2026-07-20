"""Alembic environment configuration — async SQLAlchemy 2.0 support."""

import asyncio
from pathlib import Path
from sys import path as sys_path

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

# Add the project root to sys.path so Alembic can import app modules.
sys_path.insert(0, str(Path(__file__).parent.parent))

from app.config import settings  # noqa: E402
from app.models.base import Base  # noqa: E402

# Import all models so Alembic's autogenerate can detect them.
from app.models import User  # noqa: E402, F401

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (emit SQL without a DB connection)."""
    context.configure(
        url=str(settings.DATABASE_URL),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Configure Alembic context with a live connection."""
    context.configure(
        connection=connection, target_metadata=target_metadata
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Create an async engine and run migrations online."""
    connectable = create_async_engine(
        str(settings.DATABASE_URL),
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode (requires a live database)."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
