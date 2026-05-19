# Run AUTO-002 PR Review Skill

## Required inputs
- `PR_NUMBER` or `PR_URL`
- `EXPECTED_FILES`
- `ISSUE_NUMBER`
- `TASK_CLASS`

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

## Preflight commands

```bash
git remote -v
git fetch origin --prune
gh pr checkout ${PR_NUMBER}
git status --short
git branch --show-current
```

Stop if `origin/main` is unavailable, the PR cannot be checked out, the target branch is not `main`, or the workspace is dirty before review work begins.

## Review commands

```bash
git diff --name-only origin/main...HEAD
git diff --check origin/main...HEAD
git status --short
```

Compare the changed-file list to `EXPECTED_FILES`. Generated reports must remain artifacts and must not appear in the source diff.

## Review decision

Return `PASS` only when:
- PR targets `main`.
- one issue maps to one branch and one PR.
- changed files match declared scope.
- validation evidence is present and credible.
- protected scope is untouched or explicitly approved.
- no auto-merge path is enabled.

Return `HOLD` when any condition is unclear or failing. HOLD output must name the exact blocking file, check, or missing evidence and route the PR to repair-loop.

## Output format

```text
AUTO-002: PASS|HOLD
PR: <url>
Issue: <number>
Changed files:
- <path>
Validation reviewed:
- <command or evidence>
Protected scope: clear|approved|blocked
Next action: human merge|repair-loop|operator decision
```

Do not merge the PR.
