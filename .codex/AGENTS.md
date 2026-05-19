# VIF Codex Agent Pack

## Purpose
This pack turns Codex into a VIF factory station.

## Primary objective
Reduce operator burden by executing repeatable issue-to-PR, repair, memory-ingest, and skill-update workflows.

## Mandatory route
Issue -> classify -> branch -> change -> validate -> PR -> AUTO-002 review -> Codex review -> human merge.

## Operating contract
Codex must start from GitHub `main`, classify the work, create a scoped branch, make only the declared changes, validate the branch, open a PR, request AUTO-002 review, run Codex review, and leave final merge authority with the human operator.

## Factory memory route
Chat transcripts, issue discussions, lessons learned, decisions, instructions, skills, agents, plugin packs, and deployment notes belong in `factory-memory/` when they are accepted as reusable factory knowledge.

Use AUTO-003 for deterministic memory ingestion:

1. Accept a markdown/text file path or GitHub issue number.
2. Store the source chat or issue evidence in `factory-memory/chats/inbox/`.
3. Generate a summary stub in `factory-memory/chats/summaries/`.
4. Generate decision and lesson-learned stubs.
5. Generate a skill-update recommendation stub.
6. Open a PR for review.
7. Do not treat generated memory as approved knowledge until human merge.

## GitHub-native memory triggers
AUTO-004 allows factory memory ingestion to start without local GitHub CLI access.

Approved triggers:

- Add the `factory-memory-ingest` label to an issue.
- Comment `/factory-memory ingest` on an issue.
- Run `Factory Memory Ingest` manually with `workflow_dispatch`.
- Send a `repository_dispatch` event of type `factory-memory-ingest` from an approved external factory orchestrator.

AUTO-005 adds a scheduled fallback poller. If a webhook trigger is missed, the workflow scans open issues labeled `factory-memory-ingest` and not labeled `factory-memory-ingested`, then opens the same deterministic memory PR.

AUTO-006 hardens the automation loop:

- The scheduled poller runs every 5 minutes.
- The source issue receives a run-start comment with the workflow run URL.
- Existing open memory-ingest PRs are detected to prevent duplicates.
- Workflow-created memory PRs receive an inline AUTO-002 review comment because GitHub can suppress chained workflow triggers from its default automation token.
- If the repository secret `VIF_FACTORY_TOKEN` exists, workflows use it for GitHub CLI operations; otherwise they fall back to the default workflow token.
- `VIF_FACTORY_TOKEN` is optional but required when the factory must trigger downstream workflows from workflow-created branches or PRs.

Trigger behavior:

1. GitHub Actions resolves the source issue or input file.
2. The workflow creates an `auto-issue-*auto-003-factory-memory*` branch from `main`.
3. The workflow creates deterministic factory-memory stubs.
4. The workflow opens a PR.
5. The workflow runs inline AUTO-002 review for the memory PR.
6. The source issue is marked `factory-memory-ingested` after PR creation.
7. Human merge authority remains mandatory.

## Multi-LLM routing boundary
Do not claim autonomous multi-LLM routing until the provider is listed in `factory-memory/registers/LLM_PROVIDER_CAPABILITY_REGISTER.md` with its approved work classes, usage limits, tool permissions, and handoff rules.

Provider adapters must stay thin. Shared VIF logic belongs in factory instructions, skills, registers, and workflows; platform-specific adapters belong only in the relevant Codex, Claude, Copilot, Cursor, Gemini, Ollama, or other runtime pack.

## Core rules
- GitHub main is source of truth.
- Do not work from stale local main.
- Do not push directly to main.
- One issue = one branch = one PR.
- Human merge authority remains mandatory.
- Auto-merge prohibited.
- Generated reports are artifacts, not source payloads.
- Factory memory records are source payloads only when they are deliberately created by the memory-ingest route and merged by a human.
- If workspace cannot confirm origin/main, STOP.
- If changed files exceed declared scope, STOP.
- If AUTO-002 returns HOLD, run repair-loop skill.

## Forbidden
- direct push to main
- auto-merge
- broad repair
- generated report commits
- protected scope changes
- Supabase/RLS/deployment/customer data/app repo mutation unless specifically approved
- treating unreviewed chats, summaries, or skill recommendations as approved factory knowledge
- routing work to an unregistered LLM/provider adapter as if it were approved factory capacity

## Required preflight
```bash
git remote -v
git fetch origin --prune
git checkout -B <task-branch> origin/main
git status --short
```

## Stop conditions
- origin/main unavailable
- dirty workspace before task
- unexpected changed files
- forbidden paths
- missing issue number
- no rollback path
- unclear scope
- memory-ingest input cannot be found
- generated memory output exceeds declared AUTO-003 scope
- provider usage cap, tool permission, or platform authority cannot be confirmed

## Protected scope
Treat these as protected unless the issue explicitly authorizes them:
- Supabase configuration, migrations, RLS, secrets, and customer data paths
- deployment configuration and release automation
- app repository mutation outside the declared issue scope
- generated reports and audit outputs that should remain workflow artifacts

## Output required
- branch
- PR URL
- changed files
- validation run
- PASS/HOLD state
- next action
