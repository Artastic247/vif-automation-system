# Pre-PR Hook

Run this hook after changes are complete and before opening a PR.

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

## Required checks

```bash
git fetch origin --prune
git diff --name-only origin/main...HEAD
git diff --check origin/main...HEAD
git status --short
```

## PR readiness checklist
- changed files match the declared expected file list
- no forbidden paths changed
- no generated reports committed
- validation has run or the reason it cannot run is recorded
- protected scope is clear or explicitly approved
- PR target is `main`
- PR body includes branch, issue number, changed files, validation evidence, PASS/HOLD state, and next action

## Stop immediately if
- unexpected files appear
- validation fails without a narrow repair
- the branch contains unrelated commits
- PR body lacks validation evidence
- auto-merge is requested or enabled
