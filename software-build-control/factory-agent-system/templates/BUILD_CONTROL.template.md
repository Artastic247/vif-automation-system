# Build Control

## Purpose

This document defines how this repository is controlled when AI coding agents are used.

The objective is to make the agent a controlled workstation, not the process owner.

## Build repo identity

| Item | Detail |
| --- | --- |
| Product/repo | [Insert repo name] |
| Product owner | [Insert owner] |
| Technical owner | [Insert owner] |
| Release authority | [Insert authority] |
| Main branch | `main` |
| Agent work branch pattern | `agent/<issue-number>-<short-title>` |

## Controlled workflow

```text
Issue/task
  ↓
Branch
  ↓
Implementation
  ↓
Verification
  ↓
Pull request
  ↓
Review
  ↓
Fix if required
  ↓
Human release decision
  ↓
Merge
```

## Required repo controls

| Control | Required state | Status |
| --- | --- | --- |
| `AGENTS.md` | Present and product-specific | [TBD] |
| CI workflow | Present and runs on PR | [TBD] |
| Issue template | Present for agent tasks | [TBD] |
| PR template | Present and requires evidence | [TBD] |
| Known issues record | Present where persistent blockers exist | [TBD] |
| Release checklist | Present | [TBD] |

## Task control rules

- One issue should produce one branch and one PR.
- One PR should solve one scoped problem.
- Acceptance criteria must be visible before implementation.
- Scope exclusions must be visible before implementation.
- Schema, auth, permission, billing, production-data, and deletion changes require explicit approval.
- UI-only tasks must not alter backend/service/data logic unless approved.

## Verification controls

The agent must run available commands and report results:

```bash
npm run typecheck --if-present
npm run lint --if-present
npm test --if-present
npm run build --if-present
```

If checks are blocked, the PR must state why.

## Failure classification

| Classification | Meaning |
| --- | --- |
| Caused by change | Failure introduced by current PR |
| Pre-existing | Failure already existed before current PR |
| Environment/tooling blocked | Dependencies, registry, token, runner, or network prevented execution |
| Unknown | Not enough evidence to classify yet |

## Merge control

A PR may be merged only when:

- Scope is satisfied.
- CI/check status is known.
- Failures are fixed or consciously accepted as controlled debt.
- Review findings are resolved or accepted by the release authority.
- Residual risks are visible.
- Human release authority approves.

## Agent limitations

The agent may recommend merge readiness but may not act as the final release authority unless the repository owner explicitly delegates that control.
