# PROCESS_MAP.md

## Purpose
Map the controlled app-development process and its interfaces so work follows a defined route instead of tool-led patching.

## Scope
Covers intake, context lock, source-of-truth lock, app classification, UI/interface design, table/grid design, workflow/runtime mapping, database/backend/RLS, environment/tenant strategy, contingency review, job card, build, verification, validation/UAT, tenant rollout, release, support, problem solving, lessons learned, and system updates.

## Inputs
- Request, defect, customer change, or support issue.
- App context and source-of-truth evidence.
- Repo, branch, environment, tenant, risk, verification, and rollback evidence.

## Activities/checklist
| Process step | Main input | Activity | Main output | Interface |
|---|---|---|---|---|
| Intake | Request/defect | Classify and evidence-check | Intake decision | Customer/change control |
| Context lock | Evidence | Preserve non-truncated context | APP_CONTEXT | All tools |
| Source-of-truth lock | Repo/branch/version | Confirm baseline | Baseline decision | GitHub/Codex |
| Design maps | UI/data/workflow/runtime needs | Define maps before build | Controlled maps | Lovable/Codex/Supabase |
| Job card | Approved maps | Bound one vertical slice | CURRENT_JOB_CARD | Tool routing |
| Build/modification | Approved job card | Execute scoped work | Diff/output | Codex/Lovable/Claude |
| Verification | Build/test/backend evidence | Prove result | VERIFICATION_REGISTER | QA Gatekeeper |
| Validation/UAT | User/customer checks | Confirm fitness for use | UAT result | Customer/process owner |
| Rollout/release | Verification/UAT | Control exposure and rollback | RELEASE/TENANT registers | GitHub/Supabase/deployment |
| Support/problem solving | Incident/feedback | RCA/corrective action | Lessons/job cards | Maintenance/improvement |

## Outputs/records
Process map, interface notes, gate records, job cards, verification records, release records, and lessons learned.

## Owner/tool
Process Engineer with VIF Orchestrator; GitHub/Codex validates repo interfaces; Supabase reviewer validates backend interfaces.

## Gate controlled
Process approach and lifecycle routing gate.

## PASS/HOLD/BLOCKED rules
- PASS: process step, input, output, owner, record, and interface are clear.
- HOLD: interface or evidence is incomplete.
- BLOCKED: work bypasses required process route or protected gate.

## Update trigger
New process, app, tool, interface, recurring failure, audit finding, or lesson learned.
