# Post-PR Hook

Run this hook after the PR is opened.

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

## Required follow-up
- confirm PR URL
- confirm PR targets `main`
- confirm changed-file list
- trigger or wait for AUTO-002 review
- run Codex review after AUTO-002 passes or when the operator requests it
- leave final merge to the human operator

## HOLD route
If AUTO-002 returns `HOLD`, do not merge and do not broaden the PR. Run the repair-loop skill against the existing PR branch.

## Output required
- branch
- PR URL
- changed files
- validation run
- PASS/HOLD state
- next action
