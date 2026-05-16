# RUNTIME_MONITORING_PROCEDURE.md

## Purpose
Define controlled runtime monitoring and post-release operational review so issues are detected, escalated and linked into RCA/CAPA, audit and continual-improvement governance.

## Scope
Applies to future pilot/production releases, workflow activation, validator activation, onboarding pilots and governed operational routes.

## Owner/agent
QA Gatekeeper owns monitoring review. GitHub Release Controller owns release-event linkage. System owner reviews critical runtime incidents.

## Inputs
Release records, runtime alerts, validator outputs, incident reports, user feedback, support issues, monitoring evidence, audit findings and KPI trends.

## Activities/checklist
1. Define monitoring scope and critical indicators.
2. Monitor release behaviour, validator behaviour and onboarding stability.
3. Record incidents, anomalies, failed gates, repeated warnings or tenant issues.
4. Escalate critical runtime conditions.
5. Trigger rollback where required.
6. Trigger RCA/CAPA and lessons learned.
7. Review post-release stability and maturity impact.

## Outputs/records
Runtime monitoring record, incident record, escalation record, rollback trigger, CAPA trigger and post-release review.

## Maturity level
M3 required for controlled operational monitoring. M4/M5 require trend analysis and recurring-issue prevention.

## Evidence required
Monitoring outputs, incident evidence, escalation evidence, rollback linkage and post-release review evidence.

## Linked process
COP-15 App support and maintenance, COP-14 Release and rollback, MOP-05 Internal audit, MOP-07 Corrective action and continual improvement.

## Linked agent/skill/procedure/module
QA Gatekeeper, GitHub Release Controller, RCA/CAPA Owner, runtime review skill and effectiveness-review procedure.

## Interface/control point
Interfaces with release governance, rollback governance, validator governance, CAPA, audit programme, KPI review and management review.

## PASS/HOLD/BLOCKED rules
- PASS: runtime stable and issues controlled.
- HOLD: monitoring indicates risk or instability under review.
- BLOCKED: critical runtime instability, repeated failures, tenant/data risk or failed rollback.

## PDCA
- PLAN: define monitoring indicators and escalation rules.
- DO: monitor runtime behaviour.
- CHECK: review incidents and trends.
- ACT: improve release, rollback and operational governance.

## Audit frequency
After release events, onboarding pilots, runtime incidents and during operational audits.

## Automation allowance
Monitoring may support alerts and reporting only; no autonomous production action allowed.

## Escalation
Escalate runtime instability, failed rollback, repeated release issues, tenant exposure or false PASS conditions.

## Update trigger
Release event, onboarding pilot, runtime incident, validator issue, audit finding or lesson learned.
