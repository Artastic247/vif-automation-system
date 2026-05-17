# WI_028_VALIDATOR_CALIBRATION

## Purpose
Control validator/check effectiveness so validation results are reliable and limitations are known.

## Scope
Required artefact checks, heading checks, evidence checks, Clause 9/10 checks, app-development operating-model checks, prompt/context checks, secret/large-file/forbidden-pattern checks, CI/n8n future checks.

## When to use
Use when creating, updating, reviewing, disabling or relying on any validation script/checker.

## When not to use
Do not use validator PASS as runtime proof, release proof or UAT proof unless the validator is designed for that evidence.

## Owner/agent
Validator/Checker Auditor with QA Gatekeeper.

## Inputs
Validator purpose, scope, test cases, expected PASS/HOLD/BLOCKED outputs, false-positive risk, false-negative risk, severity logic, review frequency, disable/rollback route, linked audit and RCA/CAPA history.

## Method steps
1. Define validator purpose and scope.
2. Define required test cases.
3. Test expected PASS case.
4. Test expected HOLD/BLOCKED cases.
5. Assess false-positive risk.
6. Assess false-negative risk.
7. Review severity logic.
8. Define review frequency.
9. Define disable/rollback route.
10. Link audit and RCA/CAPA if failed.

## Outputs/records
Validator calibration record, test-case evidence, FP/FN record, severity decision, review schedule and disable/rollback route.

## Evidence required
Validator file, test cases, test output, calibration result, issue log, rollback route and owner approval.

## Linked ADP processes
ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 9 validator audit, Clause 10 RCA/CAPA and continual improvement.

## Linked gates
Validator release gate, evidence gate, automation gate and maturity gate.

## Tools allowed
Python validation scripts, local runtime, CI pilot where manual/read-only, test fixtures and validation reports.

## Tools prohibited
Using uncalibrated validators to approve app onboarding, app-repo CI, n8n, release or auto actions.

## Risks
False PASS, false negative, overbroad warnings, disabled check without control, validator drift.

## Controls
Validator PASS must be scoped. False negatives trigger RCA/CAPA and calibration update.

## Interfaces
Validator Owner, Evidence Auditor, Internal Audit Specialist, RCA/CAPA Specialist, GitHub CI Controller.

## PASS/HOLD/BLOCKED rules
PASS when validator is tested and calibrated. HOLD when calibration evidence pending. BLOCKED when validator can enable unsafe false PASS.

## Escalation
Escalate false negative, false PASS, uncontrolled disablement or critical checker gap.

## MLA / maturity dependency
M2 pilot validators require manual review. M3 released validators require calibration. M4/M5 automation requires trend evidence.

## Update trigger
Validator change, missed finding, false positive, false negative, audit finding, automation request or management review.
