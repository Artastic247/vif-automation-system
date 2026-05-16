# SHARED_COMPONENT_GOVERNANCE.md

## Purpose
Define governance for shared components, shared templates, shared validators, shared prompts, shared skills, shared UI patterns, shared schemas, shared workflows and shared logic used across multiple governed apps.

## Scope
Applies to DOS FMEA, SPC, QMS, MSA, APQP, QCPro and future apps where common components, validators, prompts, skills, templates, design patterns, schemas, or governance artefacts are reused.

## Owner/agent
VIF Orchestrator owns shared-component routing. Process Engineer owns process/template consistency. QA Gatekeeper owns validation and evidence. Security/RLS Reviewer owns security and tenant-risk review.

## Inputs
Shared-component request, affected apps, source artefact, version, owner, impact assessment, compatibility evidence, rollback route, validation evidence and release scope.

## Activities/checklist
1. Identify whether the item is shared or app-specific.
2. Register shared component with owner, version and allowed apps.
3. Define allowed reuse, prohibited reuse and adaptation rules.
4. Assess impact across affected apps.
5. Verify compatibility before adoption.
6. Confirm rollback route per affected app.
7. Prevent copying app-specific customer/process data into shared components.
8. Record release and change evidence.
9. Trigger cross-app review where shared changes affect multiple apps.

## Outputs/records
Shared-component register entry, impact assessment, compatibility evidence, release decision, rollback evidence and lessons learned.

## Maturity level
M2 for pilot reuse, M3 for controlled released reuse, M4/M5 for managed/optimised shared-component governance.

## Evidence required
Component owner, version, allowed apps, impact assessment, validation evidence, compatibility evidence and rollback route.

## Linked process
SOP-09 Configuration and version control, SOP-02 Organisational knowledge control, COP-10 Build/modification control, COP-14 Release and rollback, MOP-07 Corrective action and continual improvement.

## Linked agent/skill/procedure/module
VIF Orchestrator, QA Gatekeeper, Process Engineer, Security/RLS Reviewer, release check skill, evidence-map skill, configuration control and shared-component review.

## Interface/control point
Interfaces with app onboarding, release governance, validator governance, prompt governance, AI governance, configuration control, tenant governance and lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: shared component is registered, versioned, impact-assessed, validated and rollback-ready.
- HOLD: reuse candidate lacks full compatibility or impact evidence.
- BLOCKED: component contains app/customer-specific data, breaks tenant/security boundaries, lacks owner/version, or affects multiple apps without impact review.

## PDCA
- PLAN: define shared-component purpose, scope, owner and reuse rules.
- DO: implement or reuse under controlled scope.
- CHECK: validate compatibility, impact and evidence.
- ACT: update shared library, affected apps, lessons learned and maturity rating.

## Audit frequency
Before shared release, after shared-component incident and during portfolio governance review.

## Automation allowance
Shared-component automation is blocked unless component maturity, validation evidence, cross-app impact review and rollback route support it.

## Escalation
Escalate cross-app breakage, contamination, version conflict, tenant/security risk, uncontrolled copying or shared-component drift.

## Update trigger
New shared component, component change, app onboarding, cross-app issue, release issue, validator/prompt change, audit finding or lesson learned.
