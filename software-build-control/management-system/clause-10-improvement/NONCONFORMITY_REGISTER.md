# NONCONFORMITY_REGISTER

## Purpose
Record and track all controlled nonconformities.

## Scope
All software-build, management-system, audit, validation, release, security/data, prompt, AI, agent, skill and automation nonconformities.

## Owner/agent
RCA/CAPA Specialist with finding owner.

## Inputs
NC trigger, evidence, affected artefacts, risk classification and gate impact.

## Activities/method
Maintain fields: NC ID, source, date, process affected, app/module affected, agent affected, skill/WI affected, procedure affected, workflow affected, validator/check affected, maturity level, requirement/gate breached, description, evidence, containment required, correction required, RCA required yes/no, CAPA required yes/no, owner, due date, linked audit finding, linked MLA assessment, linked lesson learned, status.

## Outputs/records
NC record, action tracking and closure status.

## Evidence required
Objective evidence, gate breach, owner decision, action evidence and closure evidence.

## Linked process
Clause 10 nonconformity control.

## Linked gate
NC register gate.

## MLA / maturity dependency
Open critical NCs can force maturity downgrade and block automation/onboarding/release.

## Clause 9 input
Audit findings, MLA findings, performance evaluation and validator findings.

## Clause 10 output
NC tracking, correction/RCA/CAPA route and improvement input.

## PASS/HOLD/BLOCKED rules
PASS when NC is closed with evidence. HOLD when actions are open. BLOCKED when critical NC lacks containment, owner or due date.

## Escalation
Escalate overdue, repeat, customer/security-impacting or false-PASS NCs.

## Management-review input
NC trend, age, recurrence and critical status feed management review.

## Continual-improvement input
NC patterns feed systemic improvement and lessons learned.

## Update trigger
New NC, containment update, RCA/CAPA decision, closure or recurrence.
