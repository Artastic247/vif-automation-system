# Command: auto003-repair

Use this command when AUTO-002 returns `HOLD` or a scoped PR fails validation.

## Required inputs
- PR number or PR URL
- HOLD reason or failed validation evidence
- expected files
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

## Route
1. Run `.codex/skills/repair-loop/run.md`.
2. Repair only the named HOLD or validation failure.
3. Keep changed files inside expected scope.
4. Push to the existing PR branch.
5. Rerun AUTO-002 review.
6. Route PASS results to Codex review and human merge.
7. Do not merge.

## Output required
- PR URL
- repair summary
- changed files
- validation run
- AUTO-002 PASS/HOLD state
- next action
