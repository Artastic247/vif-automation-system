# APP_DEVELOPMENT_RISK_OBJECTIVES_CHANGE_PLANNING

## Purpose
Link app-development work to risk, opportunity, objectives, KPIs and change planning.

## Scope
All ADP processes where risk, change, cost, AI, security, tenant, release, rollback, automation or app-repo CI decisions may occur.

## Owner/agent
Risk Specialist with QA Gatekeeper, Credit-Burn Controller and VIF Orchestrator.

## Inputs
Risk register, opportunity register, objectives/KPIs, change request, credit/tool cost, AI-output risk, security/RLS/tenant risk, customer-data risk, release/rollback risk, automation risk and maturity level.

## Activities/method
Identify risks/opportunities per ADP stage, define objective/KPI, classify change trigger, define control, assign evidence and decide PASS/HOLD/BLOCKED gate. Keep app-repo CI and n8n HOLD until maturity and onboarding gates pass.

## Outputs/records
Risk/control record, objective/KPI link, change-planning decision and gate status.

## Linked ADP processes
ADP-01 to ADP-21, especially ADP-05, ADP-08, ADP-09, ADP-10, ADP-11, ADP-16, ADP-18, ADP-20 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 6 planning, Clause 8 operation/change control, Clause 9 monitoring and Clause 10 improvement.

## Linked skills/WIs
Risk review, change impact, credit-burn control, AI output verification, security/data audit, release/rollback review, app onboarding readiness.

## Linked gates
Risk gate, change gate, build gate, security gate, verification gate, release gate, automation gate.

## Evidence required
Risk record, objective/KPI, change trigger, control decision, cost impact where relevant and gate evidence.

## Risks
Credit burn, AI hallucination, customer data exposure, RLS weakness, release without rollback, automation before maturity, uncontrolled change.

## Controls
No backend/RLS, release, app-repo CI or n8n work without risk-based gate evidence. Auto-fix, auto-merge and auto-release remain BLOCKED.

## Interfaces
Risk owner, QA, release, security/data, AI auditor, app owner, GitHub CI controller, n8n controller.

## Risk/objectives/change matrix
| ADP process | Risk/opportunity | Objective/KPI | Change trigger | Control | Evidence | Gate |
|---|---|---|---|---|---|---|
| ADP-01 | Wrong classification | Intake accuracy | New app/change | Classify risk/type | Intake record | Intake |
| ADP-02 | Source drift | Source-lock completeness | Repo/context change | Current commit lock | Context pack | Context |
| ADP-05 | Vague requirement | Rework reduction | Requirement change | Acceptance criteria | Req record | Requirements |
| ADP-08 | RLS/data design risk | Backend defect rate | Schema/RLS need | DB/RLS review | Design evidence | Backend |
| ADP-09 | Security/tenant/customer data risk | Open high-risk count | Sensitive data/tenant | Security review | Risk evidence | Risk |
| ADP-10 | Prompt drift/tool burn | Prompt defect rate/cost | Tool route | Prompt/cost gate | Prompt packet | Job card |
| ADP-11 | Scope drift | Build rework | Build request | Job-card-only build | Diff evidence | Build |
| ADP-16 | False PASS | Evidence gap rate | Verification | Evidence audit | Verification record | Verification |
| ADP-18 | Release/rollback risk | Rollback readiness | Release request | Release review | Release/rollback record | Release |
| ADP-20 | Support trend | Incident recurrence | Feedback | Classify issue | Feedback log | Monitoring |
| ADP-21 | Repeat failure | CAPA effectiveness | NC/repeat | RCA/CAPA | Improvement evidence | Improvement |

## PASS/HOLD/BLOCKED rules
PASS when risks are assessed and controlled with evidence. HOLD when risk/control evidence is incomplete. BLOCKED when high-risk change proceeds without control.

## Escalation
Escalate high-risk data/security, failed rollback, repeated false PASS, uncontrolled cost burn or automation attempted before maturity.

## Update trigger
New risk, change request, failed gate, RCA/CAPA, KPI trend or management-review decision.
