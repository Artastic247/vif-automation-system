# Release Checklist

## Release identity

| Item | Detail |
| --- | --- |
| Product/repo | [Insert repo] |
| Issue/PR | [Insert links] |
| Release authority | [Insert name/role] |
| Date | [Insert date] |

## Scope confirmation

- [ ] The PR links to a scoped issue/task.
- [ ] Acceptance criteria are visible.
- [ ] Scope exclusions are visible.
- [ ] No unapproved schema/auth/permission/billing/customer-data change is included.
- [ ] No unrelated refactor is included.

## Verification evidence

| Evidence | Status | Notes |
| --- | --- | --- |
| Typecheck | [PASS / FAIL / N/A / BLOCKED] | [notes] |
| Lint | [PASS / FAIL / N/A / BLOCKED] | [notes] |
| Tests | [PASS / FAIL / N/A / BLOCKED] | [notes] |
| Build | [PASS / FAIL / N/A / BLOCKED] | [notes] |
| UI evidence | [PASS / FAIL / N/A] | [notes] |
| Review findings | [RESOLVED / OPEN / N/A] | [notes] |

## Risk review

- [ ] Residual risks are stated.
- [ ] Rollback path is known.
- [ ] Known failures are classified.
- [ ] Controlled debt, if any, is explicitly accepted.

## Release decision

Select one:

- [ ] PASS — merge/release authorised.
- [ ] HOLD — additional correction/evidence required.
- [ ] REJECT — change not acceptable.

Decision note:

```text
[Write decision note here]
```

## Lessons learned trigger

- [ ] No reusable lesson identified.
- [ ] Reusable lesson identified and captured for VIF feedback.

Lesson reference:

```text
[Insert lesson ID or follow-up task]
```
