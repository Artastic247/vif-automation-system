# VIF Release Checklist

## Release identity

| Item | Detail |
| --- | --- |
| Repository | `Artastic247/vif-automation-system` |
| PR | [Insert PR link] |
| Issue / build order | [Insert issue link] |
| Release authority | [Insert name/role] |
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
| Sensitive-file guard | [PASS / FAIL / BLOCKED] | |
| Optional Node checks | [PASS / FAIL / NOT PRESENT / BLOCKED] | |
| Optional Python checks | [PASS / FAIL / NOT PRESENT / BLOCKED] | |
| PR review | [PASS / HOLD / REJECT] | |

## Risk review

- [ ] Residual risks are stated.
- [ ] Rollback method is stated.
- [ ] Any failed or blocked check is classified.
- [ ] Any controlled debt is accepted by the release authority.
- [ ] Any required lessons learned are captured or assigned.

## Release decision

Select one:

- [ ] PASS — merge/release authorised.
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
