# Software Build Control System

Purpose: prevent context drift, truncation, uncontrolled scope, false PASS decisions, missing verification evidence, unsafe tenant rollout, and repeated AI-assisted development failures.

This repository is foundation/control-system only. It does not contain production app code, Supabase migrations, RLS policies, customer data, environment variables, deployment configuration, n8n flows, or app repair instructions.

## Layers

1. Foundation templates and gate records.
2. Safe automation MVP for read-only validation.
3. Software Build Management System layer: context, leadership, planning, support, operation, performance evaluation, improvement, standards, agents, skills, prompts, and maps/schematics.
4. Hardened validation rules after DOS FMEA sandbox dry-run.

## Run locally

```bash
cd software-build-control
python scripts/validate_control_pack.py --root . --mode control-pack
```

For an app-repo dry run:

```bash
python software-build-control/scripts/validate_control_pack.py --root /path/to/app --mode app-repo --control-path software-build-control
```

## Safety boundaries

- Scripts are read-only except writing reports under `reports/`.
- Workflow files are templates under `github/workflows/` and are not active until copied to `.github/workflows/` under an approved job card.
- No auto-fix, auto-merge, deployment, Supabase/RLS change, customer-data access, n8n flow, or release action is allowed.

## Gate language

- PASS: no hold/block condition.
- PASS_WITH_WARNINGS: warnings only; human review may still be useful.
- HOLD: review required before proceeding.
- BLOCKED: unsafe or missing critical evidence.
