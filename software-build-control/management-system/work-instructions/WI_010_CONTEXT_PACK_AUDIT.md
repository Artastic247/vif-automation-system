# WI_010_CONTEXT_PACK_AUDIT

## Purpose
Audit context packs to ensure they contain current app identity, source truth, job card, gate state, decisions, gaps and protected boundaries.

## Scope
All context packs used for app development, reviews, repairs, audits, validation alignment, app onboarding and automation readiness.

## When to use
Use before major prompts, build tasks, validation alignment, app onboarding, release decisions or whenever context may be stale/truncated.

## When not to use
Do not use as a replacement for runtime validation, UAT, release approval or customer acceptance.

## Owner/agent
Context Pack Auditor with Context Management Specialist.

## Inputs
Context pack, app identity, repo/branch/commit, current job card, current gate, source basis, latest decisions, unresolved gaps, protected-scope boundary, no-truncation handling and old draft list.

## Method steps
1. Verify app/project identity.
2. Verify repo/branch/commit or tree SHA.
3. Verify current job card and gate.
4. Verify source basis and latest decisions.
5. Verify unresolved gaps and validation status.
6. Verify protected-scope boundary.
7. Check stale context and truncation risk.
8. Check old drafts are demoted or marked superseded.
9. Confirm no customer-data/secrets included unless approved.
10. Issue PASS/HOLD/BLOCKED decision.

## Outputs/records
Context-pack audit result, missing-context finding, source-lock update or escalation.

## Evidence required
Context pack, repo/commit evidence, job card, gate decision, source list, gap list, protected-scope statement and superseded-draft note.

## Linked ADP processes
ADP-02, ADP-05, ADP-10, ADP-11, ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 4 context, Clause 7 documented information/knowledge, Clause 8 operation, Clause 9 context-pack audit and Clause 10 improvement.

## Linked gates
Context-pack, source-lock, prompt, build, verification, release and improvement gates.

## Tools allowed
File-search, GitHub evidence, context registers, job cards, validation reports and evidence registers.

## Tools prohibited
Relying on memory, stale chats, old drafts, uncited files or unsupported assumptions as active context.

## Risks
Wrong app identity, wrong repo/branch, stale decision, unresolved gap hidden, protected scope touched, no-truncation failure.

## Controls
Context pack must show active truth and demoted old drafts. Missing critical context creates HOLD or BLOCKED.

## Interfaces
VIF Orchestrator, Prompt Engineer, GitHub Controller, Evidence Auditor, QA Gatekeeper and Knowledge Controller.

## PASS/HOLD/BLOCKED rules
PASS when context pack is current and complete. HOLD when non-critical items are pending. BLOCKED when repo/source/gate/protected boundary is unknown for risky work.

## Escalation
Escalate stale-context use, source conflict, hidden gap, wrong branch/repo or protected-scope uncertainty.

## MLA / maturity dependency
M1 context packs require review. M2 pilot packs require evidence. M3 released packs require audit. M4/M5 require trend review and automation readiness.

## Update trigger
New evidence, commit/branch change, job-card change, gate change, audit finding, RCA/CAPA or lessons learned.
