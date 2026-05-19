# FACTORY_MEMORY_REGISTER

## Purpose

Track controlled factory-memory areas, ownership, review state, and routing rules.

## Register

| Area | Path | Review state | Notes |
|---|---|---|---|
| Chat inbox | `factory-memory/chats/inbox/` | Proposed source evidence | Raw chat, transcript, or issue evidence awaiting review. |
| Processed chats | `factory-memory/chats/processed/` | Controlled archive | Source evidence after routing or closure. |
| Summaries | `factory-memory/chats/summaries/` | Proposed or approved | AUTO-003 v1 creates deterministic stubs only. |
| Decisions | `factory-memory/decisions/` | Proposed or approved | Requires human review before becoming authority. |
| Lessons learned | `factory-memory/lessons-learned/` | Proposed or approved | Must include failure mode and verification method. |
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
- Human merge: required
- Auto-merge: prohibited

## Approved ingest triggers

| Trigger | How to use | Result |
|---|---|---|
| Manual workflow | Run `Factory Memory Ingest` with `workflow_dispatch`. | Creates deterministic memory stubs from an issue number or repository text file. |
| Repository dispatch | Send `repository_dispatch` type `factory-memory-ingest` with `issue_number`, or `input_file`, and optional `short_task_name`. | Gives approved external orchestrators a direct trigger route without relying on issue webhooks. |
| Issue label | Add `factory-memory-ingest` to an issue. | Uses the labeled issue as source evidence and opens a memory PR. |
| Issue comment | Comment `/factory-memory ingest` on an issue. | Uses the commented issue as source evidence and opens a memory PR. |
| Scheduled poller | Runs every 5 minutes. | Picks up open issues labeled `factory-memory-ingest` and not labeled `factory-memory-ingested`. |

All trigger routes must keep human merge authority. Triggered memory records are proposed evidence until merged.

## Processing markers

- Pending label: `factory-memory-ingest`
- Processed label: `factory-memory-ingested`

The processed label is applied only after a memory-ingest PR is opened.

## Observability rules

- Each active ingest run comments on the source issue with the workflow run URL.
- Existing open ingest PRs are detected before a new branch is created.
- If a memory PR is opened by the workflow, the workflow also runs an inline AUTO-002 review and comments the result on the PR.
- Inline AUTO-002 is required because GitHub may suppress chained workflow triggers when a PR is created by the default workflow token.

## Token boundary

`VIF_FACTORY_TOKEN` is optional. If present as a repository secret, the ingest workflow uses it for GitHub CLI operations. If absent, the workflow falls back to GitHub's default workflow token.

Use `VIF_FACTORY_TOKEN` when the factory must trigger downstream workflows from workflow-created branches or PRs. The token must be scoped narrowly to the repository and must not authorize auto-merge, deployment, Supabase/RLS mutation, or customer data access.

## Related registers

- `factory-memory/registers/LLM_PROVIDER_CAPABILITY_REGISTER.md` controls provider routing, usage caps, tool permissions, and approved work classes.

## Next register gap

Add runtime evidence records for actual workflow-run outcomes before claiming measured factory maturity. The system may propose and review automatically, but human merge remains the final authority.
