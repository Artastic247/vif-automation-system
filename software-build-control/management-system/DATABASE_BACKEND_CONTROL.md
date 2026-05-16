# DATABASE_BACKEND_CONTROL.md

## Purpose
Control database design, backend behaviour, RLS, tenant isolation, protected actions, migrations, demo data, and backend evidence before any backend claim, schema change, or release.

## Scope
Applies to database schema, ERD/data maps, migrations, RLS policies, tenant_id rules, roles, RPCs, edge functions, audit logs, seeded demo data, dev/staging/prod separation, migration rollback/corrective migration, backend reads/writes, and protected actions.

## Inputs
- RUNTIME_MAP and WORKFLOW_MAP.
- Database/schema evidence, migration files, RLS policies, Supabase project/environment evidence.
- Tenant model, user roles, protected actions, audit/evidence requirements.
- Rollback/corrective migration route.

## Activities/checklist
Before backend, DB, or RLS work, confirm:

- Data model/ERD exists or is explicitly scoped.
- Every customer/business table has tenant ownership rules where multi-tenant.
- tenant_id or equivalent tenant boundary is defined.
- User roles and permissions are defined.
- Protected actions are enforced below the UI.
- RLS policy intent is defined and evidenced.
- RPC/edge function use is justified and reviewed.
- Audit logs/evidence records are defined.
- Demo/seed data is separated from real customer data.
- Dev/staging/prod environment separation is defined.
- Migration replay and rollback/corrective migration route are considered.
- Backend read and write proof is required before PASS.

Rules:
- No schema change without RUNTIME_MAP.
- No backend claim without read/write proof.
- No frontend-only security claim.
- No customer data in dev unless explicitly approved and sanitised.
- No destructive migration without approved contingency and rollback route.

## Outputs/records
DATABASE_BACKEND_CONTROL record, RUNTIME_MAP, RLS/backend evidence, migration review, rollback route, verification register entry, and release/tenant rollout impact note.

## Owner/tool
Supabase Backend Reviewer owns backend/RLS evidence. Security/RLS Reviewer owns security and tenant risk. Codex Repo Inspector reviews migrations/code. QA Gatekeeper controls verification evidence.

## Gate controlled
Database/backend/RLS gate and protected-action gate.

## PASS/HOLD/BLOCKED rules
- PASS: database design, tenant rules, roles, RLS/protected actions, audit evidence, read/write proof, and rollback route are defined.
- HOLD: evidence incomplete but no backend/schema/release action proceeds.
- BLOCKED: schema/RLS/protected action/customer-data/release change is attempted without evidence or rollback.

## Update trigger
Schema change, RLS change, protected-action change, migration, Supabase issue, data exposure risk, tenant rollout, release, incident, or lesson learned.
