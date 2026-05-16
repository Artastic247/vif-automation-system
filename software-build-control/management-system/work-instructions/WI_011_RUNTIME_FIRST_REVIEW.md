# WI_011_RUNTIME_FIRST_REVIEW

## Purpose
Prove that an app/module is a real governed runtime workflow, not only a visual route, table, drawer, chart or mock screen.

## Scope
All app modules, workflow routes, protected actions, data actions and release candidates.

## When to use
Use before schema/build work, before verification, before UAT, before release, and whenever a module-complete claim is made.

## When not to use
Do not use to approve UI-only, mock-only, read-only or ungoverned write behaviour as complete.

## Owner/agent
Runtime Architect with QA Gatekeeper and Process Owner.

## Inputs
Process route, requirements, user/operator workflow, runtime object, role/tenant model, data/backend concept, evidence expectations and current gate.

## Method steps
1. Confirm process route before schema/build.
2. Define start event and start actor.
3. Define runtime object and initial state.
4. Define allowed next actions and state transitions.
5. Identify protected actions.
6. Define evidence rule and approval rule.
7. Define exception/reassessment route.
8. Define audit trace and handoff to adjacent process.
9. Classify runtime-depth level.
10. Hold release until governed workflow evidence exists.

## Outputs/records
Runtime-first review record, runtime-depth classification, protected-action list, evidence rule and gate decision.

## Evidence required
Runtime map, state/action map, backend read/write evidence where applicable, audit trace, approval evidence, role/tenant evidence and handoff record.

## Linked ADP processes
ADP-03, ADP-04, ADP-05, ADP-06, ADP-08, ADP-13, ADP-16, ADP-17 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 operation/design control, Clause 9 verification/audit and Clause 10 improvement.

## Linked gates
Runtime gate, backend/RLS gate, verification gate, validation/UAT gate and release gate.

## Tools allowed
Runtime map, workflow map, data table spec, code review evidence, test evidence, backend/RLS proof, UAT evidence.

## Tools prohibited
Treating route/sidebar/table/chart/drawer/mock data as module completion or release evidence.

## Risks
UI-shell false PASS, schema-first build, ungoverned writes, frontend-only protection, missing audit trail, release without runtime proof.

## Controls
No module is complete because it has a route, sidebar item, table, chart, drawer or mock data. Process route comes before schema/build.

## Interfaces
Process Owner, Runtime Architect, UI/UX Specialist, Backend Coder, Supabase/RLS Engineer, QA Gatekeeper, Release Controller.

## Runtime-depth levels
| Level | Meaning | Gate result |
|---|---|---|
| UI shell only | Screen/route/table/mock only | HOLD |
| Backend read active | Data read proven only | HOLD |
| Backend write active | Write/save proven only | HOLD |
| Governed workflow active | Role/state/evidence/audit/protected action proven | Verification candidate |
| Validation-ready | User/process-owner can test process fit | UAT candidate |
| Release-ready | Verification, validation, rollback and support evidence complete | Release candidate |

## PASS/HOLD/BLOCKED rules
PASS when governed workflow evidence exists. HOLD when runtime proof is partial. BLOCKED when protected action is frontend-only or release is requested without runtime evidence.

## Escalation
Escalate false runtime claim, missing runtime object, protected-action gap, role/tenant risk or release without runtime proof.

## MLA / maturity dependency
M1 may define runtime concept. M2 requires pilot runtime evidence. M3 requires controlled runtime records. M4/M5 require measured runtime performance and audit trends.

## Update trigger
New module, changed workflow, protected action, backend/RLS change, verification finding, UAT failure or RCA/CAPA.
