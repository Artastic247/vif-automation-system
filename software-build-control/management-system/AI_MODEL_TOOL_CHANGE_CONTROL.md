# AI_MODEL_TOOL_CHANGE_CONTROL.md

## Purpose
Control AI model, tool and provider changes so behaviour, risk, cost, capability and validation impact are reviewed before continued or expanded use.

## Scope
Applies to model upgrades, tool behaviour changes, Lovable/Codex/Claude/GPT/Gemini/Copilot changes, local LLM changes, new AI tools, provider outages, pricing/credit changes and capability/risk reassessment.

## Owner/tool
AI Governance Owner owns model/tool change control. VIF Orchestrator controls routing changes. QA Gatekeeper controls validation impact. Credit-Burn Controller reviews cost/resource impact. Security/RLS Reviewer reviews data/security impact.

## Inputs
Tool change notice, observed behaviour change, provider outage, pricing/credit change, model upgrade, new tool request, bad-output trend, risk register and validation evidence.

## Activities/fields
| Change ID | Tool/model | Change type | Trigger | Risk impact | Data impact | Cost impact | Required validation | Decision | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| AIC-001 | TBD | Model upgrade / behaviour change / outage / pricing change / new tool | TBD | Low/Medium/High/Critical | TBD | TBD | Prompt/output verification and tool route review | PASS/HOLD/BLOCKED | AI Governance Owner | Open |

## Outputs/records
AI model/tool change record, validation requirement, risk update, tool inventory update, prompt/library update and route decision.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-05 Tool routing and tool qualification, SOP-06 Prompt control, SOP-11 Supplier/tool-provider control, MOP-07 Improvement.

## Linked gate
AI change-control gate, AI governance gate, tool-routing gate, provider review gate, validation gate.

## Human approval
Required for model/tool upgrades affecting approved prompts, code generation, repo access, data exposure, automation, cost, release support or protected work.

## Data boundary
Any tool/model change affecting data processing, retention, context handling, external calls or provider access must be reviewed against AI_DATA_GOVERNANCE before continued use.

## PASS/HOLD/BLOCKED rules
- PASS: change is assessed, risk/data/cost impacts are known, validation is complete and controls are updated.
- HOLD: change is known but validation or impact assessment is incomplete.
- BLOCKED: change creates uncontrolled protected-action, data, release, schema/RLS, automation or cost risk.

## PDCA
- PLAN: define change impact and validation needs.
- DO: review and test the changed tool/model in controlled scope.
- CHECK: compare output quality, risk, data and cost impact.
- ACT: update inventory, risks, prompts, provider review, tool routing and lessons learned.

## Update trigger
Model upgrade, tool behaviour change, new AI tool, provider outage, pricing/credit change, repeated bad output, audit finding, CI finding or lesson learned.
