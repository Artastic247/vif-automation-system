# VALIDATOR_FALSE_POSITIVE_FALSE_NEGATIVE_REGISTER

## Purpose
Control validator false positives and false negatives so validation results improve and false PASS risk is contained.

## Scope
All validators/checks, validation reports, scan profiles, workflow checks and future n8n workflow checks.

## Owner/agent
Validator/Checker Auditor with RCA/CAPA Specialist and QA Gatekeeper.

## Inputs
Validator output, expected result, actual result, evidence, impact, root cause, correction, corrective action, owner, due date and effectiveness review.

## Activities/method
Record each suspected false positive or false negative, assess impact, contain false PASS risk, complete RCA/CAPA where required, update validator rules/test cases and verify effectiveness after use.

## Outputs/records
FP/FN finding record, correction, corrective action, validator update, effectiveness review and status.

## Linked processes
Clause 9 validator audit, Clause 10 NC/RCA/CAPA, validation-control, app onboarding, CI/n8n readiness and release control.

## Linked skills/WIs
WI_021_INTERNAL_AUDIT, WI_023_RCA, WI_024_CAPA_EFFECTIVENESS_REVIEW and WI_028_VALIDATOR_CALIBRATION.

## Linked gates
Validator calibration gate, evidence gate, app onboarding gate, release gate, CI/n8n gate and maturity gate.

## Evidence required
Finding ID, affected validator/check, FP/FN classification, evidence, impact, root cause, correction, corrective action, owner, due date, effectiveness review and closure status.

## Risks
False PASS, critical issue missed, blocked work due to noisy false positive, trust loss in validator, unsafe gate movement.

## Controls
False negatives affecting critical gates trigger BLOCKED until contained and corrected. False positives are reviewed without weakening critical safety checks prematurely.

## Interfaces
Validator Owner, Evidence Auditor, RCA/CAPA Specialist, QA Gatekeeper, Process Owner and Management Review Owner.

## FP/FN register fields
| Finding ID | Validator/check affected | False positive or false negative | Evidence | Impact | Root cause | Correction | Corrective action | Owner | Due date | Effectiveness review | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FP-FN-001 | To be assigned | FP/FN | Evidence required | Impact required | RCA required if significant | Correction required | CAPA if systemic | Owner required | Date required | Review required | OPEN |

## PASS/HOLD/BLOCKED rules
PASS when FP/FN is corrected and effectiveness is proven. HOLD when investigation or correction is open. BLOCKED when a false negative can permit unsafe PASS, release, onboarding, app-repo CI or n8n.

## Escalation
Escalate critical false negative, repeated false positive causing bypass pressure, unapproved severity downgrade, or ineffective corrective action.

## MLA / maturity dependency
Repeated FP/FN downgrades validator maturity. M3+ validators require controlled FP/FN review; M4/M5 require trend evidence.

## Update trigger
Any suspected FP/FN, failed validation, audit finding, false PASS, validator change or automation-readiness review.
