# AGENT_PROCESS_ASSIGNMENT_MATRIX

## Purpose
Map agents to management-system processes and ADP-01 to ADP-21 app-development processes.

## Scope
All MOP/COP/SOP processes and all ADP app-development processes.

## Owner/agent
VIF Orchestrator with Process Engineer and QA Gatekeeper.

## Inputs
Master agent register, process architecture, ADP process register, work instructions and current maturity levels.

## Activities/method
Assign one primary agent and supporting/specialist agents to each process. Confirm evidence output, gate authority and escalation path.

## Outputs/records
Agent-to-process assignment matrix and process accountability record.

## Linked processes
Clause 4 to Clause 10 management processes, MOP/COP/SOP process set and ADP-01 to ADP-21.

## Linked skills/WIs
WI_001 to WI_030 as applicable by process.

## Linked gates
All management-system and ADP gates.

## Evidence required
Assignment row, owner confirmation, work output and gate decision evidence.

## Risks
Process without owner, wrong specialist, handoff gap, false PASS, uncontrolled implementation.

## Controls
Every process must have one primary owner/agent and defined gate authority.

## Interfaces
Process owners, agent owners, specialist reviewers, QA Gatekeeper and Management Review Owner.

## MOP/COP/SOP assignment
| Process family | Process/control | Primary agent | Supporting/specialist agents | Evidence output | Gate authority |
|---|---|---|---|---|---|
| Clause 4 | Context, interested parties, scope, process architecture | Context Management Specialist | Process Engineer, Standards Specialists | Context/process records | QA Gatekeeper |
| Clause 5 | Leadership, authority, accountability | VIF Orchestrator | Management Review Owner, QA Gatekeeper | Authority records | VIF Orchestrator |
| Clause 6 | Risk, objectives, change planning | ISO 31000/31010 Risk Specialist | Credit-Burn Controller, Security/Data Reviewer | Risk/objective records | QA Gatekeeper |
| Clause 7 | Competence, WIs, prompts, tools, knowledge | Organisational Knowledge Controller | Prompt Auditor, Tool Reviewer, Skill/WI Auditor | Support/knowledge records | QA Gatekeeper |
| Clause 8 | Operation, build/change/release/support | VIF Orchestrator | Runtime Architect, Coders, Release Controller | Job cards/release records | QA Gatekeeper/Release Controller |
| Clause 9 | Audit, MLA, evidence and performance evaluation | Internal Audit Specialist | MLA Assessor, Evidence Auditor, Specialist Auditors | Audit/MLA records | QA Gatekeeper |
| Clause 10 | NC, RCA/CAPA, CI, lessons, knowledge update | RCA/CAPA Specialist | CI Owner, Lessons Learned Controller, Knowledge Controller | NC/RCA/CAPA/improvement records | RCA/CAPA Specialist |

## ADP assignment
| ADP | Process | Primary agent | Supporting/specialist agents | Evidence output | Gate authority |
|---|---|---|---|---|---|
| ADP-01 | App intake/classification | VIF Orchestrator | App Owner, QA Gatekeeper | Intake record | VIF Orchestrator |
| ADP-02 | Context/source lock | Context Management Specialist | GitHub Controller, Evidence Auditor | Context/source record | QA Gatekeeper |
| ADP-03 | Domain/process truth | Process Owner | Domain Specialist, Process Engineer | Domain truth record | Process Owner |
| ADP-04 | User/operator workflow | Operator/User Tester | UI/UX Reviewer, Process Owner | Workflow evidence | Process Owner |
| ADP-05 | Requirements/acceptance | App Owner | QA Gatekeeper, Compliance Specialist | Acceptance criteria | App Owner/QA |
| ADP-06 | Runtime route/module map | Runtime Architect | Process Engineer, Security Reviewer | Runtime map | QA Gatekeeper |
| ADP-07 | UI/interface design | UI/UX Interface Reviewer | Frontend Coder, Operator/User Tester | UI review | App Owner |
| ADP-08 | Data/backend/RLS design | Backend Coder | Supabase/RLS Engineer, Security Reviewer | Backend/RLS concept | Supabase/RLS Engineer |
| ADP-09 | Risk/security/tenant review | Security/Data Reviewer | Risk Specialist, Tenant/App Owner | Risk/security evidence | QA Gatekeeper |
| ADP-10 | Job card/prompt packet | VIF Orchestrator | Prompt Audit Specialist, Tool Reviewer | Job card/prompt | QA Gatekeeper |
| ADP-11 | Coding/build execution | Frontend/Backend Coder | Lovable Builder/Codex Implementer, GitHub Controller | Code/build evidence | VIF Orchestrator |
| ADP-12 | Code review | AI/Code Reviewer | GitHub Controller, Security Reviewer | Review record | QA Gatekeeper |
| ADP-13 | Backend/RLS review | Supabase/RLS Engineer | Security/Data Reviewer, Backend Coder | RLS proof | Supabase/RLS Engineer |
| ADP-14 | UI/adaptive review | UI/UX Interface Reviewer | Operator/User Tester | UI/adaptive evidence | App Owner |
| ADP-15 | Test planning/execution | Test Owner | QA Gatekeeper, Integration Specialist | Test report | QA Gatekeeper |
| ADP-16 | Verification | QA Gatekeeper | Evidence Auditor, Validator Auditor | Verification record | QA Gatekeeper |
| ADP-17 | Validation/UAT | Operator/User Tester | Process Owner, App Owner, UAT Coordinator | UAT record | App Owner |
| ADP-18 | Release/rollback review | Release/Configuration Controller | QA Gatekeeper, Support Owner | Release/rollback record | Release Controller |
| ADP-19 | Handover/support readiness | Support Owner | Knowledge Controller, Maintenance Owner | Support pack | Support Owner |
| ADP-20 | Monitoring/feedback | Support Owner | Incident Owner, Customer Change Owner | Feedback/incident record | Support Owner |
| ADP-21 | Lessons/NC/RCA/CAPA trigger | RCA/CAPA Specialist | Lessons Learned Controller, Knowledge Controller | Improvement trigger | RCA/CAPA Specialist |

## PASS/HOLD/BLOCKED rules
PASS when every process has primary agent and gate authority. HOLD when supporting role evidence is incomplete. BLOCKED when active work lacks owner or protected decision authority.

## Escalation
Escalate unassigned process, missing owner, false PASS, security/data risk, release risk or automation bypass.

## MLA / maturity dependency
Processes below M2 require manual review; M3+ may operate in defined scope; M4/M5 require audit/KPI evidence.

## Update trigger
Process change, new ADP process, role change, audit finding, RCA/CAPA or app onboarding.
