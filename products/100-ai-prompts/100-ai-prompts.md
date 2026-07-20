# 100 Developer AI Prompts

100 battle-tested prompts for daily development work. Copy, paste, ship.

## What's Inside

- **Code & Architecture** (30 prompts) — review, refactor, design, document, debug
- **Testing & QA** (15 prompts) — unit tests, integration tests, edge cases, property-based
- **Git & DevOps** (12 prompts) — commit messages, CI/CD, deployment, incident response
- **Databases & APIs** (13 prompts) — schema design, query optimization, API contracts
- **Security & Performance** (10 prompts) — vulnerability scanning, profiling, optimization
- **Career & Communication** (10 prompts) — code review comments, RFCs, postmortems
- **Learning & Onboarding** (10 prompts) — codebase onboarding, technology deep-dives

Each prompt includes: **context**, **task**, **output format**, and **example output**.

---

## Quick Start

```bash
# Pick a prompt, replace the PLACEHOLDERS, paste to your AI
```

---

## 1. Code & Architecture

### 1.1 Architecture Review
```
Context: I'm reviewing a [TYPE] system architecture.
Task: Analyze the attached architecture for:
- Single points of failure
- Scaling bottlenecks
- Coupling between modules
- Data flow inconsistencies
Output: Markdown table with Issue | Severity | Impact | Suggested Fix
```

### 1.2 Code Decomposition
```
Context: [filename] has grown to [N] lines and does too many things.
Task: Identify the 3-5 distinct responsibilities in this file.
For each, propose:
- Extract to [filename]
- Interface signature
- Dependencies
Output: Refactoring plan with file tree diagram
```

### 1.3 Dependency Decision
```
Context: Choosing between [LIB_A] and [LIB_B] for [USE_CASE].
Task: Compare on:
- API quality (0-10)
- Performance (benchmark if available)
- Bundle size / dependency weight
- Maintenance status (last release, open issues, contributor count)
- Community adoption
Output: Recommendation with trade-off table
```

### 1.4 API Design Review
```
Context: Reviewing [endpoint] in [framework].
Task: Check for:
- REST / GraphQL best practices
- Status code correctness
- Error response structure
- Pagination strategy
- Rate limiting
- Authentication/authorization
Output: Review with severity levels
```

### 1.5 Database Schema Review
```
Context: Reviewing [table/collection] schema for [USE_CASE].
Task: Analyze:
- Normalization level
- Index coverage (actual vs. query patterns)
- Data type appropriateness
- Migration impact
- Foreign key / referential integrity
Output: Schema review report
```

### 1.6 Error Handling Audit
```
Context: [filename] - audit all error handling paths.
Task: For each function/method, check:
- Are all error paths handled?
- Are errors logged with context?
- Do errors bubble up appropriately?
- Are there bare except / catch-all clauses?
Output: Error handling matrix
```

### 1.7 Configuration Design
```
Context: Designing config system for [PROJECT].
Task: Recommend:
- Config file format (YAML/TOML/env/JSON)
- Layering strategy (defaults → env → file → CLI)
- Secret management approach
- Validation approach
Output: Config architecture doc
```

### 1.8 Logging Strategy
```
Context: Setting up logging for [PROJECT].
Task: Design:
- Log levels and when to use each
- Structured vs. unstructured
- Context fields to include (request_id, user_id, etc.)
- Sampling strategy for high-volume paths
- PII redaction
Output: Logging standards document
```

### 1.9 Async Architecture
```
Context: Converting [PROJECT] from sync to async.
Task: Identify:
- I/O boundaries that benefit from async
- Shared state that needs protection
- Task/message boundaries
- Error propagation across async boundaries
Output: Migration plan with dependency graph
```

### 1.10 State Machine Design
```
Context: [FEATURE] has complex state transitions.
Task: Model as a state machine:
- List all states
- List all transitions with triggers
- Identify invalid transitions
- Error states and recovery paths
Output: State transition diagram (text/Mermaid)
```

