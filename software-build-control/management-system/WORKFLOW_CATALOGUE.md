# WORKFLOW_CATALOGUE.md

## Purpose
Catalogue reusable workflow/BPM patterns for controlled app development so repeated work follows known process routes instead of being rediscovered by tools.

## Scope
Covers software build-control workflows for app intake, baseline, UI/interface design, database/backend/RLS review, verification, validation/UAT, tenant rollout, release, rollback, support, problem solving, lessons learned, and automation readiness.

## Inputs
- Approved process map.
- Current job cards, gate checklists, app records, customer requests, incidents, and lessons learned.

## Activities/checklist
| Workflow | Trigger | Actor/owner | Key steps | Gate | Evidence | Exception route | Rollback route | Linked skills/templates |
|---|---|---|---|---|---|---|---|---|
| App intake | New request | VIF Orchestrator | Classify, evidence-check, decide gate | Intake | Intake checklist | HOLD/BLOCKED | None | APP_CONTEXT, APP_INTAKE_CHECKLIST |
| Baseline lock | Before app work | Codex Repo Inspector | Confirm repo, branch, version, env | Baseline | Repo evidence | HOLD | Revert wrong baseline | APP_CONTEXT |
| UI/interface control | UI work | UI/Adaptive Reviewer | Screen map, layout, states | UI gate | SCREEN_MAP | HOLD | No UI build | SCREEN_MAP |
| Database/backend/RLS control | Backend work | Supabase Backend Reviewer | Runtime map, DB/RLS proof | DB/RLS gate | RUNTIME_MAP/RLS proof | BLOCKED | No schema change | DATABASE_BACKEND_CONTROL |
| Verification | After build/change | QA Gatekeeper | Build, lint, test, backend checks | Verification | VERIFICATION_REGISTER | HOLD/BLOCKED | Revert/fix card | VERIFICATION_REGISTER |
| Validation/UAT | Before rollout | Product/customer owner | Fit-for-use check | Validation | UAT record | Reject/hold | Disable feature | RELEASE/TENANT registers |
| Tenant rollout | Pilot/release | Release Controller | Tenant exposure, flags, rollback | Tenant gate | TENANT_ROLLOUT_REGISTER | BLOCKED | Flag/deploy rollback | TENANT_ROLLOUT_REGISTER |
| Lessons learned | Closure/failure | Lessons Learned Controller | Capture cause, prevention, update controls | Improvement | LESSONS_LEARNED | HOLD | Add corrective action | LESSONS_LEARNED |

## Outputs/records
Workflow catalogue, linked records, reusable routes, and exception/rollback routes.

## Owner/tool
Process Engineer and VIF Orchestrator maintain; QA Gatekeeper and specialist reviewers verify gate-specific workflows.

## Gate controlled
Workflow/BPM gate.

## PASS/HOLD/BLOCKED rules
- PASS: workflow has trigger, owner, steps, gate, evidence, exception, rollback, and linked artefacts.
- HOLD: workflow exists but evidence/owner/exception route is incomplete.
- BLOCKED: workflow authorises uncontrolled app, data, backend, tenant, release, or automation work.

## Update trigger
New workflow, repeated task, failed tool route, incident, release issue, or lesson learned.
