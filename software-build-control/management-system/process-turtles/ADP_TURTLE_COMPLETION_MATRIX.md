# ADP_TURTLE_COMPLETION_MATRIX

## Purpose
Complete turtle mapping for app-development production processes ADP-01 to ADP-21.

## Scope
The app-development production line from app opportunity/request to support feedback and improvement.

## Owner/agent
Runtime Architect and Process Engineer with VIF Orchestrator and QA Gatekeeper.

## Inputs
App-development operating model, ADP process register, agent assignment matrices, WI_001 to WI_030, runtime-first workflow and evidence matrices.

## Activities/method
For each ADP process define trigger, owner, input, activity, output, receiver, workstation, specialist, WI, gate, runtime-first control where applicable, evidence, KPI, risk/control, interface/handoff, maturity dependency and status.

## Outputs/records
ADP turtle completion matrix.

## Linked processes
ADP-01 to ADP-21.

## Linked agents/workstations
VIF Orchestrator, Context Specialist, Process Owner, Operator/User Tester, Runtime Architect, UI/UX Reviewer, Backend/RLS Engineer, QA Gatekeeper, Release Controller, Support Owner and RCA/CAPA Specialist.

## Linked skills/WIs
WI_001 to WI_030, mapped per ADP row.

## Linked gates
ADP intake, context, domain, workflow, requirements, runtime, UI, backend/RLS, risk, job card, build, review, test, verification, validation, release, support, monitoring and improvement gates.

## Evidence required
ADP-specific record, runtime/evidence where applicable, review output, gate decision and handoff record.

## KPIs/measures
Cycle time, evidence gap rate, rework, runtime gaps, review findings, test pass rate, UAT issues, release readiness, support incidents and recurrence.

## Risks
Jump to tool, weak context, UI shell, RLS risk, false PASS, release without evidence, support gap, repeat failure.

## Controls
Context lock, scope lock, runtime-first, backend/RLS proof, verification, UAT, release/rollback, support and RCA/CAPA gates.

## Interfaces
ADP handoffs to COP/SOP and Clause 9/10.

## Handoffs
ADP sequence handoffs from intake through improvement.

