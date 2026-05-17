# VALIDATOR_CALIBRATION_PROCEDURE

## Purpose
Define how validators/checks are created, reviewed, calibrated, updated, approved and used without creating false PASS risk.

## Scope
All validation scripts, manual checks, external-app scan profiles, CI workflow checks and future n8n workflow checks.

## Owner/agent
Validator/Checker Auditor with QA Gatekeeper.

## Inputs
Validator register, validation rule, target artefacts, test cases, expected PASS/HOLD/BLOCKED outcomes, FP/FN records, severity rules, linked gates and approval authority.

## Activities/method
Create validator with defined scope, select test cases, calibrate PASS/HOLD/BLOCKED logic, review false positives, review false negatives, update rules, approve changes, regenerate reports and determine when external runtime execution is required.

## Outputs/records
Calibration record, approved rule change, test-case result, regenerated report status and gate decision.

## Linked processes
Clause 9 performance evaluation, Clause 10 RCA/CAPA, validator calibration, app onboarding and automation governance.

## Linked skills/WIs
WI_017_VERIFICATION_REVIEW, WI_021_INTERNAL_AUDIT, WI_023_RCA, WI_024_CAPA_EFFECTIVENESS_REVIEW and WI_028_VALIDATOR_CALIBRATION.

## Linked gates
Validator release gate, evidence gate, external validation gate, app onboarding gate, CI/n8n readiness gates.

## Evidence required
Validator purpose/scope, selected test cases, expected vs actual result, FP/FN assessment, approval record and report regeneration evidence.

## Risks
Overbroad checks, missed critical finding, false PASS, false negative, noisy warnings, validation report trusted beyond scope.

## Controls
Validator output must be scoped. External runtime execution is required when file-system checkout, Python runtime, app runtime, build/test execution or real report generation is needed.

## Interfaces
Validator owner, Evidence Auditor, Internal Audit Specialist, RCA/CAPA Specialist, GitHub CI Controller, n8n Controller and QA Gatekeeper.

## Calibration method
1. Define validator purpose and scope.
2. Link validator to process, WI and gate.
3. Select positive PASS test case.
4. Select expected HOLD test case.
5. Select expected BLOCKED test case.
6. Include missing file and missing heading cases where applicable.
7. Include protected-scope breach and early onboarding/CI/n8n cases where applicable.
8. Run or manually review test cases according to tool capability.
9. Compare expected vs actual result.
10. Log false positives and false negatives.
11. Adjust severity logic only after approval.
12. Regenerate reports only in execution-capable environment.
13. Record whether external validation is required.

## External runtime execution required when
- Python validation scripts must be run.
- Reports must be regenerated.
- Full repo checkout is required.
- Build/lint/test/static scan is required.
- App runtime or database/RLS proof is required.
- GitHub Actions behaviour must be proven.
- n8n workflow execution must be proven.

## PASS/HOLD/BLOCKED rules
PASS when validator is calibrated and evidence supports use. HOLD when calibration/report execution is pending. BLOCKED when validator could enable false PASS for critical gates.

## Escalation
Escalate false negative, false PASS, unsafe severity downgrade, unapproved rule change or report claim without execution.

## MLA / maturity dependency
M1 draft validator; M2 pilot/manual review; M3 released after calibration; M4/M5 require review trend, low FP/FN and controlled automation permission.

## Update trigger
Validator change, new artefact class, failed test case, FP/FN, audit finding, RCA/CAPA, app onboarding or automation request.
