# PROCESS_RECORDS_MATRIX.md

## Purpose
Define the controlled records and evidence required by each process so process outputs are traceable and auditable.

## Scope
All MOP, COP and SOP processes.

## Inputs
PROCESS_REGISTER, VERIFICATION_REGISTER, RELEASE_REGISTER, TENANT_ROLLOUT_REGISTER, CONTINGENCY_PLAN, LESSONS_LEARNED and process-specific records.

## Activities/checklist
Each process must define required records/evidence, storage location, owner, review point and retention/revision rule.

| Process ID | Process name | Required records/evidence | Record location/template | Owner | Review point | Retention/revision rule | Linked gate |
|---|---|---|---|---|---|---|---|
| MOP-01 | Context and interested-party management | Context review, interested parties, scope, PESTLE/SWOT when created | APP_CONTEXT / future context records | VIF Orchestrator | Context gate | Review on major change | Context gate |
| MOP-02 | Leadership and governance | Owner matrix, authority/escalation evidence | PROCESS_OWNER_MATRIX | System owner | Governance gate | Review on role/process change | Governance gate |
| MOP-03 | Strategic planning, objectives, risk and opportunity | Objectives, risks, opportunities, actions | PROCESS_KPI_REGISTER / PROCESS_RISK_CONTROL_REGISTER | System owner | Planning gate | Review cadence/trigger | Planning gate |
| MOP-04 | AI governance and tool-use policy | AI/tool decisions, routes, failures | TOOL_ROUTING_MATRIX / AGENT_REGISTER | AI Governance Owner | AI governance gate | Review on tool/model change | AI gate |
| MOP-05 | Internal audit | Audit plan, checklist, findings, actions | Future audit records | QA Gatekeeper | Audit gate | Per audit programme | Audit gate |
| MOP-06 | Management review | Review inputs, decisions, actions | Future management review register | System owner | Management review gate | Scheduled review | Management review gate |
| MOP-07 | Corrective action and continual improvement | Problem/RCA/CA, effectiveness, lessons | LESSONS_LEARNED / future CA register | QA Gatekeeper | Improvement gate | Until effectiveness verified | Improvement gate |
| COP-01 | App intake and classification | Intake answers, classification, evidence gaps | APP_INTAKE_CHECKLIST | VIF Orchestrator | Intake gate | Per request | Intake gate |
| COP-02 | Source-of-truth and context lock | Repo, branch, version, context, baseline | APP_CONTEXT | Codex Repo Inspector | Baseline gate | Per job card | Baseline gate |
| COP-03 | Requirements and acceptance criteria | Requirements, acceptance criteria, scope | CURRENT_JOB_CARD | Product owner | Requirements gate | Per job card | Requirements gate |
| COP-04 | UI/interface design control | Screen map, UI findings, layout rules | SCREEN_MAP / UI_INTERFACE_CONTROL | UI Reviewer | UI gate | Per UI change | UI gate |
| COP-05 | Data table/grid specification | Table/grid spec, columns, source, validation | DATA_TABLE_SPEC | Runtime Architect | Data table gate | Per table/grid change | Data table gate |
| COP-06 | Workflow/runtime specification | Workflow map, runtime object/state/action map | WORKFLOW_MAP / RUNTIME_MAP | Runtime Architect | Runtime gate | Per workflow change | Runtime gate |
| COP-07 | Database/backend/RLS design control | DB/RLS review, migration evidence, read/write proof | DATABASE_BACKEND_CONTROL / VERIFICATION_REGISTER | Supabase Reviewer | DB/RLS gate | Per backend change | DB/RLS gate |
| COP-08 | Environment and tenant setup | Tenant/environment classification, data sensitivity | TENANT_ROLLOUT_REGISTER | Security/RLS Reviewer | Environment/tenant gate | Per rollout/change | Tenant gate |
| COP-09 | Job card creation and approval | Approved job card, scope, tools, rollback | CURRENT_JOB_CARD | VIF Orchestrator | Job-card gate | Per work package | Job-card gate |
| COP-10 | Build/modification control | Diff, build output, scope review | PR/diff records / VERIFICATION_REGISTER | Assigned worker | Build gate | Per build/change | Build gate |
| COP-11 | Verification | Build/lint/test/manual/backend evidence | VERIFICATION_REGISTER | QA Gatekeeper | Verification gate | Per change | Verification gate |
| COP-12 | Validation/UAT | UAT criteria, feedback, acceptance/rejection | RELEASE_REGISTER / future UAT record | Product/customer owner | Validation gate | Per release/pilot | Validation gate |
| COP-13 | Tenant rollout | Tenant exposure, pilot, rollout, rollback decision | TENANT_ROLLOUT_REGISTER | Release Controller | Tenant rollout gate | Per rollout | Tenant gate |
| COP-14 | Release and rollback | Release version, commit, deployment, rollback route | RELEASE_REGISTER | GitHub Release Controller | Release gate | Per release | Release gate |
| COP-15 | App support and maintenance | Maintenance review, support actions, issue ageing | APP_MAINTENANCE_PLAN | App owner | Maintenance gate | Per cadence/incident | Maintenance gate |
| COP-16 | Customer change control | Customer request, impact, approval, UAT | CUSTOMER_CHANGE_REGISTER | Change owner | Customer-change gate | Per customer change | Customer-change gate |
| SOP-01 | Documented information control | Controlled document list and revisions | Templates / future document register | System owner | Document control gate | Per revision | Doc info gate |
| SOP-02 | Organisational knowledge control | Knowledge records and review status | PROCESS_KNOWLEDGE_REGISTER | Process Engineer | Knowledge gate | Per review | Knowledge gate |
| SOP-03 | Competence and skill control | Skills, competence evidence, WI revisions | SKILL_REGISTER / SKILL_TEMPLATE | System owner | Competence gate | Per worker/tool change | Competence gate |
| SOP-04 | Agent/worker control | Agent assignment, limits, escalation evidence | AGENT_REGISTER | VIF Orchestrator | Agent gate | Per worker/tool change | Agent gate |
| SOP-05 | Tool routing and tool qualification | Tool route, capability, failure evidence | TOOL_ROUTING_MATRIX | VIF Orchestrator | Tool routing gate | Per tool/change | Tool gate |
| SOP-06 | Prompt control and prompt quality | Prompt record, checklist, failures | Future prompt records | Prompt Reviewer | Prompt gate | Per prompt/tool use | Prompt gate |
| SOP-07 | Evidence and record control | Evidence map and traceability records | VERIFICATION_REGISTER / reports | QA Gatekeeper | Evidence gate | Per gate/release | Evidence gate |
| SOP-08 | Security, tenant and data protection control | Security/RLS/data handling evidence | DATABASE_BACKEND_CONTROL / TENANT_ROLLOUT_REGISTER | Security/RLS Reviewer | Security/data gate | Per data-impacting change | Security gate |
| SOP-09 | Configuration and version control | Git branch, commit, release, rollback anchor | RELEASE_REGISTER | GitHub Release Controller | Configuration gate | Per job/release | Config gate |
| SOP-10 | Contingency and continuity control | Contingency trigger, containment, recovery, rollback | CONTINGENCY_PLAN | VIF Orchestrator | Contingency gate | Per incident/trigger | Contingency gate |
| SOP-11 | Supplier/tool-provider control | Provider/tool review and fallback evidence | Future provider register | System owner | Supplier/tool gate | Per provider/tool change | Supplier gate |
| SOP-12 | Lessons learned and knowledge reuse | Lessons, prevention, effectiveness status | LESSONS_LEARNED | Lessons Controller | Lessons gate | Per event/review | Lessons gate |

## Outputs/records
Process records matrix and record-control requirements.

## Owner/tool
QA Gatekeeper owns evidence integrity. Process owners maintain process records. System owner controls retention/revision rules.

## Gate controlled
Evidence and record-control gate.

## PASS/HOLD/BLOCKED rules
- PASS: every process has required records, owner, location, review point and linked gate.
- HOLD: record exists but review or retention rule is incomplete.
- BLOCKED: controlled work proceeds without required records/evidence.

## Update trigger
New process, process change, evidence failure, audit finding, CI activation, release, rollback or lesson learned.
