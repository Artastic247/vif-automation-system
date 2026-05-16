# NONCONFORMITY_CONTROL_PROCEDURE.md

## Purpose
Define how nonconformities are identified, contained, classified, corrected, escalated and linked to RCA/CAPA, lessons learned, maturity assessment and management review.

## Scope
Applies to process failures, audit findings, evidence failures, validator/check failures, AI bad outputs, prompt failures, release/rollback failures, tool/provider failures, identity/contact-data findings, app onboarding findings and future app-specific nonconformities.

## Owner/agent
QA Gatekeeper owns nonconformity control. Process owners own containment and correction. RCA/CAPA Owner owns root cause and corrective action where required. System owner reviews critical escalations.

## Inputs
Audit findings, validation failures, evidence gaps, failed gates, AI bad-output records, prompt failure records, release issues, customer feedback, support issues, maturity overstatements and management-review actions.

## Activities/checklist
1. Identify and record the nonconformity.
2. Classify severity: observation, minor NC, major NC, critical/blocking NC.
3. Define immediate containment where risk exists.
4. Correct the immediate issue where possible.
5. Decide whether RCA/CAPA is required.
6. Link the issue to affected process, agent, skill, prompt, validator, tool, app/module, tenant, release or evidence record.
7. Escalate critical/blocking NCs to management review and stop affected work.
8. Verify correction and closure evidence.
9. Update lessons learned, maturity assessment and process records.

## Outputs/records
NC record, containment record, correction, RCA/CAPA trigger, owner assignment, closure evidence, effectiveness-review trigger and lesson learned.

## Maturity level
Maturity cannot increase while major/critical NCs remain open. M4/M5 require evidence that recurring NCs are prevented by effective CAPA.

## Evidence required
NC description, source, classification, evidence, containment, correction, owner, due date, RCA/CAPA decision, closure evidence and effectiveness-review requirement.

## Linked process
MOP-07 Corrective action and continual improvement, MOP-05 Internal audit, MOP-06 Management review, SOP-07 Evidence and record control, SOP-12 Lessons learned.

## Linked agent/skill/procedure/module
QA Gatekeeper, RCA/CAPA Owner, Process Engineer, Lessons Learned Controller, audit skill, RCA skill, CAPA skill, evidence-map skill and maturity assessment.

## Interface/control point
Interfaces with audit findings, evidence audit, AI bad-output monitoring, prompt failure register, validation reports, maturity assessment, management review and continual improvement.

## PASS/HOLD/BLOCKED rules
- PASS: NC is contained, corrected, classified, linked, closed with evidence and RCA/CAPA decision is justified.
- HOLD: NC is open but contained and does not create critical risk.
- BLOCKED: critical NC, false PASS, data/security risk, release risk, automation risk, missing containment or repeated NC without RCA/CAPA.

## PDCA
- PLAN: define NC classification and response rules.
- DO: contain, correct and assign NC.
- CHECK: verify correction and closure evidence.
- ACT: trigger RCA/CAPA, lessons learned, maturity change and process update.

## Audit frequency
Reviewed during internal audits, management review and RCA/CAPA status review.

## Automation allowance
Automation is blocked where open NCs affect the relevant process, validator, AI route, release route, tenant route, prompt family or interface/control point.

## Escalation
Escalate critical/blocking NCs, overdue NCs, repeated NCs, failed containment, false PASS, maturity overstatement and ineffective correction.

## Update trigger
Audit finding, failed validation, failed gate, AI/prompt failure, release issue, customer feedback, support issue, data/security concern or lesson learned.
