# Factory Automation Smoke Test - 2026-05-19

## Control header

- Test ID: SMOKE-001
- Linked issue: #61
- Source branch: main
- Source commit: 4d484bf47492e652348e528be339f439d696537b
- Working branch: auto-issue-61-factory-smoke-test
- Date: 2026-05-19
- Test type: Controlled issue-to-PR smoke test
- Expected route: issue -> branch -> evidence change -> PR -> AUTO-002 -> app-build-line validation -> Codex review -> human merge decision

## Purpose

Confirm that the factory loop remains operational after the M7 intake record merged. This is a route smoke test, not a product-line maturity upgrade.

## Declared scope

Changed-file scope is limited to this evidence file:

- `software-build-control/management-system/audits/SMOKE_FACTORY_AUTOMATION_TEST_2026-05-19.md`

## Controls under test

| Control | Expected result |
|---|---|
| Start from GitHub main | Branch is created from `4d484bf47492e652348e528be339f439d696537b`. |
| One issue, one branch, one PR | Issue #61 maps to `auto-issue-61-factory-smoke-test`. |
| Expected-file scope check | Only this audit evidence file changes. |
| AUTO-002 route | AUTO-002 should review the PR and return PASS or HOLD. |
| VIF Factory Gate | Factory gate should complete. |
| App Build Line Validation | App build-line validation should complete. |
| Codex review | Codex review should confirm scope and gate state. |
| Human merge authority | Human remains final merge authority. |

## Protected scope confirmation

This smoke test does not modify:

- App repository source.
- Supabase configuration.
- RLS policies.
- Edge functions.
- Deployment configuration.
- Customer data.
- n8n orchestration.
- Runtime production paths.

## Gate expectation

PASS if:

- Changed-file scope remains exactly one evidence file.
- AUTO-002 returns PASS.
- VIF Factory Gate succeeds.
- App Build Line Validation succeeds.
- Codex review finds no blocking issue.

HOLD if any route or validation check fails.

BLOCKED if any protected scope is changed or auto-merge is attempted.

## Full-auto boundary

A passing smoke test permits the next controlled automation step. It does not authorize full autonomous merge, deployment, protected-scope mutation, or maturity upgrade by itself.
