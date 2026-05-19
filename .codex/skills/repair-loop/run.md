# Run AUTO-003 Repair Loop Skill

## Required inputs
- `PR_NUMBER` or `PR_URL`
- `HOLD_REASON`
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
git merge-base --is-ancestor origin/main HEAD
git diff --name-only origin/main...HEAD
```

Stop if the PR cannot be checked out, the PR target branch is not `main`, the workspace is dirty before repair, the branch does not contain current `origin/main`, or the changed-file list already exceeds `EXPECTED_FILES`.

## Diagnose

1. Read the AUTO-002 HOLD report or failing validation output.
2. Identify the smallest repair that addresses the named failure.
3. Confirm the repair stays inside `EXPECTED_FILES`.
4. Confirm no protected scope is touched.

## Repair

Make only the minimum required edit. Do not add generated reports. Do not perform broad repair. Do not retarget or merge the PR.

## Validate

```bash
git diff --name-only origin/main...HEAD
git diff --check origin/main...HEAD
gh pr view "${PR_NUMBER}" --json title,body,baseRefName,headRefName
git status --short
```

Run the task-specific validation that failed, plus any lightweight checks needed for the touched files.

## Push and rerun review

```bash
git push
```

After pushing, rerun AUTO-002 review. If AUTO-002 returns `PASS`, route to Codex review and human merge. If AUTO-002 returns `HOLD`, repeat repair-loop only when the next repair remains narrow and inside declared scope.

## Output format

```text
AUTO-003 repair: complete|blocked
PR: <url>
Issue: <number>
Repair reason: <HOLD reason>
Changed files:
- <path>
Validation:
- <command or evidence>
AUTO-002 state: PASS|HOLD
Next action: Codex review|human merge|operator decision
```
