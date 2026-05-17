# COP_TURTLE_COMPLETION_MATRIX

## Purpose
Complete turtle mapping for core operational processes COP-01 to COP-16.

## Scope
App intake through app onboarding/readiness.

## Owner/agent
Process Engineer with VIF Orchestrator and QA Gatekeeper.

## Inputs
ADP model, work instructions, agent assignments, app-development controls and protected-scope rules.

## Activities/method
Define each COP turtle with supplier/input, activity, output/customer, owner, resources, WI, KPI, risk, control, evidence, interface, handoff, PDCA, gate and gap status.

## Outputs/records
COP turtle completion matrix.

## Linked processes
COP-01 to COP-16.

## Linked agents/workstations
VIF Orchestrator, Context Specialist, App Owner, UI/UX Reviewer, Runtime Architect, Backend/RLS Engineer, QA Gatekeeper, Release Controller, Support Owner.

## Linked skills/WIs
WI_001 to WI_020, WI_029 and WI_030.

## Linked gates
Intake, context, requirements, design, runtime, backend/RLS, risk, job card, build, verification, validation, release, support, customer change and onboarding gates.

## Evidence required
Job cards, context packs, requirements, runtime/UI/data/backend records, verification/UAT, release/rollback, support/change and onboarding evidence.

## KPIs/measures
Cycle time, rework, evidence gaps, test pass rate, UAT findings, release readiness, support incidents and onboarding gaps.

## Risks
UI shell mistaken as completion, RLS/security gap, unsupported release, missing UAT, app onboarding too early.

## Controls
Runtime-first, source lock, risk review, verification/UAT, release/rollback, support handover and HOLD rules.

## Interfaces
MOP direction, SOP support, ADP production flow and Clause 10 improvement.

## Handoffs
Intake to source lock, requirements to runtime, build to review/test, verification to UAT, release to support, support to improvement.

