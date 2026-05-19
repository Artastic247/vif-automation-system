# Codex PR Flow Standard

## Purpose

This standard defines how VIF uses Codex or another coding agent without turning the user into the manual conveyor belt between chat, code, tests, and fixes.

## Target flow

```text
Issue created
  ↓
Agent implements branch/PR
  ↓
GitHub Actions runs
  ↓
Agent reviews or responds to review findings
  ↓
Agent fixes CI/review findings
  ↓
Human release authority reviews final diff
  ↓
Merge
```

## Non-target flow

```text
Chat gives loose prompt
  ↓
User copies prompt into coding agent
  ↓
Agent changes unknown files
  ↓
User screenshots failure
  ↓
Chat writes another prompt
  ↓
User copies again
  ↓
Repeat
```

This non-target flow is manual labour disguised as automation and must be eliminated from controlled VIF builds.

## Work package format

Every agent task must include:

- Task title.
- Target repo.
- Problem statement.
- Context.
- Scope included.
- Scope excluded.
- Acceptance criteria.
- Verification commands.
- Risk controls.
- Expected deliverables.

## Example task card

```text
Task: Improve FMEA process-step view without changing import logic.

Context:
- The app manages PFD, PFMEA, Control Plan, Reverse FMEA and related actions.
- Primary view must remain process-step based.
- Secondary view must show completed document sets per PFD/PFMEA/CP/RFMEA/action set.
- Customers need flow diagrams viewable separately and downloadable.

Scope included:
- UI/navigation only.
- Step view improvements.
- Document-set view improvements.
- Flow diagram view/download affordance.

Scope excluded:
- Database schema changes.
- Import/alignment/matching logic changes.
- Authentication or permission changes.
- Large unrelated refactors.

Acceptance criteria:
1. Document-set detail page has clear back navigation.
2. Primary view shows the selected process step with linked PFMEA, CP, RFMEA questions and actions below it.
3. Secondary view lists completed document sets grouped by process flow, PFMEA, CP, RFMEA and actions.
4. Flow diagrams can be viewed separately and downloaded.
5. Existing tests/build must pass or failures must be classified.

Verification:
- npm run typecheck --if-present
- npm run lint --if-present
- npm test --if-present
- npm run build --if-present

Deliverables:
- Code changes.
- PR summary.
- Files changed.
- Checks run and results.
- Risks/assumptions.
```

## Agent PR requirements

The PR description must state:

- What changed.
- Why it changed.
- What did not change.
- Tests/checks run.
- Failures or blocked checks.
- Residual risks.
- Screenshots or evidence where useful.

## CI failure handling

When CI fails, the agent must:

1. Read the failing job/log.
2. Identify the failure category.
3. Fix only the cause of the failure.
4. Re-run the failed check or allow GitHub Actions to re-run.
5. Update the PR with the result.

## Review finding handling

When review findings exist, the agent must:

1. Address only the review finding unless the user approves scope expansion.
2. Avoid broad refactoring.
3. Add tests where the finding exposes missing coverage and the repo supports testing.
4. Re-state what was fixed.

## User role

The user must not be the patch cable between tools. The user should:

- Approve or reject scope.
- Review final diff and risk.
- Make release decisions.
- Escalate when requirements are unclear.

## VIF role

VIF must:

- Generate controlled task cards.
- Maintain the standard agent method.
- Maintain templates.
- Capture lessons learned.
- Improve the factory controls when repeat failures occur.

## Build repo role

The build repo must:

- Contain local `AGENTS.md`.
- Contain CI.
- Contain PR/issue templates.
- Contain product-specific rules.
- Preserve source-of-truth records.

## Hard stop conditions

Stop and escalate when:

- The repo lacks minimum controls and the task is not to install them.
- Secrets or credentials are exposed.
- The requested change touches permissions, auth, billing, data deletion, production data, or schema without explicit approval.
- CI cannot run and no classification can be made.
- The agent cannot identify the source files being changed.
