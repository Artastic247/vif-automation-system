# Scripts README

Run all checks:

```bash
python scripts/validate_control_pack.py --root .
```

The scripts are safe and read-only except for writing reports under `reports/`.

PASS: evidence is acceptable for the check.
HOLD: evidence is incomplete or warnings need review.
BLOCKED: unsafe condition found.

Do not automate coding, RLS, destructive migrations, releases, tenant exposure, or customer-data access.
