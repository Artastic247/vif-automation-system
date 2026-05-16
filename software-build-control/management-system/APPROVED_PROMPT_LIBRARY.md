# APPROVED_PROMPT_LIBRARY.md

## Purpose
Define the approved prompt library structure so reusable prompts are controlled, versioned, linked to job cards/gates, and separated by tool and purpose.

## Scope
Applies to controlled prompt families for ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n routing.

## Inputs
PROMPT_REGISTER, PROMPT_QUALITY_CHECKLIST, PROMPT_REVISION_CONTROL, TOOL_SPECIFIC_PROMPT_INSTRUCTIONS, CONTEXT_PACK_STANDARD, CURRENT_JOB_CARD and lessons learned.

## Activities
- Store only approved or draft-controlled prompts.
- Classify prompts by tool, mode, process and gate.
- Link each prompt to its required inputs, outputs, evidence, stop condition and prohibited actions.
- Keep draft prompts separated from approved active prompts.
- Retire unsafe, stale, duplicated or ineffective prompts.

## Outputs
Approved prompt library structure, prompt categories and prompt-use boundaries.

## Records
| Library section | Purpose | Tool | Status | Required linkage |
|---|---|---|---|---|
| architecture-review | Architecture, gap review, system design | ChatGPT/Claude/Gemini | Draft/Approved | Context pack, gate, evidence |
| repo-inspection | Read-only repo baseline and evidence lock | Codex/GitHub | Draft/Approved | Repo/branch/job card |
| patch-build | Controlled patch/build prompt | Codex/Lovable/Claude Code | Draft/Approved | Approved job card, verification, rollback |
| verification | Evidence and test review | ChatGPT/Codex | Draft/Approved | Verification register |
| release-rollout | Release readiness and tenant rollout review | ChatGPT/GitHub | Draft/Approved | Release/tenant/rollback records |
| contradiction-review | Independent contradiction and risk scan | Gemini/local LLM/ChatGPT | Draft/Approved | Source evidence and scope |
| automation-boundary | Future n8n/workflow routing prompt | n8n/ChatGPT | Draft only until approved | Automation readiness gate |

## Owner/tool
Prompt Quality Reviewer maintains. VIF Orchestrator approves library structure. QA Gatekeeper reviews release/verification prompt families.

## Linked process
SOP-06 Prompt control and prompt quality, SOP-05 Tool routing and tool qualification, MOP-04 AI governance, SOP-12 Lessons learned.

## Linked gate
Prompt gate, tool-routing gate, job-card gate, verification gate, release gate, automation-readiness gate.

## PDCA
- PLAN: define prompt category, owner, inputs, tool route and use boundary.
- DO: use only approved prompts for repeat work.
- CHECK: review output quality, failure rate and evidence linkage.
- ACT: revise, deprecate, retire or create new prompt variants based on lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: prompt library entry is versioned, owned, linked to gate/process and reviewed.
- HOLD: prompt is draft or pending review.
- BLOCKED: prompt is active without approval, job-card linkage, evidence boundary or tool-specific limits.

## Update trigger
New prompt family, tool/model change, prompt failure, process change, audit finding, CI finding or lesson learned.
