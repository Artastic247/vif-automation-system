# APP_BUILD_LINE_OPERATING_GUIDE

## Purpose
Operate the VIF app-build line using GitHub as system-of-record for work orders, branch state, pull requests, checks, approvals, and evidence.

## Operating modes
- **Manual relay**: operator drives prompts manually and records outputs.
- **Linked dry-run**: GitHub issue triggers AI generation in artifact-only mode.
- **Linked PR-write**: validated route allows deterministic branch/PR mutation.
- **Autonomous merge**: disabled by policy until explicitly approved.

## Route labels
- `route/codex`
- `route/claude-review`
- `route/chatgpt-operator`
- `gate/manual-approval`

## Core branch and PR policy
- One issue maps to one branch and one PR.
- Start each run from current `main`.
- If stale/conflicted and resolution exceeds issue scope, close and recreate branch/PR.
- No mixed-scope edits.
- CI and required checks must pass before merge.

## Merge authority
Operator approval is mandatory for merge until policy is revised and approved.

## Escalation rules
Escalate to manual hold when any of the following occurs:
- Missing or malformed handoff contract.
- Scope drift versus declared allowed paths.
- Failing security/prompt hygiene checks.
- Merge conflict requiring broad non-scope edits.

## Rollback
- Close PR and delete branch when gate failure is unrecoverable in-scope.
- Recreate work from issue and replay key on fresh branch.
