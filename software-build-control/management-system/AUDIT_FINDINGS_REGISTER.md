# AUDIT_FINDINGS_REGISTER.md

## Purpose
Record, classify, control and close audit findings from process audits, evidence audits, prompt audits, AI-output audits, release audits, maturity audits, validator audits and tool/provider audits.

## Scope
Applies to all audit findings raised against MOP, COP and SOP processes, management-system artefacts, app onboarding later, validators, prompts, AI controls, identity/contact-data controls, release/rollback controls and automation-readiness controls.

## Owner/agent
QA Gatekeeper owns the audit findings register. Process owners own containment and correction. RCA/CAPA Owner owns corrective action when required. System owner reviews critical and overdue findings.

## Inputs
Audit result, sampled evidence, process owner response, finding classification, maturity level, risk impact, containment need and linked records.

## Activities/checklist
| Finding ID | Audit type | Process/module | Finding statement | Classification | Evidence | Risk/maturity impact | Containment required | Correction | RCA/CAPA required? | Owner | Due date | Status | Effectiveness check | Linked lesson |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AF-001 | TBD | TBD | TBD | Observation / Minor NC / Major NC / Critical NC | TBD | TBD | Yes/No | TBD | Yes/No | TBD | TBD | Open | TBD | TBD |

## Outputs/records
Audit finding record, containment decision, correction, RCA/CAPA trigger, owner response, closure evidence and effectiveness check.

## Maturity level
Findings may reduce maturity where evidence, repeatability, effectiveness or interface control is weak. Maturity increase is blocked while major/critical findings remain open.

## Evidence required
Objective evidence, sampled record, finding classification, owner, due date, containment decision, closure evidence and effectiveness check.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement, SOP-07 Evidence and record control, SOP-12 Lessons learned.

## Linked agent/skill/procedure/module
QA Gatekeeper, RCA/CAPA Owner, Process Engineer, Lessons Learned Controller, audit skill, evidence-map skill, RCA skill and maturity assessment.

## Interface/control point
Interfaces with internal audit, performance evaluation, management review, RCA/CAPA, maturity assessment, lessons learned and validation reports.

## PASS/HOLD/BLOCKED rules
- PASS: finding is classified, owned, corrected, closed with evidence and effectiveness verified where required.
- HOLD: finding is open but contained and does not create critical risk.
- BLOCKED: critical finding, false PASS, data/security risk, release risk, automation overreach, maturity overstatement or missing containment.

## PDCA
- PLAN: define finding classification and response rules.
- DO: record and assign finding.
- CHECK: verify correction, closure and effectiveness.
- ACT: trigger RCA/CAPA, lessons learned, process update, validator update or management review escalation.

## Audit frequency
Reviewed per audit and during performance evaluation/management review. Overdue major/critical findings reviewed at each control-system review point.

## Automation allowance
Automation is blocked where major/critical findings affect the relevant process, validator, AI route, prompt family, release route or interface/control point.

## Escalation
Escalate overdue finding, repeat finding, ineffective correction, missing evidence, critical NC, false PASS, maturity overstatement or blocked automation condition.

## Update trigger
New audit finding, owner response, containment action, closure evidence, RCA/CAPA action, management review or lesson learned.
