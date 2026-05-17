# WORKFLOW_AUDIT_CHECKLIST

## Purpose
Audit whether a workflow is runtime-real and governed, not only a route, table, sidebar item, drawer, chart, or mock UI.

## Scope
All software-build, app, release, support, customer-change, validation, CI and n8n readiness workflows.

## Owner/agent
Workflow Audit Specialist with Runtime Architect and QA Gatekeeper.

## Inputs
Workflow map, state machine, runtime map, role/tenant data, audit trail, job cards, verification evidence and maturity record.

## Activities/method
Check start event, start actor, runtime object, state model, allowed next actions, protected actions, backend guard, evidence rules, approval rules, exception/reassessment rules, audit trace, handoff to adjacent process, role/tenant impact and proof that workflow writes/reads real governed state where applicable.

## Outputs/records
Workflow audit result, runtime-depth finding, protected-action finding, NC/RCA/CAPA trigger where workflow is false or unsafe.

## Audit criteria
Workflow must prove runtime object, states, actions, evidence, approvals, exceptions and handoffs. Mock/demo evidence cannot be PASS evidence for production.

## Evidence required
State records, backend/RLS or service evidence, audit log, role/tenant evidence, test/UAT evidence.

## MLA / maturity dependency
M2 workflow requires sandbox/pilot evidence. M3+ requires released record and audit trail. Automation requires M4/M5 permission.

## Linked process
Runtime-first operation and Clause 9 workflow audit.

## Linked gate
Workflow/runtime gate.

## PASS/HOLD/BLOCKED rules
PASS when runtime evidence proves governed workflow. HOLD when evidence is partial. BLOCKED when UI shell is mistaken for workflow completion or protected action lacks backend enforcement.

## Escalation
Escalate frontend-only protected actions, tenant leakage risk, false PASS or missing backend proof.

## Management-review input
Runtime gaps and protected-action risks feed management review.

## Update trigger
Workflow change, defect, app onboarding, release, audit finding.
