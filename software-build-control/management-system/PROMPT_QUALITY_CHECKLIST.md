# PROMPT_QUALITY_CHECKLIST.md

## Purpose
Provide a mandatory prompt-quality checklist before any AI tool is used for app-development planning, review, build, repair, verification, release, rollout, automation, or management-system updates.

## Scope
Applies to ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n prompt/automation routing.

## Inputs
Context pack, source-of-truth evidence, current job card, current gate, tool route, files/modules in scope, prohibited changes, evidence requirements, verification method, rollback route, stop condition, approved project contacts and identity/contact-data boundaries.

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
| Contact-data boundary | Yes | Real emails only if approved; placeholders preferred | Unapproved email/contact identity |
| Real email/contact identity check | Yes | Prompt contains no real email or uses approved register entry | Unknown or unapproved email |
| Project contact approval check | Yes | Email approved for this project/app and purpose | Project approval missing |
| Contact/owner only check | Yes | Email used only as approved contact/owner field | Email used for role/security/access logic |
| Placeholder suitability check | Yes | Placeholder used where real email is unnecessary | Real email inserted generically |
| SNAGG email control check | Yes | SNAGG email used only where directed and registered | Generic SNAGG email insertion |
| No “fix everything” | Yes | Bounded job card | Broad repair prompt |
| No implementation without approved job card | Yes | Job card reference | Build/repair without job card |

## Outputs
Approved prompt, HOLD prompt needing revision, or BLOCKED prompt that must not be executed.

## Records
Prompt quality checklist result, linked prompt register entry, current job card, evidence pack, verification record, contact-data approval evidence and failure record where applicable.

## Owner/tool
Prompt Quality Reviewer owns the checklist. VIF Orchestrator confirms routing. QA Gatekeeper verifies evidence language. Security/RLS Reviewer reviews contact-data and role/security logic risk.

## Linked process
SOP-06 Prompt control and prompt quality, COP-09 Job card creation and approval, COP-10 Build/modification control, COP-11 Verification, SOP-08 Security, tenant and data protection control.

## Linked gate
Prompt gate, job-card gate, tool-routing gate, verification gate, identity/contact-data gate.

## PDCA
- PLAN: define objective, source basis, scope, tool route, evidence, safety boundaries and contact-data boundaries.
- DO: issue only the approved prompt.
- CHECK: evaluate output against checklist, job card, approved contact register and identity/security rules.
- ACT: revise prompt, log failure, update library/procedure/skill/tool route and contact-data controls.

## PASS/HOLD/BLOCKED rules
- PASS: all applicable checklist items are satisfied, including contact-data approval and role/security logic boundaries.
- HOLD: prompt is not yet executable because evidence/scope/output/contact approval is incomplete.
- BLOCKED: prompt contains forbidden patterns, unapproved real email use, email-based role/security logic, or unsafe app/schema/release/customer-data work.

## Update trigger
Prompt failure, tool drift, bad output, repeated rework, generated email/contact finding, audit finding, CI finding or lesson learned.
