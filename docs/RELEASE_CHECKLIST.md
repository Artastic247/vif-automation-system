# VIF Release Checklist

## Release identity

| Item | Detail |
| --- | --- |
| Repository | `Artastic247/vif-automation-system` |
| PR | [Insert PR link] |
| Issue / build order | [Insert issue link] |
| Reviewer | [Insert name/role] |
| Date | [Insert date] |

## Scope confirmation

- [ ] PR links to a scoped issue or approved build order.
- [ ] Change classification is stated.
- [ ] Scope included is visible.
- [ ] Scope excluded is visible.
- [ ] Changed files are listed.
- [ ] Protected-scope impact is declared.
- [ ] No unrelated files are changed.

## Gate evidence

| Check | Status | Notes |
| --- | --- | --- |
| Required-file gate | [PASS / FAIL / BLOCKED] | |
| Repository guard | [PASS / FAIL / BLOCKED] | |
| Optional Node checks | [PASS / FAIL / NOT PRESENT / BLOCKED] | |
| Optional Python checks | [PASS / FAIL / NOT PRESENT / BLOCKED] | |
| PR review | [PASS / HOLD / REJECT] | |

## Risk review

- [ ] Residual risks are stated.
- [ ] Rollback method is stated.
- [ ] Any failed or blocked check is classified.
- [ ] Any accepted open item is recorded with owner and follow-up.
- [ ] Any required lessons learned are captured or assigned.

## Decision

Select one:

- [ ] PASS — merge can proceed after owner review.
- [ ] HOLD — additional correction/evidence required.
- [ ] REJECT — change not acceptable.

Decision note:

```text
[Insert decision note]
```

## Post-merge check

- [ ] Main branch gate completed or failure classified.
- [ ] Follow-up issues created where needed.
- [ ] Lessons learned updated where needed.
