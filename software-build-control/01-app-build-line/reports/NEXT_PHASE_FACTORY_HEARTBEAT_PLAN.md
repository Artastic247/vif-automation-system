# NEXT PHASE — VIF FACTORY HEARTBEAT PLAN

## Purpose
Define the next implementation phase so the VIF factory behaves as a governed heartbeat: it evaluates maturity continuously, restricts unsafe automation, and triggers controlled improvement loops.

## Direct answer to coverage question
Coverage is partial. The current baseline includes smoke route automation, operator snapshot generation, and MLA HOLD gating, but it does not yet fully implement end-to-end closed-loop control for prompt engineering, hook maintenance/development, workflow management, and context lifecycle governance.

## Current status by domain

### Prompt engineering
- Present: prompt governance standards and audit checklists exist in management-system.
- Missing: executable prompt-quality gate integrated into app-build-line smoke route.

### Hook maintenance and development
- Present: workflow scripts and route commands exist.
- Missing: formal hook inventory with owner, test cadence, rollback proof, and break-glass controls linked to gate checks.

### Workflow management
- Present: route orchestration (`create-build-cards`, `run-task`, `verify-build`) and smoke workflow CI.
- Missing: event-driven workflow-state model with health SLIs/SLOs and escalation automation.

### Context development and management
- Present: context-pack standards and source-of-truth procedures in management-system.
- Missing: automated context freshness checks and source-lock validation in the smoke gate.

## Clause 4–10 conceptualisation into VIF factory heartbeat

### Clause 4 (Context)
Heartbeat control:
1. Validate context scope and source-of-truth lock before route start.
2. Block route when context provenance is missing.

### Clause 5 (Leadership)
Heartbeat control:
1. Enforce named decision owner on every gate decision.
2. Require explicit approval record for maturity overrides.

### Clause 6 (Planning)
Heartbeat control:
1. Require risk-linked plan for every automation change.
2. Auto-open HOLD when mitigation evidence is missing.

### Clause 7 (Support)
Heartbeat control:
1. Validate competence and assignment matrix for active agent/skill route.
2. Block release when required specialist assignment is absent.

### Clause 8 (Operation)
Heartbeat control:
1. Execute controlled route and verify protected-scope boundaries.
2. Record evidence artifacts for each operation cycle.

### Clause 9 (Performance evaluation)
Heartbeat control:
1. Run MLA assessment checkpoint at defined cadence and change triggers.
2. Apply permission matrix to cap automation actions by maturity.

### Clause 10 (Improvement)
Heartbeat control:
1. Convert failures/findings into RCA/CAPA actions.
2. Reassess maturity after CAPA effectiveness review; downgrade when required.

## MLA heartbeat behavior (adaptive control)
The factory must behave as an adaptive governor:
1. Assess maturity evidence.
2. Compare requested automation against permission matrix.
3. Permit only allowed actions.
4. If evidence drops or failures repeat, auto-downgrade gate to HOLD/BLOCKED.
5. Trigger improvement workflow (NC/RCA/CAPA).
6. Re-evaluate and re-open automation only after effectiveness proof.

## Implementation backlog (next 3 increments)

### Increment 1 — Prompt and context gates in smoke route
- Add prompt-quality and context-lock checks to CI workflow.
- Output machine-readable fail reasons into verification artifacts.

### Increment 2 — Hook registry and maintenance loop
- Add `HOOK_REGISTER.md` with owner/cadence/rollback fields.
- Add hook-health check script and CI enforcement.

### Increment 3 — Heartbeat orchestrator
- Add `factory_heartbeat.py` controller that:
  - runs route checks,
  - evaluates maturity permission,
  - emits PASS/HOLD/BLOCKED,
  - opens improvement-required status when downgrade triggers occur.

## Gate policy for self-development
Self-development is constrained learning, not autonomous unsafe change.
- Allowed: recommendation generation, draft control updates, evidence collation.
- Prohibited: auto-fix/auto-merge/auto-release or protected-scope mutation without maturity-permitted approval.

## Done criteria for this phase
- Clause 4–10 heartbeat controls mapped to executable checks.
- MLA checkpoint integrated into route.
- Downgrade triggers automatically change gate state.
- Improvement loop artifacts created when HOLD/BLOCKED occurs.