### 1.11 Event Schema Design
```
Context: Designing event schema for [SYSTEM].
Task: Specify:
- Event name convention (past tense: OrderPlaced, PaymentFailed)
- Required metadata (id, timestamp, version, correlation_id)
- Payload schema
- Backward compatibility strategy
Output: Event schema spec
```

### 1.12 Feature Flag Strategy
```
Context: Planning feature flags for [PROJECT].
Task: Design:
- Flag types (release/experiment/ops/permission)
- Targeting rules (user %, region, plan)
- Evaluation performance
- Cleanup process for stale flags
Output: Feature flag architecture
```

### 1.13 Dependency Injection Design
```
Context: [PROJECT] needs better testability.
Task: Redesign [MODULE] with DI:
- Interfaces/abstract classes to extract
- Composition root location
- Lifetime management (transient/scoped/singleton)
- Testing strategy with mocked dependencies
Output: DI refactoring plan
```

### 1.14 Middleware Chain Design
```
Context: [FRAMEWORK] middleware/ Middleware configuration for [USE_CASE].
Task: Design the middleware stack:
- Ordering rules (auth → rate-limit → parse → route)
- Error middleware position
- Per-route middleware overrides
- Performance impact measurement
Output: Middleware architecture
```

### 1.15 Cache Strategy
```
Context: [ENDPOINT/FUNCTION] is slow (~[N]ms) and called [N] times/second.
Task: Design caching:
- Cache key structure
- TTL policy (time-based vs. event-based invalidation)
- Cache layer (in-memory / Redis / CDN)
- Write-through vs. write-behind
- Stale-while-revalidate strategy
Output: Caching design doc
```

### 1.16 Retry Logic Design
```
Context: [INTEGRATION/API] has intermittent failures (~[N]% error rate).
Task: Design retry strategy:
- Retry count and backoff (exponential with jitter)
- Which errors are retryable (5xx vs. 4xx vs. timeout)
- Circuit breaker threshold
- Fallback behavior
Output: Retry strategy document
```

### 1.17 Graceful Degradation
```
Context: [SERVICE/DEPENDENCY] goes down in production.
Task: Design graceful degradation:
- What functionality degrades vs. disappears
- Cache fallback / stale data serving
- User-visible messaging
- Recovery auto-detection
Output: Degradation plan
```

### 1.18 Data Migration Plan
```
Context: Migrating [SOURCE] to [TARGET] for [TABLE/COLLECTION].
Task: Plan:
- Migration strategy (blue-green / parallel-write / ETL)
- Validation approach (row count, checksums, sampled comparison)
- Rollback plan
- Downtime estimate
Output: Migration runbook
```

### 1.19 Code Review Request
```
Context: PR #[N] — [DESCRIPTION]
Task: Review the attached diff for:
- Logic correctness
- Error handling
- Edge cases
- Test coverage
Output: Structured review per file
```

### 1.20 Refactoring Target Identification
```
Context: [PROJECT] has [N] files and [N] KLOC.
Task: Identify the top 5 files/modules that need refactoring:
- File size / complexity metrics
- Change frequency (git churn)
- Bug density
- Test coverage
Output: Prioritized refactoring backlog
```

### 1.21 Module Boundary Audit
```
Context: [MODULE_A] and [MODULE_B] have unclear boundaries.
Task: Audit the current state:
- Imports/cross-references between modules
- Shared types/utilities
- Circular dependencies
- Suggested boundary redefinition
Output: Module boundary document
```

### 1.22 Tech Debt Assessment
```
Context: [PROJECT] has accumulated tech debt over [TIME].
Task: Assess:
- Areas of highest debt (complexity, duplication, dead code)
- Cost of keeping vs. fixing
- Risk of not fixing (velocity impact, onboarding friction, bug rate)
- Recommended 3-month payoff plan
Output: Tech debt assessment report
```

### 1.23 Protocol/Format Migration
```
Context: Migrating [OLD_PROTOCOL] to [NEW_PROTOCOL].
Task: Plan migration:
- Adapter/proxy layer design
- Dual-write strategy and duration
- Cut-over criteria
- Old protocol sunset timeline
- Backward compatibility guarantees
Output: Migration plan
```

