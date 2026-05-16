# EVIDENCE_AUDIT_CHECKLIST.md

## Purpose
Provide a controlled checklist for auditing whether evidence supporting PASS decisions, releases, maturity claims, AI outputs and validation results is objective, traceable, current and sufficient.

## Scope
Applies to evidence used for gate decisions, validation reports, audit closure, release readiness, rollback readiness, AI verification, prompt verification, tenant rollout and maturity assessment.

## Owner/agent
QA Gatekeeper owns evidence audits. Process owners provide records. AI Governance Owner supports AI evidence review.

## Inputs
Evidence records, gate decisions, validation reports, release records, audit findings, AI traceability records and process outputs.

## Activities/checklist
- Is the evidence traceable to the process/output being claimed?
- Is the evidence current and version controlled?
- Is the evidence objective and reviewable?
- Does the evidence support the PASS decision?
- Is sampled evidence representative?
- Is the evidence linked to the correct repo/branch/version/job card?
- Is customer/protected data handled correctly?
- Are AI outputs verified by human review?
- Are release/rollback claims supported by records?
- Are maturity claims supported by operational evidence?
- Are lessons learned and CAPA updates linked where needed?

## Outputs/records
Evidence audit result, finding, escalation, RCA/CAPA trigger and management-review input.

## Maturity level
M3+ evidence requires routine evidence audit. M4/M5 evidence requires effectiveness and trend review.

## Evidence required
Sampled records, traceability references, validation output, reviewer confirmation and linked findings where gaps exist.

## Linked process
MOP-05 Internal audit, SOP-07 Evidence and record control, MOP-06 Management review.

## Linked agent/skill/procedure/module
QA Gatekeeper, evidence-map skill, audit skill, AI output verification procedure and release audit.

## Interface/control point
Interfaces with validation scripts, release audit, AI verification, maturity assessment and management review.

## PASS/HOLD/BLOCKED rules
- PASS: evidence is objective, traceable and sufficient.
- HOLD: evidence partially supports the claim but requires clarification or additional sampling.
- BLOCKED: evidence missing, stale, fabricated, untraceable or insufficient for a protected decision.

## PDCA
- PLAN: define evidence requirements.
- DO: collect and sample evidence.
- CHECK: audit evidence adequacy.
- ACT: raise findings, RCA/CAPA and lessons learned.

## Audit frequency
Per high-risk release/gate and by audit programme.

## Automation allowance
No automation, release or maturity increase is allowed where evidence audits are blocked.

## Escalation
Escalate false PASS, missing evidence, stale evidence, fabricated evidence, customer-data misuse or maturity overstatement.

## Update trigger
New release route, new validator, failed evidence audit, audit finding, RCA/CAPA or management review.
