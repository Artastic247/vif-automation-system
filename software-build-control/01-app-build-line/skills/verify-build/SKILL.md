# SKILL: verify-build

## Trigger
Use on every app-build PR.

## Steps
1. Run required checks (`vif/intake`, `vif/diff-scope`, `vif/ci`).
2. Confirm no out-of-scope files are modified.
3. Record verification packet and gate decision.

## Outputs
- Verification report.
- Gate decision (`PASS`, `PASS_WITH_WARNINGS`, `HOLD`, `BLOCKED`).
