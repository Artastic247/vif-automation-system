# ESCALATION_RULES

## Purpose
Define escalation triggers and required actions for high-risk software-build failures.

## Scope
Repeated failed repairs, prompt drift, false PASS, missing evidence after gate, customer-data risk, RLS/security risk, blocked release, failed rollback, tool/provider failure, uncontrolled app change, AI output causing rework, ineffective CAPA, maturity overstated, interface/control-point failure, automation attempted before maturity permits it, validation-script false PASS, overdue audit finding and overdue management-review action.

## Owner/agent
QA Gatekeeper with RCA/CAPA Specialist and Management Review Owner.

## Inputs
NC records, audit findings, validator results, RCA/CAPA status, release status and maturity decisions.

## Activities/method
Classify escalation severity, assign owner, trigger containment, block unsafe gates, require RCA/CAPA, notify management review and verify closure.

## Outputs/records
Escalation record, blocked-gate decision and management-review action.

## Evidence required
Escalation trigger evidence, risk assessment, containment evidence and closure approval.

## Linked process
Clause 10 escalation control.

## Linked gate
Escalation and risk gate.

## MLA / maturity dependency
Unsafe automation or repeated ineffective control can downgrade maturity and block M3+ progression.

## Clause 9 input
Critical audit findings, MLA failures and validation failures.

## Clause 10 output
Blocked gate, RCA/CAPA requirement, management escalation and improvement action.

## PASS/HOLD/BLOCKED rules
PASS when escalation resolved with evidence. HOLD when escalation remains open. BLOCKED when critical risk is uncontrolled.

## Escalation
This file defines escalation criteria and routes.

## Management-review input
All critical escalations feed management review.

## Continual-improvement input
Escalation themes drive systemic-improvement priorities.

## Update trigger
Critical event, repeated failure, ineffective action or governance change.
