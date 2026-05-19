# Factory Memory Source

- Source type: issue
- Source ID: issue-84
- Title: AUTO-007-LIVE-004 — Auto-merge enabled end-to-end smoke
- Ingested at: 20260519T120624Z

## Source content

# AUTO-007-LIVE-004 — Auto-merge enabled end-to-end smoke

Source issue: #84

## Objective

Verify the complete factory memory automation loop after repository `Allow auto-merge` was enabled.

## Expected result

Factory Memory Ingest should create a generated memory PR, AUTO-002 should PASS, Factory Auto-Merge Guard should PASS, and GitHub auto-merge should be requested for the generated memory PR.

## Controls

- Deterministic v1 only.
- Generated memory outputs only.
- Guarded auto-merge route only after AUTO-002 PASS and required checks pass.
- No deployment.
- No Supabase/RLS/customer data/app repo mutation.
