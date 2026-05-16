# AI_CREDIT_BURN_REGISTER.md

## Purpose
Monitor AI credit, token, time and resource burn so repeated failed generations, poor tool routing and low-value loops are detected and stopped before they create waste or quality drift.

## Scope
Applies to ChatGPT, Codex, Claude/Claude Code, Lovable, Gemini, Copilot, local LLMs, GitHub automation, future n8n flows and other AI-assisted software-build tools.

## Owner/tool
Credit-Burn Controller owns this register. VIF Orchestrator controls tool routing. AI Governance Owner reviews systemic waste. QA Gatekeeper checks whether failures caused quality risk.

## Inputs
Tool, task, job card, prompt, credit/token/resource use, failed attempts, output quality, rework caused, stop trigger, prevention action and future route.

## Activities/fields
| Burn ID | Tool | Task | Linked job card | Credit/token/resource use | Result achieved | Failed attempts | Rework caused | Stop trigger | Prevention action | Preferred future route | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AICB-001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Credit-Burn Controller | Open |

## Outputs/records
Credit-burn record, stop/re-route decision, prevention action, preferred future route, lesson learned and tool-routing update.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-05 Tool routing and tool qualification, SOP-06 Prompt control and prompt quality, MOP-07 Corrective action and continual improvement.

## Linked gate
AI governance gate, tool-routing gate, prompt gate, improvement gate, automation-readiness gate.

## Human approval
Required when burn exceeds stop trigger, repeated failed repairs occur, or a tool route should be changed for future work.

## Data boundary
Credit-burn records must not include secrets, customer data, production data or uncontrolled identity/contact data. Use task summaries and placeholders.

## PASS/HOLD/BLOCKED rules
- PASS: burn is tracked, result is known, stop trigger is clear and prevention/future route is defined.
- HOLD: burn is known but result, rework or prevention evidence is incomplete.
- BLOCKED: repeated failed AI work continues without stop trigger, re-route or quality review.

## PDCA
- PLAN: define expected tool route, stop trigger and resource limit before high-cost work.
- DO: track use, failed attempts and result achieved.
- CHECK: compare burn against result and quality evidence.
- ACT: stop, re-route, update prompts, update tool routing and capture lessons learned.

## Update trigger
High AI spend, failed generation loop, repeated repair failure, tool-route concern, poor output quality, pricing change, audit finding, CI finding or lesson learned.
