# TENANT_ISOLATION_MAP

## Purpose
Show tenant separation between dev, demo, pilot, and real customer data.

## When to use
Before demo, pilot, rollout, or customer-data handling.

## Owner/tool
Tenant/data owner.

## Inputs
Tenant list, environment, RLS, feature flags, data sensitivity.

## Activities or fields
Tenant; type; environment; data class; access; feature exposure; rollback.

## Outputs/records
Tenant isolation evidence.

## Gate controlled
No tenant isolation map → no real customer pilot.

## PASS/HOLD/BLOCKED rules
PASS if isolation evidence is clear. HOLD if tenant data incomplete. BLOCKED if real data exposure risk exists.

## Update trigger
Tenant, environment, RLS, feature, or rollout change.
