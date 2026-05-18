# VIF_FACTORY_ORGANISATION_AND_ROLE_MODEL

## Purpose

Define the VIF factory organisation, roles, stations, authorities, and responsibilities.

This document makes the management system specific to the VIF factory. It is not a generic governance document. It defines how the factory is organised to design, build, verify, review, release, improve, and control AI-assisted software production.

## Factory hierarchy

```text
Head of Factory / Release Authority
→ Management Review Function
→ Factory Manager / Controller
→ Route Supervisor
→ Inspection and Audit Stations
→ Build Operators / AI Build Agents
→ Review Operators / AI Review Agents
→ Corrective Action and Improvement Loop
→ Product-Line Cells
```

## Head of Factory / Release Authority

Role holder:

```text
Angus
```

Authority:

- final maturity approval,
- final release authority,
- escalation acceptance,
- management review chair,
- approval of automation capability upgrades,
- approval of protected-scope exceptions,
- approval to move from one maturity level to the next.

The Head of Factory may request LLM analysis, recommendations, audits, risk reviews, and corrective-action proposals. The LLM may recommend but may not approve release or maturity upgrades.

## Management Review Function

The management review function evaluates whether the VIF factory is suitable, adequate, effective, controlled, and ready for maturity expansion.

Reviews:

- audit results,
- corrective actions,
- defects,
- recurring issues,
- provider/tool constraints,
- maturity upgrades,
- operator burden,
- CI/gate performance,
- improvement opportunities,
- automation incidents,
- readiness failures,
- generated-artifact exceptions.

Outputs:

- approved improvements,
- HOLD decisions,
- corrective action assignments,
- OFI assignments,
- escalation to Angus,
- requests for LLM analysis or recommendations,
- maturity upgrade approval/rejection.

## Factory Manager / Controller

Function:

- maintains the current maturity state,
- ensures work follows the issue/branch/PR route,
- confirms management-system controls before factory expansion,
- monitors gate results,
- monitors conflicts and recurring defects,
- confirms that documented status matches actual verified capability.

The Factory Manager / Controller must stop the route if the documented maturity state and actual operating state diverge.

## Route Supervisor

Function:

- verifies issue scope,
- confirms route and mode,
- checks allowed and forbidden paths,
- blocks stale or mixed-scope work,
- routes failed work to corrective action,
- confirms one issue / one branch / one PR discipline,
- verifies expected changed files before merge.

## Build Operators / AI Build Agents

Examples:

- Codex,
- future coding agents,
- workflow execution agents,
- local or cloud build stations.

Allowed:

- scoped tasks,
- dry-run execution,
- approved PR-write classes,
- evidence production,
- controlled runtime changes within approved gates.

Not allowed:

- auto-merge,
- broad repair,
- protected-scope changes without approval,
- hidden branch recovery,
- uncontrolled generated-artifact commits,
- maturity upgrades.

## Review Operators / AI Review Agents

Examples:

- ChatGPT,
- Claude,
- future review models,
- audit/reasoning agents.

Function:

- audit support,
- logic review,
- issue analysis,
- corrective action recommendation,
- management review input,
- risk analysis,
- maturity recommendation,
- process improvement recommendation.

Review agents may recommend action. They may not approve release, merge, protected-scope exceptions, or maturity upgrades.

## Inspection Stations

Examples:

- GitHub Actions,
- CI checks,
- artifact review,
- audit checks,
- changed-file preflight,
- generated-artifact policy checks,
- branch and PR discipline checks.

Function:

- detect nonconformity,
- generate evidence,
- support gate decisions,
- block uncontrolled changes,
- surface warnings and failures for operator review.

## Corrective Action Loop

The corrective-action loop is triggered by:

- audit findings,
- repeated PR conflicts,
- readiness failures,
- generated-artifact recursion,
- failed gates,
- toolchain defects,
- operator-interface defects,
- process defects,
- product-line defects.

Corrective action must identify:

- problem statement,
- root cause,
- containment where needed,
- correction,
- corrective action,
- verification of effectiveness,
- management review input where applicable.

## Improvement Loop

Opportunities for improvement are reviewed by management review and may be:

- approved,
- deferred,
- rejected,
- pushed back to an LLM for analysis/recommendation,
- escalated to Angus for decision,
- converted into corrective action if risk or recurrence justifies it.

## Product-Line Cells

Product-line cells are future factory execution routes for business outputs such as:

- PFMEA,
- Control Plan,
- SPC,
- APQP,
- inspection systems,
- app-build lines,
- quality-management tools.

Product-line cells may not proceed to live mutation until the relevant maturity gate has been passed and approved.

## Authority principle

Tools execute work.

The factory controls work.

The management system governs the factory.

The Head of Factory retains final release and maturity authority.
