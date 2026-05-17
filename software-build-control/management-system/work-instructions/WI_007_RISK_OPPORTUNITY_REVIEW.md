# WI_007_RISK_OPPORTUNITY_REVIEW

## Purpose
Review risks and opportunities so app-development and management-system work is controlled before execution, release or automation.

## Scope
Risks and opportunities affecting scope, source truth, app development, AI output, prompts, tools, credit burn, tenant/data security, RLS, release/rollback, CI and n8n.

## When to use
Use during intake, change planning, design, backend/RLS review, security review, release review, automation readiness, management review and RCA/CAPA.

## When not to use
Do not use to justify uncontrolled work; risk review must result in treatment, acceptance, HOLD or BLOCK.

## Owner/agent
Risk Specialist with QA Gatekeeper, Security/Data Reviewer and Credit-Burn Controller when applicable.

## Inputs
Risk source, risk criteria, severity, likelihood, detection weakness, controls, owner, evidence, residual risk, opportunity statement and escalation threshold.

## Method steps
1. Identify risk/opportunity source.
2. Define risk criteria and affected process/app.
3. Assess severity, likelihood and detection weakness.
4. Define treatment/control and owner.
5. Define evidence required.
6. Assess residual risk.
7. Identify opportunity or improvement action.
8. Compare to escalation threshold.
9. Record gate decision.

## Outputs/records
Risk/opportunity record, control action, residual-risk decision, escalation or improvement action.

## Evidence required
Risk assessment, control evidence, owner approval, residual-risk record and escalation/improvement link where applicable.

## Linked ADP processes
ADP-01, ADP-05, ADP-08, ADP-09, ADP-10, ADP-11, ADP-16, ADP-18, ADP-20 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 6 planning, Clause 8 operation/change control, Clause 9 monitoring and Clause 10 improvement.

## Linked gates
Risk, change, security, backend/RLS, release, automation and improvement gates.

## Tools allowed
Risk register, opportunity register, credit-burn register, security checklist, release checklist, audit findings.

## Tools prohibited
Unapproved automation, app-repo CI, n8n, schema/RLS changes or release actions used as risk treatment without gate approval.

## Risks
Risk understated, residual risk ignored, opportunity treated as scope creep, automation attempted too early, customer data exposed.

## Controls
High risk creates HOLD or BLOCK until treatment evidence exists. Opportunities are routed to backlog/change/improvement, not uncontrolled implementation.

## Interfaces
Risk owner, process owner, security/data reviewer, AI auditor, release controller, n8n controller and GitHub CI controller.

## PASS/HOLD/BLOCKED rules
PASS when risk is assessed and controlled. HOLD when treatment evidence is pending. BLOCKED when high residual risk affects customer data, security, release, RLS, CI or n8n.

## Escalation
Escalate critical risk, repeated risk escape, uncontrolled change, high credit burn or automation before maturity.

## MLA / maturity dependency
M1 risks may be identified. M2 requires pilot treatment. M3 requires released risk controls. M4/M5 require monitoring, trends and proactive improvement.

## Update trigger
New risk, change request, audit finding, incident, release request, automation request or management-review action.