### 1.24 RFC / Decision Document Outline
```
Context: Need to document a decision about [TOPIC].
Task: Generate an RFC outline:
- Problem statement
- Constraints
- Options considered
- Recommended approach
- Implementation plan
- Risks and mitigations
Output: RFC template filled with [TOPIC]
```

### 1.25 Dependency Upgrade Impact
```
Context: Upgrading [LIB_DEPENDENCY] from [v1] to [v2].
Task: Analyze:
- Breaking changes
- Deprecated APIs in use
- Performance differences
- Migration steps
- Test gaps to fill
Output: Upgrade impact report
```

### 1.26 Code Ownership Map
```
Context: [PROJECT] needs clear code ownership.
Task: Analyze git history to produce:
- File → primary contributor mapping
- Bus factor for each module
- Review coverage gaps
- Suggested ownership assignments
Output: Ownership map
```

### 1.27 API Versioning Strategy
```
Context: [API] needs a versioning strategy.
Task: Compare approaches:
- URL path vs. header vs. content negotiation
- Deprecation policy
- Sunset timeline
- Client migration support
Output: Versioning strategy document
```

### 1.28 Build Performance Optimization
```
Context: Build takes [N] minutes for [PROJECT].
Task: Identify:
- Slowest steps in build pipeline
- Caching opportunities
- Parallelization opportunities
- Optional/skip-able steps
Output: Build optimization plan
```

### 1.29 Code Generator Spec
```
Context: [PATTERN] is repeated [N] times across the codebase.
Task: Design a code generator:
- Input parameters
- Template structure
- Output file layout
- Integration with build process
Output: Code generator spec
```

### 1.30 Integration Test Architecture
```
Context: [PROJECT] needs integration tests for [COMPONENT].
Task: Design test architecture:
- Test environment (Docker / local / staging)
- Data seeding strategy
- Assertion patterns
- Coverage targets
- CI integration
Output: Integration test plan
```

---

## 2. Testing & QA

### 2.1 Unit Test Generator
```
Context: [FUNCTION] in [FILE].
Task: Generate unit tests covering:
- Happy path
- Edge cases (empty input, null, boundary values)
- Error conditions
- Side effect verification
Output: pytest/unittest/jest test code
```

### 2.2 Test Gap Analysis
```
Context: [MODULE] has existing tests at [FILE].
Task: Analyze coverage gaps:
- Untested functions/lines
- Missing edge case branches
- Missing error path coverage
- Test quality (assertions vs. no-assertion tests)
Output: Gap analysis report
```

### 2.3 Property-Based Testing Design
```
Context: [FUNCTION] takes [INPUT_TYPE] and returns [OUTPUT_TYPE].
Task: Design property-based tests:
- Invariant properties (idempotency, roundtrip, commutativity)
- Input generators (valid, edge, invalid)
- Shrinking strategy
Output: Property test spec (Hypothesis/QuickCheck/JSVerify)
```

### 2.4 Regression Test Selection
```
Context: PR #[N] changes [FILES].
Task: Recommend which existing tests to run:
- Directly affected tests (test the changed code)
- Integration tests (test code that uses the changed code)
- End-to-end smoke tests
- Rationale for each selection
Output: Test selection list
```

### 2.5 Mock/Stub Design
```
Context: [EXTERNAL_SERVICE] integration needs testing.
Task: Design mock layer:
- Interface to mock
- Response scenarios (success, error, timeout, empty)
- State verification (was the mock called correctly?)
- Recording/replay capability
Output: Mock design doc
```

### 2.6 Performance Test Plan
```
Context: [ENDPOINT/FEATURE] needs performance validation.
Task: Design performance tests:
- Load profile (concurrent users, ramp-up, duration)
- Success criteria (p95 latency, error rate, throughput)
- Environment requirements (isolated, comparable to prod)
- Monitoring/metrics to capture
Output: Performance test plan
```

