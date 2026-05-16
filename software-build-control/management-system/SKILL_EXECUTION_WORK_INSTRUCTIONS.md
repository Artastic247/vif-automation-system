# SKILL_EXECUTION_WORK_INSTRUCTIONS.md

## Purpose
Define executable work-instruction routes for controlled skills used within the Software Build Control System.

## Scope
Applies to operational skills including context lock, scope lock, gate check, evidence mapping, runtime review, UI review, database/RLS review, prompt review, verification review, release check and tenant rollout review.

## Owner/agent
Process Engineer owns skill execution structure. Skill owners maintain execution steps. QA Gatekeeper reviews evidence requirements.

## Inputs
Approved skill, job card, context pack, gate requirements, evidence requirements and applicable process route.

## Activities/checklist
### WI-SKILL-001 — Context Lock
- Verify app identity, repo, branch, job card and source-of-truth artefacts.
- Confirm current exclusions and rollback context.
- Confirm latest decision and unresolved gaps.
- Produce context-lock evidence.
- STOP if source of truth unclear.

### WI-SKILL-002 — Gate Check
- Review gate checklist.
- Verify required evidence.
- Review PASS/HOLD/BLOCKED criteria.
- Escalate false PASS or missing evidence.
- Produce gate decision.

### WI-SKILL-003 — Prompt Review
- Verify scope in/out.
- Verify forbidden prompt patterns absent.
- Verify tool route and evidence requirements.
- Verify stop condition and rollback wording.
- STOP if prompt vague or unsafe.

### WI-SKILL-004 — Database/RLS Review
- Verify schema/runtime map linkage.
- Verify tenant isolation and RLS evidence.
- Verify no frontend-only security claims.
- STOP if protected actions unsupported.

### WI-SKILL-005 — Release Review
- Verify verification/UAT evidence.
- Verify rollback route.
- Verify open NC/CAPA status.
- Verify maturity and automation allowance.
- STOP if evidence incomplete.

## Outputs/records
Skill execution evidence, gate decision, escalation record, updated register or linked artefact.

## Maturity level
M3+ operational use requires approved execution route and evidence outputs.

## Evidence required
Execution evidence, reviewer evidence, linked gate decision and stop-condition evidence where triggered.

## Linked process
SOP-03 Competence and skill control, SOP-04 Agent/worker control, SOP-07 Evidence and record control.

## Linked agent/skill/procedure/module
All controlled skills and linked agents.

## Interface/control point
Interfaces with prompts, job cards, validators, audits, releases, RCA/CAPA and management review.

## PASS/HOLD/BLOCKED rules
- PASS: skill executed with evidence and approved output.
- HOLD: evidence incomplete but contained.
- BLOCKED: missing evidence, unsafe route, unclear scope or failed stop condition.

## PDCA
- PLAN: define execution route.
- DO: execute skill.
- CHECK: verify evidence and gate result.
- ACT: improve skill and WI based on lessons learned.

## Audit frequency
Reviewed during audits, effectiveness reviews and after repeated execution failures.

## Automation allowance
No skill may become automated without maturity approval, audit evidence and validator confidence.

## Escalation
Escalate repeated failure, false PASS, unsafe prompt, missing evidence or weak control.

## Update trigger
Audit finding, CAPA, prompt failure, release issue, validation change or lesson learned.
