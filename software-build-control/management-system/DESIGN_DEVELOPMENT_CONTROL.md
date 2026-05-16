# DESIGN_DEVELOPMENT_CONTROL.md

## Purpose
Control the full app-development lifecycle from intake to support and improvement, including UI/interface, database/backend/RLS, tenant strategy, verification, validation, release, rollback, maintenance, problem solving, and lessons learned.

## Scope
Applies to new builds, defects, enhancements, refactors, releases, recovery work, customer changes, internal changes, and maintenance work. It does not authorise app-code changes without a job card.

## Inputs
- App intake checklist.
- Source-of-truth evidence.
- Repo, branch, version, environment, and tenant information.
- Screen, table, workflow, and runtime maps.
- Risk, contingency, rollback, and verification requirements.

## Activities/checklist
Lifecycle sequence:

Intake → Context lock → Source-of-truth lock → App type classification → UI/interface specification → Data table/grid specification → Workflow/runtime specification → Database/backend/RLS design → Environment/tenant strategy → Risk and contingency review → Job card → Build/modification → Verification → Validation/UAT → Tenant rollout → Release → Support/maintenance → Problem solving/RCA → Lessons learned → Skill/agent/template update.

Checklist:
- Is the work type classified?
- Is the source of truth locked?
- Are UI/interface requirements defined before UI work?
- Are data tables/grids defined before table work?
- Are runtime objects, states, actions, and protected actions mapped?
- Are database/backend/RLS needs defined before backend work?
- Are tenant/environment risks reviewed?
- Is contingency and rollback reviewed?
- Is there an approved current job card?
- Is verification evidence defined before PASS?
- Is validation/UAT required?
- Is release scope and tenant rollout controlled?
- Are lessons learned and process updates captured?

## Outputs/records
APP_CONTEXT, SCREEN_MAP, DATA_TABLE_SPEC, WORKFLOW_MAP, RUNTIME_MAP, CURRENT_JOB_CARD, VERIFICATION_REGISTER, TENANT_ROLLOUT_REGISTER, RELEASE_REGISTER, CUSTOMER_CHANGE_REGISTER, CONTINGENCY_PLAN, LESSONS_LEARNED, SKILL_REGISTER, AGENT_REGISTER.

## Owner/tool
Product owner and VIF Orchestrator maintain lifecycle control. Codex/GitHub provide repo evidence. Supabase Backend Reviewer provides backend/RLS evidence. QA Gatekeeper controls verification and release evidence.

## Gate controlled
Design and development lifecycle gate.

## PASS/HOLD/BLOCKED rules
- PASS: lifecycle stage has evidence and the next gate entry condition is satisfied.
- HOLD: evidence is incomplete but risk is contained.
- BLOCKED: build/release proceeds without source lock, job card, verification, rollback, tenant control, or protected-action evidence.

## Update trigger
New app, app repair, customer change, defect, release, incident, failed verification, or process lesson.
