# STATE_MACHINE_MAP

## Purpose
Define workflow states, allowed transitions, actors, guards, and evidence.

## When to use
Before protected action or workflow change.

## Owner/tool
Workflow/backend owner.

## Inputs
Workflow map, roles, runtime map, backend rules.

## Activities or fields
State; transition; actor; allowed?; guard; backend proof; audit record.

## Outputs/records
State machine map.

## Gate controlled
No state machine map → no protected action change.

## PASS/HOLD/BLOCKED rules
PASS if transitions and guards are defined. HOLD if incomplete. BLOCKED if protected action lacks backend guard.

## Update trigger
Workflow/protected action change.
