# ENVIRONMENT_AND_TENANT_GOVERNANCE.md

## Purpose
Define controlled governance for environments, tenants, seeded data, pilot rollout and rollback so app changes cannot expose customer data or contaminate production environments.

## Scope
Applies to dev, demo, staging, pilot and production environments and all tenant structures used by governed apps.

## Owner/agent
Security/RLS Reviewer owns tenant/data separation review. GitHub Release Controller owns controlled rollout sequencing. QA Gatekeeper reviews rollout evidence. System owner approves production/pilot exposure.

## Inputs
Tenant rollout register, onboarding evidence, environment map, deployment context, RLS/security evidence, seeded demo-data evidence, rollback route and release evidence.

## Activities/checklist
1. Classify environments: dev, demo, staging, pilot, production.
2. Classify tenants: internal/dev, demo, pilot, real customer.
3. Confirm tenant isolation rules.
4. Confirm demo/synthetic data rules.
5. Confirm customer data restrictions.
6. Confirm pilot scope and rollback route.
7. Confirm release exposure scope: selected tenant or all tenants.
8. Confirm rollback and containment before rollout.
9. Record rollout evidence and approval.
10. Review post-rollout findings and lessons learned.

## Outputs/records
Environment classification, tenant classification, rollout approval, rollback evidence, pilot review and rollout audit evidence.

## Maturity level
Pilot rollout requires M3 onboarding and validator maturity. Production rollout requires M4 operational governance evidence.

## Evidence required
Tenant inventory, environment map, RLS/security review, seeded-data evidence, rollout approval, rollback route and pilot review evidence.

## Linked process
COP-08 Environment and tenant setup, COP-13 Tenant rollout, COP-14 Release and rollback, SOP-08 Security, tenant and data protection control.

## Linked agent/skill/procedure/module
Security/RLS Reviewer, GitHub Release Controller, QA Gatekeeper, tenant rollout review skill, release review skill and onboarding procedure.

## Interface/control point
Interfaces with onboarding, release governance, CI activation governance, automation boundary matrix, customer change control and AI data governance.

## PASS/HOLD/BLOCKED rules
- PASS: environment and tenant separation are verified, rollout scope is approved and rollback route is tested/documented.
- HOLD: rollout evidence incomplete or pilot monitoring pending.
- BLOCKED: customer-data exposure risk, unknown tenant isolation, no rollback, uncontrolled pilot scope or direct production rollout without approved pilot.

## PDCA
- PLAN: define environment and rollout scope.
- DO: execute controlled rollout.
- CHECK: review rollout evidence and tenant isolation.
- ACT: rollback, improve or expand rollout based on evidence.

## Audit frequency
Before rollout, after pilot rollout and during release/tenant audits.

## Automation allowance
No automated rollout to customer tenants without approved maturity, rollback and human approval.

## Escalation
Escalate tenant exposure risk, rollback failure, uncontrolled production rollout, pilot failure or customer-data contamination.

## Update trigger
New tenant, new environment, rollout request, customer onboarding, deployment change, audit finding, CAPA or lesson learned.
