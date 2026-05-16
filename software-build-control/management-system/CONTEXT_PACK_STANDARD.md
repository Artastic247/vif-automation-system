# CONTEXT_PACK_STANDARD.md

## Purpose
Define the standard context pack required before AI-assisted app development, repair, review, release, rollout, automation or management-system work proceeds.

## Scope
Applies to all app projects and control-system work where context loss, truncation, stale evidence, wrong repo/branch, unsupported assumptions or uncontrolled identity/contact-data use could cause rework, unsafe changes or identity misuse.

## Inputs
App request, current app context, repo, branch/version, current commit if known, current job card, current gate, source-of-truth artefacts, latest evidence pack, known defects, exclusions, tenant/environment context, rollback context, latest decision, unresolved gaps, archive/reference links, approved project contacts and contact-data approval evidence.

## Activities
Create or refresh a context pack before any prompt that could affect planning, code, schema/RLS, verification, validation, release, rollout, CI, n8n, customer data or identity/contact data.

Required context pack fields:

| Field | Required content |
|---|---|
| App identity | App name, purpose, owner and current workstream |
| Repo | Repository name/path and access basis |
| Branch/version | Current branch, version and baseline state |
| Current commit if known | Commit SHA or MISSING |
| Current job card | Approved job card or HOLD if not applicable |
| Current gate | Intake, baseline, prompt, build, verification, release etc. |
| Source-of-truth artefacts | Files, screenshots, logs, DB evidence, decisions and registers |
| Latest evidence pack | Build/test/review/backend/tenant/release evidence available |
| Known defects | Current defect list and status |
| Current exclusions | What must not change |
| Tenant/environment context | Dev/demo/staging/pilot/prod and data sensitivity |
| Rollback context | Commit/deploy/feature/database rollback route where relevant |
| Approved project contacts | Contacts from APPROVED_CONTACT_REGISTER approved for this project/app and purpose |
| Prohibited contact use | No unapproved emails, no generic SNAGG email insertion, no email-based role/security logic |
| Email/contact placeholders | Use `<project-owner-email>`, `<approved-contact@example.com>`, `owner@example.com` or `user@example.test` where real contact is not approved |
| Contact-data evidence rule | Real email/contact values require project/app, purpose, allowed artefacts, owner, approval evidence, review date and status |
| Latest decision | Most recent PASS/HOLD/BLOCKED decision |
| Unresolved gaps | Missing evidence, risks and blocked decisions |
| No-truncation rule | Context must be split into stable artefacts, not one giant prompt |
| Archive/reference handling | Old drafts are references only unless reconfirmed as source of truth |

## Outputs
Current context pack, evidence gap list, source-of-truth lock decision, contact-data approval decision and prompt readiness decision.

## Records
APP_CONTEXT, CURRENT_JOB_CARD, VERIFICATION_REGISTER, RELEASE_REGISTER, TENANT_ROLLOUT_REGISTER, PROMPT_REGISTER, APPROVED_CONTACT_REGISTER and source-of-truth records.

## Owner/tool
VIF Orchestrator owns context pack completeness. Codex Repo Inspector validates repo/branch facts. QA Gatekeeper checks evidence linkage. Security/RLS Reviewer checks contact-data and identity/security risk.

## Linked process
COP-02 Source-of-truth and context lock, SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, SOP-08 Security, tenant and data protection control, SOP-09 Configuration and version control.

## Linked gate
Context gate, baseline gate, prompt gate, job-card gate, evidence gate, identity/contact-data gate.

## PDCA
- PLAN: define required context fields, source basis and approved contact-data boundary before prompt/tool use.
- DO: build the context pack from stable artefacts, current evidence and approved contact records.
- CHECK: verify current source, branch, job card, gate, tenant/environment, approved project contacts and unresolved gaps.
- ACT: update APP_CONTEXT, job cards, evidence records, contact register, prompt controls and lessons learned when context becomes stale or incomplete.

## PASS/HOLD/BLOCKED rules
- PASS: context pack is current, bounded, source-linked, contact-controlled and complete enough for the requested gate.
- HOLD: non-critical context or contact approval is missing but no implementation/release/data action proceeds.
- BLOCKED: repo/branch/version/source truth, customer data, tenant, rollback, contact approval or approved job card is missing for risky work.

## Update trigger
New job card, app change, branch/version change, context drift, stale evidence, generated email/contact value, prompt failure, tool handoff, release/rollback, customer change, audit finding or lesson learned.
