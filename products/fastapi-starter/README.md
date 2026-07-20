# FastAPI Starter Kit

A production-ready FastAPI project scaffold with async SQLAlchemy 2.0, JWT authentication, Alembic migrations, Docker Compose development environment, and a complete test suite.

Stop copy-pasting boilerplate. Download, customize your `.env`, and start building real features on day one.

## Features

- **Async SQLAlchemy 2.0** — Modern ORM with `async_sessionmaker`, connection pooling, and fully type-annotated models.
- **JWT Authentication** — Access + refresh token flow with `python-jose`. Login, register, and token refresh endpoints ready to use.
- **Pydantic v2 Settings** — Type-safe configuration via `pydantic-settings` with `.env` file support and validation.
- **Alembic Migrations** — Asynchronous migration environment configured out of the box. Run `alembic upgrade head` and go.
- **Docker Compose** — One command (`docker compose up`) starts the app, PostgreSQL 16, and Redis 7.
- **Full Test Suite** — Async pytest fixtures with SQLite in-memory database, httpx `AsyncClient`, and 10+ auth endpoint tests.
- **RESTful API Structure** — Versioned routes (`/api/v1/`), dependency injection for DB sessions and auth, clean separation of models/schemas/routes.
- **Type Hints Everywhere** — Strict `mypy` configuration. Every function, parameter, and return type is annotated.
- **Production Readiness** — Connection pooling, `pool_pre_ping`, structured exception handling, CORS-ready app factory pattern.
- **Developer Experience** — Makefile for common tasks, Ruff for linting/formatting, auto-generated OpenAPI docs at `/docs`.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI 0.115+ |
| ORM | SQLAlchemy 2.0 (async) |
| Database | PostgreSQL 16 + asyncpg |
| Migrations | Alembic 1.14+ |
| Validation | Pydantic v2 + pydantic-settings |
| Auth | python-jose (JWT) + passlib (bcrypt) |
| Testing | pytest + pytest-asyncio + httpx |
| Linting | Ruff + mypy (strict) |
| Containerization | Docker + Docker Compose |
| Cache | Redis 7 |

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 16 (or Docker)
- Redis 7 (optional, for caching)

### Installation

```bash
# 1. Clone/copy the project
cd fastapi-starter

# 2. Create a virtual environment
python -m venv .venv && source .venv/bin/activate

# 3. Install dependencies
make dev

# 4. Configure environment variables
cp .env.example .env
# Edit .env — at minimum change SECRET_KEY

# 5. Run database migrations
alembic upgrade head

# 6. Start the development server
uvicorn app.main:app --reload --port 8000
```

Open **http://localhost:8000/docs** for the interactive Swagger UI.

### Using Docker

```bash
# Start all services (app + postgres + redis)
make docker-up

# Run migrations inside the container
docker compose exec app alembic upgrade head

# Stop all services
make docker-down
```

## Project Structure

```
fastapi-starter/
├── README.md                # Documentation and quick start
├── Makefile                 # Common commands
├── pyproject.toml           # Project config and dependencies
├── .env.example             # Environment template
├── .gitignore
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # App + PostgreSQL + Redis
├── alembic.ini              # Alembic configuration
├── migrations/
│   └── env.py               # Async Alembic environment
└── app/
    ├── __init__.py
    ├── main.py              # FastAPI app factory
    ├── config.py            # Pydantic Settings v2
    ├── database.py          # Async engine + session factory
    ├── models/
    │   ├── __init__.py      # User model
    │   └── base.py          # Declarative Base + mixins
    ├── schemas/
    │   ├── user.py          # Pydantic models for users
    │   └── auth.py          # Pydantic models for auth
    ├── api/
    │   ├── deps.py          # Dependency injection
    │   └── v1/
    │       ├── router.py    # Router aggregation
    │       ├── auth.py      # Register, login, refresh
    │       └── users.py     # User CRUD endpoints
    ├── core/
    │   ├── security.py      # JWT + password hashing
    │   └── exceptions.py    # Custom exception handlers
    └── tests/
        ├── conftest.py      # Fixtures
        └── test_auth.py     # Auth endpoint tests
```

## API Reference

