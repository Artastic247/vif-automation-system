# TOOL_SPECIFIC_PROMPT_INSTRUCTIONS.md

## Purpose
Define tool-specific prompt boundaries so each AI/tool worker receives instructions suited to its role, risk level and allowed/prohibited work.

## Scope
Applies to ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n prompt/automation routing.

## Inputs
Context pack, source-of-truth lock, current job card, prompt quality checklist, tool-routing matrix, agent register, evidence requirements, rollback route, prohibited changes and current gate.

## Activities
Use the relevant tool-specific instruction before issuing a prompt.

| Tool/prompt route | Correct prompt control | Required input | Required output | Prohibited prompt behaviour | Stop condition | Linked gate |
|---|---|---|---|---|---|---|
| ChatGPT architecture/review prompt control | Use for management-system design, reconciliation, gate review and structured artefacts | Context pack, objective, scope, source basis | Analysis, artefacts, gates, next job card | Direct app coding without job card | Evidence missing or scope unclear | Prompt/context gate |
| Lovable plan-mode prompt control | Use for scoped UI planning or screen implementation planning only | SCREEN_MAP, DATA_TABLE_SPEC, current job card | Plan or bounded UI changes | Backend/RLS authority, broad app repair, feature creep | Expands scope or schema unexpectedly | UI/job-card gate |
| Lovable build/repair prompt control | Use only after approved job card and UI/data/runtime maps | Approved job card, exact files/modules, verification route | Bounded implementation output | “Fix everything”, broad repair, schema/RLS changes | Touches prohibited areas or cannot verify | Build gate |
| Codex repo-inspection prompt control | Use for read-only repo inspection, file evidence, baseline lock | Repo, branch, source-lock request, evidence checklist | File inventory, risks, evidence gaps | Patching/building without job card | Starts modifying files | Baseline/evidence gate |
| Codex patch prompt control | Use for bounded patch after approved job card | Job card, files in scope, tests, rollback route | Diff, test output, risk note | Broad rewrite or unapproved files | Out-of-scope diff or failed critical test | Build/verification gate |
| Claude/Claude Code review prompt control | Use for long-context review, contradiction scan and bounded refactor reasoning | Context pack, repo/files, job card, stop rules | Review findings or bounded patch advice | Unbounded rewrite, hidden assumptions | Touches unrelated modules or invents evidence | Review gate |
| Gemini/local LLM contradiction-review prompt control | Use for second opinion and contradiction/risk scan | Source evidence, specific question, decision to test | Contradiction list, risk notes | Source-of-truth decision without evidence | Unsupported claims or missing evidence | Contradiction/review gate |
| Copilot inline-assist boundary | Use only inside approved file/scope as local completion | Open file, small task, job-card scope | Small completion | Architecture, schema, release or broad refactor decisions | Completion changes behaviour outside scope | Build gate |
| n8n prompt/automation boundary for future use | Use only for routing/evidence notifications after automation readiness | Approved workflow, safe trigger, no destructive action | Issue, notification, evidence route | Auto-code, auto-RLS, auto-release, auto-merge | Destructive or judgement action | Automation-readiness gate |

## Outputs
Tool-specific prompt decision, approved prompt, HOLD/BLOCKED prompt, failure record or tool-routing update.

## Records
PROMPT_REGISTER, PROMPT_QUALITY_CHECKLIST, PROMPT_FAILURE_REGISTER, TOOL_ROUTING_MATRIX, AGENT_REGISTER, CURRENT_JOB_CARD, VERIFICATION_REGISTER and LESSONS_LEARNED.

## Owner/tool
Prompt Quality Reviewer owns prompt quality. VIF Orchestrator controls tool routing. Specialist agent owns tool-specific evidence. QA Gatekeeper checks verification/release prompt boundaries.

## Linked process
SOP-06 Prompt control and prompt quality, SOP-05 Tool routing and tool qualification, SOP-04 Agent/worker control, COP-09 Job card creation and approval, COP-10 Build/modification control, MOP-04 AI governance and tool-use policy.

## Linked gate
Prompt gate, tool-routing gate, job-card gate, build gate, verification gate, release gate, automation-readiness gate.

## PDCA
- PLAN: select the correct tool route and define prompt input/output/scope/safety boundaries.
- DO: issue the tool-specific prompt only within the approved route.
- CHECK: review output for scope, evidence, prohibited changes, tool drift and verification needs.
- ACT: update tool-specific prompt instructions, tool routing, agent limits, lessons learned and prompt library.

## PASS/HOLD/BLOCKED rules
- PASS: prompt matches tool purpose, source basis, job card, evidence, safety boundary and stop condition.
- HOLD: tool route or prompt inputs are incomplete and no execution proceeds.
- BLOCKED: prompt asks the tool to exceed its allowed work, alter protected areas, use customer data, activate automation, release, or act without evidence/job card.

## Update trigger
New tool, tool failure, prompt drift, output quality issue, out-of-scope edit, credit burn, CI finding, automation change, app failure, audit finding or lesson learned.
