# PROCESS_OWNER_MATRIX.md

## Purpose
Define accountable process ownership and agent/worker responsibility for every Software Build Control System process.

## Scope
All MOP, COP and SOP processes.

## Inputs
PROCESS_REGISTER, AGENT_REGISTER, TOOL_ROUTING_MATRIX and GATE_CHECKLISTS.

## Activities/checklist
Maintain process ownership. No process may be released without an accountable owner and escalation route.

| Process ID | Process name | Owner/agent | Backup/escalation | Authority | Key interfaces | Gate controlled |
|---|---|---|---|---|---|---|
| MOP-01 | Context and interested-party management | VIF Orchestrator | System owner | Context/scope approval | COP-01, MOP-03, SOP-02 | Context gate |
| MOP-02 | Leadership and governance | System owner | VIF Orchestrator | Authority/release governance | All processes | Governance gate |
| MOP-03 | Strategic planning, objectives, risk and opportunity | System owner | QA Gatekeeper | Objectives/risk approval | MOP-01, MOP-06, MOP-07 | Planning gate |
| MOP-04 | AI governance and tool-use policy | AI Governance Owner | VIF Orchestrator | AI/tool-use approval | SOP-04, SOP-05, SOP-06 | AI governance gate |
| MOP-05 | Internal audit | QA Gatekeeper | Process Engineer | Audit planning/reporting | MOP-06, MOP-07 | Audit gate |
| MOP-06 | Management review | System owner | QA Gatekeeper | Management decisions/actions | MOP-03, MOP-05, MOP-07 | Management review gate |
| MOP-07 | Corrective action and continual improvement | QA Gatekeeper | Lessons Learned Controller | CA/improvement approval | All processes | Improvement gate |
| COP-01 | App intake and classification | VIF Orchestrator | Product owner | Intake routing | MOP-01, COP-02 | Intake gate |
| COP-02 | Source-of-truth and context lock | Codex Repo Inspector | VIF Orchestrator | Baseline evidence | COP-01, SOP-09 | Baseline gate |
| COP-03 | Requirements and acceptance criteria | Product owner | VIF Orchestrator | Acceptance approval | COP-02, COP-09 | Requirements gate |
| COP-04 | UI/interface design control | UI/Adaptive Reviewer | Runtime Architect | UI gate recommendation | COP-03, COP-06 | UI gate |
| COP-05 | Data table/grid specification | Runtime Architect | UI/Adaptive Reviewer | Data/table spec | COP-04, COP-07 | Data table gate |
| COP-06 | Workflow/runtime specification | Runtime Architect | Supabase Backend Reviewer | Runtime map approval | COP-04, COP-07 | Runtime gate |
| COP-07 | Database/backend/RLS design control | Supabase Backend Reviewer | Security/RLS Reviewer | Backend/RLS evidence | COP-06, SOP-08 | DB/RLS gate |
| COP-08 | Environment and tenant setup | Security/RLS Reviewer | GitHub Release Controller | Tenant/data exposure approval | COP-07, COP-13 | Environment/tenant gate |
| COP-09 | Job card creation and approval | VIF Orchestrator | QA Gatekeeper | Work authorisation | COP-03 to COP-08 | Job-card gate |
| COP-10 | Build/modification control | Assigned worker/agent | Codex Repo Inspector | Execute approved job card | COP-09, COP-11 | Build gate |
| COP-11 | Verification | QA Gatekeeper | Codex Repo Inspector | Verification decision | COP-10, COP-12 | Verification gate |
| COP-12 | Validation/UAT | Product/customer owner | QA Gatekeeper | UAT decision | COP-11, COP-13 | Validation/UAT gate |
| COP-13 | Tenant rollout | GitHub Release Controller | Security/RLS Reviewer | Tenant exposure decision | COP-12, COP-14 | Tenant rollout gate |
| COP-14 | Release and rollback | GitHub Release Controller | System owner | Release/rollback approval | COP-13, SOP-09, SOP-10 | Release gate |
| COP-15 | App support and maintenance | App owner | QA Gatekeeper | Maintenance routing | COP-14, MOP-07 | Maintenance gate |
| COP-16 | Customer change control | Change owner | Product owner | Customer change approval | COP-01, COP-09, COP-12 | Customer change gate |
| SOP-01 | Documented information control | System owner | Process Engineer | Document control | All processes | Documented information gate |
| SOP-02 | Organisational knowledge control | Process Engineer | Lessons Learned Controller | Knowledge approval | MOP-07, SOP-12 | Knowledge gate |
| SOP-03 | Competence and skill control | System owner | Lessons Learned Controller | Skill/competence control | SOP-04 | Competence gate |
| SOP-04 | Agent/worker control | VIF Orchestrator | QA Gatekeeper | Worker assignment | SOP-05, COP-10 | Agent gate |
| SOP-05 | Tool routing and tool qualification | VIF Orchestrator | AI Governance Owner | Tool route approval | MOP-04, SOP-04 | Tool routing gate |
| SOP-06 | Prompt control and prompt quality | Prompt Quality Reviewer | VIF Orchestrator | Prompt approval | MOP-04, COP-10 | Prompt gate |
| SOP-07 | Evidence and record control | QA Gatekeeper | System owner | Evidence acceptance | COP-11, MOP-05 | Evidence gate |
| SOP-08 | Security, tenant and data protection control | Security/RLS Reviewer | Supabase Backend Reviewer | Data/security control | COP-07, COP-08 | Security/data gate |
| SOP-09 | Configuration and version control | GitHub Release Controller | Codex Repo Inspector | Version/config approval | COP-02, COP-14 | Configuration gate |
| SOP-10 | Contingency and continuity control | VIF Orchestrator | QA Gatekeeper | Contingency/rollback route | All processes | Contingency gate |
| SOP-11 | Supplier/tool-provider control | System owner | AI Governance Owner | Provider control | MOP-04, SOP-05, SOP-10 | Supplier/tool gate |
| SOP-12 | Lessons learned and knowledge reuse | Lessons Learned Controller | Process Engineer | Lessons/control updates | MOP-07, SOP-02 | Lessons gate |

## Outputs/records
Process owner matrix and escalation evidence.

## Owner/tool
System owner maintains. VIF Orchestrator verifies owners before work starts.

## Gate controlled
Ownership and authority gate.

## PASS/HOLD/BLOCKED rules
- PASS: every process has owner, backup/escalation, authority and gate.
- HOLD: backup/escalation incomplete.
- BLOCKED: accountable owner missing for controlled or risky work.

## Update trigger
Role change, process change, escalation failure, audit finding or lesson learned.
