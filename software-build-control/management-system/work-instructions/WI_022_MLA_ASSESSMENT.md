# WI_022_MLA_ASSESSMENT

## Purpose
Assess maturity level from M0 to M5 and determine gate impact, audit frequency and automation permission.

## Scope
Processes, agents, skills/WIs, procedures, workflows, prompts, context packs, validators, tools, app modules, app onboarding readiness, GitHub CI readiness and n8n readiness.

## When to use
Use for new/revised controls, app onboarding, automation readiness, post-failure downgrade, release readiness and management review.

## When not to use
Do not use maturity labels as marketing claims or proof of compliance/certification.

## Owner/agent
MLA Assessor with QA Gatekeeper and relevant specialist owner.

## Inputs
Item record, evidence, audit findings, use records, KPIs, NC/RCA/CAPA, validator evidence, risk level, automation request and previous maturity decision.

## Method steps
1. Identify item and owner.
2. Review evidence against M0-M5 criteria.
3. Confirm missing evidence and risk.
4. Determine audit frequency.
5. Determine automation permission.
6. Check maturity overstatement.
7. Define upgrade/downgrade decision.
8. Assess app onboarding, CI and n8n impact.
9. Record gate decision and review date.

## Outputs/records
MLA assessment record, maturity decision, audit frequency, automation permission, upgrade/downgrade action and management-review input.

## Evidence required
Approved artefact, use evidence, audit evidence, KPI/effectiveness evidence, RCA/CAPA status and automation risk evidence where applicable.

## Linked ADP processes
ADP-01 to ADP-21, especially ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 9 MLA/performance evaluation, Clause 10 improvement, app onboarding and automation governance.

## Linked gates
Maturity gate, app onboarding gate, CI readiness gate, n8n readiness gate and automation permission gate.

## Tools allowed
MLA register, audit reports, validator reports, evidence register, management-review outputs.

## Tools prohibited
Using MLA as customer-facing compliance claim; automation approval without evidence; app-repo CI/n8n activation while HOLD.

## Risks
Maturity overstatement, premature automation, weak evidence, no downgrade route, app onboarding before readiness.

## Controls
M0 not defined; M1 draft; M2 pilot; M3 released; M4 managed; M5 optimised/automation candidate. Automation requires evidence and explicit gate approval.

## Interfaces
Process owner, Agent owner, Skill/WI owner, Validator Auditor, CI Controller, n8n Controller, Management Review Owner.

## PASS/HOLD/BLOCKED rules
PASS when maturity evidence supports the level. HOLD when evidence is incomplete. BLOCKED when maturity is overstated or automation is attempted before maturity permits it.

## Escalation
Escalate unsupported maturity claim, repeated failure, false PASS, ineffective CAPA or automation bypass.

## MLA / maturity dependency
This WI defines the MLA dependency and must be used before maturity-dependent gates can move.

## Update trigger
New evidence, audit finding, RCA/CAPA, repeated failure, automation request, app onboarding request or management review.
