# CI_PILOT_ACTIVATION_PROCEDURE.md

## Purpose
Define the controlled route for piloting GitHub CI activation so workflow behaviour, validator enforcement, false PASS/BLOCK risk, rollback and operational evidence are proven before broader CI rollout.

## Scope
Applies to the first controlled CI pilot in the control-system repository and any future app-repo CI pilot. It does not authorise automatic release, auto-merge, deployment, schema/RLS changes, customer-data access, n8n execution or app repair.

## Owner/agent
System owner approves CI pilot start. GitHub Release Controller performs approved workflow activation. QA Gatekeeper verifies validator readiness and live evidence. VIF Orchestrator controls the job-card route.

## Inputs
Approved CI pilot activation job card, CI activation governance, automation boundary matrix, validator register, validator effectiveness review, maturity assessment, audit status, CAPA status, rollback execution route, workflow templates and first-run monitoring plan.

## Activities/checklist
1. Confirm dedicated CI pilot job card exists.
2. Confirm target repository and branch.
3. Confirm selected workflow templates and validators.
4. Confirm workflow files remain non-destructive.
5. Confirm validators meet required maturity for pilot enforcement.
6. Confirm rollback route: disable workflow, remove workflow or revert activation commit.
7. Confirm first-run monitoring owner.
8. Activate only approved workflow(s) in the approved repo/branch.
9. Monitor first CI run and record behaviour.
10. Classify results: PASS, HOLD or BLOCKED.
11. Decide whether to keep, adjust, disable or expand pilot.

## Outputs/records
CI pilot activation record, workflow activation evidence, first-run evidence, validator behaviour evidence, false PASS/BLOCK review, rollback evidence and pilot decision.

## Maturity level
CI pilot requires M4-level readiness for involved validators and workflow route. M5 is required before broader automation candidate status.

## Evidence required
Pilot job card, workflow diff, workflow run result, validator output, reviewer decision, rollback evidence and post-run review.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, SOP-05 Tool routing and tool qualification, SOP-07 Evidence and record control, SOP-09 Configuration and version control.

## Linked agent/skill/procedure/module
GitHub Release Controller, QA Gatekeeper, VIF Orchestrator, CI Activation Governance, Validator Control Procedure, Runtime Monitoring Procedure and Rollback Execution Procedure.

## Interface/control point
Interfaces with GitHub workflows, validators, audit findings, CAPA status, management review, rollback governance and automation boundary matrix.

## PASS/HOLD/BLOCKED rules
- PASS: pilot workflow runs as expected, remains non-destructive, validators behave correctly, evidence is recorded and rollback is proven.
- HOLD: workflow runs but validator tuning, warnings or evidence gaps require review before expansion.
- BLOCKED: workflow deploys, auto-merges, alters schema/RLS, accesses customer data, releases, auto-fixes, fails rollback, or creates false PASS/BLOCK risk.

## PDCA
- PLAN: define CI pilot scope, validators, rollback and monitoring.
- DO: activate approved pilot workflow only.
- CHECK: review live run, validator behaviour and evidence.
- ACT: keep, disable, tune, escalate CAPA or approve next pilot stage.

## Audit frequency
Before activation, after first run, after workflow change, after false PASS/BLOCK and during management review.

## Automation allowance
CI pilot may report and gate only. It may not deploy, auto-merge, auto-fix, change schema/RLS, access customer data, release or trigger n8n.

## Escalation
Escalate unauthorised activation, false PASS/BLOCK, workflow overreach, missing rollback, failed first run, validator drift or security/data concern.

## Update trigger
CI pilot request, workflow change, validator change, first-run finding, audit finding, CAPA, rollback event or management-review decision.
