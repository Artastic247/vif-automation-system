# APP_DEVELOPMENT_AGENT_ASSIGNMENT_MATRIX

## Purpose
Assign one primary workstation/agent to every ADP process so app-development work is routed through controlled production stations.

## Scope
ADP-01 to ADP-21 app-development processes.

## Owner/agent
VIF Orchestrator.

## Inputs
ADP process register, workstation model, specialist matrix, skill/WI matrix, current job card and maturity level.

## Activities/method
Map each ADP process to a primary workstation, supporting workstation, specialist requirement, skill/WI, evidence output, gate decision authority and escalation route.

## Outputs/records
Agent/workstation assignment matrix and gate authority record.

## Linked process
ADP-01 to ADP-21.

## Linked skills/WIs
Scope lock, context lock, source lock, process mapping, runtime-first review, UI review, DB/RLS proof, prompt quality, code review, test planning, verification, validation, release/rollback, RCA/CAPA and lessons learned.

## Linked gates
All ADP process gates.

## Evidence required
Assignment row, produced evidence and gate decision per ADP process.

## Risks
Unassigned work, wrong workstation, unsupported specialist, uncontrolled handoff, false PASS.

## Controls
Every ADP process must have one primary workstation/agent and gate authority before active use.

## Interfaces
Workstation handoffs and specialist activation interfaces.

## Assignment matrix
| Process | Primary workstation/agent | Supporting workstation | Specialist required | Skill/WI required | Evidence output | Gate decision authority | Escalation |
|---|---|---|---|---|---|---|---|
| ADP-01 App intake and classification | VIF Orchestrator | Product/App Owner | Domain Specialist if unclear | Scope lock | Intake record | VIF Orchestrator | Unknown scope or risk |
| ADP-02 Context/source-of-truth lock | Context Management Specialist | GitHub Controller | Configuration Controller | Context lock, source lock | Context pack | QA Gatekeeper | Wrong repo/branch/source |
| ADP-03 Domain truth and process-owner capture | Process Owner | Domain Specialist | ISO/IATF Specialist when regulated | Process mapping | Domain truth record | Process Owner | Missing process owner |
| ADP-04 User/operator workflow capture | Operator Workflow Specialist | Operator/User Tester | UI/UX Specialist | User workflow capture | Workflow evidence | Process Owner | Workflow conflict |
| ADP-05 Requirements and acceptance criteria | Product/App Owner | QA Gatekeeper | Compliance Specialist if needed | Requirements review | Acceptance criteria | Product/App Owner | Vague acceptance |
| ADP-06 Runtime-first process route and module map | Runtime Architect | Process Engineer | Security/Data Specialist if protected actions | Runtime-first review | Runtime map | QA Gatekeeper | No runtime object/state |
| ADP-07 UI/interface design control | UI/UX Specialist | Frontend Coder | Operator/User Tester | UI/interface review | UI concept | Product/App Owner | UI not process-fit |
| ADP-08 Data/backend/RLS design control | Backend Coder | Supabase/RLS Engineer | Security/Data Specialist | DB/RLS proof | Backend/RLS concept | Supabase/RLS Engineer | Tenant/security risk |
| ADP-09 Risk/security/tenant review | Security/Data Protection Specialist | QA Gatekeeper | ISO/IEC 27001 Specialist | Risk/security review | Risk/tenant evidence | QA Gatekeeper | High risk untreated |
| ADP-10 Job card and prompt packet creation | VIF Orchestrator | Prompt Engineer | Tool/Supplier Reviewer if new tool | Prompt quality review | Job card/prompt packet | QA Gatekeeper | Broad unsafe prompt |
| ADP-11 Coding/build execution | Codex Implementer or Lovable Builder | Frontend/Backend Coder | Integration Specialist if required | Build execution WI | Change evidence | VIF Orchestrator | Scope breach |
| ADP-12 Code review | Claude Code Reviewer | GitHub Controller | Security/Data Specialist if sensitive | Code review | Review record | QA Gatekeeper | Critical review finding |
| ADP-13 Backend/RLS review | Supabase/RLS Engineer | Backend Coder | Security/Data Specialist | Backend/RLS proof | RLS evidence | Supabase/RLS Engineer | RLS/protected-action gap |
| ADP-14 UI/adaptive review | UI/UX Specialist | Operator/User Tester | Frontend Coder | UI/adaptive review | UI review evidence | Product/App Owner | Usability rejection |
| ADP-15 Test planning and test execution | Test Owner | QA Gatekeeper | Integration Test Owner if needed | Test planning | Test report | QA Gatekeeper | Failed/insufficient tests |
| ADP-16 Verification | QA Gatekeeper | Evidence Auditor | Validator Auditor if checker involved | Verification review | Verification register | QA Gatekeeper | Evidence gap/false PASS |
| ADP-17 Validation/UAT | UAT Coordinator | Process Owner/User | Operator/User Tester | Validation/UAT review | UAT signoff | Product/App Owner | UAT fail/process misfit |
| ADP-18 Release/rollback review | Release Controller | Configuration Controller | Release Auditor | Release/rollback review | Release/rollback record | Release Controller | Rollback not proven |
| ADP-19 Handover/support readiness | Support Owner | Knowledge Controller | Maintenance Owner | Handover/support WI | Support pack | Support Owner | No support owner |
| ADP-20 Post-release monitoring and feedback | Support Owner | Incident Owner | Customer Change Owner | Feedback review | Feedback/incident record | Support Owner | Critical incident |
| ADP-21 Lessons learned / NC / RCA / CAPA trigger | RCA/CAPA Specialist | Lessons Learned Controller | Organisational Knowledge Controller | RCA, CAPA, lessons learned | Improvement trigger | RCA/CAPA Specialist | Repeat/systemic failure |

## PASS/HOLD/BLOCKED rules
PASS when each ADP process has assigned primary agent, evidence output and gate authority. HOLD when supporting role or WI is incomplete. BLOCKED when active work has no primary owner or gate authority.

## Escalation
Escalate unassigned process, wrong workstation, protected-scope breach or missing evidence.

## Update trigger
New workstation, process change, audit finding, app onboarding or RCA/CAPA.