### 2.7 Snapshot/Approval Test Plan
```
Context: [COMPONENT] produces output that should not change unexpectedly.
Task: Design snapshot tests:
- What to snapshot (output, rendered component, API response)
- Update trigger (intentional change vs. drift)
- Diff review process
- CI integration
Output: Snapshot test plan
```

### 2.8 Chaos Engineering Scenario
```
Context: [SERVICE] resilience validation.
Task: Design chaos experiments:
- Faults to inject (latency, crash, resource exhaustion, network partition)
- Steady-state hypothesis (what "healthy" looks like)
- Blast radius control
- Rollback procedure
Output: Chaos experiment spec
```

### 2.9 Test Data Factory Pattern
```
Context: [PROJECT] needs consistent test data across test suites.
Task: Design a test data factory:
- Default valid data for each entity
- Override/partial pattern (only specify what's different)
- Related entity creation (cascading)
- Unique constraint handling
Output: Factory pattern spec with examples
```

### 2.10 Contract Test Design
```
Context: [PROVIDER/CONSUMER] interface needs contract testing.
Task: Design contract tests:
- Provider contract (what the provider guarantees)
- Consumer contract (what the consumer expects)
- Verification frequency (CI / scheduled)
- Breaking change detection
Output: Contract test plan (Pact/Pactum style)
```

### 2.11 Mutation Testing Plan
```
Context: [MODULE] test suite quality assessment.
Task: Design mutation testing approach:
- Mutator types (negate conditions, remove calls, swap returns)
- Code to target (high-risk, complex, frequently changed)
- Quality gate (mutation score threshold)
- CI integration
Output: Mutation testing plan
```

### 2.12 Accessibility Test Plan
```
Context: [UI/COMPONENT] needs accessibility validation.
Task: Design a11y testing:
- Automated checks (axe, Lighthouse)
- Manual check scenarios (keyboard navigation, screen reader)
- WCAG level targeting (A/AA/AAA)
- CI gate
Output: A11y test plan
```

### 2.13 End-to-End Test Scenario
```
Context: [USER_STORY] end-to-end validation.
Task: Write E2E test scenario:
- User flow steps
- Data prerequisites
- Assertions at each step
- Teardown/cleanup
Output: E2E test script (Playwright/Cypress/Selenium)
```

### 2.14 Fuzz Testing Target
```
Context: [FUNCTION/API] handles external/untrusted input.
Task: Design fuzz testing:
- Input format structure
- Mutation strategies
- Crash/oracle detection
- Corpus minimization
Output: Fuzz testing spec
```

### 2.15 Flaky Test Detection
```
Context: Test suite has flaky tests.
Task: Analyze test history to identify flaky tests:
- Failure rate over time
- Common failure patterns (timing, ordering, data pollution)
- Suggested fixes
Output: Flaky test report with fix recommendations
```

---

## 3. Git & DevOps

### 3.1 Commit Message Generation
```
Context: [DIFF / CHANGES]
Task: Generate a Conventional Commit message:
type(scope): short description

- Bullet points for each logical change
- Closes/Fixes/Refs references
Output: Commit message
```

### 3.2 PR Description
```
Context: PR #[N] — [BRANCH_NAME]
Task: Generate a PR description:
- What this PR does
- Why this approach
- Testing done
- Deployment notes
- Screenshots (if UI)
Output: PR description template
```

### 3.3 CI Pipeline Design
```
Context: [PROJECT] needs CI for [LANGUAGE/STACK].
Task: Design pipeline stages:
- Lint → Type Check → Unit Test → Build → Integration Test → Deploy
- Caching strategy
- Parallel vs. sequential stages
- Failure gates
Output: CI config outline
```

### 3.4 CD Pipeline Design
```
Context: [PROJECT] deploys to [TARGET] (Kubernetes/serverless/VPS).
Task: Design deployment pipeline:
- Build and tag
- Registry push
- Environment promotion (dev → staging → prod)
- Rollback strategy
- Health check gates
- Feature flag integration
Output: CD pipeline spec
```

