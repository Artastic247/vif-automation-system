# WI_030_CI_N8N_READINESS_REVIEW

## Purpose
Assess readiness for Continual Improvement controls, GitHub Continuous Integration and n8n workflow automation without confusing their meanings or activating immature automation.

## Scope
Control-system CI pilot, app-repo GitHub CI, blocking validators, external app scans, n8n notification, n8n issue creation, n8n evidence collection and n8n auto-routing.

## When to use
Use before changing control-system CI, activating app-repo CI, designing n8n workflows or using automation to route evidence/actions.

## When not to use
Do not use to approve auto-fix, auto-merge or auto-release; these remain BLOCKED.

## Owner/agent
GitHub CI Controller and n8n Automation Controller with QA Gatekeeper and MLA Assessor.

## Inputs
Automation request, maturity level, validator calibration evidence, app onboarding status, authority matrix, issue templates, evidence schema, privacy/data rules, rollback/disable route and audit route.

## Method steps
1. Clarify CI meaning: Continual Improvement vs GitHub Continuous Integration.
2. Confirm current maturity and MLA permission.
3. Confirm validator calibration and evidence quality.
4. Confirm app onboarding status.
5. Confirm authority matrix and human approval points.
6. Assess control-system CI, app-repo CI and blocking validators.
7. Assess n8n notification, issue creation, evidence collection and auto-routing.
8. Confirm privacy/data and rollback/disable route.
9. Record HOLD/BLOCK/PASS decision for allowed scope only.

## Outputs/records
CI/n8n readiness record, maturity decision, HOLD/BLOCK conditions, escalation and next job card recommendation.

## Evidence required
MLA record, validator calibration, app onboarding evidence, workflow/CI design, authority matrix, privacy/evidence schema and disable/rollback route.

## Linked ADP processes
ADP-16, ADP-18, ADP-20 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 9 performance evaluation, Clause 10 continual improvement, automation governance and app onboarding.

## Linked gates
CI readiness gate, n8n readiness gate, automation permission gate, validator gate and app onboarding gate.

## Tools allowed
Manual/read-only control-system CI pilot, calibrated validators, readiness checklists, n8n design notes only when maturity permits.

## Tools prohibited
Auto-fix, auto-merge, auto-release, app-repo CI before onboarding, n8n before automation maturity, customer data in unapproved workflows.

## Risks
Confusing CI meanings, premature app-repo CI, automating immature process, n8n privacy risk, workflow creating false evidence, auto action risk.

## Controls
CI = Continual Improvement when used in Clause 10 context. GitHub CI = Continuous Integration. n8n = workflow automation. App-repo CI remains HOLD until app onboarding readiness passes. n8n remains HOLD until automation maturity gate passes. Auto-fix, auto-merge and auto-release are BLOCKED.

## Interfaces
QA Gatekeeper, MLA Assessor, GitHub CI Controller, n8n Controller, Validator Auditor, App Onboarding Owner, Security/Data Reviewer.

## PASS/HOLD/BLOCKED rules
PASS only for defined low-risk scope with evidence and approval. HOLD when readiness evidence is incomplete. BLOCKED for auto-fix, auto-merge, auto-release or automation before maturity.

## Escalation
Escalate premature CI/n8n request, privacy risk, uncalibrated validator reliance or auto-action attempt.

## MLA / maturity dependency
M1/M2 permits manual/read-only or design-only. M3+ may consider controlled CI. M4/M5 may consider limited automation only with evidence, audit route and rollback.

## Update trigger
CI/n8n request, validator calibration, app onboarding result, maturity change, audit finding or management-review action.
