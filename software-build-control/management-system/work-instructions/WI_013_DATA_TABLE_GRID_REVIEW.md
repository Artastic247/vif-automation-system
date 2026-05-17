# WI_013_DATA_TABLE_GRID_REVIEW

## Purpose
Review tables and grids so displayed data, row actions, lifecycle controls and evidence fields support a governed workflow.

## Scope
All app tables, grids, lists, registers and data-entry views.

## When to use
Use before table/grid build, during code review, before verification/UAT, and whenever table evidence is used to claim runtime completion.

## When not to use
Do not use to approve backend persistence or security unless backend/RLS proof also exists.

## Owner/agent
UI/UX Specialist with Backend Coder, Supabase/RLS Engineer and QA Gatekeeper.

## Inputs
Table/grid source of truth, runtime object, columns, filters, row actions, bulk actions, lifecycle fields, role rules, evidence fields, audit trail expectations and backend proof.

## Method steps
1. Confirm table/grid source of truth.
2. Review columns and field meaning.
3. Review filters and search.
4. Review row actions and bulk actions.
5. Review edit/create/deactivate/supersede controls.
6. Review status/lifecycle fields.
7. Review role-based action availability.
8. Review evidence fields and audit trail needs.
9. Confirm backend read/write proof requirement.
10. Confirm no mock/demo data is used as production PASS evidence.

## Outputs/records
Data table/grid review record, lifecycle/action finding, backend-proof requirement and gate decision.

## Evidence required
Data table spec, UI evidence, backend read/write proof, role action matrix, lifecycle rules and audit trail evidence.

## Linked ADP processes
ADP-06, ADP-07, ADP-08, ADP-11, ADP-13, ADP-16, ADP-17 and ADP-18.

## Linked MOP/COP/SOP processes
Clause 8 operation/design, Clause 9 evidence/app audit and Clause 10 improvement.

## Linked gates
UI, backend/RLS, verification, validation and release gates.

## Tools allowed
Data table spec, screen map, backend proof, RLS evidence, test report, audit log.

## Tools prohibited
Using front-end table display as proof of persistence, tenant isolation, lifecycle control or auditability.

## Risks
Wrong source of truth, missing lifecycle, unsafe bulk actions, role mismatch, stale/mock data, no audit trail.

## Controls
Table/grid must define source, lifecycle, role actions, evidence, backend read/write and audit expectations.

## Interfaces
UI/UX, Backend Coder, Supabase/RLS Engineer, Evidence Auditor, QA Gatekeeper.

## PASS/HOLD/BLOCKED rules
PASS when table/grid is source-linked and backend/evidence expectations are met. HOLD when fields/actions are incomplete. BLOCKED when actions can alter protected data without backend/RLS control.

## Escalation
Escalate unsafe action, lifecycle deletion risk, mock-data PASS claim or role/tenant leakage.

## MLA / maturity dependency
M1 table concept. M2 pilot table evidence. M3 released lifecycle control. M4/M5 KPI/audit trend control.

## Update trigger
New table, column/action change, lifecycle change, role/RLS change, defect or audit finding.
