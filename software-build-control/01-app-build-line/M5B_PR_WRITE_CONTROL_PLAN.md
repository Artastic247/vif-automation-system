# M5B_PR_WRITE_CONTROL_PLAN

## Purpose

This document defines the planning controls for M5B: controlled PR-write automation under VIF management-system governance.

M5B is not full autonomy.

M5B is a controlled maturity step from dry-run artifact generation toward narrow-scope branch and pull request creation, while retaining human release authority.

## Current maturity basis

M5B planning is permitted because:

- CA-001 was implemented and verified effective,
- CA-002 was implemented and merged,
- CA-003 and CA-004 were implemented and merged,
- AUD-001 was completed,
- VER-001 passed,
- M5A dry-run route completed with PASS_WITH_WARNINGS.

## Approved target route

```text
GitHub Issue
→ router
→ readiness checks
→ controlled branch creation
→ narrow-scope PR generation
→ CI inspection
→ human review and merge
```

## Non-negotiable controls

M5B must retain:

- GitHub as control plane,
- issue as work order,
- human merge authority,
- generated-artifact policy,
- branch and PR discipline,
- toolchain readiness checks,
- interface authority controls,
- fallback routes,
- auditability.

## Prohibited behaviours

M5B must not permit:

- autonomous merge,
- broad conflict repair,
- stale branch reuse,
- uncontrolled branch recovery,
- generated reports committed as source,
- protected-scope modification without approval,
- unrestricted runtime mutation,
- bypass of CI,
- bypass of human release authority.

## M5B readiness criteria

Before M5B implementation, the following must be defined and accepted:

1. Allowed PR-write task classes.
2. Forbidden PR-write task classes.
3. Branch creation rule.
4. Changed-file preflight rule.
5. Generated-artifact rejection rule.
6. Tool readiness rule.
7. Human approval checkpoints.
8. CI inspection requirements.
9. HOLD conditions.
10. Verification strategy.

## Allowed PR-write task classes

Initial M5B PR-write scope may only include:

- documentation-only changes,
- governance file updates,
- operator-panel note updates,
- issue template text updates,
- PR template text updates,
- non-runtime control documentation.

## Forbidden PR-write task classes

The following remain prohibited unless separately approved:

- runtime code changes,
- workflow logic changes,
- generated report changes,
- Supabase/RLS changes,
- deployment changes,
- customer data changes,
- app repository changes,
- broad refactors,
- conflict recovery patches,
- auto-merge enablement.

## Branch creation control

Each M5B task must:

- start from current `main`,
- use one issue,
- create one branch,
- create one PR,
- declare expected changed files before mutation.

Branch naming pattern:

```text
m5b-issue-<issue-number>-<short-scope>
```

## Changed-file preflight rule

Before PR creation, the route must compare actual changed files against declared expected files.

If unexpected files appear:

```text
STOP
```

Do not open or update the PR until the unexpected file list is reviewed.

## Generated-artifact rejection rule

Any generated report, snapshot, gate output or runtime evidence file must be rejected as a source-control payload unless explicitly approved in the issue.

Default action:

```text
Do not commit generated artifacts.
Upload as CI artifact instead.
```

## Tool readiness rule

Before assigning Codex or any build station, confirm:

- GitHub repo access,
- current main visibility,
- branch creation capability,
- PR creation capability,
- permissions are adequate,
- task fits current plan/runtime capability,
- fallback route exists.

If readiness cannot be confirmed:

```text
route = dry-run or manual fallback
```

## Human approval checkpoints

Human approval is required at:

1. issue approval,
2. PR review,
3. any generated-artifact exception,
4. any protected-scope exception,
5. merge decision,
6. maturity upgrade decision.

## HOLD conditions

M5B must HOLD when:

- branch is stale,
- main cannot be confirmed,
- unexpected files change,
- generated reports appear,
- protected scope appears,
- conflict appears,
- CI fails,
- readiness check fails,
- authority is unclear.

## M5B verification strategy

The first M5B verification must use a documentation-only task with exactly one expected changed file.

Pass criteria:

- one issue,
- one branch from current main,
- one PR,
- expected file only,
- no generated artifacts,
- no runtime/workflow changes,
- CI visible,
- human merge required.

Fail criteria:

- extra files,
- generated report payloads,
- stale branch,
- conflict recursion,
- auto-merge,
- hidden operator recovery.

## VER-002 verification note

The first M5B PR-write verification was limited to documentation-only scope and did not permit runtime, workflow, generated-artifact, protected-scope or auto-merge actions.

VER-002 passed and verified documentation-only PR-write under human release authority.

## Current decision

M5B planning is complete.

Documentation-only PR-write has been verified through VER-002.

Runtime/source mutation moved to M6A and M6B controls and has been verified for low-risk controlled task classes.

Broader PR-write remains controlled by approved task class.

Auto-merge remains prohibited.

Product-line automation remains HOLD pending M7 dry-run.
