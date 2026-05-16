# WI_016_MIGRATION_REPLAY_ROLLBACK_SAFETY

## Purpose
Review database migrations for replay safety, rollback/correction route, destructive-change risk and dependency control before execution or release.

## Scope
All database migrations, schema changes, RLS/helper changes, seed changes and corrective migrations.

## When to use
Use before creating, applying, reviewing, validating or releasing migrations, especially when DELETE, DROP, ALTER, RLS or helper dependencies are involved.

## When not to use
Do not use to approve production schema/RLS changes without controlled environment proof and approval.

## Owner/agent
Supabase/RLS Engineer with Release/Configuration Controller and Security/Data Reviewer.

## Inputs
Migration purpose, migration file, dependency list, destructive statements, RLS/helper dependencies, test environment, backup status, rollback/corrective migration route and approval need.

## Method steps
1. Confirm migration purpose and scope.
2. Check replay safety/idempotency risk.
3. Identify destructive statements: DELETE, DROP, ALTER and irreversible updates.
4. Check RLS/helper/function dependency.
5. Confirm test environment proof.
6. Confirm backup requirement.
7. Define rollback or corrective migration route.
8. Confirm approval before high-risk migration.
9. Stop if destructive risk is uncontrolled.
10. Record gate decision.

## Outputs/records
Migration safety review, destructive-risk finding, rollback/corrective route, approval record and test evidence.

## Evidence required
Migration file, test-run proof, dependency evidence, backup evidence, rollback/corrective migration plan, approval record and residual risk.

## Linked ADP processes
ADP-08, ADP-09, ADP-11, ADP-13, ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 8 design/change control, Clause 9 release/security audit and Clause 10 RCA/CAPA.

## Linked gates
Backend/RLS, migration, verification, release and rollback gates.

## Tools allowed
Sandbox/local DB, migration runner, Supabase CLI where approved, diff/review tools, backup evidence, test logs.

## Tools prohibited
Unapproved production migration, destructive migration without backup/rollback, customer data access, app-repo CI migration execution while HOLD.

## Risks
Migration replay failure, data loss, RLS breakage, helper mismatch, unrollbackable change, production outage.

## Controls
Destructive migration risk creates HOLD/BLOCK until backup, test proof and rollback/corrective route exist.

## Interfaces
Backend Coder, Supabase/RLS Engineer, Security/Data Reviewer, Release Controller, QA Gatekeeper.

## PASS/HOLD/BLOCKED rules
PASS when replay/test/rollback evidence exists. HOLD when evidence incomplete. BLOCKED when destructive migration risk is uncontrolled or customer data is exposed.

## Escalation
Escalate destructive change, failed migration, RLS/helper breakage, missing backup or rollback failure.

## MLA / maturity dependency
M2 requires sandbox migration proof. M3 requires released migration control. M4/M5 require trend review and rollback drills.

## Update trigger
New migration, schema/RLS/helper change, failed replay, release request, rollback issue or audit finding.
