# PROMPT_CONTROL_PROCEDURE.md

## Purpose
Control prompt engineering as a managed process so AI-assisted app development cannot proceed from vague, truncated, tool-inappropriate, unapproved, or unsafe prompts.

## Scope
Applies to ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLMs, Copilot, future n8n prompt/automation routing, and any AI-assisted work that affects architecture, reviews, app code, schema/RLS, tenant rollout, release, evidence, or management-system records.

## Process owner
Prompt Quality Reviewer owns the procedure. VIF Orchestrator approves prompt route and gate fit. QA Gatekeeper verifies evidence before PASS.

## Inputs
- Current APP_CONTEXT or CONTEXT_PACK_STANDARD record.
- Approved CURRENT_JOB_CARD where implementation, repair, build, schema/RLS, release, rollout, or automation work is requested.
- Source-of-truth evidence: repo, branch, version, files, logs, screenshots, DB/RLS evidence, tenant/environment records, or prior gate outputs.
- Tool routing decision and tool boundary.
- Required outputs, verification method, rollback route and stop condition.

## Activities
1. Classify prompt type: intake, architecture/review, planning, repo inspection, patch/build, contradiction review, inline assist, automation routing, verification, release, or rollback.
2. Confirm source basis and context pack are current.
3. Confirm current gate and linked process ID.
4. Confirm whether an approved job card is required.
5. Apply the PROMPT_QUALITY_CHECKLIST.
6. Check FORBIDDEN_PROMPT_PATTERNS.
7. Select tool-specific prompt instruction.
8. Include required scope, prohibited actions, evidence, verification, rollback, stop condition, secret-safety and customer-data boundaries.
9. Execute only through the approved tool route.
10. Review AI output against job card and evidence.
11. Log failures in PROMPT_FAILURE_REGISTER and link to lessons learned, RCA, skills, agents, tool routing and process updates.

## Outputs
- Approved prompt or rejected prompt decision.
- Prompt register entry where reusable.
- Prompt failure record where applicable.
- Linked job card, gate decision and verification/evidence record.
- Procedure, skill, agent, tool-routing or process update where failures repeat.

## Records
PROMPT_REGISTER, PROMPT_QUALITY_CHECKLIST, PROMPT_FAILURE_REGISTER, PROMPT_REVISION_CONTROL, FORBIDDEN_PROMPT_PATTERNS, APPROVED_PROMPT_LIBRARY, CURRENT_JOB_CARD, VERIFICATION_REGISTER, LESSONS_LEARNED.

## Linked process IDs
SOP-06 Prompt control and prompt quality, COP-02 Source-of-truth and context lock, COP-09 Job card creation and approval, COP-10 Build/modification control, COP-11 Verification, COP-14 Release and rollback, MOP-04 AI governance and tool-use policy, MOP-07 Corrective action and continual improvement, SOP-12 Lessons learned and knowledge reuse.

## Linked agents
VIF Orchestrator, Prompt Quality Reviewer, QA Gatekeeper, Codex Repo Inspector, Lovable Builder, Claude Code Reviewer, GitHub Release Controller, Supabase Backend Reviewer, Security/RLS Reviewer, Lessons Learned Controller.

## Linked skills
Context lock, scope lock, prompt quality review, evidence map, tool routing, runtime-first review, database/RLS review, verification review, release check, lessons learned.

## Linked gates
Context gate, source-of-truth gate, job-card gate, prompt gate, tool-routing gate, build gate, DB/RLS gate, verification gate, release gate, tenant rollout gate, lessons-learned gate.

## PDCA
- PLAN: define prompt purpose, source basis, context pack, tool route, scope, prohibited actions, evidence, verification, rollback and stop condition.
- DO: issue the prompt only within the approved tool route and current job card.
- CHECK: compare output to source evidence, job-card scope, verification requirements, prohibited-change boundaries and gate criteria.
- ACT: reject, correct, revise prompt, update prompt register/library, log failures, update lessons learned, skills, agents, tool routing, procedures or validation rules.

## PASS/HOLD/BLOCKED rules
- PASS: prompt has objective, source basis, mode, scope in/out, files/modules in scope, prohibited changes, required inputs/outputs, evidence, verification, rollback, stop condition, tool route, secret/customer-data boundary and linked job card where required.
- HOLD: prompt intent is useful but context, evidence, output, verification or rollback is incomplete and no implementation proceeds.
- BLOCKED: prompt asks to fix everything, build broadly, continue from previous chat without context pack, change schema/RLS without gate, release without evidence, use customer data without approval, apply to all tenants without rollout register, or proceed without approved job card where required.

## Update trigger
Prompt failure, tool drift, hallucination, context loss, wrong repo/branch, out-of-scope edits, failed build/test/release, customer-data risk, credit burn, audit finding, CI finding, or lesson learned.
