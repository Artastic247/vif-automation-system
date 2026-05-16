# VALIDATOR_CHECK_AUDIT_CHECKLIST

## Purpose
Audit validator/check effectiveness, calibration and operational limitations.

## Scope
Required-artifact checks, template checks, secret detection, forbidden-pattern checks, evidence completeness checks and future workflow validators.

## Owner/agent
Validator/Checker Auditor.

## Inputs
Validator register, test cases, false-positive/false-negative records, severity rules and validation reports.

## Activities/method
Audit validator purpose, owner, scope, test evidence, false-positive control, false-negative control, severity logic, maturity level, review frequency, disable/rollback route, linked audit and linked RCA/CAPA.

## Outputs/records
Validator audit result, calibration finding and improvement recommendation.

## Audit criteria
Validator PASS must not be overstated as operational proof.

## Evidence required
Validator outputs, test records, calibration evidence, review history and disable route.

## MLA / maturity dependency
Automation and onboarding readiness depend on validator maturity and audit evidence.

## Linked process
Validator calibration and Clause 9 validator audit.

## Linked gate
Validator release gate.

## PASS/HOLD/BLOCKED rules
PASS when validator limits and evidence are understood. HOLD when calibration evidence is incomplete. BLOCKED when validator false PASS can enable unsafe implementation or release.

## Escalation
Escalate false negatives, false PASS or uncontrolled severity logic.

## Management-review input
Validator failures and calibration trends feed management review.

## Update trigger
Validator update, failed detection, RCA/CAPA or audit finding.
