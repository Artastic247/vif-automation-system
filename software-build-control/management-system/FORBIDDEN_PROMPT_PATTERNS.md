# FORBIDDEN_PROMPT_PATTERNS.md

## Purpose
Define prompt patterns that are prohibited because they cause uncontrolled scope, tool drift, missing evidence, unsafe backend/schema/RLS changes, tenant exposure, release risk, customer-data risk or false PASS decisions.

## Scope
Applies to all AI-assisted work across planning, design, build, repair, review, verification, validation, release, rollout, automation and management-system changes.

## Inputs
Prompt quality checklist, prompt failure register, lessons learned, tool output failures, audit findings, CI findings and app-development incidents.

## Activities
- Check every prompt against this register before execution.
- Reject or rewrite prompts containing forbidden patterns.
- Link repeated patterns to PROMPT_FAILURE_REGISTER and LESSONS_LEARNED.
- Update tool-specific prompt instructions and skills when new forbidden patterns emerge.

## Outputs
Prompt rejection, prompt rewrite, failure record, lesson learned, skill/procedure update or tool-route update.

## Records
| Pattern ID | Forbidden prompt pattern | Why blocked | Required safer route | Gate impact |
|---|---|---|---|---|
| FPP-001 | fix everything | Unbounded scope and uncontrolled changes | Create approved job card with scope in/out | BLOCKED |
| FPP-002 | make it work | Vague objective and no evidence | Define defect, evidence and expected result | BLOCKED |
| FPP-003 | complete the backend without runtime map | Backend assumptions and data/security risk | Complete RUNTIME_MAP and DB/backend gate | BLOCKED |
| FPP-004 | build all features | Feature creep and no release control | Add features to backlog and select one job card | BLOCKED |
| FPP-005 | clean up everything | Broad refactor risk | Define exact files and cleanup objective | BLOCKED |
| FPP-006 | improve the app without scope | Uncontrolled design/build changes | Define scope, outputs and verification | HOLD/BLOCKED |
| FPP-007 | continue from previous chat without context pack | Truncation and stale context risk | Rebuild context pack and source lock | BLOCKED |
| FPP-008 | use all tools | Tool misuse and uncontrolled execution | Use TOOL_ROUTING_MATRIX | BLOCKED |
| FPP-009 | release/publish without verification evidence | False release and rollback risk | Complete verification and release registers | BLOCKED |
| FPP-010 | change schema/RLS without database/backend gate | Security and tenant exposure risk | Complete DATABASE_BACKEND_CONTROL and RLS evidence | BLOCKED |
| FPP-011 | apply to all tenants without tenant rollout register | Wide blast-radius risk | Complete TENANT_ROLLOUT_REGISTER | BLOCKED |
| FPP-012 | use customer data for testing without approval and data rules | Data protection risk | Use approved/sanitised data rules | BLOCKED |
| FPP-013 | rewrite the whole app | High regression and scope risk | Justify architecture decision and job card | BLOCKED |
| FPP-014 | skip tests or trust the tool | False PASS risk | Run verification evidence route | BLOCKED |
| FPP-015 | push/merge/deploy now | Release governance bypass | Use release and rollback gate | BLOCKED |

## Owner/tool
Prompt Quality Reviewer maintains. VIF Orchestrator enforces tool routing. QA Gatekeeper enforces evidence/release boundaries.

## Linked process
SOP-06 Prompt control and prompt quality, COP-09 Job card creation and approval, COP-10 Build/modification control, COP-14 Release and rollback, SOP-08 Security/data protection, SOP-12 Lessons learned.

## Linked gate
Prompt gate, job-card gate, DB/RLS gate, tenant rollout gate, release gate, lessons-learned gate.

## PDCA
- PLAN: define forbidden patterns and safer routes.
- DO: screen prompts before use.
- CHECK: review prompt failures for new patterns.
- ACT: update register, skills, procedures, prompts and validation rules.

## PASS/HOLD/BLOCKED rules
- PASS: prompt contains no forbidden pattern and has required controls.
- HOLD: prompt can be rewritten safely before use.
- BLOCKED: prompt contains a forbidden pattern that could lead to app, data, schema/RLS, tenant, release, or automation risk.

## Update trigger
Prompt failure, AI tool drift, bad patch, missing evidence, release incident, schema/RLS risk, tenant exposure risk, audit finding, CI finding or lesson learned.
