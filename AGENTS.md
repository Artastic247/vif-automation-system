# Root Execution Guard

Scope: entire repository unless overridden by a deeper `AGENTS.md`.

## Control-plane rule

GitHub is the control plane for this repository.

- GitHub Issues are work orders.
- Branches are controlled build lanes.
- Pull requests are release gates.
- GitHub Actions are inspection stations.
- Human review remains the merge/release authority unless explicitly changed for a specific PR.

## Operating rules

- One approved issue or build order = one branch = one pull request.
- Do not mix unrelated scopes in one PR.
- Do not reuse stale branches.
- Do not continue from a local branch if `main` or `origin/main` cannot be confirmed.
- Do not touch protected paths unless the task explicitly authorises them.
- M2 automation-control layer remains `HOLD_PENDING_CLEAN_REBUILD` unless a fresh approved M2 task is opened from current `main`.

## Codex authority

Codex may:

- create branches,
- create commits,
- open pull requests,
- update pull requests in response to validation findings,
- run approved validation commands,
- report evidence and gate status.

Codex may not:

- merge pull requests,
- auto-approve pull requests,
- bypass CI,
- modify protected areas without explicit approval,
- proceed from an unconfirmed or stale base branch,
- continue if changed files exceed declared scope.

## Stop conditions

Stop and report immediately if any of the following occur:

- `main` or the approved base branch cannot be confirmed,
- branch is stale or local-only,
- unexpected files change,
- protected-scope files appear,
- merge conflicts appear,
- gate decision is `HOLD`,
- task requires release authority,
- validation cannot be run or evidence cannot be produced.

## Protected scope

Do not modify without explicit task approval:

- app repositories,
- Supabase,
- RLS,
- edge functions,
- deployment,
- n8n,
- customer data,
- DOS FMEA repair,
- unrelated governance files.

## Reporting rule

Every agent task response must report:

1. branch name,
2. pull request URL,
3. changed files,
4. validation commands run,
5. gate result,
6. warnings,
7. protected-scope confirmation,
8. whether human merge is required.
