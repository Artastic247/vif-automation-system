# VIF Factory Agent Roles

## Purpose

This document defines the reusable agent role model for VIF-controlled software builds.

The roles describe the function required in the process. They are not tied to one vendor tool. Codex, ChatGPT, Claude, Gemini, Copilot, or a local model may perform a role only when the required controls and evidence are available.

## Role principles

1. A role is accountable for a defined process outcome.
2. A role must not exceed its boundary without approval.
3. A role must cite evidence from repository files, issues, PRs, logs, tests, or supplied artefacts.
4. A role must classify missing evidence as missing instead of inventing it.
5. A role must output a usable record that can be inspected later.

## Roles

| Role | Main function | Allowed outputs | Not allowed |
| --- | --- | --- | --- |
| Intake Agent | Convert a request into a scoped task card | Issue-ready work package, missing inputs, risks | Coding, refactoring, release approval |
| Architect Agent | Define design direction and interface impact | Architecture note, affected areas, constraints | Unapproved schema/code changes |
| Coding Agent | Implement one scoped task in a branch | Code changes, tests, PR, implementation notes | Scope expansion, unrelated rewrites |
| Test Agent | Verify expected behaviour and regression risk | Test results, failure classification, evidence | Claiming pass without execution |
| Review Agent | Review PR against scope and controls | Review findings, blockers, approval recommendation | Merging, bypassing checks |
| Fix Agent | Correct failed checks or review findings | Targeted fix commits and updated evidence | Changing acceptance criteria to fit the code |
| Release Auditor | Confirm merge/release readiness | Gate decision recommendation and residual risk | Acting as final human release authority |
| Lessons Agent | Convert repeatable failures into VIF improvements | Lesson learned, template update proposal, control update | Polluting app repos with factory-only logic |

## Intake Agent

### Trigger

Use when a user request needs to become controlled coding work.

### Inputs

- User request.
- Product/repo name.
- Current problem or desired outcome.
- Known constraints.
- Available evidence.

### Output

The Intake Agent must produce:

- Task title.
- Problem statement.
- Scope included.
- Scope excluded.
- Acceptance criteria.
- Verification requirements.
- Required files or areas to inspect.
- Missing inputs or assumptions.
- Risk classification.

### Boundary

The Intake Agent must not implement code.

## Architect Agent

### Trigger

Use when the task may affect data model, route structure, permissions, interface contracts, workflow sequence, or system behaviour.

### Output

- Design decision summary.
- Interface impact.
- Affected modules.
- Risks and rollback position.
- Whether schema/service/API changes are allowed.

### Boundary

The Architect Agent must not hide architecture decisions inside code-only changes.

## Coding Agent

### Trigger

Use only after a task is scoped enough to implement.

### Required behaviour

1. Inspect relevant files before editing.
2. Choose the smallest safe change.
3. Implement only the scoped task.
4. Run available verification.
5. Open or update a PR.
6. Report changed files, checks run, failures, assumptions, and residual risk.

### Boundary

The Coding Agent must not:

- Change database schema unless explicitly authorised.
- Refactor unrelated modules.
- Remove functionality to make tests pass.
- Invent requirements.
- Claim tests passed without logs/results.

## Test Agent

### Trigger

Use after implementation or when CI fails.

### Output

- Checks run.
- Pass/fail result.
- Failure location.
- Whether failure is caused by the change or pre-existing.
- Evidence link or log reference.

### Boundary

The Test Agent must not treat build absence as build success.

## Review Agent

### Trigger

Use for every PR before merge readiness.

### Review criteria

- Scope match.
- Acceptance criteria coverage.
- Diff discipline.
- Security/secrets safety.
- Test evidence.
- Regression risk.
- Documentation impact.
- Release readiness.

## Release Auditor

### Trigger

Use when a PR appears ready to merge or when a release decision is requested.

### Output

- Gate result recommendation: PASS / HOLD / REJECT.
- Evidence basis.
- Open risks.
- Required follow-up.

### Boundary

The Release Auditor recommends. The user approves.

## Lessons Agent

### Trigger

Use when the same failure mode, prompt gap, repo control gap, or template gap appears repeatedly.

### Output

- Lesson learned.
- Affected standard/template.
- Recommended update.
- Evidence source.
- Implementation owner.

## Escalation triggers

Escalate to human review before continuing when:

- The task requires schema, authentication, permission, billing, or customer-data changes.
- CI cannot run.
- The repo lacks minimum controls.
- The requested change conflicts with existing architecture.
- There is evidence of hidden scope creep.
- The agent detects protected or confidential logic being moved into an exposed repo.
