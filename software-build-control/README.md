# Software Build Control System

Purpose: prevent context drift, truncation, uncontrolled scope, false PASS decisions, unsafe tenant rollout, and unverified AI-assisted software changes.

This package is foundation/control-system only. It does not authorise app-code changes, Supabase changes, RLS changes, deployments, n8n flows, customer-data access, auto-fixes, auto-merges, or releases.

## Local validation

```bash
python scripts/validate_control_pack.py --root . --mode control-pack
```

## Gate language

- PASS: sufficient evidence to proceed.
- HOLD: evidence missing or incomplete.
- BLOCKED: unsafe to proceed.

## Current automation boundary

Automation may inspect files and write reports under `reports/`. It must not edit source files, call external services, deploy, merge, release, access customer data, or modify Supabase/RLS.
