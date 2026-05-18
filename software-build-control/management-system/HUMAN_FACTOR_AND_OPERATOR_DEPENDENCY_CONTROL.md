# HUMAN_FACTOR_AND_OPERATOR_DEPENDENCY_CONTROL

## Purpose

This document controls the human-factor dependency within the VIF app-build-line.

It closes CA-004 from AUD-001.

## Problem addressed

The audit identified that the operator became the hidden automation layer by:

- relaying prompts manually,
- reconstructing context,
- repairing stale branches,
- interpreting conflicts,
- manually coordinating tools,
- compensating for missing readiness checks.

This reduced repeatability and increased process risk.

## Core rule

The operator must not become the uncontrolled integration layer.

If the process relies on memory, hidden manual coordination or repeated manual reconstruction, the process is not sufficiently controlled.

## Operator role

The operator remains responsible for:

- release authority,
- escalation decisions,
- final merge approval,
- risk acceptance,
- corrective action initiation,
- audit review,
- management review input.

## Operator must not routinely perform

The following activities should reduce over time through controlled automation:

- repeated prompt relaying,
- repeated manual context reconstruction,
- repeated stale-branch repair,
- repeated conflict interpretation,
- manual evidence reconciliation,
- manual route tracking.

## Human-factor risks

| Risk | Description | Current state |
|---|---|---|
| Memory dependency | Process relies on human remembering context | Present |
| Manual relay dependency | Human copies outputs between tools | Present |
| Hidden orchestration | Human acts as integration engine | Present |
| Conflict fatigue | Human repeatedly repairs AI-generated conflicts | Reduced after CA-001 |
| Capability assumption | Human assumes tool can perform unsupported action | Present but improving |
| Release overload | Human reviews too many mixed-scope changes | Reduced |

## Required controls

### 1. Structured issue routing

All significant work should originate from:

- issue,
- audit,
- corrective action,
- approved build card,
- or controlled task packet.

### 2. Readiness checks

Tools must pass readiness checks before assignment.

### 3. Narrow-scope PRs

PRs must remain:

- small,
- traceable,
- single-purpose,
- evidence-backed.

### 4. Explicit stop conditions

Automation must stop when:

- workspace state unconfirmed,
- origin/main unavailable,
- generated-artifact recursion detected,
- branch scope drifts,
- provider limitations block execution,
- readiness cannot be confirmed.

### 5. Escalation routes

Escalate to operator when:

- broad conflict occurs,
- release decision required,
- capability uncertain,
- provider/tool access fails,
- corrective action required.

## Automation maturity and human dependency

| State | Human dependency |
|---|---|
| Manual | Human performs almost all orchestration |
| Controlled semi-automation | Human supervises controlled automation |
| Dry-run automation | Human reviews artifacts and release decisions |
| Controlled PR automation | Human approves merges and escalation |
| Full autonomy | Not approved |

## Current approved state

```text
Controlled semi-automation / dry-run pilot
```

Human release authority remains mandatory.

## Reduction strategy

Human dependency should reduce through:

- issue-driven routing,
- controlled handoff packets,
- readiness checks,
- interface controls,
- CI evidence,
- operator dashboards,
- automation maturity gates.

## Conclusion

The operator remains essential to governance and release control.

However, hidden manual integration activity must reduce over time through controlled process and interface maturity rather than through uncontrolled AI autonomy.
