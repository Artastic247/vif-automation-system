# Pre-Task Hook

Run this hook before any VIF Codex task begins.

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
git remote -v
git fetch origin --prune
git status --short
```

## Confirm before editing
- issue number is present
- task class is known
- expected file list is declared
- rollback path is known
- branch will start from `origin/main`
- protected scope is not required, or explicit approval is present

## Stop immediately if
- `origin/main` cannot be fetched
- workspace is dirty before task work
- scope is unclear
- expected files are missing or undeclared
- the task requests direct push to `main`
- the task requests auto-merge
- the task touches Supabase, RLS, deployment, customer data, or app repo mutation without explicit approval
