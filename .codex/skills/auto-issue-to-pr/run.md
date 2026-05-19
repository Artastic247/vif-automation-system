# Run AUTO-001 Issue-to-PR Skill

## Required inputs
- `ISSUE_NUMBER`
- `SHORT_TASK_NAME`
- `TASK_CLASS`
- `EXPECTED_FILES`
- `INSTRUCTION_TEXT`

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
SHORT_TASK_SLUG=$(printf '%s' "${SHORT_TASK_NAME}" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')
TASK_BRANCH="auto-issue-${ISSUE_NUMBER}-${SHORT_TASK_SLUG}"
test -n "${ISSUE_NUMBER}"
test -n "${SHORT_TASK_SLUG}"
git checkout -B "${TASK_BRANCH}" origin/main
git status --short
```

Stop if `origin/main` is unavailable, the checkout fails, the workspace is dirty before task work begins, the issue number is missing, or the sanitized task slug is empty.

## Execute

1. Read the issue and classify the task.
2. Record the expected files before editing.
3. Apply the smallest change that satisfies the issue.
4. Keep generated reports out of source commits.
5. Confirm protected scope is untouched.
6. Run validation for the task class.

## Scope check

```bash
git diff --name-only origin/main...HEAD
git status --short
```

Every changed file must be listed in `EXPECTED_FILES`. If any extra file appears, stop and remove the unexpected change before proceeding.

## Validation

Run the narrowest available deterministic validation first. Use repository-specific tests, linters, scripts, or document checks when present. If no automated validation exists, record a manual validation statement and the reason automation was unavailable.

## Create PR body

Create `pr-body.md` before calling `gh pr create`. The body must contain the exact AUTO-002 control tokens: `workflow_dispatch only`, `expected-file scope check`, `no auto-merge`, and `human merge required`.

```bash
cat > pr-body.md <<EOF
## Summary
${INSTRUCTION_TEXT}

## Issue
Issue #${ISSUE_NUMBER}

## Task class
${TASK_CLASS}

## Branch
${TASK_BRANCH}

## Changed files
${EXPECTED_FILES}

## Validation
- <record commands or evidence here>

## AUTO-002 controls
- workflow_dispatch only
- expected-file scope check
- no auto-merge
- human merge required

## Protected scope
Protected scope unchanged unless explicitly approved in Issue #${ISSUE_NUMBER}.

## Next action
Run AUTO-002 review, then Codex review, then human merge only if accepted.
EOF
```

## Create PR

```bash
git push -u origin "${TASK_BRANCH}"
gh pr create --base main --head "${TASK_BRANCH}" --title "AUTO: Issue #${ISSUE_NUMBER} - ${SHORT_TASK_NAME}" --body-file pr-body.md
```

The PR body must include branch, issue number, task class, changed files, validation evidence, protected-scope confirmation, and next action. It must preserve the AUTO-002 control tokens exactly.

## After PR

Trigger or wait for AUTO-002 review. If AUTO-002 returns `HOLD`, run the repair-loop skill. Do not merge the PR.
