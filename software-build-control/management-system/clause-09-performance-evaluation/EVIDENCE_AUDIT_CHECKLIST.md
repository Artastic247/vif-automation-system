# EVIDENCE_AUDIT_CHECKLIST

## Purpose
Audit whether claims and gate decisions are supported by objective evidence.

## Scope
All verification, validation, runtime, release, rollback, onboarding and audit evidence.

## Owner/agent
Evidence Auditor.

## Inputs
Verification register, release records, build/test reports, screenshots, logs, validation reports and runtime evidence.

## Activities/method
Audit whether every claim has evidence, build/lint/test proof exists where relevant, backend read/write proof exists where relevant, RLS/role evidence exists where relevant, screenshots/logs/reports are current, verification register is complete, release/rollback evidence exists and whether demo/mock data is incorrectly used as PASS evidence.

## Outputs/records
Evidence audit report, evidence gaps, false PASS finding and escalation actions.

## Audit criteria
No release, onboarding or operational claim without objective evidence.

## Evidence required
Reports, logs, screenshots, runtime traces, approval records and rollback evidence.

## MLA / maturity dependency
Higher maturity requires stronger operational evidence.

## Linked process
Verification, validation and Clause 9 evidence audit.

## Linked gate
Evidence completeness gate.

## PASS/HOLD/BLOCKED rules
PASS when evidence fully supports claims. HOLD when evidence is partial. BLOCKED when evidence is missing, stale or mock/demo evidence is misused.

## Escalation
Escalate false PASS, unsupported release or unverifiable backend claims.

## Management-review input
Evidence gaps and repeat false PASS trends feed management review.

## Update trigger
Release, audit finding, failed validation or onboarding request.
