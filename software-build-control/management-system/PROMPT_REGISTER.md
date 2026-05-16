# PROMPT_REGISTER.md

## Purpose
Maintain a controlled inventory of reusable prompts used for architecture, review, planning, repo inspection, patching, verification, validation, release, contradiction review and automation-boundary work.

## Scope
Applies to all approved reusable prompts used by ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n routing.

## Inputs
Approved job card, context pack, source-of-truth evidence, tool route, prompt quality checklist, linked process and linked gate.

## Activities
- Register only prompts that have passed PROMPT_QUALITY_CHECKLIST.
- Link every registered prompt to a process, skill, agent, tool and gate.
- Identify prompt version, status, owner, allowed use, prohibited use and review trigger.
- Retire prompts that cause drift, rework, unsafe tool use or repeated failure.

## Outputs
Approved prompt inventory, prompt status, prompt owner, version/revision evidence and review decision.

## Records
| Prompt ID | Prompt name | Tool/model | Purpose | Linked process | Linked gate | Owner/tool | Approved use | Prohibited use | Required inputs | Required outputs | Version | Status | Last review | Linked job card/skill |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PRM-001 | Architecture/review mode | ChatGPT | Controlled architecture and gap review | SOP-06 / MOP-04 | Prompt gate | Prompt Quality Reviewer | Review/planning only | App implementation without job card | Context pack, objective, scope | Findings, gates, next job card | v0.1 | Draft | TBD | Prompt quality review |

## Owner/tool
Prompt Quality Reviewer maintains. VIF Orchestrator approves tool route. QA Gatekeeper checks evidence linkage.

## Linked process
SOP-06 Prompt control and prompt quality; MOP-04 AI governance and tool-use policy; COP-09 Job card creation and approval.

## Linked gate
Prompt gate, tool-routing gate, job-card gate.

## PDCA
- PLAN: define prompt purpose, tool, source basis and allowed use.
- DO: use prompt only within approved context and tool route.
- CHECK: review output quality, scope adherence and evidence linkage.
- ACT: revise, retire or update linked skills/procedures after failures.

## PASS/HOLD/BLOCKED rules
- PASS: prompt is registered, versioned, linked to process/gate, and has allowed/prohibited use.
- HOLD: prompt is useful but lacks review or full linkage.
- BLOCKED: prompt is broad, unsafe, unversioned, or authorises implementation without job card.

## Update trigger
New reusable prompt, prompt revision, tool change, prompt failure, audit finding, CI finding or lesson learned.
