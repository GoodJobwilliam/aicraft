.PHONY: install dev test lint format clean

install:
	pip install -r requirements.txt

dev:
	pip install -e ".[dev]"

test:
	python -m pytest --cov=src --cov-report=term --cov-report=html

lint:
	python -m ruff check src/
	python -m mypy src/

format:
	python -m ruff format src/

clean:
	rm -rf dist/ build/ *.egg-info .coverage htmlcov .mypy_cache .pytest_cache
