# ENVIRONMENT_MAP

## Purpose
Map local, dev, QA/staging, demo, pilot, production, and rollback environments.

## When to use
Before deployment, pilot, test, or release.

## Owner/tool
Environment owner.

## Inputs
Hosting, repo branches, Supabase projects, secrets, tenants.

## Activities or fields
Environment; purpose; data allowed; branch; DB; deployment; owner; rollback.

## Outputs/records
Environment map.

## Gate controlled
No environment map → no deployment/pilot plan.

## PASS/HOLD/BLOCKED rules
PASS if environment purpose and data rules are defined. HOLD if partial. BLOCKED if real data is used in wrong environment.

## Update trigger
Environment or deployment change.
