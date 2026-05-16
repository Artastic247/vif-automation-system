# WI_001_CONTEXT_LOCK

## Purpose
Lock the active app/project context before any design, build, review, validation, release, automation or repair work starts.

## Scope
All Software Build Management System work, including app builds, repairs, audits, validation alignment, prompt packets and management-system artefact updates.

## When to use
Use at the start of every job card, after new evidence is uploaded, when a repo/branch/commit changes, when a gate changes, or when there is risk of stale context or truncation.

## When not to use
Do not use as a substitute for requirements approval, runtime proof, validation/UAT, release approval or customer acceptance.

## Owner/agent
Context Management Specialist with VIF Orchestrator and QA Gatekeeper.

## Inputs
Project/app identity, current job card, current gate, source documents, latest commit/tree SHA, protected scope, exclusions, unresolved gaps, validation status, prior decisions and uploaded evidence.

## Method steps
1. Identify project/app and active repo.
2. Record current job card and gate.
3. Record source documents and evidence pack.
4. Record latest commit/tree SHA or mark SOURCE REQUIRED.
5. Record protected scope and explicit exclusions.
6. Record unresolved gaps and validation state.
7. Demote old drafts from active truth unless revalidated.
8. Check stale-context and truncation risk.
9. Confirm tool route and whether external validation is required.
10. Issue PASS/HOLD/BLOCKED context decision.

## Outputs/records
Context lock record, active source list, exclusions list, validation status note, stale-context risk note and gate decision.

## Evidence required
Repo/branch/commit or tree SHA, job card, source files, latest decisions, validation/report status and protected-scope confirmation.

## Linked ADP processes
ADP-01, ADP-02, ADP-05, ADP-10, ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 4 context, Clause 6 planning, Clause 7 documented information, Clause 8 operation, Clause 9 audit and Clause 10 improvement.

## Linked gates
Intake, context, source-of-truth, job-card, validation, release and improvement gates.

## Tools allowed
GitHub connector for file evidence, file-search for uploaded artefacts, local runtime/Codex for execution validation, ChatGPT for review and audit drafting.

## Tools prohibited
Any tool that modifies app repos, Supabase/RLS, deployment, app-repo CI or n8n while the protected scope is HOLD.

## Risks
Stale context, wrong repo, old draft used as truth, missing validation state, truncated history, protected-scope breach, false PASS.

## Controls
No work proceeds without current context. If repo/commit/source truth is unknown, gate remains HOLD or BLOCKED.

## Interfaces
VIF Orchestrator, GitHub Controller, QA Gatekeeper, Prompt Engineer, Evidence Auditor and Process Owner.

## PASS/HOLD/BLOCKED rules
PASS when active context, source, scope and gate are evidenced. HOLD when non-critical evidence is missing. BLOCKED when source truth, repo/branch, protected scope or validation state is unknown for risky work.

## Escalation
Escalate stale context, conflicting evidence, protected-scope conflict, missing source-of-truth or false PASS risk.

## MLA / maturity dependency
M1 allows controlled drafting. M2 requires pilot evidence. M3 requires released context discipline. M4/M5 require audited trend evidence and automation permission.

## Update trigger
New file, new decision, commit/tree change, gate change, validation result, audit finding or RCA/CAPA.
