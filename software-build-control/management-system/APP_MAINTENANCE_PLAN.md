# APP_MAINTENANCE_PLAN.md

## Purpose
Control ongoing support, maintenance, dependency review, security review, backend/RLS review, release health, and controlled improvement after an app is built or repaired.

## Scope
Applies to maintained apps, app modules, Supabase-backed apps, deployed environments, tenant rollouts, support incidents, and recurring review cycles. This plan does not authorise changes without a job card.

## Inputs
- Current app context, repo, branch, version, deployment, and environment.
- Open defects, incidents, support requests, dependency alerts, verification evidence, release records, tenant rollout records, and lessons learned.

## Activities/checklist
- Review open defects and support issues.
- Review build/lint/test status.
- Review dependency/security alerts.
- Review Supabase migrations, RLS, edge functions, and protected actions where applicable.
- Review tenant exposure, feature flags, demo/dev/real separation, and rollback route.
- Review app performance, usability concerns, and customer/UAT feedback.
- Convert approved work into controlled job cards.
- Update lessons learned, skills, agents, and templates where needed.

## Outputs/records
Maintenance log, risk/actions, approved maintenance job cards, updated verification/release/tenant/lessons records.

## Owner/tool
App owner, VIF Orchestrator, QA Gatekeeper, GitHub Release Controller, Supabase Backend Reviewer, and Support owner.

## Gate controlled
Support and maintenance gate.

## PASS/HOLD/BLOCKED rules
- PASS: maintenance status reviewed, risks controlled, and required actions converted to job cards.
- HOLD: review incomplete or evidence missing but no critical risk exists.
- BLOCKED: critical security, RLS, tenant, rollback, or release-health risk is uncontrolled.

## Update trigger
Scheduled review, support incident, dependency/security alert, release, rollback, customer feedback, or repeated defect.