### 3.5 Incident Response Checklist
```
Context: [SERVICE] is down/degraded.
Task: Generate incident response steps:
1. Confirm the incident (monitoring alert, user report)
2. Assess severity and impact (P0/P1/P2)
3. Communication: status page, stakeholders
4. Mitigation: rollback, feature flag, scale up, traffic reroute
5. Root cause investigation
6. Fix and deploy
7. Postmortem
Output: Incident response checklist
```

### 3.6 Postmortem Template
```
Context: [INCIDENT_ID] — [BRIEF DESCRIPTION]
Task: Generate postmortem:
- Summary (what happened, impact, duration)
- Timeline
- Root cause
- What went well
- What went wrong
- Action items (mitigation, prevention, tracking)
Output: Postmortem document
```

### 3.7 Dockerfile Review
```
Context: [Dockerfile]
Task: Review for:
- Layer caching optimization
- Security (non-root user, pinned versions, no secrets)
- Size optimization (multi-stage, .dockerignore)
- Build performance
Output: Dockerfile review
```

### 3.8 Docker Compose Design
```
Context: [PROJECT] needs local development environment.
Task: Design docker-compose.yml:
- Services needed (app, db, cache, queue, etc.)
- Volume mounts (hot reload, persistent data)
- Network configuration
- Health checks
- Resource limits
Output: Docker Compose config
```

### 3.9 GitHub Actions Workflow
```
Context: [PROJECT] needs GitHub Actions for [TASK].
Task: Generate a workflow:
- Trigger (push, PR, scheduled, manual)
- Matrix strategy (OS, version, etc.)
- Step dependencies
- Artifact handling
- Secrets management
Output: GitHub Actions YAML
```

### 3.10 Terraform/Infra Review
```
Context: [INFRA_FILE] (Terraform/Pulumi/CloudFormation).
Task: Review for:
- Security (public exposure, encryption, IAM)
- Cost (over-provisioned resources)
- State management (remote state, locking)
- Naming conventions
- Tagging
Output: Infrastructure review
```

### 3.11 Monitoring Dashboard Design
```
Context: [SERVICE] needs a monitoring dashboard.
Task: Design dashboard panels:
- RED metrics (Rate, Errors, Duration)
- USE metrics (Utilization, Saturation, Errors) for infrastructure
- Business metrics (users impacted, orders, etc.)
- Logs / events correlation
Output: Dashboard layout specification
```

### 3.12 On-Call Runbook
```
Context: [SERVICE] — common failure scenarios.
Task: Write runbook entries for:
1. High error rate
2. High latency
3. Service down
4. Certificate expiry
5. Disk full
6. Memory leak
Each entry: symptoms → diagnosis → fix → verify
Output: On-call runbook
```

---

## 4. Databases & APIs

### 4.1 SQL Query Optimization
```
Context: [SLOW_QUERY] takes [N]ms.
Task: Analyze and optimize:
- Execution plan review
- Index suggestions
- Query restructuring
- Hint usage
Output: Optimized query + explanation
```

### 4.2 Index Strategy
```
Context: [TABLE] has [N] rows and frequent queries on [COLUMNS].
Task: Design indexing strategy:
- Clustered/primary index
- Secondary indexes for query patterns
- Covering indexes
- Partial indexes
- Maintenance (rebuild, fragmentation)
Output: Index design
```

### 4.3 NoSQL Schema Design
```
Context: [USE_CASE] in [MongoDB/DynamoDB/Firestore].
Task: Design schema:
- Access patterns first (not data modeling first)
- Document structure
- Secondary indexes / GSI
- Denormalization decisions
- TTL / expiry strategy
Output: Schema design document
```

### 4.4 API Pagination Strategy
```
Context: [ENDPOINT] returns large datasets.
Task: Design pagination:
- Cursor-based vs. offset-based
- Default page size
- Max page size enforcement
- Cursor encoding (opaque vs. transparent)
- Total count approach (count estimate vs. exact)
Output: Pagination spec
```

