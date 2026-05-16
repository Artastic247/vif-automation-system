# PILOT_KPI_REGISTER.md

## Purpose
Define and track pilot KPIs used to evaluate onboarding, release, validator, automation and operational readiness.

## Scope
Applies to all controlled pilots.

## Owner/agent
QA Gatekeeper owns KPI evidence. System owner reviews pilot KPI acceptance.

## Inputs
Pilot scope, pilot evidence, runtime monitoring, validation results, issue records and management-review criteria.

## Activities/checklist
| KPI ID | KPI | Purpose | Target | Warning threshold | Block threshold | Evidence source | Review frequency | Owner |
|---|---|---|---|---|---|---|---|---|
| KPI-001 | Validation stability | Confirm validators behave consistently | Stable/no false PASS | Minor warning trend | False PASS/critical drift | Validation reports | Per pilot cycle | QA Gatekeeper |
| KPI-002 | Rollback success | Confirm rollback route works | Successful rollback | Delayed rollback | Failed rollback | Rollback evidence | Per pilot | GitHub Release Controller |
| KPI-003 | Tenant isolation stability | Confirm no tenant exposure | No exposure | Minor isolation warning | Exposure/security event | Monitoring/audit evidence | Per pilot | Security/RLS Reviewer |
| KPI-004 | Pilot issue recurrence | Monitor repeated issues | Declining recurrence | Stable recurrence | Increasing recurrence | CAPA/issues | Weekly/pilot | QA Gatekeeper |
| KPI-005 | Runtime stability | Monitor runtime behaviour | Stable | Warning trend | Critical instability | Runtime monitoring | Per pilot | QA Gatekeeper |

## Outputs/records
Pilot KPI trend, escalation, pilot decision input and management-review input.

## Maturity level
M3+ requires KPI trend review and effectiveness linkage.

## Evidence required
KPI evidence, trend evidence, escalation evidence and reviewer approval.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, COP-12 Validation/UAT, COP-13 Tenant rollout.

## Linked agent/skill/procedure/module
QA Gatekeeper, GitHub Release Controller, Security/RLS Reviewer, Pilot Execution Procedure and Runtime Monitoring Procedure.

## Interface/control point
Interfaces with pilot governance, runtime monitoring, CAPA, maturity assessment and management review.

## PASS/HOLD/BLOCKED rules
- PASS: KPIs meet acceptance criteria.
- HOLD: warning thresholds reached or review incomplete.
- BLOCKED: block thresholds reached or critical KPI failure exists.

## PDCA
- PLAN: define KPI targets.
- DO: collect KPI evidence.
- CHECK: review KPI trends.
- ACT: escalate or improve based on KPI performance.

## Audit frequency
Per pilot cycle and during management review.

## Automation allowance
Automation pilots blocked when KPI block thresholds are reached.

## Escalation
Escalate KPI instability, false PASS, rollback failure, tenant risk or runtime instability.

## Update trigger
Pilot change, KPI failure, runtime issue, CAPA or lesson learned.
