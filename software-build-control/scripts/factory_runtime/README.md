VIF Factory Runtime (MVP)

This folder contains a minimal read-only factory runtime script that performs a lightweight scan of the `software-build-control` workspace and emits a set of JSON and markdown reports under `software-build-control/reports/factory-runtime/`.

Usage

Run from the repository root:

```bash
python3 software-build-control/scripts/factory_runtime/factory_runtime.py --root software-build-control
```

Generated reports

- `factory-object-registry.json` - registry of files and counts
- `factory-audit-report.json` - findings about missing required directories
- `factory-audit-report.md` - human readable summary
- `factory-gate-decision.json` - gate decision (BLOCKED/HOLD/PASS_WITH_WARNINGS)
- `prompt-inventory.json` - discovered prompt-like markdown files
- `workflow-inventory.json` - discovered workflow-like markdown files
- `process-inventory.json` - placeholder
- `agent-skill-map.json` - placeholder

Notes

- The script is intentionally minimal: it currently detects prompt-like files by name containing `prompt` and workflow-like files by `workflow` in their name or path. Work instruction files prefixed `WI_` are counted.
- The gate is `BLOCKED` if any required management-system directory is missing, `HOLD` if WI count is below 30, otherwise `PASS_WITH_WARNINGS`.
- The runtime is read-only except for writing reports under `software-build-control/reports/factory-runtime/`.
