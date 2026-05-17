# APP_DEVELOPMENT_SKILL_WI_LINKAGE_MATRIX

## Purpose
Map ADP processes to required skills and work instructions.

## Scope
ADP-01 to ADP-21 and all critical app-development skills/WIs.

## Owner/agent
Skill/WI Audit Specialist with VIF Orchestrator.

## Inputs
ADP process register, skill register, WI status, maturity record and gate rules.

## Activities/method
For each ADP process define required skill/WI, trigger, input, output, evidence, gate, maturity dependency and gap if WI is not released.

## Outputs/records
Skill/WI linkage matrix and WI release-gap record.

## Linked process
ADP process architecture.

## Linked skills/WIs
Context lock, scope lock, source lock, process mapping, interface mapping, runtime-first, UI review, workflow capture, data table/grid, DB/RLS proof, protected-action backend enforcement, migration rollback, prompt quality, code review, testing, verification, validation, release, evidence audit, onboarding, RCA/CAPA, lessons learned, knowledge update.

## Linked gates
All ADP gates.

## Evidence required
Linked WI reference, use evidence and gate output.

## Risks
Skills remain register-only, user cannot execute WI, wrong method used, weak evidence.

## Controls
If WI is not released, ADP process remains HOLD for operational use.

## Interfaces
Skill owners, process owners, agents and QA Gatekeeper.

## Skill/WI linkage matrix
| Process | Required skill/WI | Trigger | Input | Output | Evidence | Gate | Maturity dependency | Gap if WI not released |
|---|---|---|---|---|---|---|---|---|
| ADP-01 | Scope lock | New request | Request | Classified scope | Intake record | Intake | M1 | Scope drift |
| ADP-02 | Context lock; source-of-truth lock | Work starts | Repo/source | Locked context | Context pack | Context | M1 | Wrong truth |
| ADP-03 | Process mapping | Domain capture | Process input | Domain truth | Process record | Domain | M1 | Assumed process |
| ADP-04 | User/operator workflow capture | User workflow needed | User input | Workflow record | Workflow evidence | Workflow | M1 | Desk design |
| ADP-05 | Requirements review | Acceptance needed | Workflow | Requirements | Acceptance matrix | Requirements | M1 | Vague build |
| ADP-06 | Runtime-first review | Module design | Requirements | Runtime map | Runtime evidence | Runtime | M2 | UI shell |
| ADP-07 | UI/interface review | UI concept | Runtime map | UI concept | Screen evidence | UI | M1 | Visual drift |
| ADP-08 | Data table/grid review; database/RLS proof | Data/backend design | Runtime map | Backend concept | DB/RLS evidence | Backend | M2 | Unsafe data |
| ADP-09 | Risk/security review | Risk review | Concepts | Risk controls | Risk evidence | Risk | M2 | Data/security miss |
| ADP-10 | Prompt quality review | Build packet | Job card | Prompt packet | Prompt evidence | Prompt | M1 | Broad prompt |
| ADP-11 | Build execution WI | Build starts | Prompt/job card | Code diff | Change evidence | Build | M2 | Scope breach |
| ADP-12 | Code review | Diff ready | Code diff | Review record | Review evidence | Review | M2 | Bad code escapes |
| ADP-13 | Protected-action backend enforcement; DB/RLS proof | Backend review | Backend diff | RLS proof | Backend evidence | Backend review | M2 | Frontend-only control |
| ADP-14 | UI/adaptive review | UI ready | UI diff | UI review | UI evidence | UI review | M2 | Poor usability |
| ADP-15 | Test planning | Test ready | Build | Test results | Test report | Test | M2 | Untested change |
| ADP-16 | Verification review; evidence audit | Tests done | Test results | Verification | Verification record | Verification | M2 | False PASS |
| ADP-17 | Validation/UAT review | Verified build | Build/evidence | UAT signoff | UAT evidence | Validation | M2 | Process misfit |
| ADP-18 | Release/rollback review; migration rollback safety | Release request | UAT/release pack | Release decision | Release/rollback evidence | Release | M3 | Unsafe release |
| ADP-19 | Handover/support readiness | Release approved | Release pack | Support pack | Handover evidence | Support | M2 | No support |
| ADP-20 | Feedback review | Support feedback | Feedback | Classified issue | Feedback evidence | Monitoring | M3 | Untracked issues |
| ADP-21 | RCA; CAPA; lessons learned; organisational knowledge update | NC/repeat/lesson | Issue evidence | Improvement trigger | RCA/CAPA/LL evidence | Improvement | M2 | Repeat failure |

## PASS/HOLD/BLOCKED rules
PASS when all used processes have released WI or controlled equivalent. HOLD when WI release evidence is incomplete. BLOCKED when active process lacks critical WI.

## Escalation
Escalate missing critical WI, repeated method failure or unsupported app build.

## Update trigger
New WI, process change, audit finding, RCA/CAPA or lesson learned.
