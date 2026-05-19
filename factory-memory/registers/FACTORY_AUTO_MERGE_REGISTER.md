# FACTORY_AUTO_MERGE_REGISTER

## Purpose

Define when the VIF factory may request GitHub auto-merge.

This register exists because repository-level auto-merge is a GitHub setting, while factory-level auto-merge must remain scoped and reviewable.

## Repository prerequisite

A maintainer must enable:

Settings -> General -> Pull Requests -> Allow auto-merge

If this setting is not enabled, the factory auto-merge workflow can still evaluate PRs, but GitHub will reject the auto-merge request.

## Approved auto-merge route

Only generated factory-memory output PRs are eligible.

| Requirement | Rule |
|---|---|
| Label | `factory-auto-merge` |
| Title | Starts with `AUTO: Issue #` and contains `Factory memory ingest` |
| Branch | Starts with `auto-issue-` and contains `auto-003-factory-memory` |
| Review | PR discussion contains `AUTO-002 Review Result: PASS` |
| Draft state | PR is not draft |
| Changed files | Generated factory-memory output paths only |
| Merge method | GitHub auto-merge requested with squash merge, or immediate guarded squash merge when GitHub reports the PR is already in clean status |

## Allowed changed files

- `factory-memory/chats/inbox/*.md`
- `factory-memory/chats/summaries/*.md`
- `factory-memory/decisions/*.md`
- `factory-memory/lessons-learned/*.md`
- `factory-memory/skills/*.md`

## Explicitly blocked from auto-merge

- `.github/**`
- `.codex/**`
- `software-build-control/**`
- `factory-memory/registers/**`
- `factory-memory/instructions/**`
- `factory-memory/agents/**`
- `factory-memory/plugins/**`
- `factory-memory/deployments/**`
- `supabase/**`
- deployment paths
- app paths
- customer-data paths
- provider adapter controls

## Workflow behavior

`VIF Factory Auto Merge` may run from:

- PR opened, synchronized, reopened, ready for review, or labeled
- `/factory-auto-merge` PR comment
- manual workflow dispatch with a PR number
- scheduled scan of open PRs labeled `factory-auto-merge`

The workflow must:

1. Resolve the PR.
2. Confirm the `factory-auto-merge` label unless explicitly dispatched or commented.
3. Collect title, branch, draft state, changed files, and PR comments.
4. Run `software-build-control/scripts/factory_auto_merge_guard.py`.
5. Request GitHub auto-merge only when the guard returns PASS.
5a. If GitHub reports the PR is already in clean status, perform the same guarded squash merge immediately with head SHA matching.
6. Leave PENDING when AUTO-002 PASS has not appeared yet.
7. Remove the label and comment HOLD when the guard fails.

## Authority boundary

Guarded auto-merge closes the manual merge step only for generated factory-memory output PRs. It does not authorize auto-merge for factory controls, workflows, scripts, provider adapters, deployment, Supabase/RLS, app changes, or customer-data mutation.
