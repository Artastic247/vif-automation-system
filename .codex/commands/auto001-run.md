# Command: auto001-run

Use this command to run the AUTO-001 issue-to-PR workflow.

## Required inputs
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

## Route
1. Run `.codex/hooks/pre-task.md`.
2. Run `.codex/skills/auto-issue-to-pr/run.md`.
3. Run `.codex/hooks/pre-pr.md`.
4. Open one PR against `main`.
5. Run `.codex/hooks/post-pr.md`.
6. Wait for AUTO-002 review.

## Output required
- branch
- PR URL
- changed files
- validation run
- PASS/HOLD state
- next action
