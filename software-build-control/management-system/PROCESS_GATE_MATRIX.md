# PROCESS_GATE_MATRIX.md

## Purpose
Link every Software Build Control System process to its controlling gate so work cannot bypass required evidence, ownership, PDCA, verification, validation, release, rollback or improvement controls.

## Scope
All MOP, COP and SOP processes.

## Inputs
PROCESS_REGISTER, GATE_CHECKLISTS, PROCESS_RECORDS_MATRIX, PROCESS_RISK_CONTROL_REGISTER, PDCA_PROCESS_MODEL and validation reports.

## Activities/checklist
Maintain gate linkage for every process. No process output is accepted as PASS unless the linked gate rule and required records are satisfied.

| Process ID | Process name | Primary gate | Entry evidence | PASS condition | HOLD condition | BLOCKED condition | Required records |
|---|---|---|---|---|---|---|---|
| MOP-01 | Context and interested-party management | Context gate | Context inputs and stakeholder/change trigger | Context/scope reviewed and current | Context evidence partial | Context/scope unknown for risky work | Context record |
| MOP-02 | Leadership and governance | Governance gate | Process/role/authority need | Owner, authority and escalation clear | Backup/escalation partial | No accountable owner | Owner matrix |
| MOP-03 | Strategic planning, objectives, risk and opportunity | Planning gate | Context, risks, KPIs, incidents | Risks/objectives owned and controlled | Risk owner/action incomplete | Critical risk uncontrolled | KPI/risk records |
| MOP-04 | AI governance and tool-use policy | AI governance gate | AI/tool use or change | Tool use, data rule and oversight defined | Tool qualification incomplete | AI/tool can act without oversight | Tool/agent/prompt records |
| MOP-05 | Internal audit | Audit gate | Audit scope/evidence | Audit planned/executed and findings controlled | Audit records incomplete | Critical finding uncontained | Audit records |
| MOP-06 | Management review | Management review gate | KPIs/audits/risks/incidents | Decisions/actions recorded | Inputs incomplete | Critical systemic risk ignored | Review records |
| MOP-07 | Corrective action and continual improvement | Improvement gate | Incident/finding/repeat defect | Containment, RCA, CA and effectiveness defined | Effectiveness pending | Critical issue uncontained | CA/lessons records |
| COP-01 | App intake and classification | Intake gate | Request/evidence | App, problem, users, repo, data risk and gate clear | Non-critical data missing | App/repo/data risk unclear | Intake checklist |
| COP-02 | Source-of-truth and context lock | Baseline gate | Repo/branch/version/context evidence | Correct source locked | Partial baseline evidence | Wrong/unknown repo/branch/version | APP_CONTEXT/baseline |
| COP-03 | Requirements and acceptance criteria | Requirements gate | Request/process need | Acceptance criteria clear and testable | Acceptance detail incomplete | Build requested without requirements | Job card/requirements |
| COP-04 | UI/interface design control | UI/screen gate | Screen/prototype/UI need | SCREEN_MAP complete enough to build | Minor visual gaps | UI build without screen map | SCREEN_MAP |
| COP-05 | Data table/grid specification | Data table/grid gate | Table/grid/data need | Columns/sources/validation/export defined | Minor mapping gaps | Table build without data spec | DATA_TABLE_SPEC |
| COP-06 | Workflow/runtime specification | Runtime gate | Workflow/actions/states need | Runtime objects/states/actions/evidence mapped | Exception route incomplete | UI-only runtime claim | WORKFLOW/RUNTIME maps |
| COP-07 | Database/backend/RLS design control | DB/RLS gate | Backend/schema/RLS need | RLS/backend/read-write/migration route evidenced | Evidence incomplete | Data exposure or frontend-only security | DB/RLS evidence |
| COP-08 | Environment and tenant setup | Environment/tenant gate | Tenant/environment change | Tenant type/data exposure/rollback clear | Tenant evidence incomplete | Real data/tenant exposure uncontrolled | Tenant rollout register |
| COP-09 | Job card creation and approval | Job-card gate | Approved inputs/maps | Scope in/out/tools/verification/rollback defined | Inputs incomplete | Work starts without job card | CURRENT_JOB_CARD |
| COP-10 | Build/modification control | Build gate | Approved job card | Diff/build within scope | Build fails or evidence partial | Prohibited files changed | Diff/build evidence |
| COP-11 | Verification | Verification gate | Build/test/backend/manual evidence | Expected results verified | Non-critical check missing | Critical evidence missing or failed | VERIFICATION_REGISTER |
| COP-12 | Validation/UAT | Validation/UAT gate | UAT criteria/candidate | User/customer acceptance recorded | UAT pending | UAT rejected for release scope | UAT/release record |
| COP-13 | Tenant rollout | Tenant rollout gate | Verification/UAT/tenant data | Pilot/exposure/rollback controlled | Tenant evidence partial | Wrong tenant or uncontrolled blast radius | TENANT_ROLLOUT_REGISTER |
| COP-14 | Release and rollback | Release gate | Verification/UAT/rollout/rollback | Release and rollback evidence complete | Evidence partial | No rollback or unsafe release | RELEASE_REGISTER |
| COP-15 | App support and maintenance | Maintenance gate | Support/maintenance inputs | Maintenance risks/action route controlled | Review incomplete | Critical support/security risk uncontrolled | Maintenance records |
| COP-16 | Customer change control | Customer-change gate | Customer request/evidence | Impact, approval, UAT and rollout route clear | Approval/evidence partial | Customer change bypasses approval | CUSTOMER_CHANGE_REGISTER |
| SOP-01 | Documented information control | Documented information gate | Document/record change | Controlled revision and retrieval | Review incomplete | Obsolete/uncontrolled critical doc | Document records |
| SOP-02 | Organisational knowledge control | Knowledge gate | Knowledge/lesson source | Knowledge reusable, owned and reviewed | Review/owner partial | Critical knowledge lost/uncontrolled | Knowledge register |
| SOP-03 | Competence and skill control | Competence gate | Skill/worker need | Required skill/competence evidenced | Gap action pending | Worker lacks critical competence | Skill/competence records |
| SOP-04 | Agent/worker control | Agent gate | Worker/tool assignment | Allowed/prohibited work and stops clear | Escalation partial | Agent can bypass gates | Agent register |
| SOP-05 | Tool routing and tool qualification | Tool routing gate | Task/tool need | Correct tool route and limits defined | Qualification partial | Wrong/unsafe tool used | Tool routing record |
| SOP-06 | Prompt control and prompt quality | Prompt gate | AI/tool instruction | Prompt has context, scope, evidence, stop, rollback | Prompt review partial | Prompt authorises uncontrolled work | Prompt records |
| SOP-07 | Evidence and record control | Evidence gate | Claim/evidence need | Evidence traceable and complete | Non-critical evidence missing | False PASS risk | Evidence records |
| SOP-08 | Security, tenant and data protection control | Security/data gate | Data/security/tenant impact | Security/RLS/data controls evidenced | Evidence partial | Data exposure risk | Security/RLS records |
| SOP-09 | Configuration and version control | Configuration gate | Repo/version/release need | Correct branch/version/rollback anchor | Partial version evidence | Wrong version or no rollback anchor | Git/version records |
| SOP-10 | Contingency and continuity control | Contingency gate | Trigger/risk/incident | Containment, recovery and rollback route clear | Route partial | Critical contingency without route | Contingency record |
| SOP-11 | Supplier/tool-provider control | Supplier/tool gate | Provider/tool dependency | Provider risk/fallback reviewed | Review partial | Critical provider risk unmanaged | Provider records |
| SOP-12 | Lessons learned and knowledge reuse | Lessons gate | Event/failure/improvement | Prevention action and effectiveness route defined | Effectiveness pending | Repeat failure without control update | Lessons records |

## Outputs/records
Process gate matrix and process gate decisions.

## Owner/tool
QA Gatekeeper maintains the gate matrix. Process owners maintain process-specific gate evidence. VIF Orchestrator enforces route discipline.

## Gate controlled
Process gate linkage and PASS/HOLD/BLOCKED control gate.

## PASS/HOLD/BLOCKED rules
- PASS: every process has gate, entry evidence, PASS/HOLD/BLOCKED criteria and required records.
- HOLD: gate is defined but records/evidence are incomplete.
- BLOCKED: process can produce controlled output without a gate or required records.

## Update trigger
New process, gate failure, audit finding, process change, CI activation, app onboarding, release issue or lesson learned.
