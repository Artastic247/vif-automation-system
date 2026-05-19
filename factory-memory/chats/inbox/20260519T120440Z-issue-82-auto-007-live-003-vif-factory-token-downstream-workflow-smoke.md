# Factory Memory Source

- Source type: issue
- Source ID: issue-82
- Title: AUTO-007-LIVE-003 — VIF factory token downstream workflow smoke
- Ingested at: 20260519T120440Z

## Source content

# AUTO-007-LIVE-003 — VIF factory token downstream workflow smoke

Source issue: #82

## Objective

Verify that `VIF_FACTORY_TOKEN` enables generated factory PRs to trigger downstream pull-request workflows.

## Expected result

Applying the `factory-memory-ingest` label should run Factory Memory Ingest, create deterministic factory-memory stubs, open a PR, produce AUTO-002 PASS, trigger downstream PR checks, and allow guarded auto-merge once required checks pass.

## Controls

- Deterministic v1 only.
- Generated memory outputs only.
- Guarded auto-merge route only after AUTO-002 PASS and required checks pass.
- No deployment.
- No Supabase/RLS/customer data/app repo mutation.
