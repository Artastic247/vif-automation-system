# Validation Scripts

Run control-pack mode:

```bash
python scripts/validate_control_pack.py --root . --mode control-pack
```

Run app-repo mode:

```bash
python software-build-control/scripts/validate_control_pack.py --root /path/to/app --mode app-repo --control-path software-build-control
```

## Status meanings

- PASS: no blocking or hold findings.
- PASS_WITH_WARNINGS: warnings only.
- HOLD: human decision required before proceeding.
- BLOCKED: unsafe condition or critical missing evidence.

Scripts are report-only. They may inspect files and write reports under `reports/`. They must not auto-fix code, change Supabase/RLS, access customer data, auto-merge, deploy, or release.
