# WI_019_RELEASE_ROLLBACK_REVIEW

## Purpose
Review release readiness and rollback safety before any app/module is deployed, piloted or rolled out.

## Scope
Release scope, commit/version, verification evidence, validation/UAT evidence, release approval, known limitations, rollback route, rollback trigger and post-release monitoring.

## When to use
Use before pilot, limited rollout, full rollout, hotfix release or production-impacting change.

## When not to use
Do not use to approve release when verification, validation or rollback evidence is missing.

## Owner/agent
Release Controller with Configuration Controller, QA Gatekeeper and Support Owner.

## Inputs
Release scope, commit/version, verification report, UAT evidence, known limitations, tenant rollout decision, rollback route, support owner and monitoring plan.

## Method steps
1. Confirm release scope.
2. Confirm commit/version.
3. Confirm verification evidence.
4. Confirm validation/UAT evidence.
5. Review known limitations.
6. Confirm release approval authority.
7. Confirm rollback route and rollback trigger.
8. Confirm post-release monitoring.
9. Confirm support owner.
10. Block release if evidence is missing.

## Outputs/records
Release readiness decision, rollback plan, support handover, monitoring requirement and gate decision.

## Evidence required
Commit/version evidence, verification report, UAT record, release approval, rollback route, known limitations and monitoring plan.

## Linked ADP processes
ADP-16, ADP-17, ADP-18, ADP-19, ADP-20 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 8 release/rollback/support, Clause 9 release audit and Clause 10 improvement.

## Linked gates
Release gate, rollback gate, support handover gate and monitoring gate.

## Tools allowed
Release register, Git commit evidence, verification/UAT reports, rollback checklist, monitoring/support records.

## Tools prohibited
Auto-release, release without evidence, release using mock/demo evidence, app-repo CI release while HOLD.

## Risks
Release without proof, rollback failure, unsupported version, hidden limitation, no support owner, customer impact.

## Controls
No release without verification, validation, release approval, rollback route and support monitoring.

## Interfaces
QA Gatekeeper, Release Controller, Configuration Controller, Product/App Owner, Support Owner, Incident Owner.

## PASS/HOLD/BLOCKED rules
PASS when release and rollback evidence is complete. HOLD when non-critical limitation remains controlled. BLOCKED when verification/UAT/rollback/support evidence is missing for release.

## Escalation
Escalate failed rollback, release blocker, missing approval, unsupported version or customer-impacting defect.

## MLA / maturity dependency
M3 required for controlled release. M4/M5 require monitoring trends, rollback drills and release effectiveness review.

## Update trigger
Release request, rollback event, failed deployment, UAT issue, audit finding or support incident.
