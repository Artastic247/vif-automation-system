# APP_ONBOARDING_CONTROL_PROCEDURE.md

## Purpose
Define the controlled onboarding route for any app entering the Software Build Control System.

## Scope
Applies to all governed apps before repair, enhancement, CI activation, rollout or automation.

## Owner/agent
VIF Orchestrator.

## Inputs
Repo, branch, commit, context pack, tenant/environment evidence, rollback evidence and onboarding job card.

## Activities/checklist
1. Lock source truth.
2. Verify repo/branch/commit.
3. Verify environment separation.
4. Verify tenant/data classification.
5. Verify rollback route.
6. Create onboarding evidence.
7. Run onboarding gate review.

## Outputs/records
Onboarding evidence, onboarding gate decision and onboarding register updates.

## Maturity level
M0-M1 draft onboarding only. M2 pilot onboarding. M3 controlled onboarding.

## Evidence required
Source-truth evidence, environment evidence, tenant evidence, rollback evidence and onboarding verification.

## Linked process
COP-01, COP-02, COP-08, COP-11.

## Linked agent/skill/procedure/module
VIF Orchestrator, QA Gatekeeper, Codex Repo Inspector and onboarding skills.

## Interface/control point
Interfaces with onboarding gates, tenant governance, release governance and CI governance.

## PASS/HOLD/BLOCKED rules
- PASS: onboarding evidence complete.
- HOLD: onboarding incomplete.
- BLOCKED: unknown repo, unknown tenant risk or missing rollback.

## PDCA
- PLAN: define onboarding evidence.
- DO: collect onboarding evidence.
- CHECK: verify onboarding.
- ACT: improve onboarding governance.

## Audit frequency
Per onboarding event.

## Automation allowance
No automation before onboarding PASS.

## Escalation
Escalate tenant risk, repo mismatch or missing rollback.

## Update trigger
New onboarding request, repo change, tenant change or lesson learned.
