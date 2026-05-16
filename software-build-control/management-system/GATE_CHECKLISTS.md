# GATE_CHECKLISTS.md

## Purpose
Provide practical gate checklists for controlled app development from intake through release, rollback, lessons learned, and automation readiness.

## Scope
Applies to every gate used by the Software Build Control System. These checklists support decisions but do not authorise app-code, Supabase, RLS, deployment, n8n, customer-data, or release work without approved evidence.

## Inputs
- Current app context and source-of-truth evidence.
- Relevant maps, job cards, verification, validation, tenant rollout, rollback, release, and lessons records.

## Activities/checklist
For each gate confirm entry evidence, checklist questions, PASS/HOLD/BLOCKED condition, and required records.

| Gate | Entry evidence | Checklist questions | PASS condition | HOLD condition | BLOCKED condition | Required records |
|---|---|---|---|---|---|---|
| Intake | Request/evidence | App? problem? users? repo? branch? data? gate? | Target and evidence clear | Non-critical evidence missing | Source/data/destructive risk unclear | APP_INTAKE_CHECKLIST |
| Baseline | Repo/branch/version | Correct repo? current branch? live/ZIP mismatch? | Source locked | Partial source evidence | Wrong/unknown baseline | APP_CONTEXT |
| UI/screen | SCREEN_MAP | Routes/tabs/panels/states/actions defined? | UI complete enough to build | Minor visual gaps | UI build without screen map | SCREEN_MAP |
| Data table/grid | DATA_TABLE_SPEC | Columns/sources/edit/validation/export defined? | Table spec complete | Minor gaps | Table build without spec | DATA_TABLE_SPEC |
| Workflow | WORKFLOW_MAP | Actors/states/actions/exceptions/approvals defined? | Workflow clear | Missing exception detail | Protected action undefined | WORKFLOW_MAP |
| Runtime/backend | RUNTIME_MAP | Object/state/action/backend/evidence mapped? | Runtime proof defined | Backend evidence missing | UI-only runtime claim | RUNTIME_MAP |
| Database/RLS | DATABASE_BACKEND_CONTROL | tenant_id, roles, RLS, migrations, audit, rollback defined? | Backend/RLS controlled | Evidence incomplete | Schema/RLS/customer-data risk | DATABASE_BACKEND_CONTROL |
| Job card | CURRENT_JOB_CARD | Scope in/out, tools, verification, rollback, stop condition? | Bounded job approved | Inputs missing | Feature creep/unbounded work | CURRENT_JOB_CARD |
| Build | Approved job card | Files match scope? prohibited areas untouched? | Build within scope | Build failed | Out-of-scope/protected file changed | Job card + diff |
| Verification | VERIFICATION_REGISTER | Build/lint/test/backend/manual checks evidenced? | Evidence passes | Partial evidence | Critical check failed | VERIFICATION_REGISTER |
| Validation/UAT | UAT criteria | User/customer fit-for-use accepted? | UAT accepted | UAT pending | UAT rejected | UAT record |
| Tenant rollout | TENANT_ROLLOUT_REGISTER | tenant type, exposure, pilot, rollback approved? | Tenant exposure controlled | Tenant evidence incomplete | Real tenant risk uncontrolled | TENANT_ROLLOUT_REGISTER |
| Release | RELEASE_REGISTER | Verification, rollback, scope, tenant impact complete? | Release safe | Evidence missing | False release risk | RELEASE_REGISTER |
| Rollback | CONTINGENCY_PLAN | rollback route, owner, trigger, evidence clear? | Rollback ready | Route incomplete | No rollback for risky change | CONTINGENCY_PLAN |
| Lessons learned | LESSONS_LEARNED | Cause/prevention/template update captured? | Learning captured | Pending improvement | Repeat failure unmanaged | LESSONS_LEARNED |
| Automation-readiness | Validation evidence | Manual process proven? safe boundaries? | Ready for limited automation | Evidence partial | Automation before control stable | Validation report |

## Outputs/records
Completed gate checklist, PASS/HOLD/BLOCKED decision, required records, evidence gaps, and next job card where needed.

## Owner/tool
QA Gatekeeper owns gate decisions. VIF Orchestrator coordinates. Specialist workers provide evidence for UI, backend/RLS, tenant, release, and automation gates.

## Gate controlled
All Software Build Control System gates.

## PASS/HOLD/BLOCKED rules
- PASS: entry evidence satisfies checklist and required records exist.
- HOLD: incomplete evidence but no unsafe action proceeds.
- BLOCKED: unsafe, destructive, data, tenant, release, or uncontrolled automation risk exists.

## Update trigger
Any new gate, failed gate, repeated failure, audit finding, automation change, or lesson learned.