### 4.5 GraphQL Schema Design
```
Context: [USE_CASE] needs a GraphQL API.
Task: Design schema:
- Types and relationships
- Queries and mutations
- N+1 prevention (DataLoader)
- Subscription design (if real-time needed)
Output: GraphQL schema skeleton
```

### 4.6 API Error Response Design
```
Context: [API] needs consistent error responses.
Task: Design error response format:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable description",
    "details": [{"field": "email", "issue": "invalid format"}],
    "request_id": "req_abc123",
    "docs_url": "https://docs.example.com/errors/VALIDATION_ERROR"
  }
}
Output: Error response specification
```

### 4.7 Rate Limiting Design
```
Context: [API] needs protection from abuse.
Task: Design rate limiting:
- Algorithm (token bucket / sliding window / fixed window)
- Per-endpoint vs. global limits
- Response headers (X-RateLimit-*)
- Over-limit response (429 with Retry-After)
- Distributed implementation (Redis)
Output: Rate limiting spec
```

### 4.8 Webhook Design
```
Context: [SYSTEM] needs to send webhook events.
Task: Design webhook system:
- Event catalog
- Payload schema per event
- Retry policy (exponential backoff, max attempts)
- Signature verification
- Idempotency keys
- Dead letter queue
- Webhook UI for subscribers
Output: Webhook system design
```

### 4.9 Message Queue Design
```
Context: [ASYNC_TASK] needs a message queue.
Task: Design queue architecture:
- Queue/topic structure
- Message schema
- Ordering requirements (single vs. multi-partition)
- Dead letter / retry strategy
- Consumer scaling
- Monitoring visibility
Output: Message queue architecture
```

### 4.10 Database Connection Pool Config
```
Context: [APP] connects to [DB] with [N] instances.
Task: Recommend pool configuration:
- Min/max connections
- Connection lifetime
- Queue strategy (fair vs. LIFO)
- Pool starvation detection
- Connection health checks
Output: Pool configuration
```

### 4.11 API Migration (Breaking Change)
```
Context: [API_V1] → [API_V2] breaking change.
Task: Plan migration:
- Dual-support period
- Sunset header (Sunset: Sat, 31 Dec 2026 23:59:59 GMT)
- Deprecation header
- Client notification strategy
- Migration guide generation
Output: API migration plan
```

### 4.12 Search Feature Design
```
Context: [ENTITY] needs search functionality.
Task: Design search (Elasticsearch/Meilisearch/SQL FTS):
- Index mapping / schema
- Searchable and filterable fields
- Ranking/boosting strategy
- Typo tolerance
- Faceted search
- Autocomplete/suggestions
Output: Search feature design
```

### 4.13 Data Seeding Strategy
```
Context: [ENVIRONMENT] (dev/staging/demo) needs realistic data.
Task: Design seeding strategy:
- Data generation approach (factory, anonymized production dump, synthetic)
- Referential integrity across seed data
- Environment-specific seed variants
- Seed refresh cadence
Output: Seeding strategy document
```

---

## 5. Security & Performance

### 5.1 Security Vulnerability Assessment
```
Context: [FILE/MODULE] — security review.
Task: Scan for OWASP Top 10:
- Injection
- Broken Authentication
- Sensitive Data Exposure
- XML External Entities
- Broken Access Control
- Security Misconfiguration
- Cross-Site Scripting
- Insecure Deserialization
- Using Components with Known Vulnerabilities
- Insufficient Logging & Monitoring
Output: Findings table with severity
```

### 5.2 Secure Config Checklist
```
Context: [PROJECT/TYPE] — security hardening.
Task: Generate security checklist:
- HTTPS enforcement
- CORS configuration
- Content Security Policy
- Rate limiting
- Auth token storage
- Secret rotation
- Audit logging
Output: Security checklist
```

### 5.3 Performance Profiling Plan
```
Context: [FUNCTION/ENDPOINT] is slow.
Task: Design profiling approach:
- Profiling tool selection (cProfile, py-spy, perf, Chrome DevTools)
- Metrics to capture (wall time, CPU, memory, I/O)
- Baseline measurement
- Comparison benchmark
Output: Profiling plan
```

