# TOOLCHAIN_INTERFACE_CONTROL

## Purpose

This document defines the process interfaces between the VIF management system, factory controls, AI tools, GitHub control plane and inspection stations.

The purpose is to ensure:

- interface authority is clear,
- inputs and outputs are controlled,
- fallback routes exist,
- tools do not operate outside approved scope.

## Core interface principle

Tools are execution stations.

They are not the management system.

The management system governs how tools may be used.

## Interface map

```text
Management system
→ Factory control layer
→ GitHub control plane
→ AI execution/review stations
→ CI inspection stations
→ Product-line outputs
```

## Primary interfaces

### 1. Human operator ↔ GitHub control plane

Inputs:

- approved work,
- audit findings,
- corrective actions,
- release decisions.

Outputs:

- issue creation,
- PR approval/rejection,
- merge decisions,
- escalation decisions.

Authority:

- final release authority.

Fallback:

- manual GitHub UI control.

## 2. GitHub control plane ↔ Codex

Inputs to Codex:

- issue/task scope,
- approved branch scope,
- repository state,
- readiness conditions.

Outputs from Codex:

- proposed code/documentation changes,
- PRs,
- dry-run outputs,
- status reports.

Constraints:

- readiness checks mandatory,
- stale workspaces prohibited,
- generated-artifact recursion prohibited,
- broad conflict recovery prohibited.

Fallback:

- operator-controlled branch,
- GitHub-only correction,
- dry-run mode.

## 3. GitHub control plane ↔ ChatGPT

Inputs:

- audit evidence,
- governance questions,
- planning inputs,
- process issues.

Outputs:

- audit analysis,
- corrective-action recommendations,
- governance controls,
- process recommendations.

Authority:

- planning/review only.

Fallback:

- direct issue review.

## 4. GitHub control plane ↔ Claude/other review stations

Inputs:

- scoped review request,
- repository context,
- targeted problem statement.

Outputs:

- review feedback,
- reasoning support,
- optional implementation guidance.

Constraints:

- authority boundaries must remain defined.

Fallback:

- alternate review route.

## 5. GitHub Actions ↔ Factory inspection layer

Inputs:

- workflows,
- repository state,
- CI triggers.

Outputs:

- smoke results,
- artifacts,
- validation evidence,
- gate status.

Constraints:

- generated evidence should remain artifacts unless explicitly approved.

Fallback:

- manual validation.

## Interface authority matrix

| Interface | Allowed authority | Prohibited authority |
|---|---|---|
| Human operator | Release, escalation, risk acceptance | Hidden manual orchestration as permanent control method |
| Codex | Controlled dry-run support and narrow PRs | Autonomous merge, broad recovery |
| ChatGPT | Planning, audit, governance support | Direct uncontrolled repo mutation |
| Claude | Review/support | Uncontrolled release authority |
| GitHub Actions | CI inspection/evidence | Autonomous release |

## Interface failure conditions

The process must STOP when:

- tool readiness unconfirmed,
- provider access blocked,
- stale branch detected,
- broad conflicts detected,
- generated-artifact recursion detected,
- authority unclear,
- fallback route unavailable.

## Interface evidence requirements

Interfaces should produce evidence such as:

- issues,
- PRs,
- CI artifacts,
- audit reports,
- corrective actions,
- readiness confirmations,
- branch/merge records.

## Current approved state

```text
Controlled semi-automation / dry-run pilot
```

No interface currently has autonomous release authority.

## Conclusion

The VIF factory must operate through controlled interfaces with defined authority, readiness, constraints and fallback routes.

If tools begin driving the process outside management-system controls, audit and corrective action must be triggered.
