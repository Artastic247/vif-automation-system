# OPERATIONAL_WORK_INSTRUCTION_STANDARD.md

## Purpose
Define the standard format for executable operational work instructions so agents/workers and skills can be used consistently, safely and with evidence.

## Scope
Applies to every operational work instruction used by the Software Build Control System, including intake, context lock, repo inspection, UI review, database/RLS review, prompt review, AI output verification, audit, RCA/CAPA, release review, tenant rollout and validator review.

## Owner/agent
Process Engineer owns the work-instruction standard. QA Gatekeeper verifies evidence requirements. VIF Orchestrator controls worker routing.

## Inputs
Process register, agent register, skill register, job card, gate checklist, evidence requirements, risk controls, maturity level and applicable procedure.

## Activities/checklist
Every work instruction must include:

| Section | Required content |
|---|---|
| WI ID | Unique work instruction identifier |
| Purpose | What the WI controls |
| Scope | Where it applies |
| Trigger | When to use it |
| Required inputs | Evidence and records needed before starting |
| Worker/agent | Responsible worker or agent |
| Method steps | Step-by-step execution sequence |
| Required outputs | Records/evidence produced |
| Quality checks | Checks before PASS |
| Stop conditions | When work must stop |
| Escalation | Who/what to escalate to |
| Linked process | MOP/COP/SOP linkage |
| Linked skill | Skill/method linkage |
| Linked gate | Gate controlled |
| Records | Required records/evidence |
| PASS/HOLD/BLOCKED | Decision rules |
| PDCA | Plan/Do/Check/Act link |
| Update trigger | When WI must change |

## Outputs/records
Approved work instruction, execution records, evidence outputs and revision history.

## Maturity level
M2 pilot use requires draft WI. M3 released use requires approved WI. M4/M5 require effectiveness review and audit evidence.

## Evidence required
Completed WI, execution evidence, reviewer evidence and linked gate decision.

## Linked process
SOP-03 Competence and skill control, SOP-04 Agent/worker control, SOP-07 Evidence and record control, MOP-07 Corrective action and continual improvement.

## Linked agent/skill/procedure/module
All operational agents and skills.

## Interface/control point
Interfaces with job cards, gates, skills, agent assignments, evidence registers, audit findings and lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: WI is executable, scoped, evidence-linked and approved for maturity level.
- HOLD: WI is draft or missing non-critical detail.
- BLOCKED: WI lacks inputs, method, outputs, stop conditions, escalation or evidence requirements for controlled work.

## PDCA
- PLAN: define method, inputs, evidence and controls.
- DO: execute work instruction.
- CHECK: verify outputs and evidence.
- ACT: update WI based on findings, CAPA and lessons learned.

## Audit frequency
Reviewed during skill/agent audits, maturity assessments and after execution failures.

## Automation allowance
No automated execution route may replace a WI until the WI is mature, audited and approved for automation candidate status.

## Escalation
Escalate missing WI, unclear steps, unsafe output, repeated failure, scope drift or evidence failure.

## Update trigger
New process, skill, agent, tool, audit finding, CAPA, lesson learned, validation change or maturity change.