## ADP turtle matrix
| ADP | Trigger/start event | Owner/agent | Input | Activity/method | Output | Receiver | Workstation | Specialist if required | Linked WI | Linked gate | Runtime-first control | Evidence required | KPI/measure | Risk/control | Interface/handoff | Maturity dependency | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADP-01 | App request | VIF Orchestrator | Opportunity/request | Classify app/risk | Intake record | Context Specialist | Management/control | App Owner | WI_002, WI_029 | Intake | Not applicable | Intake evidence | Intake completeness | Wrong classification / risk classify | To ADP-02 | M1+ | STRUCTURAL PASS |
| ADP-02 | Intake approved | Context Specialist | Request/repo/source | Lock context/source | Context pack | Process Owner | Context station | GitHub Controller | WI_001, WI_003, WI_010 | Context | Not applicable | Source lock | Source gaps | Stale source / source lock | To ADP-03 | M1+ | STRUCTURAL PASS |
| ADP-03 | Context locked | Process Owner | Context/domain info | Capture domain truth | Domain record | Operator workflow | Process station | Domain Specialist | WI_004 | Domain | Process route basis | Domain evidence | Truth gaps | Assumption / owner approval | To ADP-04 | M1+ | STRUCTURAL PASS |
| ADP-04 | Domain truth ready | Operator/User Tester | Process truth/user input | Capture workflow | Workflow record | Requirements | User station | UI/UX Specialist | WI_012, WI_018 | Workflow | User route informs runtime | Workflow evidence | Workflow defects | Desk design / user review | To ADP-05 | M1+ | STRUCTURAL PASS |
| ADP-05 | Workflow captured | App Owner | Workflow/domain | Define requirements/acceptance | Acceptance criteria | Runtime Architect | Product station | QA Gatekeeper | WI_002, WI_017 | Requirements | Runtime criteria | Acceptance record | Rework | Vague requirements / criteria | To ADP-06 | M1+ | STRUCTURAL PASS |
| ADP-06 | Requirements approved | Runtime Architect | Acceptance criteria | Define runtime route/module map | Runtime map | UI/backend design | Runtime station | Process Engineer | WI_011 | Runtime | Start event/object/state/actions | Runtime evidence | Runtime gaps | UI shell / runtime-first | To ADP-07/08 | M2+ | STRUCTURAL PASS |
| ADP-07 | Runtime map ready | UI/UX Reviewer | Runtime map | Design UI/interface | UI concept | Build/review | UI station | Operator/User Tester | WI_012 | UI | Link UI to object/actions | UI evidence | UI defects | Dashboard drift / UI review | To ADP-10/14 | M1+ | STRUCTURAL PASS |
| ADP-08 | Runtime/data need | Backend Coder | Runtime/data spec | Design backend/RLS | Backend/RLS concept | Risk/review | Backend station | Supabase/RLS Engineer | WI_013, WI_014 | Backend/RLS | Persistence/protection route | Backend evidence | RLS gaps | Security review | To ADP-09/13 | M2+ | STRUCTURAL PASS |
| ADP-09 | Design concepts ready | Security/Data Reviewer | UI/backend/tenant | Risk/security/tenant review | Risk controls | Job card owner | Security station | Risk Specialist | WI_007, WI_020 | Risk | Protect tenant/data | Risk evidence | Data/security risk | Risk treatment | To ADP-10 | M2+ | STRUCTURAL PASS |
| ADP-10 | Inputs approved | VIF Orchestrator | Requirements/design/risk | Create job card/prompt | Job card/prompt packet | Builder | Orchestration | Prompt Auditor | WI_008, WI_009 | Job card | Runtime evidence requested | Job card/prompt | Prompt drift | Scope/prompt control | To ADP-11 | M1+ | STRUCTURAL PASS |
| ADP-11 | Job card approved | Coder/Builder | Job card/prompt | Execute scoped build | Change set | Reviewer | Build station | Frontend/Backend Coder | WI_008, WI_017 | Build | Only build approved runtime scope | Diff evidence | Scope drift | Job-card-only build | To ADP-12 | M2+ | STRUCTURAL PASS |
| ADP-12 | Build complete | Reviewer | Change set | Code review | Review findings | Backend/UI/test | Review station | Security Reviewer if needed | WI_017 | Review | Runtime/control review | Review record | Missed issue | Review checklist | To ADP-13/14/15 | M2+ | STRUCTURAL PASS |
| ADP-13 | Backend changes ready | Supabase/RLS Engineer | Backend diff | Review DB/RLS/protected actions | RLS proof | QA/test | Backend/RLS station | Security Reviewer | WI_014, WI_015, WI_016 | Backend review | Backend enforcement proof | RLS evidence | Tenant breach | DB/RLS proof | To ADP-15/16 | M2+ | STRUCTURAL PASS |
| ADP-14 | UI changes ready | UI/UX Reviewer | UI diff | UI/adaptive review | UI review | Test owner | UI review station | Operator/User Tester | WI_012 | UI review | UI mapped to runtime | UI review evidence | Usability gap | User review | To ADP-15 | M2+ | STRUCTURAL PASS |
| ADP-15 | Build/reviews ready | Test Owner | Build/review evidence | Plan/execute tests | Test results | QA Gatekeeper | Test station | Integration Specialist if needed | WI_017 | Test | Test runtime paths | Test report | Untested changes | Test plan | To ADP-16 | M2+ | STRUCTURAL PASS |
| ADP-16 | Tests complete | QA Gatekeeper | Test/review evidence | Verify evidence | Verification record | UAT Coordinator | QA station | Evidence Auditor | WI_017, WI_028 | Verification | Governed workflow proof checked | Verification evidence | False PASS | Evidence audit | To ADP-17 | M2+ | STRUCTURAL PASS |
| ADP-17 | Verification PASS | UAT Coordinator | Verified build | Validate with user/process | UAT signoff | Release Controller | UAT station | Process Owner/User | WI_018 | Validation | Process fit validated | UAT evidence | Process misfit | UAT review | To ADP-18 | M2+ | STRUCTURAL PASS |
| ADP-18 | UAT accepted | Release Controller | UAT/release pack | Release/rollback review | Release decision | Support Owner | Release station | Config Controller | WI_019 | Release | Release-ready level only | Release/rollback evidence | Rollback gap | Release gate | To ADP-19 | M3+ | STRUCTURAL PASS |
| ADP-19 | Release approved | Support Owner | Release/support pack | Handover/support readiness | Support pack | Monitoring | Support station | Knowledge Controller | WI_019, WI_027 | Support | Runtime support route | Support evidence | No support owner | Handover | To ADP-20 | M2+ | STRUCTURAL PASS |
| ADP-20 | Support feedback | Support Owner | Feedback/incidents | Monitor/classify feedback | Feedback record | RCA/backlog | Support/incident station | Customer Change Owner | WI_025, WI_029 | Monitoring | Runtime issues classified | Feedback evidence | Untracked issue | Issue classification | To ADP-21 | M3+ | STRUCTURAL PASS |
| ADP-21 | NC/repeat/lesson | RCA/CAPA Specialist | Finding/feedback | Trigger lessons/NC/RCA/CAPA | Improvement action | Knowledge/process owners | Improvement station | Lessons Learned Controller | WI_023-WI_027 | Improvement | Runtime lessons update controls | RCA/CAPA/LL evidence | Repeat failure | CAPA/LL control | To Clause 10/SOP | M2+ | STRUCTURAL PASS |

## PASS/HOLD/BLOCKED rules
PASS requires operational use evidence. STRUCTURAL PASS means ADP turtle rows are completed. HOLD remains for validation, app onboarding, app-repo CI, n8n and DOS FMEA repair.

## Escalation
Escalate skipped runtime-first control, missing evidence, protected-scope breach, release blocker or repeat failure.

## MLA / maturity dependency
ADP processes are structurally M1/M2; operational maturity requires pilot/use evidence and audit.

## Update trigger
ADP model change, app onboarding, audit finding, RCA/CAPA, release/support issue or validation result.
