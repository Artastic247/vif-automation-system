# WI_023_RCA

## Purpose
Perform root cause analysis for software-build and management-system failures using evidence, not assumptions.

## Scope
Audit findings, false PASS, prompt drift, AI bad output, failed validation, failed release/rollback, backend/RLS/security issues, repeated repair failure, maturity overstatement and validator false negative.

## When to use
Use when a significant NC, repeat issue, false PASS, escaped failure, blocked release, security/data risk or failed CAPA occurs.

## When not to use
Do not use RCA to justify a preferred answer without evidence or to bypass containment.

## Owner/agent
RCA/CAPA Specialist with affected process owner and QA Gatekeeper.

## Inputs
Linked NC, evidence, containment record, correction status, audit finding, failed output, validation result, release/rollback issue, prompt/tool record and affected artefacts.

## Method steps
1. Define problem statement.
2. Confirm source and objective evidence.
3. Confirm containment taken.
4. Identify direct cause.
5. Identify systemic cause.
6. Identify escaped-detection cause.
7. Identify maturity-level cause.
8. Identify interface/control-point failure.
9. Identify prompt/tool, agent/skill, process/procedure and validator contributions.
10. Define corrective action and effectiveness-review requirement.

## Outputs/records
RCA record, cause analysis, corrective-action requirement, affected artefact list and effectiveness-review trigger.

## Evidence required
Linked NC, evidence pack, cause logic, method used, containment proof, corrective-action decision and review requirement.

## Linked ADP processes
ADP-16, ADP-18, ADP-20 and ADP-21, plus affected ADP process.

## Linked MOP/COP/SOP processes
Clause 10 RCA/CAPA, Clause 9 audit findings and Clause 8 operational control.

## Linked gates
NC gate, RCA gate, CAPA gate, effectiveness gate, maturity gate and improvement gate.

## Tools allowed
NC register, audit findings, evidence logs, prompts/outputs, validation reports, RCA methods and lessons learned.

## Tools prohibited
Guessing root cause, blaming user/tool without evidence, closing RCA without corrective-action decision.

## Risks
Superficial cause, no systemic fix, repeat failure, false confidence, validator gap not corrected.

## Controls
RCA must include direct, systemic and escaped-detection cause. Validator false negatives and maturity overstatement must be considered.

## Interfaces
RCA/CAPA Specialist, Process Owner, Prompt Auditor, AI Output Auditor, Validator Auditor, QA Gatekeeper and Knowledge Controller.

## PASS/HOLD/BLOCKED rules
PASS when root cause is evidence-supported and action defined. HOLD when evidence is incomplete. BLOCKED when high-risk issue lacks containment or RCA owner.

## Escalation
Escalate repeat failure, unresolved systemic cause, security/data risk, failed rollback or false PASS.

## MLA / maturity dependency
Systemic RCA findings may downgrade maturity and block onboarding, CI, n8n or release.

## Update trigger
NC opened, repeat issue, validation failure, release failure, audit finding, ineffective CAPA or management review.
