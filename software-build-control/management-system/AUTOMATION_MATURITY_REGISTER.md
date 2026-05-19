# AUTOMATION_MATURITY_REGISTER

## Purpose

Track verified automation maturity for the VIF factory.

This register is the management-system source of truth for maturity state, verified capability, remaining restrictions, and next approved gate.

## Maturity scale

| Level | Name | Description |
|---|---|---|
| Level 0 | Prompt chaos | Ad hoc ChatGPT/Codex use, no stable controls. |
| Level 1 | Documented control foundation | Policies, procedures, branch rules, and basic governance exist. |
| Level 2 | Controlled dry-run / governed manual execution | Issue routing and artifact-only execution exist, but the operator still performs most coordination and release activity. |
| Level 3 | Governed semi-automation | The factory has controlled issue/branch/PR rules, dry-run artifacts, readiness outputs and human release gates, but the operator still drives execution and recovery. |
| Level 4 | Controlled product-line dry-run | Real PFMEA/SPC/Control Plan/APQP/product-line work flows through the factory in dry-run/product-line mode with reduced manual coordination. |
| Level 5 | Limited autonomous execution | Approved task classes may execute automatically with CI gates and human release authority. |
| Level 6 | Full autonomous factory | Broad autonomous execution with mature monitoring, rollback, provider controls, and release governance. |

## Current maturity

```text
Level 3.2 — Governed Semi-Automation / Operator-Assisted Execution
```

This is not controlled autonomy.

The current state proves that governance controls, routing, PR discipline, artifact handling and readiness signalling exist. It does not yet prove that the factory can operate without the operator performing substantial coordination, triggering, interpretation, recovery, push and merge activity.

## Verified gates

| Gate | Status | Evidence route |
|---|---|---|
| M1 — app-build execution cell | Complete | app-build-line execution cell and status records |
| CA-001 — generated artifact / conflict recovery | Effective | corrective action and merged governance controls |
| CA-002 — context / interested parties / readiness | Effective | context and Codex readiness controls |
| AUD-001 — management-system/factory alignment audit | Complete | audit report |
| CA-003 — management-system traceability | Effective | traceability control |
| CA-004 — human-factor/toolchain/interface control | Effective | role, interface, and capability controls |
| VER-001 — corrective action effectiveness | PASS | controlled operator-panel verification |
| M5A — issue-driven dry-run | PASS_WITH_WARNINGS | router to dry-run artifact route |
| VER-002 — documentation PR-write | PASS | one-file documentation PR-write verification |
| M6A — single-file runtime mutation | PASS | readiness HOLD output added to router |
| M6B — multi-file runtime/control propagation | PASS | readiness decision propagated to workflow artifact |

## Current approved capability

- issue-driven routing,
- dry-run workflow dispatch,
- artifact-only handoff,
- documentation-only PR-write,
- low-risk single-file runtime mutation,
- controlled related runtime/workflow propagation,
- human merge authority.

## Current operator dependency

The operator still performs substantial factory work, including:

- interpreting tool output,
- triggering manual workflow steps,
- coordinating between ChatGPT, Codex, VS Code and GitHub,
- resolving local workspace readiness issues,
- deciding when to push and merge,
- checking whether branch and PR state is correct,
- recovering from toolchain failures.

This means the current state is governed semi-automation, not autonomous or fully controlled automation.

## Current prohibited capability

- auto-merge,
- broad autonomous repair,
- unrestricted runtime mutation,
- product-line mutation,
- app repo mutation,
- deployment,
- Supabase/RLS,
- n8n orchestration,
- customer data access,
- claims of autonomous factory execution.

## Current restrictions

The following remain mandatory:

- one issue = one branch = one PR for controlled changes,
- current `main` must be confirmed before branch creation,
- changed files must match expected scope,
- generated artifacts remain CI artifacts unless explicitly approved,
- human release authority remains active,
- protected-scope exceptions require explicit approval,
- maturity upgrades require management review and Head of Factory approval.

## Next gate

```text
M7 — first product-line dry-run
```

M7 may not start until MR-001 is merged and current maturity/status alignment is complete.

## Maturity caution

M7 must not be treated as proof of autonomy.

The next improvement target is to reduce hidden operator load and prove that product-line routing can produce useful, reviewable evidence with less manual reconstruction.

## Decision rule

The factory may not claim a maturity level higher than the latest verified gate.

The next maturity gate may only be attempted when:

- prior gate evidence is recorded,
- documented maturity matches actual verified capability,
- management-system controls are current,
- operator dependency is visible and controlled,
- Head of Factory / Release Authority approval is retained.
