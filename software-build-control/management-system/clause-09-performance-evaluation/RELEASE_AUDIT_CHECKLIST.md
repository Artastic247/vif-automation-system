# RELEASE_AUDIT_CHECKLIST

## Purpose
Audit release readiness, release evidence and rollback safety before any controlled rollout.

## Scope
All app, module, validator, workflow and control-system releases.

## Owner/agent
Release Auditor with Release/Configuration Controller.

## Inputs
Release register, version/commit, verification results, validation/UAT, rollout plan, rollback plan and known limitations.

## Activities/method
Audit release scope, version/commit, acceptance evidence, verification result, validation/UAT result, tenant rollout decision, known limitations, rollback route, release approval, post-release monitoring and customer-facing claim control.

## Outputs/records
Release audit report, gate decision, blocked release finding and RCA/CAPA trigger where required.

## Audit criteria
No release without objective verification, validation and rollback evidence.

## Evidence required
Build/test/UAT reports, rollback evidence, approval records, rollout records and monitoring plan.

## MLA / maturity dependency
Release maturity and onboarding readiness must support the rollout scope.

## Linked process
Release management and Clause 9 release audit.

## Linked gate
Release gate.

## PASS/HOLD/BLOCKED rules
PASS when evidence and rollback are complete. HOLD when evidence is partial. BLOCKED when release lacks rollback, validation or approval.

## Escalation
Escalate unsupported release, unsafe customer claim or rollback failure.

## Management-review input
Release failures and rollout risks feed management review.

## Update trigger
Release request, failed deployment, onboarding or audit finding.
