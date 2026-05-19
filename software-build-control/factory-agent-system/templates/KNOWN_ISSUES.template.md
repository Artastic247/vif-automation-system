# Known Issues

## Purpose

This record prevents the agent from rediscovering the same blockers, claiming false regressions, or hiding pre-existing failures.

## Issue register

| ID | Date opened | Area | Issue | Evidence | Status | Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KI-001 | [date] | [area] | [issue] | [link/log] | Open | [owner] | [notes] |

## Status values

- Open
- Under investigation
- Controlled debt
- Fixed pending verification
- Closed

## Use rules

- If CI fails, check this record before classifying the failure.
- If a failure is pre-existing, cite the known issue ID in the PR.
- If a new persistent blocker is found, add it here or raise a task to add it.
- Do not use this record to excuse failures introduced by the current PR.
