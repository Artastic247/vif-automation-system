# Branch and PR Rules — App Build Line

## 1. Purpose

This document defines branch, pull request, scope, and merge discipline for the VIF app-build line.

Its purpose is to prevent repeated manual rework caused by stale branches, mixed-scope pull requests, uncontrolled Codex context carry-over, and broad conflict recovery.

## 2. One Issue = One Branch = One Pull Request

Each build activity must start from one approved issue or build order.

One issue must produce one branch and one pull request unless explicit release authority approves otherwise.

A branch must not be reused for a later scope after a pull request is closed, rejected, merged, or found to be conflicted.

## 3. Branch Naming Rules

Branch names must identify the milestone and scope.

Recommended format:

```text
m<milestone>-<short-scope>
```

Examples:

```text
m4-branch-pr-rules
m5-first-real-app-slice
m3-ci-validation-gate
```

Avoid generic or reused names such as:

```text
work
update
fix
codex-task
baseline
```

Codex-generated branches are allowed, but the PR must still comply with the scope and changed-file rules in this document.

## 4. PR Title Rules

Pull request titles must clearly state the scope and milestone.

Examples:

```text
Add M4 branch and PR discipline rules
Add M3 CI validation gate for app-build-line route
Close M1 execution-cell build cycle
```

Titles must not imply a broader release than the PR actually delivers.

## 5. Allowed Changed-File Expectations

Each pull request must list the intended changed files in its body.

The actual changed files must match the approved scope.

Examples:

| PR Type | Expected Changed Files |
|---|---|
| Status closure | `APP-BUILD-LINE-STATUS.md` only |
| Branch/PR rules | `BRANCH_AND_PR_RULES.md` only |
| CI validation | `.github/workflows/app-build-line-validation.yml` and necessary status update only |
| Runtime change | Runtime script plus directly related reports/docs only |

If unexpected files appear, the PR must stop for review before merge.

## 6. No Mixed-Scope PR Rule

A pull request must not mix unrelated milestones or scopes.

Do not combine:

- M1 closure with M2 automation-control work
- CI workflow changes with prompt/hook/inflow/schedule rebuilds
- status report edits with unrelated runtime changes
- app-build-line changes with app repo changes
- governance files with Supabase, n8n, deployment, customer data, or DOS FMEA changes

Mixed-scope pull requests must be rejected or split.

## 7. Stale Branch Handling

A branch is stale if it was created before the current accepted `main` baseline and cannot be cleanly updated without conflicts or unrelated carry-over.

Stale branch rule:

1. Do not continue building on the stale branch.
2. Do not manually repair broad conflicts unless release authority approves.
3. Close the conflicted PR if it carries mixed scope.
4. Rebuild from current `main` on a fresh branch.
5. Reapply only the approved delta.

## 8. Conflict Handling Rules

Small single-file conflicts may be resolved manually when the intended final content is clear.

Broad conflicts or conflicts involving multiple scopes must not be repaired inside GitHub conflict editor.

Conflict response:

| Conflict Type | Action |
|---|---|
| One status file only | Resolve manually if final content is clear |
| Workflow plus unrelated docs | Review carefully; split if mixed scope |
| Multiple app-build-line areas | Close and rebuild from current `main` |
| Any protected-scope file | Stop and escalate |
| M2 mixed with M1/M3/M4 | Close and rebuild cleanly |

## 9. Merge Authority Rules

Codex may create branches, commits, and pull requests.

Codex may update a pull request in response to validation findings.

Codex must not merge a pull request unless explicitly authorised for that specific pull request.

Default merge authority remains human-controlled.

While the gate result is `PASS_WITH_WARNINGS`, manual review is required before merge.

A `HOLD` gate blocks merge.

## 10. CI Validation Requirements

The app-build-line CI validation workflow must run before merge when applicable.

The CI gate must:

- execute the M1 app-build-line route
- produce or inspect the gate decision report
- fail on `HOLD`
- allow `PASS_WITH_WARNINGS` with visible warning
- avoid claiming full `PASS` unless supported by stronger validation evidence

CI passing does not remove human release authority while the line remains at `PASS_WITH_WARNINGS`.

## 11. M2 HOLD Rule

M2 automation-control work remains `HOLD_PENDING_CLEAN_REBUILD` until explicitly reopened.

M2 may only proceed when:

1. a new approved issue/build order exists,
2. the branch is created from current `main`,
3. the PR contains only approved M2 files,
4. the M1/M3/M4 baselines are not reintroduced as duplicate changes,
5. CI validation passes or produces an accepted warning state.

## 12. Codex Authority Limitations

Codex must follow the approved build order and this rule document.

Codex must stop and report when:

- more files changed than allowed,
- the branch is stale,
- `main` cannot be fetched or confirmed,
- merge conflicts appear,
- protected-scope files appear,
- gate decision is `HOLD`,
- the task requires release authority.

Codex must report:

- branch name,
- changed files,
- validation commands run,
- gate decision,
- warnings,
- PR URL,
- whether human merge is required.

## 13. Example Good PR Flow

```text
Issue #8 opened for M4 branch/PR rules
→ new branch: m4-branch-pr-rules
→ one file added: BRANCH_AND_PR_RULES.md
→ CI runs
→ PR body lists one changed file
→ human reviews
→ merge approved
```

## 14. Example Bad PR Flow

```text
M4 branch/PR rules task
→ stale Codex branch reused
→ workflow file appears again
→ status file appears again
→ M2 automation files appear
→ conflict created
→ PR rejected and closed
```

## 15. Closure and Cleanup Rules

After merge or rejection:

- close superseded PRs,
- do not reuse rejected branches,
- record the accepted baseline in status where required,
- keep M2 on HOLD unless explicitly reopened,
- ensure the next task starts from current `main`.

## 16. Current Operating Rule

The current app-build line operating rule is:

```text
Small scope. Clean branch. CI visible. Human merge. No mixed payloads.
```