### 5.4 Memory Leak Investigation
```
Context: [PROCESS] memory grows over time.
Task: Debug memory leak:
1. Heap diff between startup and after [N] operations
2. Identify growing objects
3. Trace retention paths
4. Check for: unclosed resources, event listeners, caches, global state
Output: Leak analysis report
```

### 5.5 Concurrent Code Review
```
Context: [FILE] uses threads/goroutines/async.
Task: Review for concurrency issues:
- Race conditions
- Deadlocks
- Starvation
- Atomicity violations
- Lock granularity
Output: Concurrency review
```

### 5.6 Authentication Audit
```
Context: [AUTH_SYSTEM] review.
Task: Audit:
- Password policy (complexity, hashing algorithm, storage)
- Session management (token lifetime, rotation, revocation)
- MFA support
- OAuth/SAML configuration
- Brute force protection
Output: Authentication audit report
```

### 5.7 Authorization Model Design
```
Context: [APP] needs role-based access.
Task: Design authorization:
- Roles and permissions matrix
- Resource-level vs. action-level permissions
- Hierarchical vs. flat roles
- Attribute-based overrides
- Audit trail
Output: Authorization model
```

### 5.8 Secrets Management
```
Context: [PROJECT] needs secrets management.
Task: Design approach:
- Secret storage (vault / env / secret manager)
- Rotation policy
- Access audit
- Emergency access / break-glass procedure
- Local development secrets
Output: Secrets management plan
```

### 5.9 CORS/Security Headers Config
```
Context: [WEB_APP] needs security headers.
Task: Generate security header configuration:
- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy
Output: Security headers config
```

### 5.10 API Fuzzing Targets
```
Context: [API] needs fuzz testing.
Task: Identify fuzzing targets:
- Input fields accepting free text
- File upload endpoints
- JSON/XML parsers
- URL/redirect parameters
- Numeric/boundary parameters
Output: Fuzzing target list
```

---

## 6. Career & Communication

### 6.1 Code Review Comment (Constructive)
```
Context: PR #[N] — reviewer sees [ISSUE].
Task: Write a constructive review comment:
{positive framing}
{Specific issue with line reference}
{Why it matters}
{Suggestion, not demand}
Output: Review comment
```

### 6.2 Technical RFC
```
Context: Proposing [CHANGE] to [PROJECT].
Task: Generate RFC:
- Summary
- Motivation
- Design
- Alternatives considered
- Open questions
- Implementation plan
Output: RFC document
```

### 6.3 Standup Update
```
Context: Yesterday/Today/Blockers.
Task: Generate standup update:
- Yesterday: [completed tasks]
- Today: [planned tasks]
- Blockers: [what's blocking, who can unblock]
Output: Standup update (30 words max)
```

### 6.4 Project Status Report
```
Context: [PROJECT] status for [AUDIENCE].
Task: Generate status report:
- Progress against target
- Key accomplishments
- Risks and issues
- Next milestones
Output: Status report
```

### 6.5 Technical Onboarding Doc
```
Context: New developer joining [PROJECT].
Task: Generate onboarding guide:
- Dev environment setup
- Key architecture concepts
- First PR step-by-step
- Who to ask for what
- Common pitfalls
Output: Onboarding document
```

### 6.6 Escalation Email
```
Context: [ISSUE] is blocking [DEADLINE].
Task: Draft escalation:
- What's blocked
- Impact
- What's needed
- Deadline
Output: Escalation email
```

### 6.7 Retrospective Notes
```
Context: [SPRINT/PERIOD] retrospective.
Task: Generate retrospective template:
- What went well
- What went wrong
- What to improve
- Action items (owner, deadline)
Output: Retro notes
```

### 6.8 Technical Interview Question
```
Context: Interviewing for [ROLE/SENIORITY].
Task: Design a technical question:
- Problem statement
- Expected approach
- Follow-up questions
- Evaluation criteria
Output: Interview question
```