## COP turtle matrix
| Process ID | Process name | Input/source | Activities/method | Output/receiver | Owner/agent | Resources/tools | Skills/WIs | KPI/measure | Risk | Control | Records/evidence | Interfaces/handoffs | PDCA | Gate | Escalation | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COP-01 | App intake | Request/app opportunity | Classify app and risk | Intake record to context lock | VIF Orchestrator | Job card | WI_002, WI_029 | Intake completeness | Wrong classification | Intake gate | Intake record | To COP-02 | Plan | Intake | Unknown scope | STRUCTURAL PASS |
| COP-02 | Context/source-of-truth lock | Intake, repo/source | Lock active truth | Context pack to requirements | Context Specialist | GitHub/evidence | WI_001, WI_003, WI_010 | Source gaps | Stale source | Source lock | Context/source record | To COP-03 | Plan | Context | Wrong repo | STRUCTURAL PASS |
| COP-03 | Requirements/acceptance | Context, domain/user input | Define requirements and acceptance | Acceptance criteria to runtime | App Owner | Requirements register | WI_004, WI_018 | Rework | Vague requirements | Acceptance gate | Requirements evidence | To COP-06 | Plan | Requirements | Ambiguity | STRUCTURAL PASS |
| COP-04 | UI/interface design | Runtime/user workflow | Design UI/interface | UI concept to build/review | UI/UX Reviewer | Screen map | WI_012 | UI findings | Dashboard drift | UI review | UI evidence | To COP-10/12 | Do/Check | UI | User rejection | STRUCTURAL PASS |
| COP-05 | Data/table/grid design | Runtime/data need | Define tables/grids/lifecycle | Data spec to backend | UI/UX + Backend | Data table spec | WI_013 | Data gaps | Wrong truth/lifecycle | Table review | Data spec | To COP-07 | Do | Data gate | Unsafe action | STRUCTURAL PASS |
| COP-06 | Workflow/runtime specification | Requirements | Define runtime object/state/actions | Runtime map to UI/backend | Runtime Architect | Runtime map | WI_011 | Runtime gaps | UI shell | Runtime-first | Runtime evidence | To COP-04/07 | Plan/Do | Runtime | No runtime object | STRUCTURAL PASS |
| COP-07 | Database/backend/RLS design | Runtime/data spec | Design backend/RLS | Backend/RLS concept to review | Supabase/RLS Engineer | DB/RLS docs | WI_014, WI_015, WI_016 | RLS gaps | Tenant/security breach | DB/RLS proof | Backend evidence | To COP-11 | Do/Check | Backend/RLS | Security risk | STRUCTURAL PASS |
| COP-08 | Environment/tenant setup | App/tenant context | Define env/tenant boundaries | Environment record to verification | Security/Data Reviewer | Tenant register | WI_020 | Boundary gaps | Data mixing | Data boundary | Tenant evidence | To COP-11/12 | Plan/Do | Environment | Customer data risk | STRUCTURAL PASS |
| COP-09 | Job card approval | Requirements/risk/design | Create/approve job card | Job card to builder | QA Gatekeeper | Job card | WI_002, WI_008 | Prompt defects | Broad prompt | Scope/prompt gate | Job card/prompt | To COP-10 | Plan | Job card | Unsafe prompt | STRUCTURAL PASS |
| COP-10 | Build/modification | Approved job card | Scoped build/change | Change set to review | Coder/Builder | Codex/Lovable/GitHub | WI_008, WI_017 | Build failures | Scope drift | Job-card-only build | Diff evidence | To COP-11 | Do | Build | Protected-scope breach | STRUCTURAL PASS |
| COP-11 | Verification | Change set/tests | Verify build and evidence | Verification record to UAT | QA Gatekeeper | Test/scan reports | WI_017, WI_028 | Evidence gaps | False PASS | Verification review | Verification record | To COP-12 | Check | Verification | Failed test | STRUCTURAL PASS |
| COP-12 | Validation/UAT | Verified build | Validate user/process fit | UAT record to release | UAT Coordinator | UAT script | WI_018 | UAT findings | Process misfit | UAT signoff | UAT evidence | To COP-13 | Check | Validation | Release blocker | STRUCTURAL PASS |
| COP-13 | Release/rollback | UAT/release pack | Review release and rollback | Release decision to support | Release Controller | Release register | WI_019 | Rollback readiness | Unsafe release | Release gate | Release/rollback evidence | To COP-14 | Act | Release | Rollback gap | STRUCTURAL PASS |
| COP-14 | Support/maintenance | Release handover | Support and maintain | Support records to feedback | Support Owner | Support log | WI_025, WI_027 | Incident trend | No support route | Support owner | Support evidence | To COP-15/Clause10 | Act/Check | Support | Critical incident | STRUCTURAL PASS |
| COP-15 | Customer change control | Customer/support change | Classify and control change | Change record to intake/job card | Customer Change Owner | Change register | WI_002, WI_007 | Change lead time | Uncontrolled change | Change gate | Change evidence | To COP-01/09 | Plan | Change | Scope drift | STRUCTURAL PASS |
| COP-16 | App onboarding/readiness | App/context/evidence | Check readiness | Onboarding decision to CI/n8n HOLD | VIF Orchestrator | Readiness checklist | WI_029, WI_030 | Onboarding gaps | Premature app CI/n8n | Onboarding HOLD | Readiness evidence | To app CI/n8n readiness | Check | Onboarding | Readiness fail | HOLD |

## PASS/HOLD/BLOCKED rules
PASS requires app-specific evidence and validation. STRUCTURAL PASS means turtle row exists. HOLD applies to onboarding, app-repo CI, n8n and repair until external validation and readiness pass.

## Escalation
Escalate protected-scope breach, release without evidence, customer-data risk, false PASS or premature automation.

## MLA / maturity dependency
M2 permits controlled pilot evidence; M3+ required for release/onboarding readiness; M4/M5 for automation consideration.

## Update trigger
App onboarding, process change, audit finding, RCA/CAPA, support issue or release event.
