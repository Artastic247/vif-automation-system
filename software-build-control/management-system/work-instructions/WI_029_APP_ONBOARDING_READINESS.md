# WI_029_APP_ONBOARDING_READINESS

## Purpose
Check whether an app is ready to receive the Software Build Control System without risking customer data, app code, CI, release or automation drift.

## Scope
Any app repo considered for onboarding, including DOS FMEA, SPC, QMS, MSA, APQP, QCPro and future apps.

## When to use
Use before installing control pack, scanning app repo, activating app-repo CI, starting repair, or creating app-specific job cards.

## When not to use
Do not use as permission to repair the app or activate CI; those require separate gates.

## Owner/agent
VIF Orchestrator with QA Gatekeeper and App/Product Auditor.

## Inputs
App context pack, repo/branch/commit evidence, source-of-truth lock, validation profile, tenant/environment boundary, runtime-first status, release/rollback boundary, protected scope, app-repo CI HOLD rule and n8n HOLD rule.

## Method steps
1. Confirm app identity and owner.
2. Confirm repo/branch/commit.
3. Confirm source-of-truth lock.
4. Confirm app validation profile.
5. Confirm tenant/environment boundary.
6. Confirm demo vs production data boundary.
7. Confirm runtime-first status.
8. Confirm release/rollback boundary.
9. Confirm protected scope.
10. Confirm app-repo CI and n8n remain HOLD.
11. Decide onboarding PASS/HOLD/BLOCKED.

## Outputs/records
App onboarding readiness record, evidence register, risk gaps, HOLD/BLOCK conditions and next job card recommendation.

## Evidence required
App context pack, repo evidence, branch/commit, tenant/data boundary, validation profile, runtime status, release/rollback boundary and protected-scope statement.

## Linked ADP processes
ADP-01, ADP-02, ADP-06, ADP-09, ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 4 context, Clause 6 risk, Clause 8 operation, Clause 9 audit and Clause 10 improvement.

## Linked gates
App onboarding gate, source lock gate, risk gate, validation profile gate, CI readiness gate and n8n readiness gate.

## Tools allowed
GitHub evidence, context pack, read-only scans, validation profile, evidence register.

## Tools prohibited
App repo modifications, app-repo CI activation, n8n implementation, Supabase/RLS changes, customer-data access and release actions.

## Risks
Wrong repo, customer-data exposure, tenant leakage, premature CI/n8n, app repair starts before readiness, false onboarding PASS.

## Controls
App onboarding requires evidence before any app control-pack install, CI activation or repair work.

## Interfaces
App Owner, GitHub Controller, Security/Data Reviewer, Release Controller, CI Controller, n8n Controller, QA Gatekeeper.

## PASS/HOLD/BLOCKED rules
PASS when onboarding evidence is complete and protected scope controlled. HOLD when non-critical evidence pending. BLOCKED when repo/source/data/tenant boundary is unsafe or unknown.

## Escalation
Escalate customer-data risk, wrong repo/branch, protected-scope conflict, app-repo CI request or n8n request.

## MLA / maturity dependency
App onboarding requires adequate maturity of context, validators, WIs, agent assignments and risk controls; app-repo CI/n8n require later maturity gates.

## Update trigger
New app onboarding request, repo change, tenant/data change, risk finding, audit finding or management-review action.
