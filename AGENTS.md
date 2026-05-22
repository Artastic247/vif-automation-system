# VIF Repository Execution Guard

Scope: entire repository unless a deeper `AGENTS.md` adds a narrower local rule.

## Control Plane

- GitHub Issues are work orders.
- Branches are controlled build lanes.
- Pull requests are release gates.
- GitHub Actions are inspection stations.
- Human review remains the merge/release authority unless a specific PR explicitly changes that authority.

## Repo Attachment Gate

- Treat `C:\Users\AngusKhan\Documents\IDEAS FOLDER` as a knowledge/workflow area, not a repository execution root.
- Execute VIF repo work from `C:\Users\AngusKhan\Documents\VIF Factory\vif-automation-system` or another checkout that has been proven with Git.
- Before changing files, prove and report:
  - `cwd`
  - Git root
  - remote
  - branch
  - HEAD
  - confirmed `main`, `origin/main`, or approved base branch
  - gate decision
- Connector visibility does not prove local checkout attachment.

## Branch and PR Rules

- Agents may create branches, commits, pull requests, validation evidence, and PR updates within the approved task scope.
- Agents may not merge, auto-approve, bypass CI, or expand scope without explicit approval.
- One approved issue or build order = one branch = one pull request.
- Start from current `main` or the approved base branch.
- Do not push directly to `main`.
- Do not reuse stale branches.
- Do not mix unrelated scopes in one PR.
- Never auto-merge unless a specific approved automation route allows it.
- Human merge is required for normal control-plane changes.
- M2 automation-control remains `HOLD_PENDING_CLEAN_REBUILD` unless a fresh approved M2 task starts from current `main`.

## Protected Scope

Do not modify without explicit task approval:

- app repositories
- Supabase, RLS, or edge functions
- deployment, n8n, or release settings
- customer data, secrets, credentials, or `.env` files
- DOS FMEA repair scope
- generated reports or JSON evidence outputs unless the task requires them
- unrelated governance files

## Validation Evidence

- Run the task-specific checks requested by the issue or build order.
- For AUTO-001 family work, use:
  - `python -m py_compile software-build-control/scripts/auto_doc_control_pr.py`
  - `git diff --name-only`
  - `git diff --check`
  - `python -m unittest software-build-control/scripts/tests/test_factory_automation_controls.py`
- Report command outcomes directly; do not summarize validation as only "done" or "validated".

## Stop Conditions

Stop and report immediately if any of these occur:

- `main` or the approved base branch cannot be confirmed
- branch is stale, local-only, or attached to the wrong remote
- unexpected files change
- protected-scope files appear
- merge conflicts appear
- gate decision is `HOLD`
- validation cannot be run or evidence cannot be produced
- requested work requires release or merge authority

## Required Final Report

Every agent task response must report:

1. branch name
2. pull request URL, or why no PR exists
3. changed files
4. validation commands run and outcomes
5. gate result
6. warnings
7. protected-scope confirmation
8. whether human merge is required
