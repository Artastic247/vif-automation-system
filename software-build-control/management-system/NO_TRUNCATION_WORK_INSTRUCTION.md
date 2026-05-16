# NO_TRUNCATION_WORK_INSTRUCTION.md

## Purpose
Define how to preserve development context without relying on one giant prompt or fragmented chat memory, so release-critical details, decisions, evidence and exclusions are not lost.

## Scope
Applies to all AI-assisted app development, recovery, repair, review, verification, validation, release, rollout, management-system work and tool handoffs.

## Inputs
Current context pack, source-of-truth lock, current job card, latest gate decision, evidence pack, known defects, exclusions, tenant/environment context, rollback context, previous decisions and archive/reference records.

## Activities
1. Split context into stable artefacts instead of one giant prompt.
2. Carry forward decisions through APP_CONTEXT, CURRENT_JOB_CARD, VERIFICATION_REGISTER, RELEASE_REGISTER and relevant management-system records.
3. Mark old drafts, old chats, old ZIPs and old prompts as reference-only unless reconfirmed as source of truth.
4. Identify stale context by comparing repo, branch/version, commit, deployment, Supabase evidence, tenant evidence and latest gate decision.
5. Summarise only after preserving release-critical details: scope, exclusions, evidence, rollback, tenant risk, RLS/security risk, current gate and stop condition.
6. Before tool handoff, provide context pack plus current job card, not raw chat history only.
7. If context is too large, split by: app context, evidence, defects, UI map, runtime map, backend/RLS, tenant/release, lessons learned and prompt/tool route.
8. If conflict exists between artefacts, HOLD until source-of-truth lock is resolved.

## Outputs
Current context pack, stable artefact references, stale-context list, source-lock decision and prompt readiness decision.

## Records
APP_CONTEXT, CURRENT_JOB_CARD, PROMPT_REGISTER, SOURCE_OF_TRUTH_LOCK_PROCEDURE records, VERIFICATION_REGISTER, RELEASE_REGISTER, TENANT_ROLLOUT_REGISTER, LESSONS_LEARNED.

## Owner/tool
VIF Orchestrator owns context continuity. Prompt Quality Reviewer enforces no-truncation prompts. Codex Repo Inspector validates repo/current-state evidence. QA Gatekeeper verifies release-critical details are preserved.

## Linked process
COP-02 Source-of-truth and context lock, SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, SOP-12 Lessons learned and knowledge reuse.

## Linked gate
Context gate, baseline gate, prompt gate, evidence gate, release gate.

## PDCA
- PLAN: define context artefacts, source references, split strategy and required carry-forward details.
- DO: maintain stable artefacts and pass only current, controlled context into prompts/tools.
- CHECK: check for stale context, missing decisions, contradictions, scope drift and lost release-critical details.
- ACT: update context pack, source-lock records, job card, lessons learned, prompt library and validation rules.

## PASS/HOLD/BLOCKED rules
- PASS: context is current, split into stable artefacts, and release-critical details are preserved.
- HOLD: context has gaps but no implementation/release/data-risk action proceeds.
- BLOCKED: prompt/tool work relies on stale chat history, old drafts, old ZIPs, unknown branch/version or missing source lock.

## Update trigger
Long-running chat, tool handoff, new file upload, repo change, source conflict, truncation event, prompt failure, app repair, release/rollback, audit finding or lesson learned.
