# APP_DEVELOPMENT_RUNTIME_FIRST_WORKFLOW

## Purpose
Enforce runtime-first control for every app/module so app development proves real governed operation before release or onboarding.

## Scope
All modules, workflows, protected actions, UI routes, backend/data functions and release decisions.

## Owner/agent
Runtime Architect with QA Gatekeeper.

## Inputs
Requirements, process route, domain truth, user workflow, data/backend concept, role/tenant model and risk review.

## Activities/method
For every module define start event, start actor, runtime object, initial state, next allowed actions, protected actions, evidence rule, approval rule, exception/reassessment rule, audit trace and handoff to adjacent process.

## Outputs/records
Runtime-first workflow record, runtime-depth decision and evidence requirements.

## Linked process
ADP-06, ADP-08, ADP-13, ADP-16, ADP-17 and ADP-18.

## Linked skills/WIs
Runtime-first review, process mapping, interface mapping, DB/RLS proof, protected-action backend enforcement, evidence audit, validation/UAT, release/rollback.

## Linked gates
Runtime, backend, verification, validation and release gates.

## Evidence required
Runtime object/state/action map, backend read/write proof, role/tenant proof, audit trace, protected-action evidence and approval evidence where required.

## Risks
Route/sidebar/table/chart/mock data treated as completion; backend read treated as persistence; backend write treated as governed workflow; frontend-only protection.

## Controls
A module is not complete because there is a route, sidebar item, table, drawer, chart or mock UI. Backend read alone does not equal persistence. Backend write alone does not equal governed workflow. Governed workflow requires role control, evidence, audit trail, protected-action control and approval where required.

## Interfaces
Runtime architect to UI/UX, backend/RLS, tester, verifier, validator and release controller.

## Runtime-depth levels
| Level | Meaning | Gate impact |
|---|---|---|
| UI shell only | Route/screen/table/mock exists only | HOLD, not runtime complete |
| Backend read active | Data can be read | HOLD, no persistence claim |
| Backend write active | Data can be saved | HOLD until governance proven |
| Governed workflow active | Roles, states, evidence, audit and protected actions proven | Verification candidate |
| Validation-ready | User/process-owner can test process fit | UAT candidate |
| Release-ready | Verification, validation, rollback and support evidence complete | Release candidate |

## Runtime workflow fields
| Field | Required content |
|---|---|
| Start event | What starts the workflow |
| Start actor | Role/person/system that starts it |
| Runtime object | Business object being controlled |
| Initial state | Starting state |
| Next allowed actions | Valid transitions |
| Protected actions | Actions requiring backend/service/RLS guard |
| Evidence rule | Record/proof required |
| Approval rule | Who approves and when |
| Exception route | Reassessment or stop route |
| Audit trace | Log/evidence trail |
| Handoff | Adjacent process/role |

## PASS/HOLD/BLOCKED rules
PASS when governed workflow evidence exists. HOLD when only shell/read/write evidence exists. BLOCKED when protected action is frontend-only or runtime object/state is undefined.

## Escalation
Escalate protected-action gap, role/tenant risk, false runtime claim or release request without runtime evidence.

## Update trigger
New module, workflow change, backend/RLS change, release request, audit finding or RCA/CAPA.
