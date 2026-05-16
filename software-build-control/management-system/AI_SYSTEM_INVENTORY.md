# AI_SYSTEM_INVENTORY.md

## Purpose
Maintain a controlled inventory of AI systems, tools, models and automation routes used or planned for AI-assisted software development.

## Scope
Covers ChatGPT, Codex, Claude/Claude Code, Lovable, Gemini, Copilot, local LLMs, GitHub Actions, future n8n automation and future Supabase AI/automation if applicable.

## Owner/tool
AI Governance Owner maintains the inventory. VIF Orchestrator approves tool route. QA Gatekeeper reviews verification impact. Security/RLS Reviewer reviews data classification.

## Inputs
Tool/model information, provider, intended use, allowed/prohibited tasks, data classification, oversight requirement, linked agent/skill, risk rating, owner and review frequency.

## Activities/fields
| Tool/model name | Provider | Intended use | Allowed tasks | Prohibited tasks | Data classification allowed | Human oversight required | Linked agent/skill | Risk rating | Owner | Review frequency |
|---|---|---|---|---|---|---|---|---|---|---|
| ChatGPT | OpenAI | Architecture, planning, review, drafting | Review, reconciliation, prompts, procedures | AI-only PASS, unapproved app changes, invented facts | Public/internal only unless approved | Yes | VIF Orchestrator / prompt quality | Medium | AI Governance Owner | Quarterly/tool change |
| Codex | OpenAI/GitHub route | Repo inspection and bounded patches | Read-only inspection, approved patches | Unapproved broad rewrite, secret access, schema/RLS without gate | Repo data allowed by project approval | Yes | Codex Repo Inspector | High | VIF Orchestrator | Per repo use/tool change |
| Claude / Claude Code | Anthropic | Long-context review and bounded code review | Review, contradiction scan, scoped advice | Unbounded rewrite, production release decisions | Public/internal only unless approved | Yes | Claude Code Reviewer | Medium | AI Governance Owner | Quarterly/tool change |
| Lovable | Lovable | UI/app generation under approved scope | Plan mode, bounded UI/build slices | Backend/RLS authority, broad repair, release | Project-approved non-sensitive context | Yes | Lovable Builder | High | VIF Orchestrator | Per use/tool change |
| Gemini | Google | Contradiction/risk review | Independent review, comparison | Source-truth decision without evidence | Public/internal only unless approved | Yes | Contradiction Reviewer | Medium | AI Governance Owner | Quarterly/tool change |
| Copilot | GitHub/Microsoft | Inline assistance | Small local completion in approved file | Architecture, release, schema/RLS, security decisions | Local approved repo context | Yes | Developer assist | Medium | System owner | Quarterly/tool change |
| Local LLMs | Local/provider-specific | Offline contradiction/review where safe | Review, summarisation, pattern checks | Production truth, unverified code decisions | Data per local policy only | Yes | Contradiction Reviewer | Medium | AI Governance Owner | Per model change |
| GitHub Actions | GitHub | Future validation automation | Read-only checks, reports | Auto-merge, release, deploy, schema/RLS changes | Repo metadata/control files | Yes for activation | GitHub Release Controller | Medium | System owner | Per workflow change |
| n8n future automation | n8n | Future workflow routing after approval | Notifications, routing, evidence reminders | Auto-code, auto-release, auto-RLS, destructive actions | Minimal metadata only | Yes | Automation Controller | High | System owner | Before activation/quarterly |
| Supabase AI/automation | Supabase/future | Not active; future review only | None until approved | Schema/RLS/data changes without gate | None until approved | Yes | Supabase Backend Reviewer | High | Security/RLS Reviewer | Before any use |

## Outputs/records
AI system inventory, tool risk rating, allowed/prohibited task map, data classification and review record.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-05 Tool routing and tool qualification, SOP-04 Agent/worker control, SOP-08 Security/data protection.

## Linked gate
AI governance gate, tool-routing gate, data protection gate, automation-readiness gate.

## Human approval
Required before introducing a new AI tool, expanding allowed tasks, changing data classification or connecting external systems.

## Data boundary
Each tool may only receive data within its approved classification and project approval. Secrets, credentials, production data and customer data are blocked unless explicitly approved by exception.

## PASS/HOLD/BLOCKED rules
- PASS: tool has provider, intended use, allowed/prohibited tasks, data classification, owner, oversight and review frequency.
- HOLD: tool is useful but classification, owner, risk or review is incomplete.
- BLOCKED: tool can perform protected/destructive/customer-data actions without approval or evidence.

## PDCA
- PLAN: define tool purpose, boundaries, data class, owner and risk.
- DO: use tool only within approved route.
- CHECK: review failures, model changes, output quality and risk events.
- ACT: update inventory, controls, provider review, prompts and lessons.

## Update trigger
New AI tool, model upgrade, provider change, behaviour change, outage, pricing change, data classification change, incident, audit finding or lesson learned.
