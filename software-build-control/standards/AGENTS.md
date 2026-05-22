# Standards Execution Guard

Scope: `software-build-control/standards/**`.

This file adds only local rules. The root `AGENTS.md` remains the repo-wide source of truth for Git, PR, validation, protected-scope, and final-report requirements.

## Local Rules

- Do not start standards work without an approved job card, issue, or build order.
- Do not mark standards work `PASS` without evidence.
- Do not change app code from this standards scope.
- Do not include secrets, customer data, Supabase/RLS, deployment, or release changes unless specifically approved.
- Stop on missing source truth, failed verification, scope drift, unsafe data exposure, or `HOLD`.
