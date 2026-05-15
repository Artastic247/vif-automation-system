# APP_MAINTENANCE_PLAN

## Purpose
Control ongoing app maintenance and support.

## When to use
Scheduled reviews, dependency updates, security updates, backend reviews, or recurring maintenance.

## Owner/tool
App owner with GitHub/Codex evidence.

## Inputs
Repo status, dependencies, test results, Supabase state, RLS policies, backup/rollback status, lessons learned.

## Activities or fields
Routine maintenance; dependency updates; security updates; Supabase review; RLS review; backup/rollback review; test review; prompt/template review; lessons learned review.

## Outputs/records
Maintenance log, risks, actions, evidence.

## Gate controlled
Maintenance gate.

## PASS/HOLD/BLOCKED rules
PASS when maintenance evidence is current. HOLD if items are overdue. BLOCKED if critical security/rollback evidence is missing.

## Update trigger
Scheduled cadence, incident, release, dependency/security alert.
