# AI Code Review Prompt Pack

20 battle-tested prompts for security, correctness, and quality reviews with Claude, GPT, Gemini, or any capable model. Pair with `aicraft-code-review` for automated scanning plus deep LLM analysis.

## How to use

1. Attach the diff or file you want reviewed.
2. Paste the prompt (replace `{{...}}` placeholders).
3. Feed the model's findings to your issue tracker or PR comments.

---

## Security (1–7)

1. **OWASP sweep** — "Act as a security engineer. Review this diff for the OWASP Top 10: injection, broken auth, sensitive data exposure, XXE, broken access control, misconfiguration, XSS, unsafe deserialization, vulnerable components, insufficient logging. For each finding give: file, line, severity (critical/high/medium/low), one-sentence impact, and a concrete fix. Do not mention style issues."

2. **Injection audit** — "Find every place where user input reaches {{SQL/command/shell/template}} execution. Trace the data flow and mark which paths are exploitable vs. already sanitized. Suggest the smallest fix for each exploitable path."

3. **Secret hunt** — "Scan this code for hardcoded credentials, API keys, tokens, private keys, and passwords. Also flag places where secrets are logged, printed, or embedded in error messages. Output a checklist I can paste into my secrets manager migration."

4. **AuthZ/AuthN review** — "Review the authentication and authorization logic in this diff. Look for: missing ownership checks (IDOR), privilege escalation, token handling mistakes, timing attacks, and insecure session management. Rate each finding by exploitability."

5. **Crypto misuse** — "Audit all uses of cryptography in this code: hash functions, encryption modes, IV/nonce handling, randomness sources, and key management. Flag any use of MD5/SHA1, predictable RNGs, ECB mode, or hardcoded keys."

6. **Supply chain & deps** — "Review this dependency update for security risk: what changes, what breaks, and whether the new versions have known CVEs or license changes. Recommend pinning or alternatives."

7. **Input validation map** — "List every external input in this code (HTTP params, files, env, events) and describe: (a) what could go wrong, (b) the current validation, (c) the missing validation. Output as a table."

## Correctness & reliability (8–14)

8. **Race condition hunt** — "Find race conditions and concurrency bugs: unsynchronized shared state, check-then-act patterns, TOCTOU on files, and non-atomic updates. For each, explain the interleaving that breaks it and propose a fix."

9. **Error handling audit** — "Review all error handling in this diff. Flag: swallowed exceptions, empty catch blocks, missing timeouts on network calls, retries without backoff, and panics in library code. Suggest how each failure should propagate."

10. **Edge case fuzz** — "Generate 15 adversarial inputs for the function {{function_name}}: empty, null, zero, negative, max-size, unicode, malformed, duplicate, and out-of-order values. For each, predict the current behavior and whether it fails."

11. **Resource lifecycle** — "Check this code for resource leaks: unclosed files, connections, streams, goroutines/threads, or caches without eviction. Also flag unbounded lists/queues that can grow without limit."

12. **Transaction & consistency** — "Review the write path in this diff. Where could a partial failure leave inconsistent state (DB rows, files, external calls)? Propose idempotency keys, transactions, or compensating actions."

13. **Migration safety** — "Review this schema/migration change for safety: does it work on large tables, is it reversible, does it lock, and what happens if the app is rolled back? Suggest a zero-downtime rollout order."

14. **Null / optional handling** — "Trace every nullable/optional value in this diff. Where can a null slip through and crash or corrupt logic? Suggest defensive checks or type-level fixes."

## Performance (15–17)

15. **N+1 & query plan** — "Look for N+1 query patterns, missing indexes, unbounded result sets, and queries built in loops in this diff. For each, show the data volume at which it becomes a problem and the fix."

16. **Hot path analysis** — "Assume {{function_name}} runs on the hot path. Find unnecessary allocations, copies, serialization, or repeated work. Show the before/after with measured complexity."

17. **Client-side payload** — "Review what this code ships to the browser/bundle: payload size, unused imports, and heavy libraries. Suggest tree-shaking, lazy loading, or lighter alternatives."

## Quality & maintainability (18–20)

18. **Naming & intent** — "Find names in this diff that mislead, duplicate, or hide intent (single letters, abbreviations, negations). Suggest renames that make the code read like a spec."

19. **Test gap analysis** — "Given this diff, list the 10 highest-value tests that are missing: the ones most likely to catch a regression. For each, write the test name and the scenario in one line."

20. **Review summary** — "Summarize this diff in 5 bullets: what changed, why, risk level, what to test manually, and the single most important thing to fix before merge. Then list every concrete issue found, ordered by severity."

---

## Pairing with automated rules

Run `mcp-code-review` first for deterministic findings (security patterns, style, config), then use prompts 1–20 for the semantic layer. The automated scan catches what the model skims; the model catches what regex can't.
