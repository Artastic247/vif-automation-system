# INCIDENT_REGISTER

## Purpose
Capture incidents, failures, escapes, and unsafe conditions.

## When to use
When a defect, failed release, data issue, tool drift, or control failure occurs.

## Owner/tool
Incident owner.

## Inputs
Evidence, logs, screenshots, affected app/tenant, impact.

## Activities or fields
| Incident ID | App/process | Description | Impact | Containment | Owner | Status | Linked RCA |
|---|---|---|---|---|---|---|---|

## Outputs/records
Incident record and containment evidence.

## Gate controlled
Incident containment gate.

## PASS/HOLD/BLOCKED rules
PASS if contained and assigned. HOLD if analysis pending. BLOCKED if customer/data/release risk remains uncontrolled.

## Update trigger
Any incident or control failure.
