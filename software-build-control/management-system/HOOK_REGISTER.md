# HOOK REGISTER

## Purpose
Define controlled lifecycle management for automation hooks that influence workflow execution, quality gates, evidence capture, or release decisions.

## Scope
- In scope: CI workflow hooks, pre/post verification hooks, validation hooks, and evidence-publish hooks within `software-build-control`.
- Out of scope: app-repository runtime hooks, deployment hooks, tenant/customer-data automation hooks (unless separately approved).

## Inputs
- Hook owner assignment.
- Hook change request and risk assessment.
- Verification and rollback evidence.

## Activities
1. Register hook metadata and ownership.
2. Define test cadence and last/next test dates.
3. Record rollback route and break-glass conditions.
4. Execute health checks and update effectiveness notes.

## Outputs/records
- Current hook inventory and status.
- Hook-health check output report.
- Failed-hook escalation and CAPA linkage when applicable.

## Hook inventory

| Hook ID | Hook name | Owner role | Trigger point | Purpose | Test cadence | Last test date | Next test due | Rollback route | Break-glass condition | Current status | Evidence ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HK-001 | Prompt/context control check | Automation control owner | CI pre-route | Block route when prompt/context governance controls are missing | Every PR + weekly | 2026-05-18 | 2026-05-25 | Revert workflow step and run manual validation route | False blocking on validated controls | active | `reports/prompt-context-check.json` |
| HK-002 | App-build-line smoke route | App build-line owner | CI execution | Execute create/run/verify smoke sequence and capture gate result | Every PR | 2026-05-18 | Next PR | Disable workflow job and switch to manual runbook | CI outage or runner instability | active | `01-app-build-line/reports/build-verification-report.json` |
| HK-003 | Smoke evidence artifact upload | Automation control owner | CI post-route | Preserve evidence artefacts for audit and gate review | Every PR | 2026-05-18 | Next PR | Manual archive of reports to controlled evidence path | Artifact upload service failure | active | `app-build-line-smoke-evidence` |

## Audit criteria
- Every active hook has an owner, cadence, rollback route, and break-glass condition.
- Last test date is not older than defined cadence.
- Any failed hook has CAPA reference before returning to active status.

## Linked gate
- PASS/HOLD/BLOCKED app-build-line gate decisions.
- MLA automation permission decision checkpoints.

## Update trigger
- Hook added/removed/changed.
- Any hook failure, false block, or missed cadence.
- Governance review, internal audit, or management review action.
