# CI_ACTIVATION_GOVERNANCE.md

## Purpose
Define controlled governance for activating GitHub CI workflows and future automation so validation enforcement cannot be enabled before maturity, validator effectiveness, audit evidence, rollback and human approval are complete.

## Scope
Applies to GitHub Actions activation, control-pack workflow activation, app-repo workflow activation later, validator enforcement, future n8n activation, automation routing, automation rollback and automation monitoring.

## Owner/agent
System owner approves CI activation. GitHub Release Controller implements approved workflow movement. QA Gatekeeper verifies validator readiness. VIF Orchestrator controls route and gate sequence.

## Inputs
Approved CI activation job card, validator register, validator effectiveness review, maturity assessment, audit results, CAPA status, management-review decision, workflow template review, rollback route and safe-boundary confirmation.

## Activities/checklist
1. Confirm CI activation is explicitly authorised by a dedicated job card.
2. Confirm target repo and branch.
3. Confirm workflow source and destination.
4. Confirm validators are mature enough for enforcement.
5. Confirm false PASS/BLOCK risks reviewed.
6. Confirm no production deploy, auto-merge, schema/RLS change, customer-data access or release action exists in workflow.
7. Confirm rollback route: disable workflow, revert commit or remove workflow.
8. Confirm first run is monitored manually.
9. Confirm outputs are reports/gates only, not autonomous fixes.
10. Record activation decision, evidence and post-run review.

## Outputs/records
CI activation decision, workflow activation evidence, validator readiness evidence, rollback evidence, first-run review and management-review input.

## Maturity level
CI activation requires relevant validators and workflow route to be at least M4 for limited governed automation. M5 is required before automation may become a candidate for broader enforcement.

## Evidence required
Approved job card, workflow diff, validator maturity, effectiveness review, audit evidence, management approval, rollback route and monitored first-run evidence.

## Linked process
MOP-04 AI governance, MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement, SOP-05 Tool routing and tool qualification, SOP-07 Evidence and record control, SOP-09 Configuration and version control.

## Linked agent/skill/procedure/module
GitHub Release Controller, QA Gatekeeper, VIF Orchestrator, Validator Control Procedure, Maturity Assessment Register, Audit Programme and Release/Register controls.

## Interface/control point
Interfaces with validator governance, GitHub workflow templates, audit findings, CAPA status, management review, release governance, automation-readiness and future app onboarding.

## PASS/HOLD/BLOCKED rules
- PASS: CI activation is approved, validator maturity/effectiveness is proven, workflow is non-destructive, rollback is clear and first run is monitored.
- HOLD: CI route is plausible but approval, validator evidence, audit evidence or rollback evidence is incomplete.
- BLOCKED: workflow can deploy, auto-merge, alter schema/RLS, access customer data, auto-fix, release, or run without approved job card and rollback.

## PDCA
- PLAN: define activation scope, validators, evidence, owner and rollback.
- DO: activate only approved workflow in controlled repo/branch.
- CHECK: monitor first run, review findings and validator behaviour.
- ACT: disable/revert/tune workflow, raise CAPA, update validator governance and lessons learned.

## Audit frequency
Before activation, after first run, after workflow change and during periodic validator/automation audit.

## Automation allowance
CI activation is limited to reporting/gating until management review approves expanded enforcement. No autonomous fixes, releases, deployments or protected changes are allowed.

## Escalation
Escalate failed first run, false PASS/BLOCK, workflow overreach, missing rollback, validator weakness, security/data issue or unauthorised activation.

## Update trigger
CI activation request, workflow change, validator change, app onboarding, audit finding, CAPA, management-review decision or automation incident.
