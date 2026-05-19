# AGENTS.md

## Product context

[Describe the product/app here. State what the system does and the main process flow it supports.]

## Source of truth

- Repository files are the source of truth for implementation.
- GitHub issues define scoped work packages.
- Pull requests are the source of truth for proposed changes.
- CI logs are the source of truth for verification results.
- Do not invent requirements that are not in the issue, repo, or supplied artefacts.

## Working rules

- Treat this repository as a controlled build repo.
- Prefer small, reviewable changes.
- Work on one scoped task per branch/PR.
- Inspect relevant files before editing.
- Do not refactor unrelated files.
- Do not remove existing functionality to make tests pass.
- Do not change database schema unless the task explicitly allows it.
- Do not change authentication, permissions, billing, or production-data behaviour unless explicitly authorised.
- Do not expose secrets, credentials, protected strategic logic, or confidential customer data.
- If information is missing, state the assumption and keep the change minimal.

## Required workflow

1. Read the issue/task and this `AGENTS.md`.
2. Identify the relevant files and current behaviour.
3. Confirm the smallest safe implementation path.
4. Make the scoped change.
5. Run available verification commands.
6. Open or update a PR.
7. Report:
   - Files changed.
   - What changed.
   - What did not change.
   - Checks run.
   - Failures or blocked checks.
   - Assumptions.
   - Residual risks.

## Verification commands

Run commands that exist in this repo:

```bash
npm run typecheck --if-present
npm run lint --if-present
npm test --if-present
npm run build --if-present
```

If a command does not exist, state that it is not present. If a command fails, classify the failure as caused by the change, pre-existing, environment/tooling blocked, or unknown.

## Product-specific hard rules

[Add rules for this app. Examples:]

- Preserve the core process flow.
- Preserve traceability between process step, document set, evidence, and action.
- UI changes must not alter import, matching, alignment, or release logic unless explicitly scoped.
- Service/data/permission logic must not be bypassed by frontend-only controls.

## Pull request requirements

Every PR must include:

- Task/issue reference.
- Summary of changes.
- Scope exclusions.
- Verification results.
- Screenshots where UI changed.
- Residual risks or follow-up work.

## Stop and escalate

Stop and ask for human review before continuing when:

- The task requires schema/auth/permission/billing/customer-data changes.
- The requested change conflicts with existing architecture.
- CI cannot run and the failure cannot be classified.
- The task requires protected or confidential logic to be exposed.
- The implementation requires broad refactoring beyond the approved scope.
