# AUDIT_PROGRAMME.md

## Purpose
Define the audit programme for the Software Build Control System so audits are planned, risk-based, maturity-based and linked to performance evaluation, RCA/CAPA, management review and continual improvement.

## Scope
Applies to all process audits, evidence audits, prompt audits, AI-output audits, release/rollback audits, tool/provider audits, validator/check audits and maturity audits.

## Owner/agent
QA Gatekeeper owns the audit programme. Process owners support audit evidence. System owner reviews audit priorities and escalations.

## Inputs
Process register, maturity level model, process risks, process KPIs, validation reports, prior findings, RCA/CAPA status, AI/prompt monitoring records, release/rollback records and management-review actions.

## Activities/checklist
| Audit type | Scope | Frequency rule | Owner | Required output |
|---|---|---|---|---|
| Process audit | MOP/COP/SOP process conformance and effectiveness | Risk/maturity based | QA Gatekeeper | Audit finding and action record |
| Evidence audit | Evidence supporting PASS decisions | Per high-risk gate/release or sample | QA Gatekeeper | Evidence audit result |
| Prompt audit | Prompt quality, source lock and forbidden patterns | Monthly/sample or after failure | Prompt Quality Reviewer | Prompt audit finding |
| AI-output audit | AI output verification and traceability | Per high-risk AI use/sample | AI Governance Owner | AI output audit record |
| Release audit | Release and rollback readiness | Before production release/pilot rollout | Release Controller | Release audit result |
| Tool/provider audit | Tool routing, provider limits and failures | Quarterly/change triggered | AI Governance Owner | Provider/tool review record |
| Validator/check audit | Validation script/check suitability and false PASS risk | Per validation change/quarterly | QA Gatekeeper | Validator audit record |
| Maturity audit | Maturity claim and automation allowance | Before maturity increase/automation | QA Gatekeeper | Maturity assessment result |

## Outputs/records
Audit programme, audit schedule, audit scope, audit results, findings, escalation records, RCA/CAPA links and management-review inputs.

## Maturity level
M0/M1 readiness review only; M2 audit after pilot/use; M3 periodic audit; M4 KPI/effectiveness audit; M5 optimisation and automation-readiness audit.

## Evidence required
Audit scope, criteria, sampled evidence, finding classification, owner response, due date, RCA/CAPA link where applicable and closure/effectiveness record.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement, SOP-07 Evidence and record control.

## Linked agent/skill/procedure/module
QA Gatekeeper, Process Engineer, Prompt Quality Reviewer, AI Governance Owner, Security/RLS Reviewer, audit skill, evidence-map skill and maturity assessment.

## Interface/control point
Interfaces with performance evaluation, internal audit procedure, audit findings register, management review, RCA/CAPA, maturity assessment and validation reports.

## PASS/HOLD/BLOCKED rules
- PASS: audit programme covers risk, maturity, process families, AI/prompt/evidence/release/tool/validator controls and assigns owners.
- HOLD: audit coverage exists but schedule, scope or owner detail is incomplete.
- BLOCKED: high-risk process, release, AI route, validator or automation candidate has no audit coverage.

## PDCA
- PLAN: define audit programme and audit criteria.
- DO: execute scheduled and trigger-based audits.
- CHECK: review findings, trends and audit coverage.
- ACT: update programme, raise RCA/CAPA, revise controls and escalate to management review.

## Audit frequency
Audit frequency is risk/maturity based and may increase after incidents, repeated findings, failed gates, release issues, AI failures or validator changes.

## Automation allowance
No automation increase is permitted unless audit coverage supports the relevant maturity level and no blocking findings remain open.

## Escalation
Escalate overdue audits, missing audit coverage, critical findings, repeated findings, maturity overstatement or automation candidate with weak audit evidence.

## Update trigger
New process, new tool, maturity change, automation request, app onboarding, audit finding, validation change, release issue, AI/prompt failure or management review.
