# VALIDATOR_CONTROL_PROCEDURE.md

## Purpose
Define how validation scripts, checklists, gates and automated/manual checks are controlled so they remain suitable, accurate, effective and trusted before CI or automation activation.

## Scope
Applies to control-pack validators, script checks, evidence checks, prompt/context checks, identity/contact checks, AI-management checks, process-architecture checks, forbidden-pattern checks, secret-risk checks, large-file checks, future CI checks and future app-scan checks.

## Owner/agent
QA Gatekeeper owns validator control. Process Engineer owns validator-process alignment. System owner approves validator use for automation. Specialist owners review technical validators.

## Inputs
Validator inventory, validation reports, audit findings, false PASS/BLOCK events, script changes, process changes, CI plans, app-scan plans, lessons learned and management-review decisions.

## Activities/checklist
1. Register every validator/check.
2. Define validator purpose, scope and detection intent.
3. Define what the validator can and cannot prove.
4. Define expected PASS/HOLD/BLOCKED behaviour.
5. Define false PASS and false BLOCK risks.
6. Define test cases or review evidence for validator effectiveness.
7. Review validator after process, prompt, AI, identity, app-scan or CI changes.
8. Escalate failed validator effectiveness to RCA/CAPA.
9. Block CI/automation use where validators are not mature enough.

## Outputs/records
Validator inventory, calibration/effectiveness review, validator change record, false PASS/BLOCK record, audit finding and management-review input.

## Maturity level
M0/M1 validators are draft/manual only. M2 validators may be piloted. M3 validators may support controlled operational checks. M4 validators may support limited governed automation. M5 validators may be automation candidates with monitoring.

## Evidence required
Validator purpose, test/review evidence, last review date, false PASS/BLOCK assessment, owner approval, maturity rating and linked reports.

## Linked process
SOP-07 Evidence and record control, MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement, SOP-05 Tool routing and tool qualification.

## Linked agent/skill/procedure/module
QA Gatekeeper, Process Engineer, validator review skill, evidence-map skill, RCA/CAPA procedure, audit programme and maturity assessment.

## Interface/control point
Interfaces with validation scripts, CI activation governance, audit findings, RCA/CAPA, management review, app onboarding, release readiness and automation-readiness controls.

## PASS/HOLD/BLOCKED rules
- PASS: validator purpose, scope, evidence, maturity and review status support its intended use.
- HOLD: validator is useful but effectiveness, maturity or review evidence is incomplete.
- BLOCKED: validator has unresolved false PASS risk, uncontrolled change, missing owner, unclear scope or is used for automation before maturity approval.

## PDCA
- PLAN: define validator intent, risks, review method and maturity requirement.
- DO: run validator and collect output.
- CHECK: review effectiveness, false PASS/BLOCK risk and audit findings.
- ACT: update validator, raise RCA/CAPA, adjust maturity and lessons learned.

## Audit frequency
Per validator change, quarterly for active validators, before CI activation, and after any false PASS/BLOCK or major process change.

## Automation allowance
No validator may be used to support CI enforcement or automation unless it is at least M4 for limited automation or M5 as an automation candidate.

## Escalation
Escalate false PASS, false BLOCK, validator drift, unsupported automation use, missing evidence, stale validator logic or repeated validator failure.

## Update trigger
Validator change, CI plan, app-scan plan, false PASS/BLOCK, audit finding, process change, AI/prompt/identity control change, app onboarding or lesson learned.
