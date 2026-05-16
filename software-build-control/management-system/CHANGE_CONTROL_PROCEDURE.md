# CHANGE_CONTROL_PROCEDURE.md

## Purpose
Control internal, customer, defect, emergency, design, backend, schema, RLS, tenant rollout, release, and rollback changes so app work does not bypass impact review, approval, verification, or customer/UAT evidence.

## Scope
Applies to all app-development changes across new builds, defects, enhancements, refactors, releases, recovery work, and support. This procedure does not authorise app-code, Supabase, RLS, or deployment work without an approved job card.

## Inputs
- Change request, defect, incident, customer request, or internal improvement.
- App/module, repo, branch, environment, tenant, and version evidence.
- Expected behaviour, actual behaviour, evidence, risk, rollback, and validation needs.

## Activities/checklist
- Classify change: new build, defect, enhancement, refactor, release, recovery, emergency, backend/RLS, tenant rollout, or maintenance.
- Confirm source of truth and current branch/version.
- Identify affected UI, tables, workflows, runtime objects, database, RLS, tenants, reports, exports, and integrations.
- Define scope in, scope out, prohibited changes, owner, evidence, verification, validation/UAT, and rollback.
- Approve or reject change.
- Create CURRENT_JOB_CARD only after approval.
- Verify, validate, release, close, and update lessons learned.

## Outputs/records
CUSTOMER_CHANGE_REGISTER, CHANGE_BACKLOG, CURRENT_JOB_CARD, VERIFICATION_REGISTER, TENANT_ROLLOUT_REGISTER, RELEASE_REGISTER, LESSONS_LEARNED.

## Owner/tool
Change owner with VIF Orchestrator. Customer/business owner approves customer impact. Codex/GitHub validates repo evidence. Supabase Backend Reviewer validates backend/RLS impact.

## Gate controlled
Change-control and customer-change gates.

## PASS/HOLD/BLOCKED rules
- PASS: classification, impact, approval, scope, verification, validation, and rollback are clear.
- HOLD: evidence is incomplete but change is not active.
- BLOCKED: change touches app code, schema/RLS, customer data, deployment, release, or tenant exposure without approval/evidence.

## Update trigger
Every change request, defect, customer request, emergency fix, release, rollback, or maintenance change.
