# WI_018_VALIDATION_UAT_REVIEW

## Purpose
Review whether the app/module fits user, operator, process-owner and customer needs before release.

## Scope
User acceptance criteria, process-owner validation, operator/user validation, role paths, tenant/data validation, release blocker classification, UAT evidence, sign-off and unresolved limitations.

## When to use
Use after verification PASS and before release/rollback review or app onboarding.

## When not to use
Do not use before technical verification or as approval for unresolved critical issues.

## Owner/agent
UAT Coordinator with Product/App Owner, Process Owner, Operator/User Tester and QA Gatekeeper.

## Inputs
Acceptance criteria, verified build, role paths, tenant/data test context, UAT script, user/operator feedback, limitation list and release blocker criteria.

## Method steps
1. Confirm user acceptance criteria.
2. Confirm process-owner validation scope.
3. Confirm operator/user validation where relevant.
4. Validate role paths.
5. Validate tenant/data boundaries.
6. Classify release blockers.
7. Capture UAT evidence.
8. Record sign-off/approval or rejection.
9. Record unresolved limitations and actions.

## Outputs/records
UAT review record, validation evidence, sign-off/approval, blocker list, limitation list and release readiness status.

## Evidence required
UAT script, user/process-owner feedback, screenshots/logs where useful, role/tenant test evidence, sign-off record and limitation record.

## Linked ADP processes
ADP-04, ADP-05, ADP-14, ADP-16, ADP-17 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 validation, Clause 9 performance evaluation and Clause 10 improvement.

## Linked gates
Validation/UAT gate, release readiness gate and improvement gate.

## Tools allowed
UAT script, verified build, test tenant/demo data where labelled, feedback records, sign-off register.

## Tools prohibited
Using mock UI or unverified build for final validation; using real customer data in unapproved tools.

## Risks
Process misfit, operator rejection, role path missed, tenant boundary missed, release with blockers, fake UAT.

## Controls
Validation requires user/process-owner evidence and blocker classification after verification.

## Interfaces
UAT Coordinator, Process Owner, Operator/User Tester, QA Gatekeeper, Release Controller.

## PASS/HOLD/BLOCKED rules
PASS when acceptance criteria and user/process-owner validation are met. HOLD when limitations are non-critical and controlled. BLOCKED when release blocker or data/tenant issue remains.

## Escalation
Escalate UAT failure, unresolved release blocker, customer-data risk or process-owner rejection.

## MLA / maturity dependency
M2 requires pilot validation evidence. M3 requires controlled release validation. M4/M5 require trend review and usability improvement.

## Update trigger
New UAT, changed workflow, user feedback, release request, failed validation or RCA/CAPA.
