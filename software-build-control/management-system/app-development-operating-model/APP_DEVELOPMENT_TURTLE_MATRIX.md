# APP_DEVELOPMENT_TURTLE_MATRIX

## Purpose
Provide completed turtle content for ADP-01 to ADP-21.

## Scope
All app-development production processes.

## Owner/agent
Process Engineer with VIF Orchestrator.

## Inputs
ADP process register, role/workstation model, skills/WIs, evidence matrix, interface map and gates.

## Activities/method
Each turtle defines inputs, outputs, owner, supporting roles, resources/tools, methods/skills/WIs, measures/KPIs, risks, controls, records/evidence, interfaces, PDCA, gate and escalation.

## Outputs/records
Completed turtle matrix.

## Linked process
ADP-01 to ADP-21.

## Linked skills/WIs
All process-linked WIs in skill linkage matrix.

## Linked gates
Each ADP process gate.

## Evidence required
Turtle row plus process records when executed.

## Risks
Generic turtle without process-specific content, missing owner, no KPI, no handoff.

## Controls
Every ADP process has a completed row; generic template alone is not enough.

## Interfaces
All ADP handoffs and workstation interfaces.

## Turtle matrix
| ADP | Inputs | Outputs | Owner | Supporting roles | Resources/tools | Methods/skills/WIs | Measures/KPIs | Risks | Controls | Records/evidence | Interfaces | PDCA | Gate | Escalation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADP-01 | Request | Classified intake | Orchestrator | App Owner | Job card | Scope lock | Intake time | Wrong class | Risk classify | Intake record | App owner | Plan | Intake | Unknown scope |
| ADP-02 | Intake/source | Locked context | Context Specialist | GitHub Controller | Repo/files | Source lock | Source gaps | Drift | Current commit | Context pack | GitHub | Plan | Context | Wrong repo |
| ADP-03 | Context | Domain truth | Process Owner | Domain Specialist | Interviews/maps | Process mapping | Truth gaps | Assumption | Owner approval | Domain record | Operator | Plan | Domain | Missing owner |
| ADP-04 | Domain truth | User workflow | Operator Workflow Specialist | Users | Screens/process | Workflow capture | Workflow defects | Desk design | User review | Workflow evidence | Process owner | Plan | Workflow | User conflict |
| ADP-05 | Workflow | Requirements | App Owner | QA | Acceptance matrix | Requirements review | Rework | Vague ask | Acceptance criteria | Req record | Runtime architect | Plan | Requirements | Ambiguity |
| ADP-06 | Requirements | Runtime map | Runtime Architect | Process Engineer | Runtime map | Runtime-first | Runtime gaps | UI shell | State/object rule | Runtime evidence | UI/backend | Plan | Runtime | No runtime object |
| ADP-07 | Runtime map | UI concept | UI/UX | Process Owner | Screen map | UI review | UI defects | Poor layout | Workflow match | UI concept | Frontend | Do | UI | Layout conflict |
| ADP-08 | Runtime map | Backend concept | Backend Coder | RLS Engineer | DB/RLS map | DB/RLS proof | RLS gaps | Unsafe data | Tenant/role review | Backend concept | Supabase | Do | Backend | Data risk |
| ADP-09 | Concepts | Risk controls | Security Reviewer | Tenant owner | Risk register | Risk review | Open risks | Customer data | Risk treatment | Risk evidence | Job card | Check | Risk | High risk |
| ADP-10 | Approved inputs | Job card/prompt | Orchestrator | Prompt Engineer | Prompt register | Prompt quality | Prompt defects | Broad prompt | Scope/prohibit | Job card | Builder | Plan | Job card | Unsafe prompt |
| ADP-11 | Job card | Code/build diff | Builder | Coders | Lovable/Codex | Build WI | Build errors | Scope drift | Diff review | Change evidence | Reviewer | Do | Build | Scope breach |
| ADP-12 | Diff | Review findings | Reviewer | GitHub Controller | Repo diff | Code review | Defect density | Missed issue | Review checklist | Review record | Tester | Check | Review | Critical issue |
| ADP-13 | Backend diff | RLS proof | RLS Engineer | Security | Supabase evidence | Backend proof | RLS defects | Frontend-only | Backend guard | RLS evidence | QA | Check | Backend | Security risk |
| ADP-14 | UI diff | UI review | UI/UX | User tester | Preview/screens | Adaptive review | UI defects | Usability gap | User review | UI evidence | Tester | Check | UI review | User rejection |
| ADP-15 | Build/review | Test results | Test Owner | QA | Test runner | Test plan | Pass rate | Untested code | Test scope | Test report | Verifier | Check | Test | Failed tests |
| ADP-16 | Test results | Verification | QA Gatekeeper | Evidence Auditor | Reports/logs | Verification | Evidence gaps | False PASS | Evidence rule | Verification register | UAT | Check | Verification | Missing evidence |
| ADP-17 | Verified build | UAT result | UAT Coordinator | Process/user | UAT script | Validation | UAT defects | Poor fit | User signoff | UAT record | Release | Check | Validation | UAT fail |
| ADP-18 | UAT/release | Release decision | Release Controller | Config | Release register | Rollback review | Rollback ready | Unsafe release | Rollback proof | Release record | Support | Act | Release | Rollback gap |
| ADP-19 | Release decision | Support readiness | Support Owner | Knowledge | Support pack | Handover | Support gaps | No support | Owner assigned | Handover record | Monitoring | Act | Support | No owner |
| ADP-20 | Live/support | Feedback | Support Owner | Incident Owner | Feedback log | Monitoring | Incident trend | Untracked issues | Classification | Feedback record | RCA/backlog | Check/Act | Monitoring | Critical incident |
| ADP-21 | Feedback/NC | Improvement trigger | RCA/CAPA Specialist | LL Controller | Clause 10 regs | RCA/CAPA/LL | Recurrence | Repeat failure | NC/CAPA route | Improvement record | CI/knowledge | Act | Improvement | Repeat failure |

## PASS/HOLD/BLOCKED rules
PASS when every ADP row is complete and used evidence exists for applied processes. HOLD when use evidence is pending. BLOCKED when a required ADP owner/control is missing for active work.

## Escalation
Escalate missing owner, missing runtime evidence, missing release evidence or repeated failure.

## Update trigger
Process change, app onboarding, audit finding, RCA/CAPA or lesson learned.
