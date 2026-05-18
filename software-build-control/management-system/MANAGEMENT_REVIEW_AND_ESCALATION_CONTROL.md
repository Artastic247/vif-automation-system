# MANAGEMENT_REVIEW_AND_ESCALATION_CONTROL

## Purpose

Define how VIF management review evaluates audit results, defects, corrective actions, automation maturity, and improvement opportunities.

The management review process governs maturity upgrades, escalation, corrective action effectiveness, and factory direction.

## Inputs to management review

Management review inputs include:

- audit findings,
- corrective actions,
- failed gates,
- defects,
- PR conflict trends,
- generated-artifact exceptions,
- tool readiness failures,
- provider/tool limitations,
- operator burden,
- maturity upgrade requests,
- CI/action lifecycle warnings,
- LLM recommendations,
- runtime propagation issues,
- repeated HOLD conditions,
- product-line readiness concerns.

## Review outputs

Management review outputs may include:

- approve action,
- reject action,
- request more evidence,
- raise corrective action,
- raise OFI,
- assign LLM analysis,
- escalate to Angus,
- approve maturity upgrade,
- place route on HOLD,
- limit approved task class,
- require additional verification.

## Escalation to Angus

Escalate to Angus when:

- maturity upgrade is requested,
- release authority is required,
- protected-scope exception is requested,
- risk acceptance is required,
- recurring failure is observed,
- automation exceeds approved class,
- governance and actual operating behaviour diverge,
- provider/tool constraints materially affect factory operation.

## Escalation to LLM review/recommendation

Use LLM review for:

- root cause analysis,
- corrective-action proposal,
- audit summary,
- risk analysis,
- process improvement recommendation,
- toolchain comparison,
- maturity recommendation,
- workflow and governance review.

LLMs may recommend.

LLMs may not:

- approve release,
- approve protected-scope changes,
- approve maturity upgrades,
- approve auto-merge,
- override Head of Factory authority.

## Defect handling

Defects must be classified as:

- process defect,
- toolchain defect,
- artifact defect,
- routing defect,
- operator-interface defect,
- product-line defect,
- governance defect,
- maturity-control defect.

Each defect must have:

- issue reference,
- owner,
- containment decision,
- corrective action decision,
- effectiveness verification requirement,
- escalation decision where required.

## Review cadence

Management review must run:

- after major maturity gates,
- after failed verification,
- after recurring PR conflicts,
- after corrective action closure,
- before full automation expansion,
- before product-line expansion,
- before autonomous capability increase.

## Records

Management review records must include:

- issue/PR references,
- decision,
- evidence reviewed,
- responsible owner,
- next action,
- HOLD/PASS decision,
- escalation route,
- maturity impact.

## Current maturity governance position

Current approved maturity:

```text
Level 3.2 — Governed Controlled Automation
```

Current approved capabilities:

- issue-driven routing,
- dry-run artifact generation,
- documentation-only PR-write,
- low-risk runtime mutation,
- related runtime/control propagation,
- human merge authority.

Current prohibited capabilities:

- autonomous merge,
- broad autonomous repair,
- unrestricted runtime mutation,
- product-line mutation,
- deployment automation,
- unrestricted orchestration.

## Current next gate

```text
M7 — first product-line dry-run
```

No maturity upgrade beyond current state may proceed without management review approval and Head of Factory acceptance.
