# CONFLICT_RECOVERY_RULES

## Purpose

This document defines mandatory conflict recovery behaviour for the VIF app-build-line.

The purpose is to stop recursive PR conflict loops, stale-branch recovery attempts, mixed-scope repair merges, and unsafe generated-output conflict handling.

This document was introduced under corrective action CA-001.

## Core rule

Broad conflict repair is prohibited.

If a branch enters mixed-scope or generated-output conflict recursion:

```text
close and rebuild
```

Do not continue stacking fixes onto contaminated branches.

## Definitions

### Small conflict

A conflict is considered small when:

- one file only is affected,
- the intended final content is obvious,
- no protected scope is involved,
- no generated evidence recursion exists.

### Broad conflict

A conflict is considered broad when:

- multiple unrelated files conflict,
- generated evidence files conflict,
- multiple milestones overlap,
- stale branch reuse is involved,
- reports/snapshots/gate outputs are repeatedly regenerated,
- branch scope cannot be confidently isolated.

## Small conflict handling

Allowed:

- resolve manually,
- remove conflict markers,
- verify final intended content,
- confirm PR scope remains valid,
- continue review.

## Broad conflict handling

Mandatory response:

1. stop,
2. do not merge,
3. do not manually repair broad conflict chains,
4. close overlapping PRs,
5. preserve current `main` as source of truth,
6. create fresh branch from current `main`,
7. reapply only approved narrow delta,
8. regenerate evidence after merge if required.

## Generated artifact conflicts

Generated evidence files must not drive branch recovery.

If generated outputs conflict:

- treat the outputs as disposable,
- preserve source/configuration logic,
- regenerate evidence later from accepted source.

Preferred recovery:

```text
keep source logic
discard regenerated evidence outputs
regenerate after merge
```

## Stale branch rule

A branch is stale when:

- it predates accepted `main`,
- it cannot cleanly update,
- it carries unrelated prior work,
- its changed-file scope exceeds approved intent.

Stale branches must not be reused.

## Mixed-scope rule

Mixed-scope PRs must be rejected.

Examples:

- M1 + M2 mixed,
- runtime + generated reports mixed,
- governance + deployment mixed,
- smoke outputs + unrelated scripts mixed.

## Recovery authority

Codex may identify conflicts and report recovery recommendations.

Codex must not autonomously decide broad conflict recovery merges.

Human release authority remains required.

## Recovery reporting

Every recovery assessment must report:

- branch name,
- source baseline,
- changed-file count,
- generated-output presence,
- protected-scope status,
- recommended action,
- whether close-and-rebuild is required.

## Prevention of recurrence

To prevent recurrence:

- generated outputs should become CI artifacts,
- PR changed-file preflight is mandatory,
- one issue = one branch = one PR remains mandatory,
- stale branch reuse is prohibited,
- branch scope must remain narrow.

## Current operating recovery rule

```text
Small conflict: repair carefully.
Broad conflict: close and rebuild.
```
