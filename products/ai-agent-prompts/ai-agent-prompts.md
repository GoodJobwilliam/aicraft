# AI Agent Prompts Pack

50 battle-tested prompts for building, debugging, and shipping AI agents. Designed for indie developers working with Claude Code, Cursor, OpenAI Agents SDK, LangChain, LangGraph, n8n, and custom agent frameworks.

## What's Inside

### 1. Agent Architecture (12 prompts)
Design decisions for agent systems that don't fall over.

- `agent-scope-boundary` — Define exactly what your agent should and should not do. Prevent scope creep and hallucination.
- `tool-selection-strategy` — Choose between function calling, MCP tools, and custom APIs for each agent capability.
- `memory-architecture` — Design short-term (context window) vs long-term (vector store/RAG) memory for your agent.
- `routing-topology` — Single agent vs supervisor + workers vs swarm — pick the right pattern for your use case.
- `state-management` — Manage agent state across multi-turn conversations without leaking context.
- `error-recovery-flow` — Design retry logic, fallback paths, and human escalation for agent failures.
- `cost-budget-design` — Set token budgets and cost limits per agent run. Prevent runaway API costs.
- `observability-setup` — Log agent decisions, tool calls, and token usage for debugging and optimization.
- `parallel-execution` — Run multiple agent branches concurrently and merge results.
- `human-in-the-loop` — Design handoff points where the agent pauses and asks for human approval.
- `versioning-strategy` — Version your agent prompts and tool definitions for safe iteration.
- `deployment-pattern` — Design for local dev vs staging vs production agent deployments.

### 2. Prompt Engineering for Agents (10 prompts)
Craft prompts that make agents actually follow instructions.

- `system-prompt-template` — Structure for a production system prompt: role, rules, tools, output format, constraints.
- `tool-description-optimization` — Write tool descriptions that LLMs actually understand and use correctly.
- `few-shot-examples` — Embed examples in prompts that teach the agent when and how to use each tool.
- `constraint-enforcement` — Phrase rules so agents follow them. "Must" vs "should" vs "consider" — word choice matters.
- `output-formatting` — Force structured JSON/Markdown output with reliable schema adherence.
- `chain-of-thought-prompting` — Prompt agents to reason step-by-step before taking action.
- `context-window-management` — Fit maximum useful context without hitting token limits. Summarization strategies.
- `dynamic-prompt-injection` — Inject real-time data (time, user info, API results) into prompts safely.
- `anti-hallucination-guard` — Prompts that reduce made-up tool calls and invented data.
- `multi-language-agent` — Design prompts for agents that work across English, Chinese, and other languages.

### 3. Tool Building (8 prompts)
Create tools your agent can actually use reliably.

- `mcp-server-scaffold` — Build a Model Context Protocol server from scratch in Python.
- `api-tool-wrapper` — Wrap any REST API as an agent-callable tool with error handling.
- `database-query-tool` — Build a safe read-only SQL query tool for your agent with guardrails.
- `file-operations-tool` — Create read/write/search file tools with path validation and safety checks.
- `web-search-tool` — Integrate web search as an agent tool with result summarization.
- `code-execution-sandbox` — Build a safe code execution tool for agents (sandboxed, time-limited).
- `email-send-tool` — Create an email tool with template support and send confirmation.
- `custom-knowledge-base` — Build a RAG tool that queries your documentation or codebase.

### 4. Debugging & Testing (8 prompts)
Find and fix agent behavior issues before they reach production.

- `agent-trace-analysis` — Analyze a full agent trace to find where it went wrong.
- `tool-call-inspection` — Verify tool calls match the intended parameters and return values.
- `prompt-regression-test` — Compare agent responses before and after a prompt change.
- `edge-case-discovery` — Generate edge case inputs that might break your agent.
- `cost-optimization-audit` — Analyze token usage and find unnecessary tool calls or context bloat.
- `latency-bottleneck` — Identify which tool calls or LLM round-trips are slowing your agent.
- `security-scan` — Check for prompt injection, tool abuse, and data leakage in your agent.
- `consistency-test` — Run the same request multiple times and measure response variation.

### 5. Agent Workflows (6 prompts)
Build multi-step agent workflows that actually complete tasks.

- `research-agent-flow` — Research a topic: search → read → synthesize → cite → report.
- `code-generation-flow` — Generate code: spec → plan → implement → test → review → fix.
- `data-pipeline-flow` — Process data: fetch → validate → transform → analyze → visualize → summarize.
- `customer-support-flow` — Handle support: classify → search knowledge base → draft response → human review.
- `content-creation-flow` — Create content: research → outline → draft → edit → format → publish.
- `monitoring-agent-flow` — Monitor systems: check health → detect anomaly → diagnose → alert → report.

### 6. Production Operations (6 prompts)
Run agents reliably in production.

- `rate-limit-handling` — Design agent behavior under API rate limits with queuing and backoff.
- `error-monitoring-setup` — Set up alerts for agent failures, slow responses, and cost spikes.
- `a-b-testing-framework` — Compare two agent versions on the same task with metrics.
- `gradual-rollout` — Deploy agent changes to 1% → 10% → 50% → 100% of traffic safely.
- `feedback-loop` — Collect user feedback on agent outputs and use it to improve prompts.
- `incident-response` — What to do when your agent goes rogue in production.

---

## Quick Start

Each prompt includes: **context**, **task**, **output format**, and **example output**.

```markdown
## agent-scope-boundary

**Context**: Your agent is drifting outside its intended purpose — answering questions it shouldn't, calling tools it doesn't need.

**Task**: Design a scope boundary system with three layers:
1. Allowed actions (explicit whitelist)
2. Disallowed actions (explicit blacklist)  
3. Grey zone handling (ask human)

**Output Format**:
- SYSTEM_PROMPT section to add
- Example of agent respecting the boundary
- Example of agent hitting the boundary and how it responds
```

Use this with any AI coding assistant. Copy the relevant prompt, paste it in your conversation, and follow the output format.

---

## Why This Pack?

Most prompt packs are generic "ChatGPT prompts" that anyone could write. This pack is different:

- **Built for builders** — Every prompt solves a real problem indie developers hit when building AI agents
- **Production focus** — Not theory. These come from shipping agent systems to production.
- **Framework agnostic** — Works with Claude Code, Cursor, OpenAI, LangChain, n8n, or custom stacks
- **Structured output** — Each prompt has context, task, format, and examples — not vague instructions

### Pricing

$29 — one-time purchase. PDF download. No subscriptions, no DRM.
