# Pull Request Evidence

## Linked task

Closes #[issue-number]

## Summary

- [Summarise what changed]
- [Summarise why it changed]

## Scope included

- [List what was changed]

## Scope excluded

- [List what was deliberately not changed]

## Files changed

- `[path]` — [reason]

## Verification performed

| Check | Result | Notes |
| --- | --- | --- |
| `npm run typecheck --if-present` | [PASS / FAIL / NOT PRESENT / BLOCKED] | [notes] |
| `npm run lint --if-present` | [PASS / FAIL / NOT PRESENT / BLOCKED] | [notes] |
| `npm test --if-present` | [PASS / FAIL / NOT PRESENT / BLOCKED] | [notes] |
| `npm run build --if-present` | [PASS / FAIL / NOT PRESENT / BLOCKED] | [notes] |

## Failure classification

If any check failed or was blocked, classify it:

- [ ] Caused by this change
- [ ] Pre-existing
- [ ] Environment/tooling blocked
- [ ] Unknown pending investigation
- [ ] Not applicable

## UI evidence

If UI changed, attach screenshots or screen notes:

- Before:
- After:

## Risk and rollback

### Residual risks

- [List known residual risks]

### Rollback

- Revert this PR if the change causes regression.
- [Add product-specific rollback steps if required]

## Release readiness

- [ ] Scope matches the issue/task.
- [ ] Acceptance criteria are addressed.
- [ ] Verification result is visible.
- [ ] Review findings are resolved or explicitly accepted.
- [ ] No unrelated refactor was included.
- [ ] No secrets or protected logic were exposed.
- [ ] Human release authority has reviewed or will review before merge.
