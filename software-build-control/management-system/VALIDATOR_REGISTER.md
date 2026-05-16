# VALIDATOR_REGISTER.md

## Purpose
Provide a controlled inventory of validators/checks used by the Software Build Control System.

## Scope
Applies to all manual and automated validators.

## Owner/agent
QA Gatekeeper.

## Inputs
Validator definitions, scripts, reports, audit findings and CI plans.

## Activities/checklist
| Validator ID | Validator/check | Purpose | What it can prove | What it cannot prove | Current maturity | False PASS risk | False BLOCK risk | Owner | Review frequency | Automation allowance | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VAL-001 | Required artefact check | Confirm required files exist | Presence of required artefacts | Operational effectiveness | M3 | Medium | Low | QA Gatekeeper | Quarterly | No CI enforcement | Active |
| VAL-002 | Secret-risk check | Detect obvious secrets/API keys | Common secret patterns | All hidden credential paths | M3 | Medium | Medium | QA Gatekeeper | Quarterly | No CI enforcement | Active |
| VAL-003 | Forbidden-pattern check | Detect unsafe coding/prompt patterns | Known forbidden patterns | Runtime correctness | M2 | High | Medium | QA Gatekeeper | Per change | Pilot only | Active |

## Outputs/records
Validator inventory, maturity rating, review evidence and escalation references.

## Maturity level
Uses M0–M5 maturity model.

## Evidence required
Validator purpose, limitations, review evidence, false PASS/BLOCK assessment and owner approval.

## Linked process
SOP-05 Tool routing and tool qualification, SOP-07 Evidence and record control, MOP-05 Internal audit.

## Linked agent/skill/procedure/module
QA Gatekeeper, validator control procedure and maturity assessment.

## Interface/control point
Interfaces with validation scripts, CI activation governance, app onboarding and automation-readiness controls.

## PASS/HOLD/BLOCKED rules
- PASS: validator controlled and reviewed.
- HOLD: validator partially reviewed or immature.
- BLOCKED: validator uncontrolled or unsafe for intended use.

## PDCA
- PLAN: define validator scope.
- DO: execute validator.
- CHECK: review effectiveness.
- ACT: improve validator and controls.

## Audit frequency
Per validator review schedule and after failures.

## Automation allowance
Automation follows approved maturity only.

## Escalation
Escalate false PASS/BLOCK and uncontrolled validator drift.

## Update trigger
Validator change, CI change, audit finding or lesson learned.
