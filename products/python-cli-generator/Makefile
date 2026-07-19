.PHONY: install dev test lint format clean build

install:
	poetry install

dev:
	poetry install --with dev

test:
	poetry run pytest --cov=src --cov-report=term --cov-report=html

lint:
	poetry run ruff check src/
	poetry run mypy src/

format:
	poetry run ruff format src/

clean:
	rm -rf dist/ build/ *.egg-info .coverage htmlcov .mypy_cache .pytest_cache

build:
	poetry build
