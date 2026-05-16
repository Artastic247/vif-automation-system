# VALIDATOR_EFFECTIVENESS_REVIEW.md

## Purpose
Define how validator/check effectiveness is reviewed and how false PASS/false BLOCK conditions are controlled.

## Scope
Applies to all validators, checks, scripts and gate-support tools used in the Software Build Control System.

## Owner/agent
QA Gatekeeper owns effectiveness review. Process Engineer supports process alignment review. System owner approves automation-related effectiveness decisions.

## Inputs
Validator reports, audit findings, false PASS/BLOCK events, CI plans, maturity assessments, RCA/CAPA records and lessons learned.

## Activities/checklist
1. Review validator purpose and intended use.
2. Review recent validator outputs and findings.
3. Review whether known issues were detected.
4. Review false PASS and false BLOCK events.
5. Review whether validator drift occurred after process or script changes.
6. Review maturity level and automation allowance.
7. Decide effective, partially effective or ineffective.
8. Trigger RCA/CAPA where validator reliability is weak.

## Outputs/records
Validator effectiveness review, maturity adjustment, escalation, RCA/CAPA trigger and management-review input.

## Maturity level
M4/M5 validators require routine effectiveness review and trend analysis.

## Evidence required
Validator outputs, sampled failures, review evidence, trend review and reviewer approval.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement.

## Linked agent/skill/procedure/module
QA Gatekeeper, validator review skill, RCA/CAPA procedure and validator control procedure.

## Interface/control point
Interfaces with CI activation governance, automation-readiness review, audit programme and app onboarding.

## PASS/HOLD/BLOCKED rules
- PASS: validator effective for intended use.
- HOLD: additional monitoring or tuning required.
- BLOCKED: unresolved false PASS/BLOCK risk or uncontrolled validator drift.

## PDCA
- PLAN: define effectiveness expectations.
- DO: execute validator.
- CHECK: review effectiveness and drift.
- ACT: improve validator and governance.

## Audit frequency
Quarterly, after validator changes, before CI activation and after false PASS/BLOCK events.

## Automation allowance
No validator may support automation enforcement if effectiveness is HOLD or BLOCKED.

## Escalation
Escalate ineffective validators, false PASS/BLOCK events, uncontrolled drift and unsafe automation dependency.

## Update trigger
Validator change, audit finding, CI change, false PASS/BLOCK or lesson learned.
