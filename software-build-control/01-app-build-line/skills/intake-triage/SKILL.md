# SKILL: intake-triage

## Trigger
Use when a new app-build issue is opened/labeled or manually dispatched.

## Steps
1. Validate issue contains objective, route, target paths, forbidden paths, acceptance checks.
2. Validate route label parity with issue body.
3. Emit intake summary and route decision artifact.

## Outputs
- Intake decision comment.
- Routed mode (`dry-run` or `pr-write`).
