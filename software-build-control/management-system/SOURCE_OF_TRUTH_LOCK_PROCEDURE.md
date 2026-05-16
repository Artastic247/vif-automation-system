# SOURCE_OF_TRUTH_LOCK_PROCEDURE.md

## Purpose
Ensure AI-assisted work uses the correct source of truth before planning, prompt creation, code review, repair, schema/RLS work, verification, release, rollout or automation.

## Scope
Applies to repo files, branches, commits, uploaded ZIPs, screenshots, logs, deployment evidence, Supabase evidence, tenant evidence, customer change records, job cards and management-system records.

## Inputs
Repo path, branch/version, current commit if known, uploaded files, app context, current job card, latest evidence pack, deployment evidence, Supabase evidence, tenant/environment records, previous decisions and unresolved gaps.

## Activities
1. Identify the requested work and affected app/process.
2. Confirm the current source of truth: live repo, branch, commit, file, ZIP, deployment, database, tenant or record.
3. Compare uploaded artefacts to live repo where both exist.
4. Mark any stale, superseded or reference-only material.
5. Confirm current gate and whether job-card approval is required.
6. Confirm missing evidence and stop conditions.
7. Lock the source basis before prompts, tool routing, build, verification or release.
8. Reject prompts that say “continue from previous chat” without a current context pack and source lock.

## Outputs
Source-of-truth lock decision, evidence gap list, current baseline, blocked stale sources and prompt readiness decision.

## Records
APP_CONTEXT, CURRENT_JOB_CARD, VERIFICATION_REGISTER, RELEASE_REGISTER, TENANT_ROLLOUT_REGISTER, PROMPT_REGISTER, source lock notes and baseline evidence.

## Owner/tool
Codex Repo Inspector validates repo/branch/file evidence. VIF Orchestrator approves the source-lock decision. QA Gatekeeper verifies source evidence before PASS.

## Linked process
COP-02 Source-of-truth and context lock, SOP-06 Prompt control and prompt quality, SOP-09 Configuration and version control, SOP-07 Evidence and record control.

## Linked gate
Baseline gate, context gate, prompt gate, configuration gate, evidence gate.

## PDCA
- PLAN: define required source evidence and comparison route.
- DO: inspect and lock source evidence before prompt/tool execution.
- CHECK: compare source against current repo/branch/version/evidence and detect stale inputs.
- ACT: update context pack, reject stale prompts, update job cards, lessons learned and source-lock rules.

## PASS/HOLD/BLOCKED rules
- PASS: source of truth, branch/version, current evidence, gate and job-card linkage are clear.
- HOLD: source evidence is partial but no build, schema/RLS, release or tenant work proceeds.
- BLOCKED: repo/branch/version/source truth is unknown, conflicting or stale for risky work.

## Update trigger
New uploaded file, repo change, branch/version change, prompt failure, stale context, ZIP/live mismatch, deployment mismatch, app repair, release, rollback, audit finding or lesson learned.