All endpoints are prefixed with `/api/v1`. Full auto-generated docs are available at `/docs` (Swagger) and `/redoc` (ReDoc).

### Health

```
GET /health
```

Response:
```json
{ "status": "ok" }
```

### Authentication

#### Register

```
POST /api/v1/auth/register
```

Request body:
```json
{
  "email": "user@example.com",
  "password": "YourSecurePassword123"
}
```

Response `201`:
```json
{
  "id": "3f3e3e3e-7b7b-4b4b-8b8b-1b1b1b1b1b1b",
  "email": "user@example.com",
  "is_active": true,
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

#### Login

```
POST /api/v1/auth/login
```

Request body:
```json
{
  "email": "user@example.com",
  "password": "YourSecurePassword123"
}
```

Response `200`:
```json
{
  "access_token": "eyJhbGci...",
  "refresh_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

#### Refresh Tokens

```
POST /api/v1/auth/refresh
```

Request body:
```json
{
  "refresh_token": "eyJhbGci..."
}
```

Response `200`:
```json
{
  "access_token": "eyJhbGci...",
  "refresh_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

#### Get Current User

```
GET /api/v1/auth/me
Authorization: Bearer <access_token>
```

Response `200`:
```json
{
  "id": "3f3e3e3e-7b7b-4b4b-8b8b-1b1b1b1b1b1b",
  "email": "user@example.com",
  "is_active": true,
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

### Users

All user endpoints require authentication (`Authorization: Bearer <token>`).

#### Get Profile

```
GET /api/v1/users/me
```

#### Update Profile

```
PUT /api/v1/users/me
```

Request body (all fields optional):
```json
{
  "email": "newemail@example.com",
  "password": "NewPassword123",
  "is_active": true
}
```

#### Get User by ID

```
GET /api/v1/users/{user_id}
```

## Development

### Makefile Commands

```bash
make install       # Install production dependencies
make dev           # Install dev dependencies (includes testing/linting)
make test          # Run tests with coverage report
make lint          # Run Ruff and mypy
make format        # Auto-format code with Ruff
make migrate       # Apply Alembic migrations
make docker-up     # Start Docker Compose environment
make docker-down   # Stop Docker Compose environment
make clean         # Remove cache files and build artifacts
```

### Creating Migrations

```bash
# Auto-generate a migration after model changes
alembic revision --autogenerate -m "describe your changes"

# Apply pending migrations
alembic upgrade head

# Roll back one step
alembic downgrade -1
```

### Running Tests

```bash
# Run all tests
make test

# Run tests without coverage
pytest -v

# Run a specific test file
pytest app/tests/test_auth.py -v

# Run with live output (no capture)
pytest -v -s
```

Tests use an in-memory SQLite database via `aiosqlite`, so no external database is required to run them.

## Configuration

All configuration is managed through environment variables (see `.env.example`):

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `FastAPI Starter` | Application name (shown in OpenAPI docs) |
| `DEBUG` | `false` | Enable debug mode (SQL echo, verbose errors) |
| `DATABASE_URL` | `postgresql+asyncpg://postgres:postgres@localhost:5432/app` | Async PostgreSQL connection string |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection string |
| `SECRET_KEY` | (default warning) | JWT signing key — **change in production** |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Access token lifetime in minutes |
| `REFRESH_TOKEN_EXPIRE_DAYS` | `7` | Refresh token lifetime in days |
| `ALGORITHM` | `HS256` | JWT signing algorithm |

## Extending the Kit

This starter is intentionally minimal so you can build on top of it without fighting opinionated abstractions. Common next steps:

1. **Add models** — Create new model classes in `app/models/`, then run `alembic revision --autogenerate`
2. **Add endpoints** — Create a new router in `app/api/v1/`, register it in `router.py`
3. **Add Pydantic schemas** — Define request/response schemas in `app/schemas/`
4. **Add business logic** — Create a `app/services/` directory for service-layer functions
5. **Add background tasks** — Integrate with `fastapi.BackgroundTasks` or Celery/ARQ
6. **Add CORS middleware** — Uncomment in `app/main.py` or configure via settings

## License

This project is licensed under the MIT License. You are free to use it in personal and commercial projects.
