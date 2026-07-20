# API Development Prompts Pack

35 prompts for designing, building, testing, and documenting REST APIs with AI assistance. Works with any framework — FastAPI, Express, Django, Gin, Spring Boot.

## What's Inside

### 1. API Design (8 prompts)
- `contract-first-design` — Design API endpoints from the OpenAPI spec first, then implement
- `resource-modeling` — Model RESTful resources, relationships, and nesting
- `pagination-strategy` — Choose cursor vs offset pagination based on data characteristics
- `error-response-format` — Design consistent error responses with codes, messages, and details
- `versioning-strategy` — URL vs header vs query parameter versioning — tradeoffs
- `rate-limiting-schema` — Design rate limit headers and response formats (429 handling)
- `webhook-pattern` — Design webhook payloads, retry logic, and event filtering
- `graphql-vs-rest` — Decision framework for when to use GraphQL vs REST for each endpoint

### 2. Implementation (10 prompts)
- `crud-generator` — Generate complete CRUD endpoints for any resource
- `auth-middleware` — Implement JWT/OAuth2 authentication middleware with role checks
- `input-validation` — Set up request validation with detailed error messages
- `query-parameter-filtering` — Implement filtering, sorting, and field selection via query params
- `bulk-operations` — Design batch create/update/delete endpoints
- `file-upload-handler` — Implement file upload with validation, size limits, and cloud storage
- `soft-delete-pattern` — Implement soft delete with query filtering and restoration
- `audit-logging` — Log all API mutations with before/after values and actor info
- `idempotency-keys` — Implement idempotency for POST/PUT endpoints to prevent duplicates
- `cors-configuration` — Set up CORS for development, staging, and production

### 3. Testing (6 prompts)
- `endpoint-test-suite` — Generate comprehensive pytest/httpx tests for all endpoints
- `contract-testing` — Verify API responses match the OpenAPI spec
- `load-test-scenario` — Design k6/locust load tests for critical endpoints
- `security-test-case` — Test for common API vulnerabilities (injection, auth bypass, rate limit)
- `mocking-strategy` — Mock external services in API integration tests
- `fixture-generation` — Generate realistic test data for API tests

### 4. Documentation (4 prompts)
- `openapi-docs-generation` — Write comprehensive OpenAPI descriptions and examples
- `readme-api-quickstart` — Write a quickstart guide for your API
- `postman-collection` — Generate a Postman/Insomnia collection from your routes
- `changelog-automation` — Track API changes across versions

### 5. Production Operations (7 prompts)
- `error-monitoring-setup` — Set up Sentry/similar for API error tracking
- `api-gateway-config` — Configure API gateway (Kong, AWS, nginx) for routing and throttling
- `graceful-shutdown` — Implement graceful shutdown for your API server
- `health-check-endpoint` — Design comprehensive health check and readiness probes
- `metrics-endpoint` — Expose Prometheus metrics for request rate, latency, errors
- `database-connection-pooling` — Configure connection pooling for production throughput
- `api-deprecation-flow` — Deprecate API endpoints with sunset headers and migration guides

---

## Quick Start

Each prompt includes: **context**, **task**, **output format**, and **example output**.

```markdown
## contract-first-design

**Context**: Your team starts coding endpoints without an API contract. Responses are inconsistent, frontend and backend disagree on formats.

**Task**: Design a contract-first workflow:
1. Write OpenAPI 3.1 spec before any implementation code
2. Generate type-safe client code from the spec
3. Validate all responses against the spec in tests

**Output Format**:
- OpenAPI snippet with one example resource
- Step-by-step workflow for your team
- Validation middleware code for response enforcement
```

---

## Why This Pack?

- **Framework agnostic** — Prompts work with FastAPI, Express, Django, Gin, Spring Boot
- **Production focus** — Real patterns from shipped APIs handling millions of requests
- **Complete lifecycle** — Design → Build → Test → Document → Operate
- **Structured output** — Every prompt has context, task, format, and examples
