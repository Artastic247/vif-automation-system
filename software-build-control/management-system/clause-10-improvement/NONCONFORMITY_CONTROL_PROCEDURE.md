# NONCONFORMITY_CONTROL_PROCEDURE

## Purpose
Control software-build nonconformities so failures are contained, corrected, analysed and prevented from recurring.

## Scope
Audit findings, MLA failures, maturity overstatement, false PASS, missing evidence, failed build/test/deployment/rollback, prompt drift, AI bad output, customer-data risk, RLS/security risk, CI/n8n workflow failure, agent out-of-scope action, skill/WI failure, validator false negative, repeated app repair failure and release blocked by missing evidence.

## Owner/agent
RCA/CAPA Specialist with QA Gatekeeper, Internal Audit Specialist and affected process owner.

## Inputs
Audit finding, MLA result, validation report, incident, failed gate, defect evidence, security/data alert, release/rollback failure, prompt/tool failure.

## Activities/method
Identify NC source, classify risk, contain issue, define correction, decide RCA/CAPA need, assign owner, link evidence, update registers, escalate if high risk, and verify closure.

## Outputs/records
Nonconformity register entry, correction record, RCA/CAPA trigger, containment evidence and management-review input.

## Evidence required
Source evidence, breached gate/control, containment action, correction proof, RCA/CAPA decision and closure evidence.

## Linked process
Clause 10 nonconformity and corrective action.

## Linked gate
NC containment and correction gate.

## MLA / maturity dependency
Major or repeat NCs can downgrade maturity and block automation, onboarding, release or CI/n8n expansion.

## Clause 9 input
Audit finding, MLA failure, validation failure, evidence audit finding, release audit finding, CI pilot finding.

## Clause 10 output
Controlled NC, correction, RCA/CAPA trigger, effectiveness-review requirement and learning update.

## PASS/HOLD/BLOCKED rules
PASS when contained and closure evidence exists. HOLD when correction/RCA/CAPA is open. BLOCKED when high-risk NC lacks containment or owner.

## Escalation
Escalate customer-data risk, security/RLS risk, false PASS, failed rollback, maturity overstatement, repeated failure or overdue action.

## Management-review input
Critical, repeated, overdue or systemic NCs feed management review.

## Continual-improvement input
NC trends feed improvement backlog, lessons learned and validator/procedure updates.

## Update trigger
Any NC trigger source, audit finding, failed gate or repeated issue.
