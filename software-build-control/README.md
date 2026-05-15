# Software Build Control System

Purpose: prevent context drift, truncation, uncontrolled scope, false PASS decisions, missing verification evidence, unsafe tenant rollout, and repeated AI-assisted development failures.

This repository is foundation/control-system only. It does not contain production app code, Supabase migrations, RLS policies, customer data, environment variables, deployment configuration, n8n flows, or app repair instructions.

Current status: safe automation MVP baseline.

Run locally from this folder:

```bash
python scripts/validate_control_pack.py --root .
```

Automation boundaries:
- scripts are read-only except writing reports under `reports/`
- workflow files are templates under `github/workflows/`
- workflows are not active until copied to `.github/workflows/` under an approved job card
- no auto-fix, auto-merge, deployment, Supabase/RLS change, or release action is allowed
