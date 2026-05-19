## Linked issue

Closes #

## Change classification

Select one primary class:

- [ ] Factory method update
- [ ] Template update
- [ ] Gate/control update
- [ ] Documentation-only update
- [ ] Verification/control evidence update
- [ ] Product-specific lesson converted into reusable factory rule

## Summary

-

## Scope included

-

## Scope excluded

-

## Changed files

- [ ] List every changed file
- [ ] Confirm all changes are within allowed scope

## Route and handoff

- Route: `codex` / `claude-review` / `manual`
- Handoff ID:
- Replay key:

## Gate status

- [ ] `vif/intake` passed
- [ ] `vif/scope-lock` passed
- [ ] `vif/diff-scope` passed
- [ ] `vif/ci` passed or failure classified
- [ ] `vif/review` ready
- [ ] `vif/operator-approval` ready

## Validation

| Check | Result | Evidence/notes |
| --- | --- | --- |
| VIF required-file gate | [PASS / FAIL / BLOCKED] | |
| Sensitive-file guard | [PASS / FAIL / BLOCKED] | |
| Optional Node checks | [PASS / FAIL / NOT PRESENT / BLOCKED] | |
| Optional Python checks | [PASS / FAIL / NOT PRESENT / BLOCKED] | |

Commands run:

```text
[Insert commands or CI run link]
```

## Failure classification

If any check failed or was blocked, classify it:

- [ ] Caused by this change
- [ ] Pre-existing
- [ ] Environment/tooling blocked
- [ ] Unknown pending investigation
- [ ] Not applicable

## Out-of-scope confirmation

- [ ] No mixed-scope changes
- [ ] No workflow/auth/secrets changes unless explicitly authorized
- [ ] No sensitive data added to prompts, logs, or artifacts
- [ ] No app repository, Supabase, RLS, edge function, deployment, n8n, customer data, or DOS FMEA repair changes are included unless explicitly scoped
- [ ] No protected strategic logic or private reasoning patterns are exposed

## Risk and rollback

- Risk level:
- Residual risks:
- Rollback method:

## Release decision record

- [ ] PASS — ready for human merge approval
- [ ] HOLD — correction/evidence required
- [ ] REJECT — not acceptable in current form

Decision note:

```text
[Insert release note]
```

## Lessons learned

- [ ] No reusable lesson identified
- [ ] Reusable lesson identified and captured or assigned

Lesson reference:

```text
[Insert lesson ID / follow-up issue]
```
