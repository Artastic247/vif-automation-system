# ENVIRONMENT_TENANT_GOVERNANCE.md

## Purpose
Define controlled governance for development, demo, staging, pilot and production environments and for multi-tenant separation.

## Scope
Applies to all environments, tenants, seeded/demo data, pilot rollouts and future deployment routes.

## Owner/agent
Security/RLS Reviewer owns tenant separation review. VIF Orchestrator owns environment routing. QA Gatekeeper verifies evidence.

## Inputs
Environment inventory, tenant register, deployment context, onboarding evidence, rollback route, data classification and release scope.

## Activities/checklist
1. Classify environments: dev, demo, staging, pilot and production.
2. Define tenant purpose and data sensitivity.
3. Verify demo/dev tenants do not expose production/customer data.
4. Verify pilot route before broad rollout.
5. Verify rollback route for environment and tenant changes.
6. Verify release scope per tenant.
7. Block global rollout without pilot evidence.
8. Record environment and tenant evidence.

## Outputs/records
Environment classification, tenant classification, rollout evidence, rollback evidence and onboarding linkage.

## Maturity level
M3 required before controlled pilot rollout. M4 required before broader governed rollout.

## Evidence required
Tenant list, environment map, data classification, rollback route, pilot evidence and rollout approval.

## Linked process
COP-08 Environment and tenant setup, COP-13 Tenant rollout, COP-14 Release and rollback, SOP-08 Security tenant and data protection control.

## Linked agent/skill/procedure/module
Security/RLS Reviewer, QA Gatekeeper, tenant rollout review skill and onboarding procedure.

## Interface/control point
Interfaces with tenant rollout register, onboarding controls, release governance, CI governance and AI data governance.

## PASS/HOLD/BLOCKED rules
- PASS: environment separation and tenant controls verified.
- HOLD: environment/tenant evidence incomplete.
- BLOCKED: customer-data exposure risk, missing rollback or uncontrolled rollout.

## PDCA
- PLAN: define environment and tenant strategy.
- DO: configure controlled environments and pilot routes.
- CHECK: verify separation and rollout evidence.
- ACT: improve governance and rollout controls.

## Audit frequency
Per onboarding, rollout, environment change and release review.

## Automation allowance
Automation may not bypass tenant rollout approval or environment separation controls.

## Escalation
Escalate tenant exposure risk, production-data misuse, uncontrolled rollout or missing rollback.

## Update trigger
Tenant change, environment change, rollout request, release issue or lesson learned.
