# AI_TOOL_PROVIDER_REVIEW.md

## Purpose
Control AI tool/provider selection and ongoing review so external AI tools are suitable, bounded, monitored and revalidated before expanded use.

## Scope
Applies to ChatGPT, Codex, Claude/Claude Code, Lovable, Gemini, Copilot, local LLMs, GitHub Actions, future n8n automation and future AI-enabled services.

## Owner/tool
AI Governance Owner owns provider review. VIF Orchestrator controls tool routing. Security/RLS Reviewer reviews data risk. System owner approves new or high-risk provider use.

## Inputs
AI system inventory, provider details, intended use, data classification, tool risk, known limitations, cost model, outage history, security/data terms where available and lessons learned.

## Activities/fields
| Provider/tool | Intended use | Risk level | Data allowed | Known limitations | Required controls | Review frequency | Decision |
|---|---|---|---|---|---|---|---|
| ChatGPT | Review/planning/drafting | Medium | Public/internal unless approved | Hallucination/context limits | Prompt/source/evidence controls | Quarterly/change | Controlled use |
| Codex | Repo inspection/patch support | High | Project-approved repo data | Repo/context/tool action risk | Job card, diff review, tests | Per repo/change | Controlled use |
| Lovable | UI/app generation | High | Project-approved non-sensitive context | Credit burn, broad generation | Plan mode, scope gates | Per use/change | Controlled use |
| n8n future | Workflow automation | High | Metadata only until approved | Automation overreach | Automation-readiness gate | Before activation | HOLD |

## Outputs/records
Provider/tool review record, allowed use decision, risk rating, data boundary, review frequency and required controls.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-05 Tool routing and tool qualification, SOP-11 Supplier/tool-provider control, SOP-10 Contingency and continuity control.

## Linked gate
AI governance gate, supplier/tool gate, tool-routing gate, data protection gate, automation-readiness gate.

## Human approval
Required for new AI tools, provider change, expanded use, external connection, automation activation or high-risk data processing.

## Data boundary
Provider/tool use is limited by AI_DATA_GOVERNANCE and must not receive secrets, credentials, production data or customer data without approved exception.

## PASS/HOLD/BLOCKED rules
- PASS: provider/tool has approved use, risk, data boundary, controls and review frequency.
- HOLD: provider/tool is useful but risk, data boundary or review evidence is incomplete.
- BLOCKED: provider/tool allows protected/destructive/customer-data actions without controls or approval.

## PDCA
- PLAN: assess provider/tool before use.
- DO: use only within approved route.
- CHECK: monitor outages, behaviour changes, cost, limitations and bad outputs.
- ACT: update inventory, routing, risks, contingency and lessons learned.

## Update trigger
New provider/tool, model/tool change, outage, pricing change, incident, data concern, audit finding, CI finding or lesson learned.
