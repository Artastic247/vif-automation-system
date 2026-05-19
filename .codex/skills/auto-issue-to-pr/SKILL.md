---
id: auto-issue-to-pr
name: AUTO-001 Issue to PR Execution
trigger:
  - issue assigned to Codex
  - operator requests automation execution
  - doc_control_update task
purpose: Use AUTO-001 or equivalent Codex execution to create scoped PRs from issues.
---

# AUTO-001 Issue to PR Execution

## Purpose
Use AUTO-001 or equivalent Codex execution to create scoped PRs from GitHub issues without relying on ad hoc chat prompts.

## Inputs
- issue number
- task class
- expected files
- instruction text
- short task name

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
1. Confirm `origin/main` is available and current.
2. Create a task branch from `origin/main`.
3. Update only expected files.
4. Run validation that matches the task class.
5. Push the branch.
6. Open one PR against `main`.
7. Ensure AUTO-002 can review the PR.
8. Do not merge.

## Scope control
Before editing, write down the expected file list. After editing, compare the changed-file list against that expected list. If any unexpected file appears, stop and repair before opening the PR.

## Protected scope
Do not modify Supabase, RLS, deployment, customer data, app repo mutation, generated reports, or any other protected path unless the issue explicitly approves that scope.

## Outputs
- PR URL
- changed-file list
- validation evidence
- next action
