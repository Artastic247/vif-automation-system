# AGENT_EXECUTION_MATRIX.md

## Purpose
Define operational execution responsibilities, allowed actions, prohibited actions, evidence outputs, escalation rules and handoff routes for agents/workers.

## Scope
Applies to all operational workers/agents used in the Software Build Control System.

## Owner/agent
VIF Orchestrator owns routing. QA Gatekeeper reviews execution boundaries.

## Inputs
Job card, process route, gate status, context pack, approved prompts, maturity level and applicable work instructions.

## Activities/checklist
| Agent/worker | Allowed work | Prohibited work | Required inputs | Required outputs | Escalation trigger | Stop condition | Linked WI |
|---|---|---|---|---|---|---|---|
| VIF Orchestrator | Route work, assign gates, coordinate context | Direct uncontrolled code change | Job card, context pack | Routing decision | Scope conflict | Missing gate | WI-ORCH-001 |
| QA Gatekeeper | Audit, verify evidence, gate review | Implement uncontrolled fixes | Audit evidence | Gate decision | False PASS risk | Missing evidence | WI-QA-001 |
| Process Engineer | Process mapping, WI/process updates | Release approval without evidence | Process records | Updated process artefact | Process conflict | Missing owner | WI-PE-001 |
| RCA/CAPA Owner | RCA and CAPA coordination | Ignore repeated failures | NC records | CAPA records | Ineffective CAPA | Root cause unknown | WI-RCA-001 |
| Lessons Learned Controller | Integrate lessons learned | Ignore recurrence | Lessons learned | Updated artefacts | Repeated failure | Lesson not integrated | WI-LL-001 |
| AI Governance Owner | AI governance review | Approve unsafe AI route | AI records | AI review decision | AI risk escalation | Missing oversight | WI-AI-001 |

## Outputs/records
Execution assignment, gate decision, escalation record, evidence output and handoff record.

## Maturity level
Operational execution at M3+ requires approved agent boundaries and linked work instructions.

## Evidence required
Assigned job card, execution evidence, gate decision and escalation/stop-condition evidence.

## Linked process
SOP-04 Agent/worker control, SOP-03 Competence and skill control, SOP-07 Evidence and record control.

## Linked agent/skill/procedure/module
All operational agents and skills.

## Interface/control point
Interfaces with job cards, work instructions, gates, audits, RCA/CAPA, AI governance and release governance.

## PASS/HOLD/BLOCKED rules
- PASS: agent execution controlled and evidence-backed.
- HOLD: execution partially defined or awaiting approval.
- BLOCKED: uncontrolled execution, missing gate, unsafe automation or role conflict.

## PDCA
- PLAN: define execution boundaries.
- DO: execute assigned work.
- CHECK: verify evidence and compliance.
- ACT: improve routing, controls and work instructions.

## Audit frequency
Reviewed during audits, management review and after execution failures.

## Automation allowance
Agents may not autonomously bypass gates, approvals or evidence requirements.

## Escalation
Escalate role conflict, uncontrolled execution, false PASS, unsafe AI route or missing evidence.

## Update trigger
New agent, audit finding, CAPA, workflow change, maturity change or lesson learned.
