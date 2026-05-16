# APP_ONBOARDING_PROCEDURE.md

## Purpose
Define the controlled process for onboarding an app into the Software Build Control System before any repair, enhancement, CI activation, tenant rollout or automation is allowed.

## Scope
Applies to DOS FMEA, SPC, QMS, MSA, APQP, QCPro and any future app or module that will be governed by the Software Build Control System.

## Owner/agent
VIF Orchestrator owns onboarding route. Codex Repo Inspector owns repo/source baseline evidence. QA Gatekeeper owns onboarding gate evidence. Security/RLS Reviewer owns tenant/data/security review. System owner approves onboarding completion.

## Inputs
App request, app identity, repo URL/path, branch/version, current commit, uploaded ZIP if applicable, deployment context, Supabase/environment context, tenant list, data classification, known defects, current exclusions, rollback route, job card and source-of-truth lock.

## Activities/checklist
1. Create app onboarding job card.
2. Confirm app identity, owner, repo, branch/version and current commit.
3. Confirm source-of-truth lock and uploaded/live artefact relationship.
4. Classify app type: new build, recovery, defect, enhancement, refactor, release, pilot or maintenance.
5. Classify data sensitivity, tenant structure and environment structure.
6. Confirm dev/demo/staging/pilot/prod separation.
7. Confirm app modules/routes, build commands, scripts, tests, migrations and deployment evidence.
8. Confirm known defects and exclusions.
9. Confirm rollback route before any change.
10. Create app-control artefacts under app-registers/[APP_NAME]/.
11. Perform onboarding verification and gate decision.
12. Block repair/build work until onboarding PASS.

## Outputs/records
App onboarding record, app-control artefacts, source-of-truth lock, environment classification, tenant classification, onboarding verification record and gate decision.

## Maturity level
An app starts at M0/M1 until source truth, environment, tenant, evidence and rollback controls are proven. M2 requires controlled pilot onboarding. M3 requires approved operational control records.

## Evidence required
Repo/branch/commit evidence, app context, module inventory, environment evidence, tenant evidence, data classification, known defect list, exclusions, rollback route and onboarding verification.

## Linked process
COP-01 App intake and classification, COP-02 Source-of-truth and context lock, COP-08 Environment and tenant setup, COP-09 Job card creation and approval, COP-11 Verification, SOP-09 Configuration and version control.

## Linked agent/skill/procedure/module
VIF Orchestrator, Codex Repo Inspector, QA Gatekeeper, Security/RLS Reviewer, context-lock skill, evidence-map skill, tenant rollout review, app onboarding checklist and environment governance.

## Interface/control point
Interfaces with source-of-truth lock, tenant rollout register, release register, verification register, CI activation governance, automation boundary matrix and customer change control.

## PASS/HOLD/BLOCKED rules
- PASS: app identity, repo, branch, version, environment, tenant/data context, rollback and onboarding evidence are complete.
- HOLD: onboarding evidence is incomplete but no app changes are allowed.
- BLOCKED: wrong repo/branch, unknown source truth, uncontrolled customer data, missing rollback, unknown tenant exposure or app repair requested before onboarding PASS.

## PDCA
- PLAN: define onboarding scope and evidence requirements.
- DO: collect and lock app evidence.
- CHECK: verify onboarding completeness and risks.
- ACT: approve, hold, block or update onboarding controls based on findings.

## Audit frequency
Per app onboarding, after major app change and before CI/app automation activation.

## Automation allowance
No app-specific CI, automation, n8n or repair may start until onboarding gate is PASS and automation maturity allows it.

## Escalation
Escalate wrong repo/branch, missing source truth, customer-data risk, tenant exposure, missing rollback or app repair pressure before onboarding PASS.

## Update trigger
New app, app recovery, repo change, branch/version change, tenant change, deployment change, customer change, CI request, automation request or lesson learned.
