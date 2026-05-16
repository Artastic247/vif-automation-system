# LIVE_OPERATIONAL_VALIDATION_REGISTER.md

## Purpose
Provide a controlled record for live operational validation evidence during CI pilots, onboarding pilots, validator pilots, release pilots and future governed operational execution.

## Scope
Applies to all live operational pilot activities.

## Owner/agent
QA Gatekeeper owns validation evidence review. System owner approves progression decisions.

## Inputs
Pilot execution evidence, runtime monitoring, workflow outputs, validator outputs, incident records, rollback evidence, KPI results and reviewer decisions.

## Activities/checklist
| Validation ID | Pilot/activity | Repo/branch | Workflow/validator | Expected behaviour | Actual behaviour | False PASS observed? | False BLOCK observed? | Rollback tested? | KPI result | Decision | Reviewer | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LOV-001 | Initial CI pilot | control-system repo | validation workflow | Reporting/gating only | Pending | Pending | Pending | Pending | Pending | Pending | QA Gatekeeper | Draft |

## Outputs/records
Operational validation evidence, escalation record, CAPA linkage, rollback evidence and management-review input.

## Maturity level
M4 required for governed operational validation. M5 requires repeatable stable operational evidence.

## Evidence required
Workflow run evidence, validator output, rollback evidence, reviewer sign-off and KPI review.

## Linked process
COP-11 Verification, COP-12 Validation/UAT, COP-14 Release and rollback, MOP-05 Internal audit, MOP-07 Corrective action and continual improvement.

## Linked agent/skill/procedure/module
QA Gatekeeper, GitHub Release Controller, Runtime Monitoring Procedure, Pilot Execution Procedure and CI Pilot Activation Procedure.

## Interface/control point
Interfaces with pilot governance, runtime monitoring, CAPA, audit programme, KPI review and management review.

## PASS/HOLD/BLOCKED rules
- PASS: operational behaviour stable and evidence complete.
- HOLD: warnings or incomplete evidence require review.
- BLOCKED: false PASS/BLOCK, rollback failure, uncontrolled behaviour or security/data risk.

## PDCA
- PLAN: define operational validation expectations.
- DO: execute controlled pilot.
- CHECK: review operational evidence and incidents.
- ACT: improve workflows, validators and governance.

## Audit frequency
Per pilot and during management review.

## Automation allowance
Operational validation does not authorise broader rollout automatically.

## Escalation
Escalate false PASS/BLOCK, rollback failure, uncontrolled behaviour or repeated instability.

## Update trigger
Pilot execution, workflow change, validator change, incident, CAPA or lesson learned.
