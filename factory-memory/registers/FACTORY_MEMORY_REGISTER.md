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
| Issue label | Add `factory-memory-ingest` to an issue. | Uses the labeled issue as source evidence and opens a memory PR. |
| Issue comment | Comment `/factory-memory ingest` on an issue. | Uses the commented issue as source evidence and opens a memory PR. |

All trigger routes must keep human merge authority. Triggered memory records are proposed evidence until merged.

## Next register gap

Add a provider capability register for LLM usage caps, context limits, tool permissions, cost class, and approved work classes before claiming autonomous multi-LLM routing.