### 6.9 Performance Review Self-Assessment
```
Context: [PERIOD] performance review.
Task: Draft self-assessment:
- Key accomplishments
- Areas of growth
- Challenges and learnings
- Goals for next period
Output: Self-assessment
```

### 6.10 Architecture Decision Log Entry
```
Context: Decision made: [DECISION].
Task: Write ADR entry:
- Title: [DECISION]
- Status: [Proposed/Accepted/Deprecated/Superseded]
- Context: Why this decision was needed
- Decision: What was decided
- Consequences: What this means going forward
- Alternatives: What else was considered
Output: ADR entry
```

---

## 7. Learning & Onboarding

### 7.1 Codebase Onboarding
```
Context: [REPO_URL] — understand the codebase.
Task: Generate onboarding summary:
- Project purpose and architecture
- Tech stack and key libraries
- Module/directory structure
- Data flow diagram (text)
- Configuration and environment setup
- Test and build commands
- Deployment process
Output: Codebase summary
```

### 7.2 Technology Deep-Dive
```
Context: I want to learn [TECHNOLOGY] deeply.
Task: Create a learning plan:
- Prerequisites
- Core concepts (list of 5-10)
- Hands-on exercises for each concept
- Recommended projects
- Pitfalls to avoid
- Resources (docs, books, courses)
Output: Learning plan
```

### 7.3 Debugging Walkthrough
```
Context: [BUG] in [COMPONENT].
Task: Debug step by step:
1. Reproduction steps
2. Instrumentation points (logs, metrics, traces)
3. Hypothesis generation (list 3-5 possible causes)
4. Elimination approach (which to test first, why)
5. Root cause identification
6. Fix and verification
Output: Debugging walkthrough
```

### 7.4 Technology Comparison
```
Context: Comparing [TECH_A] vs. [TECH_B] for [USE_CASE].
Task: Generate comparison:
- Philosophy difference
- Learning curve
- Performance characteristics
- Ecosystem and community
- Production maturity
- Recommendation
Output: Comparison table
```

### 7.5 API Client Code Generation
```
Context: [API_SPEC] (OpenAPI/gRPC/REST).
Task: Generate client code examples:
- Authentication setup
- Common operations (CRUD)
- Error handling
- Pagination usage
Output: Code examples in [LANGUAGE]
```

### 7.6 System Design Explanation
```
Context: Explain [SYSTEM] (e.g., "how does Docker work?").
Task: Generate explanation:
- High-level architecture
- Core concepts
- Key components and their roles
- Flow of a typical operation
- Analogy for non-technical audience
Output: System explanation
```

### 7.7 Career Path Exploration
```
Context: [ROLE] → [TARGET_ROLE] transition.
Task: Generate guidance:
- Skills gap analysis
- Learning path (projects, courses, certifications)
- Portfolio recommendations
- Community involvement
- Timeline expectations
Output: Career transition plan
```

### 7.8 Conference Talk Outline
```
Context: [TOPIC] presentation.
Task: Generate talk outline:
- Title and abstract (2-3 sentences)
- Problem statement
- Key takeaways
- Talk structure (5-7 sections)
- Demo plan
- Q&A preparation
Output: Talk outline
```

### 7.9 Knowledge Base Entry
```
Context: [TOPIC] — write a knowledge base article.
Task: Generate KB entry:
- Overview
- Step-by-step instructions
- Common issues and solutions
- Related topics
Output: KB article
```

### 7.10 Mentorship Guide
```
Context: Mentoring [JUNIOR_DEV] on [TOPIC].
Task: Generate mentorship plan:
- Current skill level assessment
- Learning objectives (30/60/90 day)
- Weekly check-in topics
- Practice exercises
- Success criteria
Output: Mentorship plan
```

---

## License & Usage

This product is licensed for **personal and commercial use**.
You may use these prompts in any project, including client work.
You may **not** resell or redistribute this collection as-is.

© 2026 AICraft. All rights reserved.
