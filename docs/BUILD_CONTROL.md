# VIF Repository Build Control

## Purpose

This document controls how changes to the VIF Automation System repository are proposed, verified, reviewed, and released.

The repository is a factory-control system. A weak change here can affect future app builds, agent behaviour, release gates, and evidence expectations. Therefore, changes must move through a controlled PR gate.

## Repository identity

| Item | Detail |
| --- | --- |
| Repository | `Artastic247/vif-automation-system` |
| Default branch | `main` |
| Controlled branch pattern | `install-*`, `agent/*`, `fix/*`, `docs/*`, `factory/*` |
| Release authority | Human repository owner |
| Agent role | Execution/support only; no merge authority |

## Control-plane model

```text
Issue / approved build order
  ↓
Branch
  ↓
Change implementation
  ↓
VIF Factory Gate workflow
  ↓
Pull request review
  ↓
Human release decision
  ↓
Merge
```

## Required controls

| Control | Required state |
| --- | --- |
| `AGENTS.md` | Present at repository root |
| Pull request template | Present under `.github/PULL_REQUEST_TEMPLATE.md` |
| Agent task issue template | Present under `.github/ISSUE_TEMPLATE/agent-task.yml` |
| Factory gate workflow | Present under `.github/workflows/vif-factory-gate.yml` |
| Factory agent system | Present under `software-build-control/factory-agent-system/` |
| Release checklist | Present under `docs/RELEASE_CHECKLIST.md` |
| Known issues register | Present under `docs/KNOWN_ISSUES.md` |
| Branch protection guidance | Present under `docs/BRANCH_PROTECTION.md` |

## Scope rules

Every change must state whether it is:

- Factory method update.
- Template update.
- Gate/control update.
- Documentation-only update.
- Verification/control evidence update.
- Product-specific lesson converted into reusable factory rule.

## Protected scope

The following must not be changed unless explicitly scoped and reviewed:

- App repositories.
- Supabase configuration.
- RLS policies.
- Edge functions.
- Deployment configuration.
- n8n workflows.
- Customer data.
- DOS FMEA repair content.
- Sensitive access material or private strategic logic.

## Verification rules

The VIF Factory Gate workflow must run on pull requests and on pushes to `main`.

Minimum required checks:

- Required-file gate.
- Repository guard.
- Optional Node checks when `package.json` exists.
- Optional Python checks when Python tests or dependency files exist.

If checks are unavailable or blocked, the PR must classify the result. A blocked check is a HOLD condition until accepted by the release authority.

## Merge rules

A pull request may be merged only when:

- Scope is clear.
- Changed files are listed.
- The VIF Factory Gate result is visible.
- Failures, if any, are classified.
- Review findings are resolved or accepted.
- Residual risk and rollback are stated.
- The human release authority approves.

## Agent authority

Agents may:

- Create branches.
- Create commits.
- Open PRs.
- Update PRs in response to review or CI findings.
- Report evidence and gate state.

Agents may not:

- Merge PRs.
- Approve their own PRs.
- Bypass CI.
- Remove gate requirements to make a PR pass.
- Expose protected strategy or confidential data.

## Controlled debt

A failing or blocked check may only be accepted as controlled debt when the PR records:

- The failure.
- The classification.
- The reason it is acceptable.
- The owner.
- The follow-up action.

## Lessons learned

If a PR reveals a repeatable factory failure or improvement, a lessons-learned item must be created or referenced before release.
