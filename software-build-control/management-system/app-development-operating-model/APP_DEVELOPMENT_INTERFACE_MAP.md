# APP_DEVELOPMENT_INTERFACE_MAP

## Purpose
Define controlled interfaces and handoff evidence between app-development workstations and processes.

## Scope
Interfaces from app owner/process owner through build, test, release, support, audit, RCA/CAPA, app onboarding, app-repo CI and n8n readiness.

## Owner/agent
Process Engineer with VIF Orchestrator.

## Inputs
ADP process register, workstation model, handoff needs, evidence matrix and gate rules.

## Activities/method
For each interface define input, output, sender, receiver, control point, evidence required, risk, escalation and gate impact.

## Outputs/records
Interface map and handoff-control evidence.

## Linked process
ADP-01 to ADP-21.

## Linked skills/WIs
Interface mapping, source lock, runtime-first review, UI/backend review, evidence audit, release/rollback, RCA/CAPA and lessons learned.

## Linked gates
Interface gates at handoffs and protected controls.

## Evidence required
Interface input/output record, sender/receiver confirmation and gate decision.

## Risks
Dropped handoff, wrong owner, missing evidence, app-repo CI/n8n triggered before onboarding, lessons not converted into updates.

## Controls
No handoff is complete without input, output, sender, receiver, control point and evidence.

## Interfaces
| Interface | Input | Output | Sender | Receiver | Control point | Evidence required | Risk | Escalation | Gate impact |
|---|---|---|---|---|---|---|---|---|---|
| App owner -> Process owner | App request | Process truth need | App Owner | Process Owner | Intake/domain gate | Request and process scope | Wrong process | Orchestrator | HOLD |
| Process owner -> Runtime architect | Process truth | Runtime route need | Process Owner | Runtime Architect | Runtime gate | Approved process truth | Runtime mismatch | QA | HOLD |
| Operator/user -> Process owner | User workflow | Workflow confirmation | Operator/User | Process Owner | Workflow gate | User workflow evidence | Desk design | Product Owner | HOLD |
| Process owner -> Domain specialist | Process gap | Domain clarification | Process Owner | Domain Specialist | Domain gate | Domain note | Incorrect domain | QA | HOLD |
| Runtime architect -> UI/UX specialist | Runtime map | UI concept | Runtime Architect | UI/UX Specialist | UI gate | Runtime map | UI not workflow-fit | Product Owner | HOLD |
| Runtime architect -> Backend/RLS engineer | Runtime/data need | Backend/RLS concept | Runtime Architect | Supabase/RLS Engineer | Backend gate | Runtime/data map | RLS gap | Security | HOLD/BLOCK |
| Frontend coder -> Backend coder | UI data need | API/service need | Frontend Coder | Backend Coder | Build interface | Contract note | Integration mismatch | Runtime Architect | HOLD |
| Backend coder -> Supabase/RLS reviewer | Backend diff | RLS review need | Backend Coder | Supabase/RLS Engineer | RLS review | Diff/RLS evidence | Tenant breach | Security | BLOCK |
| Coder -> Tester | Build diff | Test scope | Builder | Test Owner | Test gate | Diff/test plan | Untested change | QA | HOLD |
| Tester -> QA Gatekeeper | Test results | Verification need | Test Owner | QA Gatekeeper | Verification gate | Test report | False PASS | Evidence Auditor | HOLD/BLOCK |
| QA Gatekeeper -> Release Controller | Verification/UAT pack | Release review | QA Gatekeeper | Release Controller | Release gate | Verification/UAT evidence | Unsafe release | Product Owner | HOLD/BLOCK |
| Release Controller -> Support Owner | Release decision | Support handover | Release Controller | Support Owner | Support gate | Release/support pack | No support | Management Review | HOLD |
| Auditor -> RCA/CAPA Specialist | Finding | NC/RCA/CAPA trigger | Auditor | RCA/CAPA Specialist | Clause 10 gate | Finding evidence | No corrective action | QA | HOLD/BLOCK |
| Lessons Learned Controller -> Skill/prompt/process owners | Lesson | Update requirement | LL Controller | Artefact owners | Improvement gate | Lesson evidence | Repeat failure | CI Owner | HOLD |
| App onboarding -> App-repo CI | Onboarding PASS | CI readiness request | Orchestrator | GitHub CI Controller | CI readiness gate | Onboarding evidence | Premature CI | QA | HOLD |
| App onboarding -> n8n readiness | Onboarding/maturity evidence | n8n readiness request | Orchestrator | n8n Controller | Automation gate | Maturity evidence | Automating chaos | MLA Assessor | HOLD/BLOCK |

## PASS/HOLD/BLOCKED rules
PASS when all required interface evidence exists. HOLD when handoff evidence is incomplete. BLOCKED when protected interface has no control or evidence.

## Escalation
Escalate missing handoff, security/data risk, premature CI/n8n, or lesson not converted into control.

## Update trigger
Process change, workstation change, audit finding, app onboarding or RCA/CAPA.
