---
id: repair-loop
name: AUTO-003 Repair Loop
trigger:
  - AUTO-002 returns HOLD
  - CI validation fails on scoped PR
  - operator requests repair of failing automation
purpose: Repair failing scoped automation without broadening scope or merging automatically.
---

# AUTO-003 Repair Loop

## Purpose
Repair a scoped PR after AUTO-002 returns `HOLD` or validation fails, while preserving the one issue, one branch, one PR route.

## Inputs
- PR number or PR URL
- HOLD report or failed validation evidence
- expected changed files
- issue number
- task class
- rollback path

## Core rules
- GitHub main is source of truth.
- Do not work from stale local main.
- Do not push directly to main.
- One issue = one branch = one PR.
- Human merge authority remains mandatory.
- Auto-merge prohibited.
- Generated reports are artifacts, not source payloads.
- If workspace cannot confirm origin/main, STOP.
- If changed files exceed declared scope, STOP.
- If AUTO-002 returns HOLD, run repair-loop skill.

## Method
1. Confirm the PR branch and target `main`.
2. Read the HOLD reason or failing validation output.
3. Classify the failure as scope, validation, formatting, content, route, or protected-scope risk.
4. Repair only the files already declared in scope.
5. If repair requires a new file or protected path, stop for operator approval.
6. Rerun validation.
7. Push the repair commit to the existing PR branch.
8. Rerun AUTO-002 review.
9. Do not merge.

## Stop conditions
- no clear HOLD reason
- repair requires broad rewrite
- repair requires protected scope
- repair requires generated report commit
- changed files exceed declared scope
- PR branch cannot be confirmed
- rollback path is missing

## Outputs
- repair summary
- changed-file list
- validation evidence
- AUTO-002 PASS/HOLD state
- next action
