# TOOL_SPECIFIC_PROMPT_INSTRUCTIONS.md

## Purpose
Define tool-specific prompt boundaries so each AI/tool worker receives instructions suited to its role, risk level and allowed/prohibited work, including identity/contact-data boundaries.

## Scope
Applies to ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n prompt/automation routing.

## Inputs
Context pack, source-of-truth lock, current job card, prompt quality checklist, tool-routing matrix, agent register, evidence requirements, rollback route, prohibited changes, current gate and approved contact register.

## Activities
Use the relevant tool-specific instruction before issuing a prompt.

| Tool/prompt route | Correct prompt control | Required input | Required output | Prohibited prompt behaviour | Stop condition | Linked gate |
|---|---|---|---|---|---|---|
| ChatGPT architecture/review prompt control | Use for management-system design, reconciliation, gate review and structured artefacts | Context pack, objective, scope, source basis | Analysis, artefacts, gates, next job card | Direct app coding without job card; invented company emails | Evidence missing, scope unclear or unapproved contact requested | Prompt/context gate |
| Lovable plan-mode prompt control | Use for scoped UI planning or screen implementation planning only | SCREEN_MAP, DATA_TABLE_SPEC, current job card | Plan or bounded UI changes | Backend/RLS authority, broad app repair, feature creep, email-based role decisions | Expands scope/schema or adds unapproved email identity | UI/job-card gate |
| Lovable build/repair prompt control | Use only after approved job card and UI/data/runtime maps | Approved job card, exact files/modules, verification route | Bounded implementation output | Broad repair, schema/RLS changes, email-based access decisions | Touches prohibited areas, cannot verify, or inserts unapproved emails | Build gate |
| Codex repo-inspection prompt control | Use for read-only repo inspection, file evidence, baseline lock | Repo, branch, source-lock request, evidence checklist | File inventory, risks, evidence gaps | Patching/building without job card | Starts modifying files or treats emails as role truth | Baseline/evidence gate |
| Codex patch prompt control | Use for bounded patch after approved job card | Job card, files in scope, tests, rollback route | Diff, test output, risk note | Broad rewrite, unapproved files, email-based role decisions | Out-of-scope diff, failed critical test or contact-data finding | Build/verification gate |
| Claude/Claude Code review prompt control | Use for long-context review, contradiction scan and bounded refactor reasoning | Context pack, repo/files, job card, stop rules | Review findings or bounded patch advice | Unbounded rewrite, hidden assumptions, invented emails | Touches unrelated modules or invents evidence/contact values | Review gate |
| Gemini/local LLM contradiction-review prompt control | Use for second opinion and contradiction/risk scan | Source evidence, specific question, decision to test | Contradiction list, risk notes | Source-of-truth decision without evidence; invented contacts | Unsupported claims, missing evidence or unapproved contact assumptions | Contradiction/review gate |
| Copilot inline-assist boundary | Use only inside approved file/scope as local completion | Open file, small task, job-card scope | Small completion | Architecture, schema, release, broad refactor, email-based role decisions | Completion changes behaviour outside scope or adds real emails | Build gate |
| n8n prompt/automation boundary for future use | Use only for routing/evidence notifications after automation readiness | Approved workflow, safe trigger, no destructive action | Issue, notification, evidence route | Auto-code, auto-RLS, auto-release, auto-merge, contact-data creation | Destructive/judgement action or unapproved identity automation | Automation-readiness gate |

## Identity/contact-data prompt rules
- Never invent company emails.
- Never insert SNAGG emails unless approved in APPROVED_CONTACT_REGISTER for the specific project/app and purpose.
- Never use email addresses as role, permission, admin, tenant, auth, access or security decision logic.
- Use placeholders for examples unless a project contact is approved.
- Treat email/contact findings as evidence requiring classification before use.

## Outputs
Tool-specific prompt decision, approved prompt, HOLD/BLOCKED prompt, failure record, contact-data finding or tool-routing update.

## Records
PROMPT_REGISTER, PROMPT_QUALITY_CHECKLIST, PROMPT_FAILURE_REGISTER, TOOL_ROUTING_MATRIX, AGENT_REGISTER, CURRENT_JOB_CARD, VERIFICATION_REGISTER, APPROVED_CONTACT_REGISTER and LESSONS_LEARNED.

## Owner/tool
Prompt Quality Reviewer owns prompt quality. VIF Orchestrator controls tool routing. Specialist agent owns tool-specific evidence. QA Gatekeeper checks verification/release prompt boundaries. Security/RLS Reviewer checks identity/contact-data risk.

## Linked process
SOP-06 Prompt control and prompt quality, SOP-05 Tool routing and tool qualification, SOP-04 Agent/worker control, SOP-08 Security, tenant and data protection control, COP-09 Job card creation and approval, COP-10 Build/modification control, MOP-04 AI governance and tool-use policy.

## Linked gate
Prompt gate, tool-routing gate, job-card gate, build gate, verification gate, release gate, identity/contact-data gate, automation-readiness gate.

## PDCA
- PLAN: select the correct tool route and define prompt input/output/scope/safety/contact boundaries.
- DO: issue the tool-specific prompt only within the approved route.
- CHECK: review output for scope, evidence, prohibited changes, tool drift, verification needs and identity/contact-data findings.
- ACT: update tool-specific prompt instructions, tool routing, agent limits, approved contact register, lessons learned and prompt library.

## PASS/HOLD/BLOCKED rules
- PASS: prompt matches tool purpose, source basis, job card, evidence, safety/contact boundary and stop condition.
- HOLD: tool route, prompt inputs or contact approval are incomplete and no execution proceeds.
- BLOCKED: prompt asks the tool to exceed its allowed work, alter protected areas, use customer data, invent company emails, use email for access decisions, activate automation, release, or act without evidence/job card.

## Update trigger
New tool, tool failure, prompt drift, output quality issue, out-of-scope edit, generated email/contact finding, credit burn, CI finding, automation change, app failure, audit finding or lesson learned.
