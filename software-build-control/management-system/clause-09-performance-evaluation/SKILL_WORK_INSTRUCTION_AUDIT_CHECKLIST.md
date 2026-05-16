# SKILL_WORK_INSTRUCTION_AUDIT_CHECKLIST

## Purpose
Audit whether a skill or work instruction is usable, controlled, and effective enough to prevent repeat software-build failures.

## Scope
All skills and work instructions used for source lock, context lock, prompt control, runtime-first review, UI/backend review, DB/RLS proof, release/rollback, validator calibration, app onboarding and automation readiness.

## Owner/agent
Skill/WI Audit Specialist with Process Engineer and QA Gatekeeper.

## Inputs
Skill register, WI file, linked process, agent assignment, maturity record, evidence of use, audit findings, lessons learned.

## Activities/method
Check whether the skill/WI exists, has a defined trigger, required inputs, clear human-usable method steps, outputs/records, evidence requirements, PASS/HOLD/BLOCKED rules, escalation triggers, linked process, linked agent, linked gate, maturity level, revision history, and known failure prevention rule. Ask: can a competent human execute this without guessing? Does it block broad prompts, source drift, UI-only completion, backend claims without proof, and false PASS?

## Outputs/records
Completed checklist, skill/WI audit result, findings, maturity recommendation, NC/RCA/CAPA trigger if ineffective.

## Audit criteria
Skill/WI must be practical, role-clear, evidence-based, revision-controlled and linked to process/gate/maturity. Standards are alignment lenses only; SOURCE REQUIRED or CUSTOMER SOURCE REQUIRED where applicable.

## Evidence required
Current skill/WI, example use record, output evidence, gate decision, linked lessons learned or pattern control.

## MLA / maturity dependency
M1 draft skill requires review. M2 pilot requires use evidence. M3 released requires approved record and scheduled audit. M4/M5 require effectiveness evidence.

## Linked process
Clause 7 support, Clause 8 operation, Clause 9 audit, Clause 10 improvement.

## Linked gate
Skill/WI release and audit gate.

## PASS/HOLD/BLOCKED rules
PASS when the WI is executable and evidence-linked. HOLD when fields exist but use evidence is incomplete. BLOCKED when WI is a shell, unclear, unsafe, or allows uncontrolled implementation.

## Escalation
Escalate if WI failure caused repeated defect, false PASS, tool drift, or unsafe app/release action.

## Management-review input
Skill gaps, repeat WI failures and maturity downgrades feed management review.

## Update trigger
New skill, audit finding, failed use, RCA/CAPA, lessons learned, process change, tool change.
