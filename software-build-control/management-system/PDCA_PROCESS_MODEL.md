# PDCA_PROCESS_MODEL.md

## Purpose
Make PDCA explicit for every Software Build Control System process. A process is incomplete if PLAN, DO, CHECK or ACT is only implied.

## Scope
All MOP, COP and SOP processes in the process register.

## Inputs
PROCESS_REGISTER, PROCESS_INTERACTION_MAP, gate checklists, risk controls, records matrix and lessons learned.

## Activities/checklist
For each process define: PLAN, DO, CHECK, ACT, evidence and improvement route.

## PDCA process model

| Process ID | Process | PLAN | DO | CHECK | ACT | PDCA status |
|---|---|---|---|---|---|---|
| MOP-01 | Context and interested-party management | Plan context method, interested-party review and scope criteria | Perform PESTLE/SWOT/interested-party/scope review | Check context currency and scope fit against incidents/customer/tool changes | Update context, scope, risks and intake criteria | Explicit |
| MOP-02 | Leadership and governance | Plan roles, authorities, escalation and release rights | Assign owners/agents and approval routes | Check owner clarity, unresolved escalations and gate authority | Update owner matrix and escalation rules | Explicit |
| MOP-03 | Strategic planning, objectives, risk and opportunity | Plan objectives, risks, opportunities and controls | Maintain risk/objective actions | Check KPI trends, risk status and objective progress | Update objectives, risk controls and priorities | Explicit |
| MOP-04 | AI governance and tool-use policy | Plan AI policy, tool limits, oversight and data restrictions | Apply AI/tool routing and oversight rules | Check AI failures, prompt drift, credit burn and data-risk events | Update AI policy, prompts, tool routes and agent limits | Explicit |
| MOP-05 | Internal audit | Plan audit scope, criteria, programme and auditors | Conduct process/evidence/app/tool audits | Check audit findings and evidence adequacy | Issue corrective actions and update processes | Explicit |
| MOP-06 | Management review | Plan review cadence, inputs and decision agenda | Review KPIs, audits, risks, incidents and changes | Check system suitability, adequacy and effectiveness | Decide actions, resources, priorities and improvements | Explicit |
| MOP-07 | Corrective action and continual improvement | Plan containment, RCA and effectiveness approach | Execute correction, RCA and corrective action | Check effectiveness and recurrence | Update controls, skills, prompts, templates and validation | Explicit |
| COP-01 | App intake and classification | Plan intake questions and classification criteria | Capture request, evidence and risk classification | Check completeness and correct route | Update backlog/context/gate route | Explicit |
| COP-02 | Source-of-truth and context lock | Plan source evidence and context pack needs | Confirm repo, branch, version, files and context | Check for mismatch, truncation or missing evidence | Update context pack and stop rules | Explicit |
| COP-03 | Requirements and acceptance criteria | Plan requirement and acceptance fields | Define expected behaviour and acceptance criteria | Check clarity, testability and scope boundaries | Update requirements/job card/backlog | Explicit |
| COP-04 | UI/interface design control | Plan screens, roles, states and layout needs | Create/review screen map and UI controls | Check UI completeness and workflow links | Update screen map and UI lessons | Explicit |
| COP-05 | Data table/grid specification | Plan data fields, sources, validation and export needs | Define table/grid specification | Check completeness, source mapping and validation rules | Update data spec and patterns | Explicit |
| COP-06 | Workflow/runtime specification | Plan runtime objects, states and actions | Map workflow, state changes and evidence | Check runtime proof and protected actions | Update runtime map and state rules | Explicit |
| COP-07 | Database/backend/RLS design control | Plan schema, RLS, roles, protected actions and rollback | Review/design migrations, RLS, RPC and backend evidence | Check read/write proof, RLS tests and migration safety | Update DB/RLS controls and corrective actions | Explicit |
| COP-08 | Environment and tenant setup | Plan dev/demo/staging/pilot/prod and data rules | Classify tenants/environments and set exposure controls | Check data isolation and tenant access evidence | Update tenant/environment strategy | Explicit |
| COP-09 | Job card creation and approval | Plan bounded vertical slice and required evidence | Create job card with scope, tools, verification, rollback | Check scope, prohibited changes and readiness | Update job card or return to previous gate | Explicit |
| COP-10 | Build/modification control | Plan tool route and files in scope | Execute approved build/modification only | Check diff, build output and out-of-scope changes | Rework, revert or update controls | Explicit |
| COP-11 | Verification | Plan verification checks and evidence | Run build/lint/test/backend/manual checks | Check results against expected outcomes | Update verification records, fixes and lessons | Explicit |
| COP-12 | Validation/UAT | Plan UAT criteria and user/customer validation route | Execute validation/UAT | Check acceptance/rejection and fit for use | Update release decision, backlog or corrective action | Explicit |
| COP-13 | Tenant rollout | Plan pilot, limited and full rollout with rollback | Enable controlled exposure per tenant/stage | Check tenant impact, feedback and incidents | Expand, hold, rollback or improve | Explicit |
| COP-14 | Release and rollback | Plan release scope, version and rollback route | Release or rollback under approval | Check release health and rollback effectiveness | Update release records and lessons learned | Explicit |
| COP-15 | App support and maintenance | Plan maintenance cadence and support review | Review support issues, dependencies and app health | Check unresolved risk, ageing and recurring issues | Create job cards or corrective actions | Explicit |
| COP-16 | Customer change control | Plan customer change intake, impact, approval and UAT | Assess and route customer change | Check approval, commercial/UAT and rollout evidence | Close, reject, defer or improve process | Explicit |
| SOP-01 | Documented information control | Plan document/record rules and retention | Create, revise and control documents/records | Check currency, approval and retrieval | Update/revise/archive documents | Explicit |
| SOP-02 | Organisational knowledge control | Plan knowledge categories and review cadence | Capture process, app, tool, prompt and domain knowledge | Check reusability, ownership and review status | Update knowledge and work instructions | Explicit |
| SOP-03 | Competence and skill control | Plan required competence and skill methods | Maintain skills, competence evidence and training needs | Check competence gaps and skill failures | Update skills, work instructions and training | Explicit |
| SOP-04 | Agent/worker control | Plan agent roles, limits and escalation | Assign workers/agents to approved tasks | Check outputs, scope adherence and stop conditions | Update agent register and escalation rules | Explicit |
| SOP-05 | Tool routing and tool qualification | Plan tool capabilities and qualification criteria | Route tools to approved tasks | Check failures, drift, cost and suitability | Update tool matrix and fallback routes | Explicit |
| SOP-06 | Prompt control and prompt quality | Plan prompt structure, context and forbidden patterns | Create/review approved prompts | Check output quality, drift and evidence linkage | Update prompt library and failure register | Explicit |
| SOP-07 | Evidence and record control | Plan evidence types, records and traceability | Capture and link records to claims | Check completeness, integrity and retrieval | Correct evidence gaps and update rules | Explicit |
| SOP-08 | Security, tenant and data protection control | Plan data, tenant and security rules | Apply data/RLS/security controls | Check exposure, access and environment separation | Contain incidents and update controls | Explicit |
| SOP-09 | Configuration and version control | Plan branch, version, release and rollback rules | Maintain Git/config/version records | Check correct baseline and deploy version | Correct config drift and update release controls | Explicit |
| SOP-10 | Contingency and continuity control | Plan contingency triggers and response routes | Contain and recover from disruption | Check recovery, rollback and evidence | Update contingency plan and lessons | Explicit |
| SOP-11 | Supplier/tool-provider control | Plan provider/tool review criteria | Review providers, availability and risks | Check outages, limitations and dependency risk | Update supplier/tool controls and fallbacks | Explicit |
| SOP-12 | Lessons learned and knowledge reuse | Plan lesson capture and effectiveness method | Capture lessons and prevention actions | Check implementation and recurrence | Update processes, skills, prompts, templates and validation | Explicit |

## Outputs/records
PDCA process matrix, process improvement records and validation evidence.

## Owner/tool
Process Engineer maintains. QA Gatekeeper verifies explicit PDCA. VIF Orchestrator approves route changes.

## Gate controlled
PDCA completeness gate.

## PASS/HOLD/BLOCKED rules
- PASS: each process has explicit PLAN, DO, CHECK and ACT.
- HOLD: PDCA exists but evidence or owner is incomplete.
- BLOCKED: PDCA is implied only, or any process lacks a PDCA stage.

## Update trigger
New process, process revision, audit finding, validation failure, CI finding, or lesson learned.
