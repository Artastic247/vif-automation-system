# WI_012_UI_INTERFACE_REVIEW

## Purpose
Review UI/interface design against the runtime workflow and user/operator needs before treating screens as build-ready or validation-ready.

## Scope
Routes, pages, tabs, panels, tables, drawers, forms, buttons, badges, loading/empty/error states and operator/admin/user views.

## When to use
Use during UI concept, UI build review, adaptive review, operator review, UAT preparation and before release.

## When not to use
Do not use to claim backend, persistence, RLS, runtime or release readiness.

## Owner/agent
UI/UX Specialist with Process Owner, Operator/User Tester and QA Gatekeeper.

## Inputs
Runtime object, workflow, role views, screen concept, data fields, protected actions, evidence expectations and accessibility/usability needs.

## Method steps
1. Confirm screen purpose.
2. Review route/page/tab/panel structure.
3. Review operator/admin/user role views.
4. Review action buttons and protected actions.
5. Review disabled/hidden states.
6. Review loading, empty and error states.
7. Review touch/tablet usability where relevant.
8. Review status badges and wording.
9. Link UI to runtime object and evidence.
10. Check dashboard-first drift.

## Outputs/records
UI/interface review record, issues list, role-view decision, usability finding and gate status.

## Evidence required
Screen map, screenshots/previews, role view notes, action/protected-action list, user/operator feedback and UI review decision.

## Linked ADP processes
ADP-04, ADP-06, ADP-07, ADP-11, ADP-14, ADP-17 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 design/development control, Clause 9 app/product audit and Clause 10 improvement.

## Linked gates
UI concept gate, UI review gate, validation/UAT gate and release gate.

## Tools allowed
Screen map, UI prototype, screenshots, user workflow, UAT notes, evidence register.

## Tools prohibited
Dashboard-first design that bypasses runtime workflow or operator evidence; UI-only PASS claims.

## Risks
Pretty UI but poor process fit, hidden protected actions, missing states, tablet/operator usability failure, dashboard-first drift.

## Controls
UI must link to runtime object, role view, evidence need and protected action control.

## Interfaces
Runtime Architect, Frontend Coder, Operator/User Tester, Process Owner, QA Gatekeeper.

## PASS/HOLD/BLOCKED rules
PASS when UI is process-fit and evidence-linked. HOLD when states/views are incomplete. BLOCKED when UI enables protected action without backend control or hides critical runtime risk.

## Escalation
Escalate UI-only completion claim, protected action mismatch, operator rejection or release request with unresolved UI blockers.

## MLA / maturity dependency
M1 concept review. M2 pilot UI evidence. M3 released UI criteria. M4/M5 usability trends and improvement evidence.

## Update trigger
New screen, changed workflow, role change, UAT feedback, defect, audit finding or RCA/CAPA.
