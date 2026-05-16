# PILOT_EXECUTION_PROCEDURE.md

## Purpose
Define controlled pilot execution so app changes, validator enforcement, CI workflows, release routes, tenant rollouts or automation pilots are proven in a contained environment before broader rollout.

## Scope
Applies to controlled pilots for app onboarding, app repair, release engineering, CI activation, validator enforcement, tenant rollout, workflow automation and future n8n routes.

## Owner/agent
VIF Orchestrator owns pilot route. QA Gatekeeper owns pilot evidence and gate review. System owner approves pilot start and closure. Security/RLS Reviewer approves tenant/data/security scope.

## Inputs
Approved pilot job card, onboarding evidence, environment/tenant governance, release scope, rollback route, pilot KPI set, risk assessment, open NC/CAPA status, validation readiness and human approval.

## Activities/checklist
1. Define pilot objective, scope, success criteria and exclusions.
2. Confirm pilot environment and tenant/data boundary.
3. Confirm rollback and containment route.
4. Confirm pilot KPIs and evidence requirements.
5. Confirm open NC/CAPA and maturity status.
6. Approve pilot start.
7. Execute pilot under monitoring.
8. Record issues, containment actions and KPI evidence.
9. Decide pilot PASS/HOLD/BLOCKED.
10. Approve rejection, repeat, limited rollout or transition to production-readiness review.

## Outputs/records
Pilot plan, pilot approval, pilot evidence, KPI results, issue/containment records, pilot decision and transition recommendation.

## Maturity level
Pilot execution is normally M2. M3 requires stable controlled operational use. M4/M5 require trend evidence and managed optimisation.

## Evidence required
Pilot job card, environment/tenant evidence, rollback evidence, KPI results, monitoring evidence, issue log, decision record and post-pilot review.

## Linked process
COP-13 Tenant rollout, COP-14 Release and rollback, COP-11 Verification, COP-12 Validation/UAT, MOP-05 Internal audit, MOP-07 Corrective action and continual improvement.

## Linked agent/skill/procedure/module
VIF Orchestrator, QA Gatekeeper, Security/RLS Reviewer, GitHub Release Controller, Pilot KPI Register, Runtime Monitoring Procedure, Rollback Execution Procedure and Release Engineering Procedure.

## Interface/control point
Interfaces with app onboarding, environment/tenant governance, CI activation governance, release governance, rollback governance, runtime monitoring, CAPA, KPI review and management review.

## PASS/HOLD/BLOCKED rules
- PASS: pilot met success criteria, evidence is complete, issues are contained/closed and rollout recommendation is justified.
- HOLD: pilot evidence or issue resolution incomplete; no broader rollout allowed.
- BLOCKED: pilot exposes tenant/data/security risk, failed rollback, failed critical KPI, uncontrolled defect, false PASS or unresolved critical NC/CAPA.

## PDCA
- PLAN: define pilot scope, KPIs, containment and rollback.
- DO: execute pilot under control.
- CHECK: review evidence, KPIs, incidents and risks.
- ACT: accept, reject, repeat, improve or transition to next controlled stage.

## Audit frequency
Per pilot, after blocked pilot, before transition to wider rollout and during management review.

## Automation allowance
Pilot automation is allowed only where maturity, validator effectiveness, rollback and human approval support it. No autonomous release or protected action is allowed.

## Escalation
Escalate failed pilot, failed rollback, critical KPI miss, tenant/data exposure, unresolved NC/CAPA, uncontrolled automation behaviour or repeated pilot failure.

## Update trigger
New pilot request, pilot issue, KPI failure, rollback event, release issue, CI pilot, tenant rollout, management-review decision or lesson learned.
