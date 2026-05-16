# EFFECTIVENESS_REVIEW_PROCEDURE.md

## Purpose
Define how corrections, CAPA actions, process changes, validator changes, prompt updates, AI governance changes and improvement actions are reviewed for effectiveness.

## Scope
Applies to RCA/CAPA actions, audit actions, management-review actions, validator changes, prompt/process updates, AI governance updates, release corrections and maturity-improvement actions.

## Owner/agent
QA Gatekeeper owns effectiveness review. Process owners provide evidence. RCA/CAPA Owner coordinates review of corrective actions.

## Inputs
CAPA records, audit findings, KPI trends, validation reports, AI bad-output records, prompt failure records, release incidents, lessons learned and maturity assessments.

## Activities/checklist
1. Confirm the intended outcome of the action.
2. Review post-action evidence.
3. Review whether recurrence has been prevented.
4. Review whether unintended consequences occurred.
5. Review KPI trend and audit trend.
6. Review maturity impact and automation allowance.
7. Decide effective, partially effective or ineffective.
8. Escalate ineffective actions to additional RCA/CAPA or management review.

## Outputs/records
Effectiveness-review result, escalation decision, maturity update, revised CAPA or lesson learned.

## Maturity level
M4/M5 require routine effectiveness review and trend verification.

## Evidence required
Action evidence, trend evidence, audit results, KPI evidence, recurrence review and reviewer approval.

## Linked process
MOP-07 Corrective action and continual improvement, MOP-06 Management review, MOP-05 Internal audit.

## Linked agent/skill/procedure/module
QA Gatekeeper, RCA/CAPA Owner, Lessons Learned Controller, effectiveness-review skill and maturity assessment.

## Interface/control point
Interfaces with RCA/CAPA, audit findings, management review, validators, AI governance, prompts and lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: action effective and recurrence risk reduced.
- HOLD: more monitoring required.
- BLOCKED: action ineffective, recurrence continues or new critical risk introduced.

## PDCA
- PLAN: define expected result.
- DO: implement action.
- CHECK: review effectiveness.
- ACT: escalate or improve further.

## Audit frequency
Per CAPA/action review cycle and management-review cycle.

## Automation allowance
Automation expansion blocked where effectiveness is not proven.

## Escalation
Escalate ineffective CAPA, repeated failures, false PASS, maturity overstatement and unstable release conditions.

## Update trigger
CAPA closure, audit finding closure, validator update, AI/prompt update, release correction or management-review decision.
