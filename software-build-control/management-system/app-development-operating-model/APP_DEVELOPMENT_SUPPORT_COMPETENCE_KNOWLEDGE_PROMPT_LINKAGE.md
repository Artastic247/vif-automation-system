# APP_DEVELOPMENT_SUPPORT_COMPETENCE_KNOWLEDGE_PROMPT_LINKAGE

## Purpose
Link app-development production work to competence, agents, skills, prompts, context packs, organisational knowledge, lessons learned, tool routing and AI/tool governance.

## Scope
All ADP processes where people, agents, tools, prompts, knowledge or validators affect output quality.

## Owner/agent
VIF Orchestrator with Skill/WI Audit Specialist, Prompt Audit Specialist and Organisational Knowledge Controller.

## Inputs
Agent/workstation assignment, skill/WI linkage, prompt packet, context pack, lessons learned, tool routing matrix, AI governance record, validator competence and communication needs.

## Activities/method
Confirm required competence, assigned workstation, skill/WI, prompt/context control, knowledge record and evidence before work. If competence, WI, prompt or knowledge is missing, hold the process or escalate.

## Outputs/records
Competence linkage record, prompt/context approval, knowledge update, tool-routing evidence and gap action.

## Linked ADP processes
ADP-01 to ADP-21.

## Linked MOP/COP/SOP processes
Clause 7 support, competence, awareness, communication, organisational knowledge, documented information, prompt/context management, supplier/tool control and validator calibration.

## Linked skills/WIs
Context lock, prompt audit, runtime-first, UI review, DB/RLS proof, code review, test planning, verification, validation, release, RCA/CAPA, lessons learned, knowledge update.

## Linked gates
Competence gate, prompt gate, context gate, tool-routing gate, validation gate, improvement gate.

## Evidence required
Assigned agent, skill/WI status, prompt/context record, knowledge source, tool route and review evidence.

## Risks
Wrong tool, weak prompt, missing WI, AI bad output, stale knowledge, untrained agent, validator not competent.

## Controls
No build/review/release step proceeds without competent agent, approved prompt/context and required WI/control.

## Interfaces
Agents/workstations, prompt auditor, context specialist, tool reviewer, AI auditor, knowledge controller, QA.

## Support linkage matrix
| ADP process | Required competence | Agent/workstation | Skill/WI | Prompt/context control | Knowledge record | Evidence | Gap if missing |
|---|---|---|---|---|---|---|---|
| ADP-01 | Intake/risk classification | Orchestrator | Scope lock | Intake context | App portfolio | Intake record | Wrong route |
| ADP-02 | Source/context control | Context Specialist | Source lock | Context pack | Source hierarchy | Context record | Drift |
| ADP-03 | Process/domain knowledge | Process Owner | Process mapping | Domain context | Domain knowledge | Domain evidence | Assumption |
| ADP-06 | Runtime design | Runtime Architect | Runtime-first | Runtime source | Runtime lessons | Runtime map | UI shell |
| ADP-08 | Backend/RLS | Backend/RLS Engineer | DB/RLS proof | Data context | Security knowledge | Backend evidence | Data risk |
| ADP-10 | Prompt control | Prompt Engineer | Prompt quality | Prompt packet | Prompt lessons | Prompt record | Prompt drift |
| ADP-11 | Build execution | Builder/Coder | Build WI | Job-card prompt | Tool lessons | Diff evidence | Scope drift |
| ADP-12 | Code review | Reviewer | Code review | Review context | Coding patterns | Review record | Bad code |
| ADP-16 | Verification | QA Gatekeeper | Evidence audit | Evidence context | Validator lessons | Verification | False PASS |
| ADP-17 | Validation/UAT | UAT Coordinator | UAT review | User context | Process knowledge | UAT record | Poor fit |
| ADP-21 | Improvement | RCA/CAPA/LL | RCA/CAPA/LL | Issue context | Knowledge update | Improvement record | Repeat failure |

## PASS/HOLD/BLOCKED rules
PASS when competence, WI, prompt/context and knowledge evidence exist. HOLD when gaps are non-critical. BLOCKED when missing competence/control can cause unsafe build, release or data risk.

## Escalation
Escalate untrained agent, missing critical WI, prompt drift, AI bad output, stale knowledge or wrong tool route.

## Update trigger
New skill, tool, prompt, lesson, agent assignment, audit finding or RCA/CAPA.
