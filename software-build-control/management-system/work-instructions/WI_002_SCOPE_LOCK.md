# WI_002_SCOPE_LOCK

## Purpose
Prevent uncontrolled expansion, feature creep and unsafe implementation during controlled software-build work.

## Scope
All job cards, prompts, code/build tasks, validation work, repo changes and automation decisions.

## When to use
Use before any work instruction, prompt packet, build execution, repository change, validation alignment, CI/n8n decision, schema/RLS change or release decision.

## When not to use
Do not use to suppress legitimate risks or required corrective actions; move out-of-scope items to backlog or NC/RCA/CAPA when required.

## Owner/agent
VIF Orchestrator with QA Gatekeeper.

## Inputs
Current job card, scope in/out, protected scope, exclusions, risks, backlog, change request, validation status and gate decision.

## Method steps
1. Confirm objective and scope in.
2. Confirm scope out and protected scope.
3. Identify feature creep and broad work requests.
4. Block vague "fix everything" or "build whole app" tasks.
5. Confirm app-repo, Supabase/RLS, deployment, CI and n8n restrictions.
6. Confirm customer-data boundary.
7. Confirm no PASS claim without evidence.
8. Route extras to backlog, change control or NC/RCA/CAPA.
9. Record PASS/HOLD/BLOCKED decision.

## Outputs/records
Scope lock decision, backlog items, blocked-scope note and gate record.

## Evidence required
Job card, scope table, protected-scope statement, backlog/change record and validation evidence where applicable.

## Linked ADP processes
ADP-01, ADP-05, ADP-09, ADP-10, ADP-11, ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 6 planning/change, Clause 8 operation, Clause 9 evidence audit and Clause 10 improvement.

## Linked gates
Scope, change, job-card, build, verification, release and automation gates.

## Tools allowed
Backlog register, job cards, GitHub evidence review, local runtime validation, file-search for uploaded instructions.

## Tools prohibited
Unapproved app repo edits, app-repo CI activation, n8n implementation, schema/RLS changes, deployment changes, auto-fix, auto-merge and auto-release.

## Risks
Feature creep, false PASS, uncontrolled schema/RLS, customer-data exposure, premature CI/n8n, broad prompt drift.

## Controls
No app-repo changes during control-system work. No CI/n8n activation during HOLD. No schema/RLS change without approved runtime and rollback gate. No customer data access without approved boundary.

## Interfaces
Prompt Engineer, GitHub Controller, QA Gatekeeper, Release Controller, n8n Controller, Security/Data Reviewer.

## PASS/HOLD/BLOCKED rules
PASS when scope is bounded and protected items are excluded. HOLD when scope needs clarification but no unsafe action started. BLOCKED when prohibited work is requested or already attempted.

## Escalation
Escalate protected-scope breach, false PASS claim, customer-data risk, schema/RLS change request or automation bypass.

## MLA / maturity dependency
M0/M1 blocks implementation beyond drafting. M2 allows controlled pilot. M3+ allows defined operational scope only. M4/M5 may consider limited automation with evidence.

## Update trigger
New requirement, scope change, feature request, audit finding, validation failure or management-review action.
