# CHANGE_IMPACT_MAP

## Purpose
Map what a change affects before approval.

## When to use
For internal/customer/urgent/backend/release changes.

## Owner/tool
Change owner.

## Inputs
Change request, app context, maps, runtime evidence.

## Activities or fields
Change; affected UI; DB; workflow; tenant; report; export; permission; tests; rollback.

## Outputs/records
Change impact map.

## Gate controlled
No change impact map → no change approval.

## PASS/HOLD/BLOCKED rules
PASS if impact and rollback are clear. HOLD if partial. BLOCKED if protected/customer-data impact unknown.

## Update trigger
Every significant change.
