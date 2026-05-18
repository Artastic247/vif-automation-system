# OPERATOR_PANEL

## Current mode
Linked dry-run (target state: evidence-backed limited automation).

## Control links
- Open app-build issues: saved GitHub issue query for route-labelled app-build items.
- In-flight app-build PRs: saved GitHub PR query filtered to `software-build-control/**` changes.
- Failing required checks: saved GitHub checks query for failed required statuses.
- Workflow runs: GitHub Actions runs URL for control-pack workflows.

## Queue and triage
- Confirm issue form completeness.
- Confirm route label is present.
- Confirm `CODEX_TASK_HANDOFF.md` fields are complete.
- Confirm evidence links exist before merge.

## Required attention
- PRs with mixed-scope changed files.
- PRs blocked by stale base or merge conflict.
- PRs missing required evidence links.
- PRs that attempt protected-scope modification.

## Corrective-action control note
Before approving app-build work, confirm that generated evidence follows the generated-artifact policy, toolchain readiness is checked before assigning Codex or another build station, and human release authority remains active for merge decisions.

## Auth and safeguards snapshot
- `OPENAI_API_KEY` configured: [set at run review]
- GitHub App installed for automation: [set at run review]
- Branch protection active on `main`: [set at run review]
- Required checks configured: [set at run review]

## Last known good run
- Replay key: [required]
- Branch: [required]
- PR: [required]
- Evidence artifact: [required]

## Operator release decision
- Gate result: PASS / HOLD / BLOCKED
- Decision owner:
- Decision timestamp:
- Notes:
