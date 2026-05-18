# AUTOMATION ACCELERATION PLAN

## Objective
Reach useful, evidence-backed automation quickly without violating protected-scope controls.

## Current baseline
- M1 execution cell is closed and accepted.
- M2 automation-control layer is HOLD pending clean rebuild.
- Gate is PASS_WITH_WARNINGS.

## Fast path to "some automation" (3-5 days)

### Phase A — Stabilise existing M1 route (Day 1)
1. Lock branch from current `main` for clean M2 rebuild path.
2. Re-run M1 route (`create-build-cards`, `run-task`, `verify-build`) and archive evidence.
3. Confirm protected-scope boundaries in closure notes.

Exit criteria:
- Reproducible M1 run with evidence packet linked.
- No mixed-scope changes.

### Phase B — Add smoke-screen CI gate (Day 1-2)
1. Add one smoke workflow that runs the app-build-line route on every PR touching `software-build-control/**`.
2. Mark smoke as required check for control-pack PRs.
3. Publish failing output into verification report.

Exit criteria:
- Smoke check required and green on one reference PR.
- Failures block merge.

### Phase C — Operator panel activation (Day 2-3)
1. Replace placeholder control links with real saved queries and Actions URL.
2. Populate auth/safeguard snapshot from current environment and branch protection settings.
3. Record "last known good run" fields with replay key, branch, PR, artifact link.

Exit criteria:
- Panel usable for daily triage without manual hunting.
- One operator walkthrough completed.

### Phase D — MLA assessment and permission decision (Day 3-4)
1. Run WI_022 maturity assessment for the automation-control scope.
2. Record evidence completeness and risk.
3. Issue PASS/HOLD/BLOCKED automation permission decision against matrix.

Exit criteria:
- MLA record complete.
- Explicit automation permission documented.

### Phase E — Limited automation release (Day 4-5)
1. Enable limited, non-destructive automation only (report routing / evidence collation).
2. Keep auto-fix/auto-merge/auto-release disabled.
3. Define rollback/disable route for each automation toggle.

Exit criteria:
- Automation actions are auditable and reversible.
- No protected system modifications.

## What "full automation" requires (not immediate)
- Mature MLA level with governance approval for broader orchestration.
- Demonstrated audit history and CAPA effectiveness.
- Proven rollback/disable controls for every automated action.

## Risks to speed
- Maturity overstatement.
- Expanding automation beyond allowed maturity permission.
- Missing evidence links in PRs.

## Recommended immediate next command route
1. Execute M1 validation route.
2. Implement smoke CI workflow.
3. Activate operator panel links.
4. Run MLA assessment packet.
