# CONTEXT_PACK_STANDARD.md

## Purpose
Define the standard context pack required before AI-assisted app development, repair, review, release, rollout, automation or management-system work proceeds.

## Scope
Applies to all app projects and control-system work where context loss, truncation, stale evidence, wrong repo/branch or unsupported assumptions could cause rework or unsafe changes.

## Inputs
App request, current app context, repo, branch/version, current commit if known, current job card, current gate, source-of-truth artefacts, latest evidence pack, known defects, exclusions, tenant/environment context, rollback context, latest decision, unresolved gaps and archive/reference links.

## Activities
Create or refresh a context pack before any prompt that could affect planning, code, schema/RLS, verification, validation, release, rollout, CI, n8n or customer data.

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
| Latest decision | Most recent PASS/HOLD/BLOCKED decision |
| Unresolved gaps | Missing evidence, risks and blocked decisions |
| No-truncation rule | Context must be split into stable artefacts, not one giant prompt |
| Archive/reference handling | Old drafts are references only unless reconfirmed as source of truth |

## Outputs
Current context pack, evidence gap list, source-of-truth lock decision and prompt readiness decision.

## Records
APP_CONTEXT, CURRENT_JOB_CARD, VERIFICATION_REGISTER, RELEASE_REGISTER, TENANT_ROLLOUT_REGISTER, PROMPT_REGISTER and source-of-truth records.

## Owner/tool
VIF Orchestrator owns context pack completeness. Codex Repo Inspector validates repo/branch facts. QA Gatekeeper checks evidence linkage.

## Linked process
COP-02 Source-of-truth and context lock, SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, SOP-09 Configuration and version control.

## Linked gate
Context gate, baseline gate, prompt gate, job-card gate, evidence gate.

## PDCA
- PLAN: define required context fields and source basis before prompt/tool use.
- DO: build the context pack from stable artefacts and current evidence.
- CHECK: verify current source, branch, job card, gate, tenant/environment and unresolved gaps.
- ACT: update APP_CONTEXT, job cards, evidence records, prompt controls and lessons learned when context becomes stale or incomplete.

## PASS/HOLD/BLOCKED rules
- PASS: context pack is current, bounded, source-linked and complete enough for the requested gate.
- HOLD: non-critical context is missing but no implementation/release/data action proceeds.
- BLOCKED: repo/branch/version/source truth, customer data, tenant, rollback or approved job card is missing for risky work.

## Update trigger
New job card, app change, branch/version change, context drift, stale evidence, prompt failure, tool handoff, release/rollback, customer change, audit finding or lesson learned.
