# RCA_CAPA_PROCEDURE.md

## Purpose
Define the root cause analysis (RCA) and corrective/preventive action (CAPA) process used to eliminate causes of nonconformities, prevent recurrence, improve process effectiveness and strengthen governance maturity.

## Scope
Applies to repeated failures, major/critical NCs, false PASS events, AI bad outputs, prompt drift, validator failures, release failures, tenant/security risks, ineffective controls, repeated audit findings and maturity overstatements.

## Owner/agent
RCA/CAPA Owner owns the RCA/CAPA process. Process owners support investigation and implementation. QA Gatekeeper verifies evidence and effectiveness. System owner reviews critical/systemic CAPA.

## Inputs
Nonconformity records, audit findings, validation failures, AI bad-output records, prompt failure records, KPI trends, release incidents, customer feedback, support incidents and management-review escalations.

## Activities/checklist
1. Confirm containment and risk control.
2. Define the problem statement and scope.
3. Gather evidence and affected process/interface details.
4. Perform root cause analysis.
5. Define corrective action(s).
6. Define preventive action(s) where systemic risk exists.
7. Assign owners and due dates.
8. Implement actions.
9. Verify effectiveness and recurrence prevention.
10. Update process, skill, prompt, validator, lesson learned, maturity assessment and records where required.

## Outputs/records
RCA report, CAPA plan, implementation evidence, effectiveness review, escalation decision, maturity update and lessons learned.

## Maturity level
M4/M5 require demonstrated effective CAPA and recurrence prevention. Repeated ineffective CAPA may reduce maturity.

## Evidence required
Problem statement, root cause evidence, action plan, implementation evidence, effectiveness review, recurrence check and linked records.

## Linked process
MOP-07 Corrective action and continual improvement, MOP-05 Internal audit, MOP-06 Management review, SOP-12 Lessons learned.

## Linked agent/skill/procedure/module
RCA/CAPA Owner, QA Gatekeeper, Process Engineer, Lessons Learned Controller, RCA skill, CAPA skill, audit skill, evidence-map skill and maturity assessment.

## Interface/control point
Interfaces with nonconformity control, audit findings, management review, maturity model, AI governance, prompt governance, validators and continual improvement.

## PASS/HOLD/BLOCKED rules
- PASS: root cause identified, actions implemented, effectiveness verified and recurrence risk reduced.
- HOLD: actions in progress or effectiveness review pending.
- BLOCKED: root cause unknown, ineffective CAPA, repeated failure, false PASS risk or unresolved critical issue.

## PDCA
- PLAN: define RCA scope and CAPA actions.
- DO: implement corrective/preventive actions.
- CHECK: verify effectiveness and recurrence prevention.
- ACT: update governance, maturity, prompts, skills, validators and lessons learned.

## Audit frequency
Reviewed during audit follow-up, management review and effectiveness-review cycles.

## Automation allowance
Automation maturity cannot increase while critical CAPA actions remain open or ineffective.

## Escalation
Escalate ineffective CAPA, repeated failures, overdue actions, systemic risks, false PASS and automation-risk conditions.

## Update trigger
NC escalation, audit finding, repeated failure, AI/prompt issue, validator failure, release issue, customer complaint or management-review decision.
