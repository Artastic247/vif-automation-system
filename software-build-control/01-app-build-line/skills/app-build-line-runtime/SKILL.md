# App Build Line Runtime Skill

## Purpose
Execute the thin app-build runtime command route and collect evidence artifacts.

## Steps
1. Run `create-build-cards`.
2. Run `run-task`.
3. Run `verify-build`.
4. Confirm gate decision is `PASS_WITH_WARNINGS` unless scanner depth is upgraded and validated.

## Guardrails
- Do not edit app repos.
- Do not touch Supabase/RLS, n8n, deployment, or customer data.
