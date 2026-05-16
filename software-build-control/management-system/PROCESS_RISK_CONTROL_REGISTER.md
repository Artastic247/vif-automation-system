# PROCESS_RISK_CONTROL_REGISTER.md

## Purpose
Link each Software Build Control System process to key risks and controls so risks are visible, owned and checked before work proceeds.

## Scope
All MOP, COP and SOP processes.

## Inputs
PROCESS_REGISTER, CONTINGENCY_PLAN, DATABASE_BACKEND_CONTROL, UI_INTERFACE_CONTROL, CHANGE_CONTROL_PROCEDURE, lessons learned, audit findings and validation reports.

## Activities/checklist
Maintain one or more key risks and practical controls per process. Critical risks must have a gate, owner and containment route.

| Process ID | Process name | Key risk | Key controls | Detection/evidence | Owner | Related contingency | Gate impact |
|---|---|---|---|---|---|---|---|
| MOP-01 | Context and interested-party management | Wrong context/scope or missed stakeholder need | Context review, PESTLE/SWOT, interested-party review | Context record | VIF Orchestrator | Context loss | HOLD/BLOCKED |
| MOP-02 | Leadership and governance | No accountable owner or unclear authority | Owner matrix, authority rules, escalation | PROCESS_OWNER_MATRIX | System owner | Release blocked/missing evidence | HOLD/BLOCKED |
| MOP-03 | Strategic planning, objectives, risk and opportunity | Uncontrolled strategic/operational risk | Risk register, objectives, KPI review | PROCESS_KPI_REGISTER | System owner | Urgent production defect | HOLD/BLOCKED |
| MOP-04 | AI governance and tool-use policy | AI misuse, hallucination, data exposure, credit burn | AI/tool policy, tool routing, prompt quality, human oversight | Tool/prompt records | AI Governance Owner | AI tool failure/prompt drift | HOLD/BLOCKED |
| MOP-05 | Internal audit | Systemic failure remains hidden | Audit programme, process audit, findings register | Audit evidence | QA Gatekeeper | Missing evidence | HOLD |
| MOP-06 | Management review | System remains ineffective despite evidence | Review KPIs, audits, incidents, risks | Review actions | System owner | Unclosed critical risk | HOLD |
| MOP-07 | Corrective action and continual improvement | Repeat failure or ineffective correction | RCA/CAPA, effectiveness check, lessons update | CA/LL records | QA Gatekeeper | Repeat defect | HOLD/BLOCKED |
| COP-01 | App intake and classification | Wrong route, missing app/data context | Intake checklist and evidence gap list | Intake record | VIF Orchestrator | Wrong repo/branch/context | HOLD/BLOCKED |
| COP-02 | Source-of-truth and context lock | Wrong repo, branch, version or truncated context | Baseline evidence, APP_CONTEXT, stop condition | Repo/context evidence | Codex Repo Inspector | Wrong repo/branch | BLOCKED |
| COP-03 | Requirements and acceptance criteria | Unclear expected result or acceptance | Requirements/acceptance criteria in job card | CURRENT_JOB_CARD | Product owner | UAT rejection | HOLD |
| COP-04 | UI/interface design control | Partial UI, missing screens/states, dashboard-first build | SCREEN_MAP, UI checklist, no UI build without map | UI review evidence | UI Reviewer | Prompt drift/partial output | HOLD/BLOCKED |
| COP-05 | Data table/grid specification | Missing columns, wrong source, bad export | DATA_TABLE_SPEC and data mapping | Table spec | Runtime Architect | Failed verification | HOLD |
| COP-06 | Workflow/runtime specification | UI-only logic, undefined states/actions | RUNTIME_MAP, state/action mapping | Runtime map | Runtime Architect | Feature rejected in pilot | HOLD/BLOCKED |
| COP-07 | Database/backend/RLS design control | Data exposure, broken migration, frontend-only security | DB/RLS review, read/write proof, migration review | Backend/RLS evidence | Supabase Reviewer | RLS/security defect | BLOCKED |
| COP-08 | Environment and tenant setup | Customer data used in dev, tenant mix | Tenant classification, environment matrix | TENANT_ROLLOUT_REGISTER | Security/RLS Reviewer | Tenant data exposure | BLOCKED |
| COP-09 | Job card creation and approval | Feature creep/uncontrolled scope | Scope in/out, tools allowed/prohibited, rollback | Job card | VIF Orchestrator | AI out-of-scope edit | HOLD/BLOCKED |
| COP-10 | Build/modification control | Out-of-scope file changes or failed build | Diff review, build checks, stop rules | Diff/build log | Assigned worker | Failed build/tool drift | HOLD/BLOCKED |
| COP-11 | Verification | False PASS or missing evidence | Verification register, evidence map | Build/test/backend evidence | QA Gatekeeper | Release blocked by evidence | BLOCKED |
| COP-12 | Validation/UAT | User/customer rejects feature | UAT criteria and acceptance/rejection record | UAT evidence | Product/customer owner | UAT rejection | HOLD/BLOCKED |
| COP-13 | Tenant rollout | Wide blast radius, wrong tenant exposure | Pilot-first rollout, feature exposure control | Tenant rollout record | Release Controller | Tenant exposure | BLOCKED |
| COP-14 | Release and rollback | No rollback route, wrong release | Release checklist, version/rollback evidence | RELEASE_REGISTER | GitHub Release Controller | Lost rollback route | BLOCKED |
| COP-15 | App support and maintenance | Unmanaged support/debt/security issue | Maintenance cadence and issue ageing review | Maintenance records | App owner | Urgent defect | HOLD/BLOCKED |
| COP-16 | Customer change control | Customer scope bypasses approval/UAT | Impact/approval/UAT route | CUSTOMER_CHANGE_REGISTER | Change owner | Customer UAT rejection | HOLD/BLOCKED |
| SOP-01 | Documented information control | Obsolete or uncontrolled records | Document control, revision/review | Doc records | System owner | Missing evidence | HOLD |
| SOP-02 | Organisational knowledge control | Lost knowledge or non-reuse | Knowledge register/review | Process knowledge records | Process Engineer | Repeat failure | HOLD |
| SOP-03 | Competence and skill control | Worker lacks method/skill | Skill register, WIs, competence evidence | Skill/competence records | System owner | Tool failure | HOLD/BLOCKED |
| SOP-04 | Agent/worker control | Agent bypasses gate or modifies prohibited files | Agent register, stop/escalation rules | Agent assignment/diff | VIF Orchestrator | Out-of-scope edit | BLOCKED |
| SOP-05 | Tool routing and tool qualification | Wrong tool used for risky work | Tool matrix and qualification | Tool route record | VIF Orchestrator | Tool failure | HOLD/BLOCKED |
| SOP-06 | Prompt control and prompt quality | Prompt drift/truncation/unbounded instruction | Prompt checklist/library/failure log | Prompt records | Prompt Reviewer | Prompt drift | HOLD/BLOCKED |
| SOP-07 | Evidence and record control | Evidence missing, untraceable or unreliable | Evidence map, verification register | Evidence records | QA Gatekeeper | Missing evidence | BLOCKED |
| SOP-08 | Security, tenant and data protection control | Data/security incident | Data rules, RLS review, tenant isolation | Security evidence | Security/RLS Reviewer | Data exposure | BLOCKED |
| SOP-09 | Configuration and version control | Wrong version or rollback anchor | Git/version/release controls | Version evidence | GitHub Release Controller | Wrong branch/lost rollback | BLOCKED |
| SOP-10 | Contingency and continuity control | No containment/recovery route | CONTINGENCY_PLAN and rollback route | Contingency record | VIF Orchestrator | All contingencies | HOLD/BLOCKED |
| SOP-11 | Supplier/tool-provider control | Provider/tool outage or limitation | Provider review, fallback route | Provider record | System owner | GitHub/Supabase/tool unavailable | HOLD |
| SOP-12 | Lessons learned and knowledge reuse | Repeat defects and no control update | Lessons register, effectiveness check | Lessons records | Lessons Controller | Repeat failure | HOLD/BLOCKED |

## Outputs/records
Process risk/control register, gate decisions, containment actions and management review input.

## Owner/tool
Process Engineer maintains. Risk owners update controls. QA Gatekeeper verifies high-risk evidence.

## Gate controlled
Risk and control gate.

## PASS/HOLD/BLOCKED rules
- PASS: every process has defined risk, control, detection evidence, owner and gate impact.
- HOLD: risk/control exists but evidence or owner is incomplete.
- BLOCKED: critical risk has no control, owner or containment route.

## Update trigger
New risk, incident, audit finding, app failure, release failure, provider/tool change, CI finding or lesson learned.
