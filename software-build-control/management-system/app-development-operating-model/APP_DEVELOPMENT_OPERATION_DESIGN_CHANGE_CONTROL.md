# APP_DEVELOPMENT_OPERATION_DESIGN_CHANGE_CONTROL

## Purpose
Define operational controls for app intake, design, build, change, verification, validation, release, support and customer change.

## Scope
All app-development and repair work, including UI/interface, runtime/workflow, data table/grid, backend/RLS, tenant/environment, job cards, builds, verification, validation, release/rollback and support changes.

## Owner/agent
VIF Orchestrator with Runtime Architect, QA Gatekeeper and Release Controller.

## Inputs
Approved context/source lock, requirements, runtime map, design concept, risk/security review, job card, prompt packet, build evidence, test evidence, UAT, release/rollback evidence and support feedback.

## Activities/method
Control intake, source lock, requirements, UI/interface design, workflow/runtime design, data/backend/RLS design, environment/tenant setup, job card approval, build/modification, verification, validation/UAT, release/rollback, support/maintenance, customer change control and deletion/lifecycle decisions.

## Outputs/records
Controlled design/build/change records, verification evidence, validation evidence, release/rollback decision, support/change records and lifecycle decision.

## Linked ADP processes
ADP-01 to ADP-21.

## Linked MOP/COP/SOP processes
Clause 8 operation, design/development/change control, Clause 9 verification/audit, Clause 10 NC/RCA/CAPA.

## Linked skills/WIs
Requirements review, runtime-first, UI review, DB/RLS proof, protected-action backend enforcement, migration replay/rollback, prompt quality, code review, verification, validation/UAT, release/rollback.

## Linked gates
Context, requirements, runtime, UI, backend/RLS, risk/security, job card, build, review, test, verification, validation, release, support/change gates.

## Evidence required
Approved source/context, acceptance criteria, runtime map, design records, risk controls, job card, diff/review/test evidence, UAT, release/rollback and support handover.

## Risks
Design/build without context, backend/RLS change without rollback, release without V&V evidence, unsupported customer claim, premature onboarding, uncontrolled deletion.

## Controls
No design/build without approved context and source lock. No backend/RLS change without runtime and rollback gate. No release without verification/validation evidence. No customer-facing claim without approval. No app onboarding until operating-model gate passes. Deletion requires lifecycle rule and risk review.

## Interfaces
App owner, process owner, runtime architect, UI/UX, backend/RLS, security, builders, reviewers, testers, release, support and customer change owner.

## PASS/HOLD/BLOCKED rules
PASS when required operation/design/change evidence exists. HOLD when non-critical evidence pending. BLOCKED when protected action, RLS, customer data, release or deletion lacks approval/evidence.

## Escalation
Escalate uncontrolled app change, schema/RLS change without gate, release without evidence, customer claim risk or lifecycle deletion risk.

## Update trigger
New build, change request, customer change, support issue, release request, audit finding or RCA/CAPA.
