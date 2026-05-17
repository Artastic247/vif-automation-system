# VALIDATOR_TEST_CASE_REGISTER

## Purpose
Define required validator test cases so validation behaviour is predictable and false PASS is prevented.

## Scope
All validators in the validator register, including management-system, app-development, work-instruction, agent, process-turtle, security, CI and n8n checks.

## Owner/agent
Validator/Checker Auditor.

## Inputs
Validator register, severity rules, artefact requirements, protected scope, expected outcomes and known failure modes.

## Activities/method
Create test cases for expected PASS, expected HOLD, expected BLOCKED, missing file, missing heading, incomplete evidence, false PASS prevention, protected-scope breach, early app onboarding, early app-repo CI, early n8n, auto-fix/merge/release, customer-data/secret exposure and runtime-validation unavailable.

## Outputs/records
Validator test-case register, expected result, actual result placeholder and calibration status.

## Linked processes
Clause 9 validation, Clause 10 improvement, app onboarding, CI/n8n readiness and security/data control.

## Linked skills/WIs
WI_017_VERIFICATION_REVIEW, WI_020_MOCK_DEMO_DATA_BOUNDARY, WI_028_VALIDATOR_CALIBRATION, WI_029_APP_ONBOARDING_READINESS and WI_030_CI_N8N_READINESS_REVIEW.

## Linked gates
Validation, evidence, app onboarding, app-repo CI, n8n, release and security gates.

## Evidence required
Test case ID, validator/check, input condition, expected outcome, actual outcome, test evidence and status.

## Risks
Untested BLOCKED logic, false PASS, runtime unavailable but reported as PASS, protected-scope breach not detected.

## Controls
Every validator must include PASS, HOLD and BLOCKED-path test cases where applicable.

## Interfaces
Validator owner, QA Gatekeeper, Evidence Auditor, Security/Data Reviewer, CI/n8n Controllers.

## Test case register
| Test case ID | Scenario | Expected result | Applies to validators/checks | Evidence required | Status |
|---|---|---|---|---|---|
| TC-001 | Complete artefact set with required headings | PASS | Artefact/template/process/WI/agent/turtle checks | Sample compliant files | Defined |
| TC-002 | Non-critical warning only | PASS_WITH_WARNINGS | Large-file/forbidden-pattern where configured warning | Warning report | Defined |
| TC-003 | Missing required file | HOLD | Required artefact, Clause 9/10, ADP, WI, agent, turtle | Missing-file fixture | Defined |
| TC-004 | Missing required heading | HOLD | Template field checker, WI/agent/procedure checks | Missing-heading fixture | Defined |
| TC-005 | Incomplete evidence | HOLD | Evidence completeness, verification, release | Incomplete evidence record | Defined |
| TC-006 | False PASS prevention | BLOCKED/HOLD | All critical validators | Known-bad case | Defined |
| TC-007 | Protected-scope breach | BLOCKED | Scope/security/CI/n8n/app scans | Protected-scope breach fixture | Defined |
| TC-008 | App onboarding attempted early | BLOCKED/HOLD | App onboarding, operating model, validation coverage | Onboarding request without evidence | Defined |
| TC-009 | App-repo CI attempted early | BLOCKED | GitHub Actions workflow check, CI readiness | App CI workflow/approval gap | Defined |
| TC-010 | n8n attempted early | BLOCKED | Future n8n workflow check | n8n design/export without maturity | Defined |
| TC-011 | Auto-fix attempted | BLOCKED | CI/n8n/workflow checks | Auto-fix indicator | Defined |
| TC-012 | Auto-merge attempted | BLOCKED | CI/GitHub workflow checks | Auto-merge indicator | Defined |
| TC-013 | Auto-release attempted | BLOCKED | CI/release workflow checks | Release automation indicator | Defined |
| TC-014 | Customer-data exposure | BLOCKED | Secret/data/external app scan | Customer-data risk evidence | Defined |
| TC-015 | Secret exposure or .env | BLOCKED | Secret detector | .env/secret fixture | Defined |
| TC-016 | Runtime validation unavailable | HOLD | External validation/report generation | Runtime-unavailable note | Defined |
| TC-017 | Process-turtle misuse of non-process artefact | HOLD/BLOCKED | Corrected process-turtle checker | Misnamed support matrix fixture | Defined |
| TC-018 | Interface/KPI support matrix correctly framed | PASS | Corrected process-turtle checker | Correctly named support matrices | Defined |
| TC-019 | Backend/RLS proof missing for backend claim | BLOCKED/HOLD | Evidence/backend/RLS checks | Backend claim without proof | Defined |
| TC-020 | Unsupported compliance/customer-facing claim | BLOCKED | Standards-control checker | Claim without source/approval | Defined |

## PASS/HOLD/BLOCKED rules
PASS when test case confirms intended behaviour. HOLD when test not executed. BLOCKED when critical scenario is missing or fails unsafe.

## Escalation
Escalate failed BLOCKED-path test, runtime unavailable but reported PASS, or untested high-risk validator.

## MLA / maturity dependency
M2 validators require defined test cases. M3 requires executed calibration evidence. M4/M5 require periodic review and trend evidence.

## Update trigger
New validator, new failure mode, false positive, false negative, audit finding or automation request.
