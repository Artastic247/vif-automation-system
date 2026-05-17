# VALIDATOR_REVIEW_SCHEDULE

## Purpose
Define review cadence and trigger events for validators/checks.

## Scope
All validators/checks in the validator register.

## Owner/agent
Validator/Checker Auditor with QA Gatekeeper.

## Inputs
Validator register, maturity level, risk rating, FP/FN history, audit findings, script changes, artefact changes and automation-readiness requests.

## Activities/method
Set owner, review frequency, trigger review event, last reviewed, next review, evidence required, management-review input and status for each validator/check.

## Outputs/records
Validator review schedule, review evidence and management-review input.

## Linked processes
Clause 9 validator audit, Clause 10 continual improvement, app onboarding and automation governance.

## Linked skills/WIs
WI_021_INTERNAL_AUDIT, WI_022_MLA_ASSESSMENT, WI_028_VALIDATOR_CALIBRATION and WI_030_CI_N8N_READINESS_REVIEW.

## Linked gates
Validator review gate, maturity gate, automation permission gate and management-review gate.

## Evidence required
Review record, owner, date, test evidence, change evidence, FP/FN status and next review date.

## Risks
Stale validator, missed new artefacts, false negative not reviewed, automation using outdated checks.

## Controls
High-risk validators require event-based review after script change, false negative, protected-scope issue, app onboarding or automation request.

## Interfaces
Validator owners, Internal Audit Specialist, RCA/CAPA Specialist, GitHub CI Controller, n8n Controller and Management Review Owner.

## Review schedule table
| Validator/check | Owner | Review frequency | Trigger review event | Last reviewed | Next review | Required evidence | Management-review input | Status |
|---|---|---|---|---|---|---|---|---|
| Required artefact checker | Validator Auditor | Per release/change | Required artefact list changes | Pending | Pending | Test case results | Yes if critical gaps | HOLD |
| Template field checker | Validator Auditor | Per template change | Required heading changes | Pending | Pending | Heading test evidence | Yes if repeated gaps | HOLD |
| Evidence completeness checker | Evidence Auditor | Per validation cycle | Evidence rules change | Pending | Pending | Evidence test cases | Yes | HOLD |
| Clause 9 checker | Internal Audit Specialist | Per Clause 9 change | Audit/MLA artefact change | Completed previously | Next external validation | Validation report | Yes | PASS/HOLD context |
| Clause 10 checker | RCA/CAPA Specialist | Per Clause 10 change | Clause 10 artefact change | Pending | External validation | Validation report | Yes | HOLD |
| App-development checker | Process Engineer | Per operating-model change | ADP file change | Pending | External validation | Coverage test | Yes | HOLD |
| WI checker | Skill/WI Auditor | Per WI batch | WI file/heading change | Pending | External validation | WI coverage test | Yes | HOLD |
| Agent-assignment checker | VIF Orchestrator | Per agent batch | Agent matrix change | Pending | External validation | Agent coverage test | Yes | HOLD |
| Process-turtle checker | Process Engineer | Per turtle scope change | Turtle/support-matrix naming change | Pending | External validation | Corrected scope test | Yes | HOLD |
| Secret detector | Security/Data Reviewer | Per scan/profile change | Secret rule change or finding | Pending | External validation | Secret test fixture | Yes if BLOCKED | HOLD |
| Large-file detector | QA Gatekeeper | Per threshold change | Large-file warning trend | Pending | External validation | Threshold evidence | Trend only | HOLD |
| Forbidden-pattern detector | Security/Data Reviewer | Per pattern change | New prohibited pattern | Pending | External validation | Pattern fixture | Yes if BLOCKED | HOLD |
| GitHub Actions workflow check | GitHub CI Controller | Before CI change | Workflow changed | Pending | Before CI expansion | Workflow evidence | Yes | HOLD |
| Future n8n workflow check | n8n Controller | Before n8n work | n8n design/export exists | Not started | HOLD | Readiness evidence | Yes | HOLD |

## PASS/HOLD/BLOCKED rules
PASS when review is current and evidence complete. HOLD when review is due/pending. BLOCKED when stale validator may permit unsafe gate movement.

## Escalation
Escalate overdue high-risk review, false negative, validator used after disablement or automation request with stale validator.

## MLA / maturity dependency
M3+ validators require scheduled review. M4/M5 require trend review and management-review input.

## Update trigger
Validator change, artefact change, FP/FN, audit finding, validation run, app onboarding or automation request.
