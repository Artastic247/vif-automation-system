# DATA_FLOW_MAP

## Purpose
Map data movement, especially tenant/customer data.

## When to use
Before data handling, integration, import/export, or reporting claims.

## Owner/tool
Data/process owner.

## Inputs
Data sources, sinks, users, tenants, systems.

## Activities or fields
Source; data type; destination; access; retention; protection; evidence.

## Outputs/records
Data flow map.

## Gate controlled
No data flow map → no data handling claim.

## PASS/HOLD/BLOCKED rules
PASS if data paths and protection are known. HOLD if incomplete. BLOCKED if customer data path is unknown.

## Update trigger
Data, integration, tenant, import/export, or report change.
