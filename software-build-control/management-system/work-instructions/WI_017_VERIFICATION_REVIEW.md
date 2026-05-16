# WI_017_VERIFICATION_REVIEW

## Purpose
Review whether build and technical evidence proves that specified requirements and controls were implemented correctly before validation or release.

## Scope
Build output, lint output, unit tests, integration tests, validation scripts, static scans, file-change scope, evidence currency, false PASS risk and remaining limitations.

## When to use
Use after build/review/test execution and before UAT, release, app onboarding or PASS claim.

## When not to use
Do not use as substitute for user/process-owner validation or release approval.

## Owner/agent
QA Gatekeeper with Evidence Auditor and Test Owner.

## Inputs
Job card, change set, build logs, lint output, test output, validation-script output, static scan output, file-change list, evidence records and known limitations.

## Method steps
1. Confirm file-change scope matches job card.
2. Review build output.
3. Review lint output.
4. Review unit test output.
5. Review integration test output.
6. Review validation-script output.
7. Review static scan/security/forbidden pattern output.
8. Confirm evidence currency.
9. Identify false PASS risk.
10. Record remaining limitations and gate decision.

## Outputs/records
Verification review record, evidence gap list, limitation list, PASS/HOLD/BLOCKED decision and validation readiness.

## Evidence required
Current logs/reports, commit/diff, test results, scan results, verification register and limitation record.

## Linked ADP processes
ADP-12, ADP-13, ADP-14, ADP-15, ADP-16, ADP-17 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 verification, Clause 9 evidence audit and Clause 10 NC/RCA/CAPA.

## Linked gates
Review, test, verification, validation readiness and release gates.

## Tools allowed
Build/lint/test runners, static scans, validation scripts, GitHub diff, evidence register.

## Tools prohibited
Claiming PASS from stale logs, mock data, UI-only screenshots or unrun scripts.

## Risks
False PASS, stale evidence, untested path, scope mismatch, hidden security issue, validation without verification.

## Controls
Verification must use current evidence tied to the commit/change set and job card.

## Interfaces
Builder, Reviewer, Test Owner, Evidence Auditor, QA Gatekeeper, UAT Coordinator.

## PASS/HOLD/BLOCKED rules
PASS when evidence proves implementation against scope. HOLD when non-critical evidence pending. BLOCKED when build/test/security evidence fails or is missing for critical scope.

## Escalation
Escalate false PASS risk, failed build/test, stale evidence, protected-scope modification or unverified backend/RLS claim.

## MLA / maturity dependency
M2 requires pilot verification evidence. M3 requires released verification records. M4/M5 require trend analysis and validator calibration.

## Update trigger
New build, test failure, validation-script change, audit finding, release request or RCA/CAPA.
