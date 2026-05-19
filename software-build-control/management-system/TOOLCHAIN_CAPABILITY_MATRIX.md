# TOOLCHAIN_CAPABILITY_MATRIX

## Purpose

This matrix defines the current approved toolchain capability state for the VIF app-build-line.

The matrix prevents the factory from assuming tool capability that has not been verified.

## Core rule

Capability varies by:

- provider,
- plan/tier,
- runtime,
- integration method,
- permissions,
- environment,
- workspace state.

The factory must not assume all AI tools have equal capability.

## Current matrix

| Provider | Tool/platform | Current operating context | Approved role | Key limitations/risks | Required readiness evidence | Fallback route |
|---|---|---|---|---|---|---|
| OpenAI | ChatGPT | Plus-level interactive environment | planning, audit, governance, review | no guaranteed persistent repo execution context | connected GitHub access where required | GitHub control plane |
| OpenAI | Codex | connected workspace / variable runtime | controlled dry-run build support | stale workspace risk, missing origin/main risk, capability variance by runtime/plan | readiness checks passed | GitHub control plane/manual branch |
| Anthropic | Claude / Claude Code | optional review station | secondary review/reasoning support | local environment dependency, context drift risk | repo access + defined authority | ChatGPT/GitHub review |
| GitHub/Microsoft | GitHub | primary control plane | source of truth, PR/issue routing, audit trail | permission and branch-protection dependency | repo access + branch visibility | manual operator control |
| GitHub/Microsoft | GitHub Actions | inspection station | CI, smoke checks, artifact generation | workflow permission and minute limits | workflow success and artifact upload | manual validation |
| Future provider | n8n | not yet approved | future orchestration only | uncontrolled orchestration risk | future readiness review | manual routing |
| Supabase | Supabase platform | not in current scope | future app infrastructure | RLS/auth/runtime dependency | future infrastructure approval | local/dev isolation |
| Vercel | Vercel platform | not in current scope | future deployment | deployment/runtime limits | deployment readiness review | manual deployment |

## Capability-state definitions

| State | Meaning |
|---|---|
| Approved | capability may be used within defined scope |
| Controlled dry-run | capability allowed without autonomous release authority |
| Limited | capability usable only with fallback and operator review |
| Experimental | not yet approved for production route |
| Prohibited | not allowed in current maturity state |

## Current approved maturity

| Capability | Current state |
|---|---|
| Autonomous merge | Prohibited |
| Broad conflict repair by AI | Prohibited |
| Dry-run execution | Approved |
| Controlled PR generation | Limited / human review required |
| CI artifact generation | Approved |
| Human release authority | Mandatory |
| Generated-artifact merge payloads | Restricted |

## Current verified toolchain capability

GitHub Actions:

- verified for issue-driven dry-run
- verified for artifact handoff
- verified for readiness decision propagation

GitHub PR route:

- verified for documentation-only PR-write
- verified for low-risk runtime mutation
- verified for related runtime/control propagation

Codex / AI build station:

- still requires readiness checks
- not approved for autonomous merge
- not approved for broad repair

ChatGPT / Claude review stations:

- planning, audit, review, and recommendation only
- no release authority

Next required capability review:

```text
M7 product-line dry-run
```

## Capability review triggers

Review the matrix when:

- provider plans change,
- runtime/model changes occur,
- repeated failures occur,
- automation maturity changes,
- new tools/providers are introduced,
- audits identify capability assumptions,
- corrective actions affect tooling.

## Conclusion

The VIF factory must treat tool capability as variable and evidence-based.

No provider or tool may be assumed capable beyond verified readiness and approved operating scope.
