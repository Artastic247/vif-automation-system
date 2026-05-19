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
BASE_BRANCH=$(gh pr view "${PR_NUMBER}" --json baseRefName --jq .baseRefName)
test "${BASE_BRANCH}" = "main"
gh pr checkout "${PR_NUMBER}"
git status --short
git branch --show-current
git merge-base --is-ancestor origin/main HEAD
```

Stop if `origin/main` is unavailable, the PR cannot be checked out, the PR target branch is not `main`, the workspace is dirty before review work begins, or the branch does not contain current `origin/main`.

## Review commands

```bash
git diff --name-only origin/main...HEAD
git diff --check origin/main...HEAD
git status --short
gh pr view "${PR_NUMBER}" --json title,body,baseRefName,headRefName
```

Compare the changed-file list to `EXPECTED_FILES`. Generated reports must remain artifacts and must not appear in the source diff.

## PR metadata contract

AUTO-002-compatible PRs must include:
- title tokens: `AUTO:` and `Issue #`
- body tokens: `workflow_dispatch only`, `expected-file scope check`, `no auto-merge`, and `human merge required`

If any token is missing, return `HOLD` and route to repair-loop.

## Review decision

Return `PASS` only when:
- PR targets `main`.
- branch contains current `origin/main`.
- one issue maps to one branch and one PR.
- changed files match declared scope.
- validation evidence is present and credible.
- protected scope is untouched or explicitly approved.
- AUTO-002 metadata tokens are present.
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
