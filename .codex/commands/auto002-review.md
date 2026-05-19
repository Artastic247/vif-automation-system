# Command: auto002-review

Use this command to run the AUTO-002 PR review gate.

## Required inputs
- PR number or PR URL
- expected files
- issue number
- task class
- validation evidence

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
1. Confirm the PR targets `main`.
2. Run `.codex/skills/auto-pr-review/run.md`.
3. Compare changed files to expected files.
4. Return `PASS` or `HOLD`.
5. If `HOLD`, route to `.codex/skills/repair-loop/run.md`.
6. Do not merge.

## Output required
- PR URL
- reviewed changed files
- validation reviewed
- PASS/HOLD state
- repair instructions or human-merge next action
