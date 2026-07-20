.PHONY: install dev test lint format migrate docker-up docker-down docker-build clean

# Install production dependencies
install:
	pip install -e .

# Install with dev dependencies
dev:
	pip install -e ".[dev]"

# Run tests with coverage
test:
	pytest --cov=app --cov-report=term --cov-report=html -v

# Lint with Ruff
lint:
	ruff check app/
	mypy app/

# Format with Ruff
format:
	ruff format app/

# Run Alembic migrations
migrate:
	alembic upgrade head

# Create a new Alembic migration
migrate-create:
	@read -p "Migration message: " msg; alembic revision --autogenerate -m "$$msg"

# Start Docker services (app + postgres + redis)
docker-up:
	docker compose up --build -d

# Stop Docker services
docker-down:
	docker compose down

# Rebuild Docker images
docker-build:
	docker compose build

# Clean cache and artifacts
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	rm -rf __pycache__ */**/__pycache__
	rm -rf *.egg-info dist build
