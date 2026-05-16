# WI_015_PROTECTED_ACTION_BACKEND_ENFORCEMENT

## Purpose
Verify that protected actions are enforced at backend/service/RPC/edge/RLS level, not only by frontend disabled or hidden controls.

## Scope
Approve, release, delete, deactivate, supersede, submit, import, export, assign role, change tenant, change configuration and other protected actions.

## When to use
Use during runtime design, backend review, code review, verification, release review and app onboarding readiness.

## When not to use
Do not use to approve protected actions where only frontend hiding/disabled state exists.

## Owner/agent
Runtime Architect with Supabase/RLS Engineer, Security/Data Reviewer and QA Gatekeeper.

## Inputs
Protected action list, role matrix, tenant matrix, backend/RPC/edge/RLS enforcement route, frontend action state, negative test cases and audit evidence.

## Method steps
1. List protected actions.
2. Define role allowed and role denied.
3. Define tenant allowed and tenant denied.
4. Identify enforcement route: backend service, RPC, edge function or RLS.
5. Confirm frontend disable is not the control.
6. Execute allowed and denied tests.
7. Capture audit evidence.
8. Escalate if only UI enforcement exists.
9. Record gate decision.

## Outputs/records
Protected-action enforcement record, negative-test evidence, role/tenant decision and escalation if required.

## Evidence required
Protected-action matrix, backend/RLS evidence, allowed/denied test evidence, audit logs and code review notes.

## Linked ADP processes
ADP-06, ADP-08, ADP-09, ADP-11, ADP-13, ADP-16 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 operational control, Clause 9 security/evidence audit and Clause 10 NC/RCA/CAPA.

## Linked gates
Runtime, backend/RLS, security, verification and release gates.

## Tools allowed
Backend tests, RLS tests, RPC/edge function evidence, audit logs, role/tenant scenarios.

## Tools prohibited
Frontend-only disable/hidden controls as final enforcement proof; service-role bypass without controlled test justification.

## Risks
Unauthorized action, tenant breach, false protection claim, audit gap, destructive action without lifecycle rule.

## Controls
Protected action requires backend-enforced allow/deny proof and audit evidence.

## Interfaces
Runtime Architect, Backend Coder, Supabase/RLS Engineer, Security/Data Reviewer, QA Gatekeeper.

## PASS/HOLD/BLOCKED rules
PASS when backend enforcement and negative tests pass. HOLD when some evidence pending. BLOCKED when only UI enforcement exists or denied path succeeds.

## Escalation
Escalate frontend-only enforcement, denied action success, tenant bypass, destructive action risk or missing audit trail.

## MLA / maturity dependency
M2 requires pilot enforcement proof. M3 requires released enforcement evidence. M4/M5 require monitoring and audit trends.

## Update trigger
New protected action, role/tenant change, backend/RLS change, failed test, audit finding or release request.
