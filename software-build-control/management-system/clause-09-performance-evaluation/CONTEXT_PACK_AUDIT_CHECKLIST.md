# CONTEXT_PACK_AUDIT_CHECKLIST

## Purpose
Audit whether the current context pack prevents truncation, stale-source use and source-of-truth drift.

## Scope
All app, repo, project, job-card, audit and automation context packs.

## Owner/agent
Context Pack Auditor and Context Management Specialist.

## Inputs
APP_CONTEXT, current job card, repo/branch/commit, current gate, source artefacts, known defects, exclusions, tenant/environment context and rollback context.

## Activities/method
Check app/project identity, repo, branch/commit, current job card, current gate, source-of-truth artefacts, known defects, current exclusions, tenant/environment context, rollback context, unresolved gaps, latest decision, stale-context risk, no-truncation control and whether old drafts are demoted from active truth.

## Outputs/records
Context-pack audit result, missing-context finding, source-lock action.

## Audit criteria
Active context must be current, bounded, traceable and not mixed with stale drafts. Old chats/drafts cannot be treated as truth without revalidation.

## Evidence required
Current context pack, repo/branch proof, decision log, gap list, source hierarchy.

## MLA / maturity dependency
M2 requires controlled sandbox context; M3 requires released context discipline; M4/M5 require audit trend evidence.

## Linked process
Context management and source-of-truth lock.

## Linked gate
Context lock gate.

## PASS/HOLD/BLOCKED rules
PASS when current context is complete and traceable. HOLD when gaps are identified. BLOCKED when source/branch/tenant context is unknown for risky work.

## Escalation
Escalate stale context used for implementation, false repo/branch, or customer-data uncertainty.

## Management-review input
Context drift and truncation trends feed management review.

## Update trigger
New job card, branch change, evidence update, defect discovery, release decision.
