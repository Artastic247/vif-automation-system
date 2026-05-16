# WI_014_DATABASE_RLS_PROOF

## Purpose
Prove backend persistence, role behaviour, RLS enforcement and tenant isolation before backend/security claims are accepted.

## Scope
Database tables, Supabase/RLS policies, RPC/edge routes, service functions, tenant-scoped queries, protected actions and audit/log evidence.

## When to use
Use before backend/RLS PASS, before release, after schema/RLS change, after migration, and during app onboarding readiness.

## When not to use
Do not use as permission to change production DB/RLS or access customer data outside approved scope.

## Owner/agent
Supabase/RLS Engineer with Security/Data Protection Specialist and QA Gatekeeper.

## Inputs
Schema/table design, tenant model, role model, RLS policies, backend functions, protected action list, test users/tenants, negative-path scenarios and audit/log requirements.

## Method steps
1. Prove backend read.
2. Prove backend write.
3. Prove role-allowed behaviour.
4. Prove role-denied behaviour.
5. Prove tenant-allowed behaviour.
6. Prove tenant-denied isolation.
7. Prove protected-action enforcement.
8. Capture audit/log evidence.
9. Execute negative paths.
10. Record backend/RLS gate decision.

## Outputs/records
Database/RLS proof record, backend read/write evidence, negative-path evidence, tenant isolation result and security finding if needed.

## Evidence required
Test data boundary, query/result evidence, role/tenant scenario evidence, audit/log evidence, negative-path result and rollback route.

## Linked ADP processes
ADP-08, ADP-09, ADP-11, ADP-13, ADP-16, ADP-17 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 operation/design/security control, Clause 9 security/data audit and Clause 10 NC/RCA/CAPA.

## Linked gates
Backend/RLS gate, security gate, verification gate, release gate and app onboarding gate.

## Tools allowed
Local/sandbox DB, Supabase project evidence, test tenants, controlled test users, logs, validation scripts.

## Tools prohibited
Production customer data access, service-role shortcuts, frontend-only proof, unapproved RLS/schema changes.

## Risks
Frontend-only security claim, tenant leakage, protected action bypass, missing negative tests, persistence claim without proof.

## Controls
No backend persistence or RLS claim without read/write, role, tenant and negative-path evidence.

## Interfaces
Backend Coder, Supabase/RLS Engineer, Security/Data Reviewer, QA Gatekeeper, Release Controller.

## PASS/HOLD/BLOCKED rules
PASS when read/write, role, tenant, protected-action and negative-path evidence pass. HOLD when proof is incomplete. BLOCKED when tenant/security risk or customer-data risk exists.

## Escalation
Escalate tenant leakage, RLS bypass, service-role misuse, missing negative path or production-data exposure.

## MLA / maturity dependency
M2 requires sandbox proof. M3 requires released backend/RLS proof. M4/M5 require monitoring and audit trends.

## Update trigger
Schema/RLS change, backend function change, role/tenant change, security finding, release request or RCA/CAPA.
