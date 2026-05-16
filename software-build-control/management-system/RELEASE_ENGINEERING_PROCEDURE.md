# RELEASE_ENGINEERING_PROCEDURE.md

## Purpose
Define controlled release-engineering governance so software releases are packaged, reviewed, approved, verified, monitored and rollback-ready before pilot or production use.

## Scope
Applies to control-system releases, future app releases, pilot releases, production releases, workflow releases, validator releases, and environment/tenant release routes.

## Owner/agent
GitHub Release Controller owns release packaging and release record control. QA Gatekeeper owns release verification. System owner approves production release. Security/RLS Reviewer approves data/tenant/security impact.

## Inputs
Approved release job card, source-of-truth lock, branch/commit evidence, release scope, verification evidence, UAT evidence where applicable, audit findings, open NC/CAPA status, tenant rollout register, rollback plan, deployment environment and runtime monitoring plan.

## Activities/checklist
1. Confirm release type: control-pack, pilot app, production app, workflow, validator or hotfix.
2. Confirm source branch, target branch, commit and release scope.
3. Confirm no prohibited changes are included.
4. Confirm verification, audit, NC/CAPA and maturity status.
5. Confirm environment and tenant scope.
6. Confirm deployment evidence requirements.
7. Confirm rollback execution route before release.
8. Confirm runtime monitoring and post-release review.
9. Approve, hold or block release.
10. Record release decision and evidence.

## Outputs/records
Release package record, release approval, deployment evidence, rollback evidence, release audit record, post-release review and lessons learned.

## Maturity level
Pilot release requires M2+ controlled evidence. Operational release requires M3+. Limited governed automation requires M4. Automation candidate release route requires M5 and explicit approval.

## Evidence required
Release job card, branch/commit, diff summary, verification evidence, audit status, open NC/CAPA status, tenant/environment scope, rollback route, approval record and post-release review.

## Linked process
COP-14 Release and rollback, COP-11 Verification, COP-12 Validation/UAT, COP-13 Tenant rollout, SOP-09 Configuration and version control, MOP-05 Internal audit, MOP-06 Management review.

## Linked agent/skill/procedure/module
GitHub Release Controller, QA Gatekeeper, Security/RLS Reviewer, VIF Orchestrator, release check skill, evidence-map skill, rollback procedure and runtime monitoring procedure.

## Interface/control point
Interfaces with CI activation governance, environment/tenant governance, release register, rollback register, runtime monitoring, audit findings, CAPA, maturity assessment and management review.

## PASS/HOLD/BLOCKED rules
- PASS: release scope, evidence, approval, rollback and monitoring are complete.
- HOLD: release evidence incomplete but risk contained and no release performed.
- BLOCKED: missing rollback, failed verification, open critical NC/CAPA, tenant/data risk, unapproved deployment, auto-release or missing source truth.

## PDCA
- PLAN: define release scope, evidence, approval, rollback and monitoring.
- DO: package and approve release under control.
- CHECK: verify deployment evidence and post-release result.
- ACT: raise rollback, CAPA, lessons learned or improvement actions.

## Audit frequency
Before pilot/production release, after release incidents and during release audit cycles.

## Automation allowance
No auto-release is allowed. Release automation remains blocked unless separately approved at required maturity and with rollback/monitoring evidence.

## Escalation
Escalate failed verification, missing rollback, open critical CAPA, tenant exposure, failed deployment, release incident or unauthorised release.

## Update trigger
Release request, hotfix, pilot rollout, production rollout, workflow release, validator release, failed release, rollback or management-review decision.
