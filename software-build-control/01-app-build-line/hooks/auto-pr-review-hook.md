# AUTO-002 PR Review Hook

## Trigger point

- pull_request opened
- pull_request synchronized
- pull_request reopened
- pull_request ready_for_review

## Scope

AUTO-generated PRs only.

Branch pattern:

```text
auto-issue-
```

## Station

```text
AUTO-002 PR Review Station
```

## Input evidence

- PR title
- PR body
- head branch
- changed files
- workflow metadata

## Output evidence

- AUTO-002 Review Result comment
- PASS/HOLD recommendation
- changed-file assessment
- forbidden-path findings
- artifact upload

## PASS conditions

PASS only when:

- branch pattern is correct
- changed files are within approved AUTO documentation/control scope
- no forbidden paths are changed
- PR title contains issue traceability
- PR body contains workflow and human merge controls

## HOLD conditions

HOLD when:

- forbidden files changed
- workflow/runtime paths changed
- generated reports present
- JSON evidence outputs present
- issue traceability missing
- PR metadata incomplete

## Escalation route

HOLD findings escalate to:

- corrective action,
- workflow patch,
- skill update,
- operator review,
- Head of Factory decision if protected scope is involved.

## Authority boundary

AUTO-002 may recommend PASS or HOLD.

Human merge authority remains mandatory.
