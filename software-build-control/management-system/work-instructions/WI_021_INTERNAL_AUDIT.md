# WI_021_INTERNAL_AUDIT

## Purpose
Audit whether software-build and app-development controls are followed and supported by objective evidence.

## Scope
Process compliance, evidence quality, prompt/context control, AI-output control, runtime-first control, agent/skill use, validator/check effectiveness, release/rollback discipline, findings, NC and escalation routing.

## When to use
Use during planned audits, risk-based audits, pre-release audits, post-failure audits, MLA reviews, app onboarding readiness reviews and repeat-failure investigations.

## When not to use
Do not use audit as implementation approval without objective evidence, or as a substitute for verification, validation or release approval.

## Owner/agent
Internal Audit Specialist with relevant specialist auditor and QA Gatekeeper.

## Inputs
Audit programme, audit criteria, process records, job cards, prompts, context packs, validation reports, evidence records, release/rollback records, findings register and MLA records.

## Method steps
1. Confirm audit objective, scope and criteria.
2. Sample process and evidence records.
3. Check prompt/context/source-lock control.
4. Check AI-output verification where AI was used.
5. Check runtime-first and protected-action controls.
6. Check agent/skill/WI use and competence evidence.
7. Check validator/check outputs and limitations.
8. Check release/rollback discipline.
9. Classify findings and route NC/RCA/CAPA.
10. Record audit result and management-review input.

## Outputs/records
Audit report, checklist, findings, NC trigger, escalation record and management-review input.

## Evidence required
Audit plan, sampled records, objective evidence, findings, classification, owner, due date and closure evidence.

## Linked ADP processes
ADP-01 to ADP-21, especially ADP-16, ADP-18, ADP-20 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 9 internal audit, Clause 10 NC/RCA/CAPA and all audited MOP/COP/SOP processes.

## Linked gates
Audit gate, finding closure gate, NC/RCA/CAPA gate, management-review gate and maturity gate.

## Tools allowed
Audit checklists, evidence registers, validation reports, GitHub evidence, file-search evidence and local runtime evidence where available.

## Tools prohibited
Changing audited records during audit, claiming compliance/certification readiness, activating CI/n8n or modifying app repos.

## Risks
Audit becomes checklist-only, false PASS, weak sampling, missed runtime risk, unsupported compliance claim, findings not routed.

## Controls
Findings must be evidence-based and capable of triggering NC/RCA/CAPA. Audit outputs do not equal release approval unless release gate evidence exists.

## Interfaces
Process owners, QA Gatekeeper, Evidence Auditor, RCA/CAPA Specialist, MLA Assessor, Management Review Owner.

## PASS/HOLD/BLOCKED rules
PASS when audited controls are evidenced and findings controlled. HOLD when evidence is incomplete. BLOCKED when critical risk lacks containment or findings are bypassed.

## Escalation
Escalate false PASS, customer-data/security risk, release without evidence, repeated failure or overdue critical finding.

## MLA / maturity dependency
M1 artefacts can be audited structurally. M2 pilot audits require use evidence. M3 released controls require scheduled audits. M4/M5 require trends and effectiveness.

## Update trigger
Audit programme change, finding, RCA/CAPA, maturity change, app onboarding request or management review.
