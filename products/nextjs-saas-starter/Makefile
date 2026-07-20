.PHONY: dev build start lint test typecheck db-up db-down db-migrate db-studio db-seed db-reset clean setup

# ─── Development ────────────────────────────────────────────────

dev:
	npm run dev

build:
	npm run build

start:
	npm run start

lint:
	npm run lint

test:
	npm run test

test:watch:
	npm run test:watch

typecheck:
	npm run typecheck

format:
	npm run format

# ─── Database ───────────────────────────────────────────────────

db-up:
	docker compose up -d postgres

db-down:
	docker compose down

db-migrate:
	npm run db:migrate

db-studio:
	npm run db:studio

db-seed:
	npm run db:seed

db-reset:
	npm run db:reset

db-generate:
	npm run db:generate

# ─── Docker ─────────────────────────────────────────────────────

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-build:
	docker compose build

# ─── Setup ──────────────────────────────────────────────────────

setup:
	cp -n .env.example .env || true
	npm install
	docker compose up -d postgres
	sleep 3
	npm run db:migrate
	npm run db:seed
	npm run dev

clean:
	rm -rf node_modules .next out
	rm -rf prisma/migrations
	docker compose down -v
