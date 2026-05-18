# GENERATED_ARTIFACT_POLICY

## Purpose

This policy separates mergeable source/configuration assets from generated evidence artifacts within the VIF app-build-line.

The purpose is to prevent conflict recursion, mixed-scope pull requests, stale generated outputs, and repeated regeneration of shared-state evidence files.

This policy was introduced under corrective action CA-001.

## Problem addressed

The following failure pattern was observed:

- multiple Codex-generated PRs regenerated overlapping evidence files,
- smoke outputs and validation reports became merge payloads,
- operator snapshots and MLA reports were repeatedly regenerated,
- PRs conflicted repeatedly,
- agents attempted broad conflict recovery,
- branch scope drift increased,
- operator confidence reduced.

The root cause was that generated evidence outputs were treated as source-controlled merge content.

## Core rule

Generated evidence is not source logic.

Generated evidence must normally be treated as:

- CI artifacts,
- immutable evidence packs,
- release attachments,
- timestamped snapshots,
- inspection outputs.

Generated evidence must not normally become an active merge payload.

## Mergeable assets

The following are considered mergeable engineering/control assets:

- workflows,
- scripts,
- templates,
- policies,
- routing logic,
- handoff contracts,
- issue templates,
- pull request templates,
- operator panel structure,
- validation logic,
- governance documents.

These may be reviewed, versioned, and merged through controlled PRs.

## Generated artifacts

The following are considered generated evidence artifacts:

- `reports/*.json`
- `reports/*.md`
- gate decisions,
- smoke outputs,
- validation outputs,
- generated snapshots,
- replay evidence,
- MLA outputs,
- generated audit evidence,
- generated route outputs.

These are volatile shared-state outputs.

## Default handling rule

Generated evidence artifacts should:

- be uploaded as GitHub Actions artifacts,
- be attached to releases,
- be archived externally,
- be timestamped,
- remain reproducible from source logic.

Generated artifacts should not normally be committed directly to `main`.

## Exception rule

Generated evidence may only become a merge payload when:

1. the task explicitly authorises it,
2. the generated evidence itself is the controlled deliverable,
3. the PR scope explicitly lists the generated files,
4. the operator approves the evidence strategy,
5. the PR remains narrow and conflict-safe.

## Agent preflight rule

Before PR creation, agents must:

1. inspect the changed-file list,
2. compare it to the approved task scope,
3. identify generated evidence outputs,
4. stop and report unexpected generated outputs.

## Conflict handling rule

If generated evidence artifacts cause broad conflicts:

- do not manually repair broad conflicts,
- do not merge mixed-scope recovery PRs,
- close overlapping PRs,
- rebuild from current `main`,
- regenerate evidence after merge if required.

## CI artifact strategy

Preferred strategy:

```text
source logic committed
→ CI executes
→ evidence generated
→ evidence uploaded as artifact
→ gate reviewed
→ merge approved/rejected
```

Preferred strategy must avoid repeated committing of regenerated outputs.

## Operator responsibility

Human merge authority remains responsible for:

- reviewing generated evidence scope,
- approving exceptions,
- verifying gate decisions,
- confirming artifact retention approach,
- rejecting mixed-scope generated-output PRs.

## Current operating state

Current app-build-line state:

```text
Controlled semi-automation
```

The line is not yet fully autonomous.

Generated evidence governance is mandatory before wider automation is enabled.
