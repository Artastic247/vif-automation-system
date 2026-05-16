# AI_LIFECYCLE_CONTROL.md

## Purpose
Control the full AI lifecycle from request to context pack, tool route, prompt approval, AI output, human review, verification, decision, implementation, monitoring, lessons learned and process update.

## Scope
Applies to all AI-assisted software-build, review, verification, release-support, documentation, automation-readiness and improvement work.

## Owner/tool
AI Governance Owner owns lifecycle control. VIF Orchestrator controls routing. Prompt Quality Reviewer controls prompt approval. QA Gatekeeper controls verification and evidence.

## Inputs
Request, context pack, job card, tool route, prompt approval, AI output, impact assessment, data boundary, human approval, verification evidence and lessons learned.

## Activities/fields
Lifecycle route:

Request → Context pack → Tool route → Prompt approval → AI output → Human review → Verification evidence → Decision → Implementation if approved → Monitoring → Lessons learned → Prompt/skill/process update

| Stage | Control | Required record | Gate |
|---|---|---|---|
| Request | Intake and classification | Intake/job card | Intake gate |
| Context pack | Source and no-truncation control | APP_CONTEXT / CONTEXT_PACK_STANDARD | Context gate |
| Tool route | Tool capability and data boundary | AI_SYSTEM_INVENTORY / TOOL_ROUTING_MATRIX | Tool-routing gate |
| Prompt approval | Prompt quality and forbidden pattern check | PROMPT_REGISTER / checklist | Prompt gate |
| AI output | Output captured and bounded | AI_TRACEABILITY_REGISTER | AI output gate |
| Human review | Required approver reviews output | HUMAN_OVERSIGHT_MATRIX | Oversight gate |
| Verification evidence | Tests/evidence/source check | VERIFICATION_REGISTER | Verification gate |
| Decision | PASS/HOLD/BLOCKED | Gate record | Relevant gate |
| Implementation | Only if approved job card exists | Diff/build evidence | Build gate |
| Monitoring | Bad output and performance monitoring | AI_BAD_OUTPUT_MONITORING_REGISTER | Monitoring gate |
| Lessons/update | Update prompts/skills/processes | LESSONS_LEARNED | Improvement gate |

## Outputs/records
AI lifecycle record, traceability record, gate decision, evidence records, monitoring records and improvement actions.

## Linked process
MOP-04 AI governance, SOP-06 Prompt control, COP-09 Job card approval, COP-10 Build/modification, COP-11 Verification, MOP-07 Improvement, SOP-12 Lessons learned.

## Linked gate
AI lifecycle gate, prompt gate, tool-routing gate, verification gate, human oversight gate, improvement gate.

## Human approval
Required at human review stage before any AI output becomes accepted evidence, implementation instruction, release support, compliance/audit content or automation trigger.

## Data boundary
Data must be classified before tool routing and must remain within AI_DATA_GOVERNANCE for every lifecycle stage.

## PASS/HOLD/BLOCKED rules
- PASS: every lifecycle stage has required record, evidence and approval where needed.
- HOLD: lifecycle stage is incomplete and no protected action proceeds.
- BLOCKED: lifecycle bypasses context, prompt approval, human review, verification, data boundary or job-card control.

## PDCA
- PLAN: define lifecycle route and required records.
- DO: execute AI use through controlled stages.
- CHECK: verify evidence, decisions and monitoring results.
- ACT: update prompts, skills, processes, risks and lessons learned.

## Update trigger
New AI route, lifecycle failure, AI output defect, verification failure, audit finding, CI finding, automation change or lesson learned.
