# UI_INTERFACE_CONTROL.md

## Purpose
Control UI/interface completeness before UI build, UI repair, or UI automation so screens are not built from incomplete prototypes or truncated prompts.

## Scope
Applies to routes, pages, tabs, panels, tables/grids, modals, drawers, buttons, actions, badges, status indicators, empty/loading/error states, role-specific visibility, responsive layout, accessibility basics, and dashboard/execution-board design.

## Inputs
- Approved app context and job card.
- HTML prototype, screenshot, wireframe, or user requirement.
- SCREEN_MAP and DATA_TABLE_SPEC where applicable.
- Workflow/runtime map for actions and statuses.

## Activities/checklist
Before UI build or UI repair, confirm:

- Screen map exists.
- Route/page is defined.
- Tabs and navigation are defined.
- Panels, cards, tables, grids, and modals are defined.
- Buttons/actions are mapped to workflow/runtime actions.
- Badges/status indicators have visual and runtime rules.
- Empty, loading, error, disabled, locked, and view-only states are defined.
- Role-specific visibility is defined.
- Responsive behaviour is defined.
- Accessibility basics are considered.
- Table/grid work has DATA_TABLE_SPEC.
- Dashboard/execution-board work has runtime queue/workflow behind it.

Rules:
- No UI build without SCREEN_MAP.
- No table/grid build without DATA_TABLE_SPEC.
- No dashboard-first build without workflow/runtime queue.
- No UI claim may prove backend, RLS, release, or tenant isolation.

## Outputs/records
SCREEN_MAP, DATA_TABLE_SPEC, UI review findings, linked job card, verification evidence, and UI gate decision.

## Owner/tool
UI/Adaptive Reviewer with ChatGPT for structure, Lovable for scoped UI build only after gate approval, Codex for repo evidence, and QA Gatekeeper for verification.

## Gate controlled
UI/interface and visual/layout gate.

## PASS/HOLD/BLOCKED rules
- PASS: layout, states, actions, roles, table specs, and workflow links are defined.
- HOLD: minor visual details missing but no build starts.
- BLOCKED: UI build starts from prototype/prompt alone, dashboard-first build has no runtime, or UI is treated as backend/security proof.

## Update trigger
New screen, UI defect, dashboard/execution-board change, table/grid change, role visibility change, accessibility issue, or lesson learned.
