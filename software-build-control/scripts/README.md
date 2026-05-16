# Validation scripts

Run from `software-build-control/`:

```bash
python scripts/validate_control_pack.py --root . --mode control-pack
```

Scripts are read-only except report output under `reports/`. They do not call external services, deploy, merge, release, modify Supabase/RLS, or access customer data.
