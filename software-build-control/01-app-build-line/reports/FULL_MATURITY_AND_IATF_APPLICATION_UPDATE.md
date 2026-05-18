# FULL MATURITY + IATF-TYPE APPLICATION UPDATE

## Update intent
Provide a current-state update on:
1. the execution plan toward full maturity,
2. current maturity position,
3. IATF-type model application coverage for agent skills, hooks, workflows, intake, and new-product-introduction/project-management controls.

## Current maturity level (evidence-backed)
- Current decision remains: **M2 retained**.
- Automation permission remains: **sandbox/manual only**.
- Gate remains: **HOLD** for full-maturity claim.

Reason: full-maturity promotion evidence is not yet complete (required-check enforcement proof, fail/pass blocking proof, and rollback rehearsal evidence still required).

## Full-maturity plan status

### Completed implementation (already in place)
1. Smoke workflow for controlled route execution.
2. Prompt/context gate and artifact capture.
3. Operator panel snapshot generation for triage.
4. MLA assessment record and permission decision artifacts.
5. Clause-09 evidence structure remediated to pass validator.

### In-progress implementation (partial)
1. Heartbeat orchestration across Clause 4–10 controls.
2. Hook lifecycle maintenance control baseline implemented (register + CI check), effectiveness trending pending.
3. Workflow-state SLI/SLO + escalation automation.

### Remaining for full-maturity promotion
1. Branch protection evidence showing required smoke checks on protected branches.
2. Demonstrated merge-block on failing smoke run + release on passing run.
3. Rollback/disable rehearsal record with effectiveness verification.
4. Automated downgrade/recovery loop evidence (HOLD/BLOCKED -> CAPA -> reassessment).

## IATF-type model application (operational mapping)

| IATF-type control area | Current implementation status | Evidence posture |
|---|---|---|
| Agent skills and competence assignment | **Implemented (baseline)** via assignment/maturity matrices and specialist activation rules | Documented; needs periodic effectiveness trend evidence |
| Hook maintenance/development control | **Implemented (baseline) + Partial (advanced)** | Hook register and CI hook-health checks active; advanced cadence/effectiveness analytics pending |
| Workflow management | **Implemented (baseline) + Partial (advanced)** | Smoke CI + route controls active; event-state health SLIs/SLOs pending |
| Intake and context governance | **Implemented (baseline)** | Prompt/context checks active and artifacted; freshness automation needs expansion |
| NPI / project-management gating | **Partial** | Build-line planning and gated route active; full stage-gate pack with standardized NPI records pending |
| Performance evaluation + MLA governor | **Implemented (baseline)** | MLA decision and permission matrix applied; adaptive auto-downgrade automation pending |
| Improvement loop (Clause 10 CAPA) | **Partial** | Procedure and escalation exist; closed-loop effectiveness automation pending |

## Specific response to your implementation question
### Have these been implemented?
- **Agent skills:** implemented at baseline governance level; continue with trend/effectiveness evidence.
- **Hooks:** baseline implemented (register + enforced CI health checks); next is advanced trend analytics and escalation telemetry.
- **Workflows:** implemented for baseline smoke route; advanced telemetry/escalation still pending.
- **Intake/context management:** implemented baseline checks; broaden freshness/source-lock automation next.
- **New product introduction / project management:** partially implemented through app-build-line packet and gate model; full NPI stage-gate dossier is the next build item.


## Clarification — process controls vs quality aids
To confirm your point: some items listed in this update are **quality aids**, not mandatory core-process steps.

- **Core-process controls (required for gate decisions):** MLA permission matrix, protected-scope guardrails, required verification evidence, and PASS/HOLD/BLOCKED governance checks.
- **Quality aids (supporting output quality):** operator snapshot convenience view, additional telemetry summaries, and non-mandatory helper reports.

Rule applied: quality aids can improve consistency and speed, but they must not be treated as process-maturity evidence unless explicitly mapped to a required control in the management system.

## Next build sprint (recommended)
1. Add NPI stage-gate template set (intake, feasibility, design, verification, launch readiness, post-launch review).
2. Add heartbeat controller that evaluates MLA maturity + automation request and emits PASS/HOLD/BLOCKED with mandatory CAPA triggers.
3. Run one controlled fail/pass demonstration cycle and attach evidence packet for maturity-promotion review.
4. Add hook effectiveness trend + missed-cadence escalation metrics to close advanced hook maturity.

## Promotion criterion to claim “full automation maturity”
Do **not** claim full maturity until all four are evidenced:
1. Required check enforcement on protected branch,
2. fail-block/pass-release proof,
3. rollback rehearsal proof,
4. adaptive downgrade-and-recovery proof tied to MLA governance.
