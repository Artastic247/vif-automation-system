# FACTORY_MEMORY_REGISTER

## Purpose

Track controlled factory-memory areas, ownership, review state, and routing rules.

## Register

| Area | Path | Review state | Notes |
|---|---|---|---|
| Chat inbox | `factory-memory/chats/inbox/` | Proposed source evidence | Raw chat, transcript, or issue evidence awaiting review. |
| Processed chats | `factory-memory/chats/processed/` | Controlled archive | Source evidence after routing or closure. |
| Summaries | `factory-memory/chats/summaries/` | Proposed or approved | AUTO-003 v1 creates deterministic stubs only. |
| Decisions | `factory-memory/decisions/` | Proposed or approved | Requires later human or approved LLM review before becoming authority. |
| Lessons learned | `factory-memory/lessons-learned/` | Proposed or approved | Must include failure mode and verification method before becoming authority. |
| Instructions | `factory-memory/instructions/` | Controlled knowledge | Used to update station instructions through reviewed PRs. |
| Skills | `factory-memory/skills/` | Recommendation or approved | Skill updates require separate controlled skill-pack changes. |
| Agents | `factory-memory/agents/` | Controlled knowledge | Captures station roles, limits, caps, and handoff rules. |
| Plugins | `factory-memory/plugins/` | Controlled knowledge | Captures plugin packs and adapters. |
| Deployments | `factory-memory/deployments/` | Protected evidence | Does not authorize deployment by itself. |
| Registers | `factory-memory/registers/` | Controlled knowledge | Captures memory routing, provider capability, and factory-control registers. |

## AUTO-003 status

- Version: deterministic v1
- LLM summarisation: not enabled
- PR creation: workflow-created when triggered through `factory-memory-ingest.yml`
- Guarded auto-merge: allowed only for generated memory output PRs after AUTO-002 PASS and auto-merge guard PASS
- Human merge: required for all control-plane, workflow, script, register, deployment, provider-adapter, Supabase/RLS, app, and customer-data changes
- Unguarded auto-merge: prohibited

## Approved ingest triggers

| Trigger | How to use | Result |
|---|---|---|
| Manual workflow | Run `Factory Memory Ingest` with `workflow_dispatch`. | Creates deterministic memory stubs from an issue number or repository text file. |
| Repository dispatch | Send `repository_dispatch` type `factory-memory-ingest` with `issue_number`, or `input_file`, and optional `short_task_name`. | Gives approved external orchestrators a direct trigger route without relying on issue webhooks. |
| Issue label | Add `factory-memory-ingest` to an issue. | Uses the labeled issue as source evidence and opens a memory PR. |
| Issue comment | Comment `/factory-memory ingest` on an issue. | Uses the commented issue as source evidence and opens a memory PR. |
| Scheduled poller | Runs every 5 minutes. | Picks up open issues labeled `factory-memory-ingest` and not labeled `factory-memory-ingested`. |

All trigger routes preserve the approved merge gate. Triggered memory records are proposed evidence until accepted by human merge or guarded generated-memory auto-merge.

## Processing markers

- Pending label: `factory-memory-ingest`
- Processed label: `factory-memory-ingested`
- Auto-merge candidate label: `factory-auto-merge`

The processed label is applied only after a memory-ingest PR is opened. The auto-merge candidate label is applied only to generated memory output PRs and does not bypass the auto-merge guard.

## Observability rules

- Each active ingest run comments on the source issue with the workflow run URL.
- Issues already marked `factory-memory-ingested` are skipped before a new branch is created unless a maintainer removes that marker for an intentional rerun.
- For already processed issues, historical ingest PRs are detected before a new branch is created.
- For active ingest attempts, open ingest PRs are detected before a new branch is created.
- If a memory PR is opened by the workflow, the workflow also runs an inline AUTO-002 review and comments the result on the PR.
- Inline AUTO-002 is required because GitHub may suppress chained workflow triggers when a PR is created by the default workflow token.
- The auto-merge workflow comments a PASS, PENDING, or HOLD guard report on the PR when it acts on the PR.

## Guarded auto-merge rules

Generated memory output PRs may request GitHub auto-merge only when all conditions pass:

- PR title starts with `AUTO: Issue #` and contains `Factory memory ingest`.
- Head branch starts with `auto-issue-` and contains `auto-003-factory-memory`.
- PR is not draft.
- PR discussion contains `AUTO-002 Review Result: PASS`.
- Changed files are limited to generated outputs under `factory-memory/chats/inbox/`, `factory-memory/chats/summaries/`, `factory-memory/decisions/`, `factory-memory/lessons-learned/`, and `factory-memory/skills/`.

The guard must HOLD auto-merge for workflow files, scripts, registers, deployment paths, Supabase/RLS paths, app paths, provider-adapter controls, and customer-data paths.

## Token boundary

`VIF_FACTORY_TOKEN` is optional. If present as a repository secret, workflows use it for GitHub CLI operations. If absent, workflows fall back to GitHub's default workflow token.

Use `VIF_FACTORY_TOKEN` when the factory must trigger downstream workflows from workflow-created branches or PRs. The token must be scoped narrowly to the repository and must not authorize deployment, Supabase/RLS mutation, or customer data access.

Repository Settings -> General -> Pull Requests -> Allow auto-merge must be enabled by a maintainer before GitHub can perform automatic merges.

## Related registers

- `factory-memory/registers/LLM_PROVIDER_CAPABILITY_REGISTER.md` controls provider routing, usage caps, tool permissions, and approved work classes.
- `factory-memory/registers/FACTORY_AUTO_MERGE_REGISTER.md` controls generated-memory auto-merge eligibility.

## Next register gap

Add runtime evidence records for actual workflow-run outcomes before claiming measured factory maturity. The system may propose, review, and guarded-auto-merge generated memory output, but factory control-plane changes remain human-gated.
