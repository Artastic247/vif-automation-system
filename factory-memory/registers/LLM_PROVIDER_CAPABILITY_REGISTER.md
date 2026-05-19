# LLM_PROVIDER_CAPABILITY_REGISTER

## Purpose

Control how VIF routes work across Codex, ChatGPT, Claude, Copilot, Cursor, Gemini, Ollama, and future LLM stations.

This register does not grant autonomous authority by itself. It defines what must be known before a provider can receive factory work.

## Routing rule

A provider may receive work only when all of these are known:

- approved work classes
- tool permissions
- repository access method
- context and usage limits
- cost or rate class
- handoff contract
- stop conditions
- evidence expected from the provider

If any item is unknown, the provider can assist only as an advisory station and must not be treated as an autonomous factory worker.

## Provider register

| Provider | Runtime type | Approved work classes | Tool permissions | Known limits | Factory state |
|---|---|---|---|---|---|
| Codex | Coding station | Repo inspection, scoped edits, PR creation, deterministic review, repair loops, factory-memory maintenance | GitHub connector or verified local checkout only | Depends on connected workspace, model limits, connector permissions, and repository access | Active for VIF automation repo |
| ChatGPT | Discussion and planning station | Requirements capture, transcript source evidence, architecture review, app-design discussion | No repo mutation unless paired with approved connector or exported issue | Chat context and tool availability vary by workspace | Advisory until routed through GitHub issue or memory ingest |
| Claude | Coding or review station | Draft implementation, review, document reasoning, alternative patch proposals | Must use approved repo adapter or PR comments | Usage caps and context limits vary by plan/platform | Candidate adapter; not approved as autonomous VIF worker yet |
| Copilot | IDE coding assistant | Local code suggestions and IDE refactors | Developer workstation only unless connected to repo workflow | Depends on IDE, org policy, and subscription | Candidate adapter; human-supervised only |
| Cursor | IDE coding station | Local implementation and refactor support | Verified local checkout only | Depends on model/provider settings and local repo access | Candidate adapter; human-supervised only |
| Gemini | Advisory or coding station | Research, review, alternative implementation advice | Must use approved connector or exported issue | Usage and context limits vary by plan/platform | Candidate adapter; not approved as autonomous VIF worker yet |
| Ollama | Local model station | Offline summarisation, classification, deterministic drafts where quality is verified | Local files only; no network or GitHub mutation unless separately wrapped | Hardware and model-dependent; quality varies by model | Candidate local advisory adapter |
| Future provider | Unknown | None until registered | None until registered | Unknown | Not approved |

## Work class definitions

| Work class | Description | Requires human merge |
|---|---|---|
| Advisory | Provides analysis, options, or review text without changing source. | Yes, before any source change is accepted. |
| Scoped edit | Changes declared files in one branch for one issue. | Yes. |
| Deterministic review | Runs explicit checks and reports PASS or HOLD. | Yes. |
| Repair loop | Fixes a HOLD or failed workflow within declared scope. | Yes. |
| Memory ingest | Converts approved issue or file evidence into factory-memory stubs. | Yes. |
| Skill update | Proposes or edits reusable skill instructions. | Yes. |
| Deployment | Releases or changes runtime infrastructure. | Not approved by this register. |
| Protected data mutation | Changes customer data, Supabase/RLS, secrets, or production records. | Not approved by this register. |

## Handoff contract

Each provider handoff must include:

- issue number or source record
- branch or PR target
- expected files
- forbidden paths
- validation required
- output format
- PASS/HOLD state
- next action

## Stop conditions

Stop provider routing when:

- repository access is unverified
- usage cap or cost boundary is unknown
- a provider cannot preserve branch/PR scope
- a provider cannot report changed files
- protected paths are requested without explicit approval
- auto-merge, deployment, Supabase/RLS, secrets, or customer data mutation is requested

## Current approval state

Codex is the active VIF factory station for this repository. Other providers are candidate adapters until a reviewed PR adds their adapter instructions, permissions, evals, and evidence requirements.
