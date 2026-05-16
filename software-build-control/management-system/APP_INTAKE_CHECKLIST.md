# APP_INTAKE_CHECKLIST.md

## Purpose
Ensure every app request starts with enough evidence before planning, coding, automation, repair, release, or customer rollout.

## Scope
Applies to all new builds, defects, enhancements, refactors, releases, recovery work, support requests, customer changes, and automation requests.

## Inputs
- User/customer request.
- Existing app context where available.
- Repo, branch/version, environment, tenant, logs, screenshots, files, and known constraints.

## Activities/checklist
Before any build or repair, answer:

- What app?
- What problem?
- Who are users?
- What process does it support?
- What is the current source of truth?
- Is this new build, defect, enhancement, refactor, release, or recovery?
- What repo?
- What branch/version?
- What environment?
- Is customer data involved?
- Is it single-tenant or multi-tenant?
- Is regulated/compliance logic involved?
- What must not change?
- What evidence is available?
- What is missing?
- What gate applies?

## Outputs/records
Completed intake checklist, evidence gap list, and intake gate decision: PASS / HOLD / BLOCKED.

## Owner/tool
VIF Orchestrator with user/product owner. Codex/GitHub validates repo/branch/version when repo evidence is required.

## Gate controlled
Intake and context-lock gate.

## PASS/HOLD/BLOCKED rules
- PASS: app, problem, user/process, source truth, repo/branch/environment, data/tenant risk, prohibited changes, evidence, and gate are clear.
- HOLD: non-critical evidence missing but no build/release/data action is requested.
- BLOCKED: source truth, repo/branch, data risk, tenant risk, or destructive scope is unclear.

## Update trigger
Every new request, app repair, customer change, incident, release, or automation request.
