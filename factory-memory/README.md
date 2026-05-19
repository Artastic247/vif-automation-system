# Factory Memory

Factory memory is the controlled knowledge store for the VIF factory.

It stores source chats, summaries, decisions, lessons learned, instructions, skills, agents, plugin packs, deployment notes, and registers that are intended to be reused by Codex, GPT, Claude, Copilot, workflows, and future LLM stations.

## Operating rules

- GitHub main is the source of truth.
- Memory records are not approved until merged by a human.
- AUTO-003 v1 is deterministic and does not perform LLM summarisation.
- Source chats and issues are evidence.
- Summary, decision, lesson, and skill-update records are proposed stubs until reviewed.
- Generated CI reports remain artifacts unless a workflow deliberately promotes a controlled memory record through PR review.

## Folder map

| Folder | Purpose |
|---|---|
| `chats/inbox/` | Raw chat, transcript, or issue evidence awaiting processing. |
| `chats/processed/` | Source evidence after review or routing. |
| `chats/summaries/` | Summary stubs or approved summaries. |
| `decisions/` | Decision records extracted from accepted evidence. |
| `lessons-learned/` | Reusable lessons linked to failure modes and verification methods. |
| `instructions/` | Controlled instructions for factory stations. |
| `skills/` | Skill update recommendations and accepted skill notes. |
| `agents/` | Agent and station role knowledge. |
| `plugins/` | Plugin-pack records and adapter notes. |
| `deployments/` | Deployment evidence and release notes when separately approved. |
| `registers/` | Registers that index memory assets and operating state. |
