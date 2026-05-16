# Software Build Control System

Purpose: prevent context drift, truncation, uncontrolled scope, false PASS decisions, unsafe tenant rollout, and unverified AI-assisted software changes.

This package is foundation/control-system only. It does not authorise app-code changes, Supabase changes, RLS changes, deployments, n8n flows, customer-data access, auto-fixes, auto-merges, or releases.

## App-development control coverage

The management-system layer now covers:

- app intake
- context lock and source-of-truth lock
- UI/interface design control
- data table/grid definition
- workflow/runtime mapping
- database/backend/RLS setup control
- environment and tenant strategy
- risk and contingency planning
- gate checklists
- agents/workers
- controlled skills/methods
- process knowledge reuse
- verification and validation/UAT
- tenant rollout and release
- rollback
- support/maintenance
- problem solving and lessons learned
- automation readiness

## Local validation

```bash
python scripts/validate_control_pack.py --root . --mode control-pack
```

## Gate language

- PASS: sufficient evidence to proceed.
- HOLD: evidence missing or incomplete.
- BLOCKED: unsafe to proceed.

## Current automation boundary

Automation may inspect files and write reports under `reports/`. It must not edit source files, call external services, deploy, merge, release, access customer data, modify Supabase/RLS, activate CI, or implement n8n without an approved job card.
