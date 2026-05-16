# INTERNAL_AUDIT_PROCEDURE.md

## Purpose
Define the internal audit process for evaluating whether the Software Build Control System is implemented, effective, evidence-based, process-led and suitable for controlled AI-assisted software development.

## Scope
Applies to all MOP, COP and SOP processes; app onboarding later; prompt controls; AI controls; identity/contact controls; validation scripts; evidence records; release/rollback controls; tenant rollout controls; RCA/CAPA and continual improvement interfaces.

## Owner/agent
QA Gatekeeper owns the internal audit process. Process Engineer supports process-based audit planning. Specialist reviewers support technical audit areas. System owner reviews audit escalation.

## Inputs
Process register, process interaction map, process KPIs, maturity level model, audit programme, audit checklist, validation reports, gate records, evidence records, AI/prompt/contact findings, prior audit findings and lessons learned.

## Activities/checklist
1. Define audit objective, scope, criteria and process route.
2. Select audit type: process audit, evidence audit, release audit, AI-output audit, prompt audit, tool/provider audit or maturity audit.
3. Confirm process maturity level and risk before setting audit depth.
4. Audit process inputs, activities, outputs, records, KPIs, risks, controls, gates, interfaces and PDCA.
5. Verify evidence against claims.
6. Record findings as conformity, opportunity, observation, minor NC, major NC or critical/blocking NC.
7. Escalate critical findings to containment and RCA/CAPA.
8. Feed results into management review, maturity assessment and lessons learned.

## Outputs/records
Audit plan, audit checklist, audit evidence, audit finding, escalation record, management-review input and linked RCA/CAPA where required.

## Maturity level
Audit depth is maturity-based. M0/M1 are audited for readiness. M2 is audited after pilot/use. M3 receives periodic process audit. M4 receives effectiveness and KPI audit. M5 receives optimisation and automation-readiness audit.

## Evidence required
Audit checklist, sampled evidence, finding classification, process owner response, containment need, RCA/CAPA linkage and closure/effectiveness evidence.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement, SOP-07 Evidence and record control, SOP-12 Lessons learned.

## Linked agent/skill/procedure/module
QA Gatekeeper, Process Engineer, AI Governance Owner, Prompt Quality Reviewer, Security/RLS Reviewer, audit skill, evidence-map skill, maturity-level assessment and RCA/CAPA procedure.

## Interface/control point
Interfaces with performance evaluation, management review, RCA/CAPA, maturity model, validation scripts, AI/prompt monitoring, release readiness and lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: audit scope, evidence, finding classification and follow-up actions are complete.
- HOLD: audit evidence or owner response is incomplete, but no critical unsafe condition exists.
- BLOCKED: critical finding, false PASS, data/security risk, automation overreach, missing evidence or uncontrolled protected process requires containment before continuation.

## PDCA
- PLAN: define programme, scope, criteria and audit depth.
- DO: conduct audit and collect evidence.
- CHECK: classify findings and verify evidence adequacy.
- ACT: initiate containment, RCA/CAPA, lessons learned, process updates and management review.

## Audit frequency
Risk/maturity based and defined in AUDIT_PROGRAMME.md.

## Automation allowance
Audit results may support automation-readiness decisions only when maturity, CAPA effectiveness, validation evidence and management review support it. Audit alone does not activate CI or n8n.

## Escalation
Escalate critical/blocking findings, repeated findings, ineffective CAPA, maturity overstatement, release-risk evidence gaps, AI false PASS or data/security concerns.

## Update trigger
New audit programme, audit finding, app onboarding, process change, validation failure, release issue, AI/prompt issue, management review or lesson learned.
