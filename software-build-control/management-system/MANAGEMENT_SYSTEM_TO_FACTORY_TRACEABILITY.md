# MANAGEMENT_SYSTEM_TO_FACTORY_TRACEABILITY

## Purpose

This document defines how VIF management-system requirements flow into the factory control layer, automation layer, toolchain interfaces and product-line execution.

It closes CA-003 from AUD-001.

## Core hierarchy

```text
Management system
→ factory control
→ automation control
→ tool execution
→ product-line output
```

The reverse is not permitted.

## Traceability rule

Factory expansion may only proceed when the related management-system controls are defined, accepted and traceable.

If management-system controls are missing or immature, the factory build must remain on HOLD or controlled dry-run.

## Traceability matrix

| Management-system control | Factory control required | Evidence | Gate impact |
|---|---|---|---|
| Context and interested parties | Provider/tool context, needs, expectations and constraints defined | `CONTEXT_AND_INTERESTED_PARTIES.md` | Full automation HOLD until defined |
| Internal/external issues | Risks from provider limits, stale workspaces, human dependency and branch drift considered | context register / audit report | Must drive readiness checks |
| Risks and opportunities | Risk controls for generated artifacts, workspace drift and tool limits | CA-001, CA-002, AUD-001 | Risk unresolved = HOLD |
| Resources and infrastructure | Toolchain capability and plan/tier limits known | `TOOLCHAIN_CAPABILITY_MATRIX.md` | Unsupported tool = fallback route |
| Competence and awareness | Human/operator dependency and authority clear | `HUMAN_FACTOR_AND_OPERATOR_DEPENDENCY_CONTROL.md` | Hidden human integration = HOLD |
| Operational control | Branch, PR, artifact and toolchain rules defined | branch rules, artifact policy, interface control | uncontrolled scope = reject PR |
| Performance evaluation | CI, smoke checks, audit outputs and gate results reviewed | CI artifacts, audit reports | weak evidence = PASS_WITH_WARNINGS/HOLD |
| Corrective action | Audit findings converted into CA issues and PRs | CA issues/PRs | CA effectiveness must be reviewed |
| Management review | Automation incidents and maturity decisions reviewed | management review inputs | maturity upgrade requires approval |

## Factory acceptance prerequisites

Before a factory capability may move from dry-run to automated execution, the following must be available:

1. context and interested-party controls,
2. toolchain capability matrix,
3. toolchain interface control,
4. human-factor dependency control,
5. generated-artifact policy,
6. conflict recovery rules,
7. CI inspection evidence,
8. operator release authority,
9. corrective action closure where applicable.

## Build expansion rule

No build line may expand capability only because a tool can perform the action.

Expansion requires:

- management-system approval criteria,
- risk assessment,
- interface control,
- readiness evidence,
- rollback/fallback route,
- auditability.

## Automation maturity gates

| Maturity state | Description | Required management-system condition |
|---|---|---|
| Manual | Human performs routing and merge | Basic controls documented |
| Controlled semi-automation | GitHub issues/PRs/CI support human operation | Context, artifact and branch controls defined |
| Dry-run automation | Tool runs without source mutation | Tool readiness and interface controls defined |
| PR-write automation | Tool may create branches/PRs | Capability matrix, readiness checks and CI gates active |
| Limited autonomous execution | Tool may execute defined task classes | Management review approval and evidence-backed gates |
| Full autonomy | Not currently approved | Requires future formal release decision |

## Current VIF state

Current approved state:

```text
Controlled semi-automation / dry-run pilot
```

Full automation remains on HOLD until the audit corrective actions are closed and effectiveness is verified.

## Management review inputs

The following must be reported to management review or equivalent governance review:

- automation incidents,
- repeated PR conflicts,
- failed tool readiness checks,
- provider plan limitations,
- human workload/dependency,
- generated-artifact exceptions,
- corrective action effectiveness,
- maturity upgrade requests.

## Conclusion

The factory may only accelerate when management-system controls are demonstrably ahead of the execution layer.

If the factory begins driving governance reactively, an audit or corrective action must be raised.
