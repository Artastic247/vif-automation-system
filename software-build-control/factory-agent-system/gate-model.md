# VIF Agent Coding Gate Model

## Purpose

This gate model controls AI-assisted coding work from request to release. It prevents uncontrolled prompt loops, hidden scope expansion, unsupported pass claims, and merge decisions without evidence.

## Gate summary

| Gate | Name | Purpose | Minimum output |
| --- | --- | --- | --- |
| G0 | Intake Gate | Confirm the request is clear enough to scope | Task card or missing-input list |
| G1 | Scope Lock Gate | Freeze what is included and excluded | Acceptance criteria and exclusions |
| G2 | Build-Ready Gate | Confirm repo controls exist | Local `AGENTS.md`, CI, PR/issue template check |
| G3 | Implementation Gate | Execute only the scoped change | Branch/commit/PR |
| G4 | Verification Gate | Prove checks were run | CI/test/build/lint/typecheck result |
| G5 | Review Gate | Check scope fit and diff discipline | PR review result |
| G6 | Fix Gate | Resolve failures/findings without scope drift | Targeted fix commits and updated evidence |
| G7 | Release Gate | Confirm merge readiness | PASS/HOLD/REJECT recommendation |
| G8 | Lessons Gate | Feed reusable learning back to VIF | Lesson/update proposal |

## G0 — Intake Gate

### Entry condition

A user request, bug, feature, issue, or improvement has been raised.

### Required checks

- Is the target repo/product known?
- Is the desired outcome stated?
- Is the problem backed by evidence or clearly marked as a request?
- Are constraints known?
- Is there enough information to create a scoped task?

### Exit output

- Issue-ready task card; or
- Missing-input list.

## G1 — Scope Lock Gate

### Required checks

- Scope included.
- Scope excluded.
- Acceptance criteria.
- Verification requirements.
- Explicit non-goals.
- Approval required for schema, auth, permission, billing, or data-model changes.

### Exit rule

No coding may begin until scope is locked or assumptions are clearly stated inside the task.

## G2 — Build-Ready Gate

### Required checks

The build repo must contain or receive:

- `AGENTS.md`.
- CI workflow.
- PR template.
- Agent task issue template.
- Build control notes.
- Known issues record where applicable.

### Exit rule

If these controls are absent, the first controlled task is to install the repo controls before feature work.

## G3 — Implementation Gate

### Required checks

- Agent works on a branch, not directly on main.
- Agent inspects relevant files before editing.
- Change is limited to the task.
- No protected strategic logic is copied into exposed code or public docs.
- No unrelated refactoring.

### Exit output

- Branch or PR.
- Changed file list.
- Implementation note.

## G4 — Verification Gate

### Required checks

Run available verification commands, normally:

- Dependency install if needed.
- Typecheck if present.
- Lint if present.
- Tests if present.
- Build if present.

### Required classification

For each failure, classify as:

- Caused by this change.
- Pre-existing.
- Environment/tooling blocked.
- Unknown pending investigation.

### Exit rule

No PASS is allowed without evidence. If checks cannot run, the result is HOLD, not PASS.

## G5 — Review Gate

### Required checks

- Acceptance criteria met.
- Diff is limited and understandable.
- No schema/API/auth/security drift.
- UI changes match process flow where applicable.
- Tests and CI results are visible.
- Documentation impact considered.

## G6 — Fix Gate

### Required checks

- Fix only the identified failure or review finding.
- Do not broaden scope.
- Re-run relevant checks.
- Update PR notes with what was fixed.

## G7 — Release Gate

### Release states

| State | Meaning |
| --- | --- |
| PASS | Evidence supports merge/release |
| HOLD | More evidence or correction required |
| REJECT | Change conflicts with requirements, architecture, or safety controls |

### Minimum release evidence

- Scope locked.
- PR reviewed.
- CI status known.
- Failures classified.
- Residual risks stated.
- Human release authority confirms merge/release.

## G8 — Lessons Gate

### Trigger examples

- Repeated prompt failure.
- Repeated CI failure pattern.
- Agent drifts into unrelated files.
- Missing repo control caused rework.
- Better acceptance criterion discovered.

### Output

- Lesson learned.
- VIF file/template to update.
- Evidence source.
- Owner.
- Follow-up action.

## Gate discipline rule

A gate may move to PASS only when the required evidence exists. Discussion, confidence, or model reasoning is not evidence by itself.
