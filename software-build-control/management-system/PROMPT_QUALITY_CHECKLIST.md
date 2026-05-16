# PROMPT_QUALITY_CHECKLIST.md

## Purpose
Provide a mandatory prompt-quality checklist before any AI tool is used for app-development planning, review, build, repair, verification, release, rollout, automation, or management-system updates.

## Scope
Applies to ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n prompt/automation routing.

## Inputs
Context pack, source-of-truth evidence, current job card, current gate, tool route, files/modules in scope, prohibited changes, evidence requirements, verification method, rollback route and stop condition.

## Activities
Complete this checklist before issuing a prompt:

| Check | Required? | PASS evidence | HOLD/BLOCKED trigger |
|---|---:|---|---|
| Objective defined | Yes | Clear outcome | Vague request |
| Source basis defined | Yes | Repo/files/evidence/context pack | “Continue from previous chat” only |
| Mode defined | Yes | INTAKE/REVIEW/COMMANDER/AUDIT/BUILD/VERIFY etc. | Mode unclear |
| Scope in defined | Yes | Bounded modules/files/tasks | Broad build/change |
| Scope out defined | Yes | Prohibited actions listed | No exclusions |
| Files/modules in scope | Where applicable | Specific files/modules | Whole app by default |
| Prohibited changes | Yes | App/Supabase/RLS/deploy/data boundaries | Unsafe work allowed |
| Required inputs | Yes | Evidence list | Missing evidence |
| Required outputs | Yes | Expected artefact/result | Open-ended output |
| Evidence required | Yes | Logs/tests/screenshots/DB proof etc. | Claims without proof |
| Verification method | Yes | Build/test/review/check method | No verification |
| Rollback route | For build/release/schema/tenant work | Revert/rollback/flag route | No rollback |
| Stop condition | Yes | Explicit stop rule | Tool can continue uncontrolled |
| Gate decision | Yes | PASS/HOLD/BLOCKED expected | No gate language |
| Tool routing | Yes | Correct tool selected | “Use all tools” |
| Secret-safety boundary | Yes | No secrets/env/API keys | Secrets may be exposed |
| Customer-data boundary | Yes | No customer data unless approved | Customer data risk |
| No “fix everything” | Yes | Bounded job card | Broad repair prompt |
| No implementation without approved job card | Yes | Job card reference | Build/repair without job card |

## Outputs
Approved prompt, HOLD prompt needing revision, or BLOCKED prompt that must not be executed.

## Records
Prompt quality checklist result, linked prompt register entry, current job card, evidence pack, verification record and failure record where applicable.

## Owner/tool
Prompt Quality Reviewer owns the checklist. VIF Orchestrator confirms routing. QA Gatekeeper verifies evidence language.

## Linked process
SOP-06 Prompt control and prompt quality, COP-09 Job card creation and approval, COP-10 Build/modification control, COP-11 Verification.

## Linked gate
Prompt gate, job-card gate, tool-routing gate, verification gate.

## PDCA
- PLAN: define objective, source basis, scope, tool route, evidence and safety boundaries.
- DO: issue only the approved prompt.
- CHECK: evaluate output against checklist and job card.
- ACT: revise prompt, log failure, update library/procedure/skill/tool route.

## PASS/HOLD/BLOCKED rules
- PASS: all applicable checklist items are satisfied.
- HOLD: prompt is not yet executable because evidence/scope/output is incomplete.
- BLOCKED: prompt contains forbidden patterns or authorises unsafe app/schema/release/customer-data work.

## Update trigger
Prompt failure, tool drift, bad output, repeated rework, audit finding, CI finding or lesson learned.
