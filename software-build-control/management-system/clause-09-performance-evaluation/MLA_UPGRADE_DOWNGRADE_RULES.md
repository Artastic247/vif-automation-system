# MLA_UPGRADE_DOWNGRADE_RULES

## Purpose
Control maturity upgrade, downgrade, and prevention of unsupported maturity claims.

## Scope
Processes, agents, skills, procedures, workflows, prompts, context packs, validators, tools, AI tools, app modules, app onboarding, release readiness, GitHub CI readiness, and n8n readiness.

## Owner/agent
MLA Assessor with Internal Audit Specialist and affected process owner.

## Inputs
Current maturity record, evidence matrix, audit findings, RCA/CAPA records, validation reports, management-review decisions.

## Activities/method
Upgrade only when required evidence exists. Downgrade when evidence fails, audit finding is raised, repeat failure occurs, validator false PASS occurs, automation exceeds permission, or CAPA is ineffective.

## Audit criteria
Evidence must support the level claimed. No claim may exceed available evidence.

## Evidence required
Assessment record, objective evidence, owner approval, audit link, and downgrade/upgrade reason.

## MLA / maturity dependency
Maturity level controls gate status, audit frequency, app onboarding, CI readiness, n8n readiness, validator release, agent release, skill release, and automation permission.

## Linked process
Clause 9 MLA and Clause 10 improvement.

## Linked gate
Maturity movement gate.

## PASS/HOLD/BLOCKED rules
PASS when evidence supports the decision. HOLD when evidence is incomplete. BLOCKED when maturity is overstated or unsafe automation/release depends on unsupported maturity.

## Escalation
Escalate maturity overstatement, failed audit, unsafe automation, or unresolved downgrade trigger.

## Management-review input
Downgrades, repeated holds, and automation blocks feed management review.

## Update trigger
Assessment, audit finding, RCA/CAPA result, management review, automation request, app onboarding request.
