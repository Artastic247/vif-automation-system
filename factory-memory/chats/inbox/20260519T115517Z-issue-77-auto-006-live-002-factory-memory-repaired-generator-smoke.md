# Factory Memory Source

- Source type: issue
- Source ID: issue-77
- Title: AUTO-006-LIVE-002 — Factory memory repaired generator smoke
- Ingested at: 20260519T115517Z

## Source content

# AUTO-006-LIVE-002 — Factory memory repaired generator smoke

Source issue: #77

## Objective

Verify the repaired factory memory ingest generator after PR #76 merged.

## Expected result

Applying the `factory-memory-ingest` label should run Factory Memory Ingest, create deterministic factory-memory stubs, open a PR, include the required `human merge required` control phrase, and allow AUTO-002 to PASS for the generated memory PR.

## Controls

- Deterministic v1 only.
- No LLM summarisation yet.
- Generated memory outputs only.
- Guarded auto-merge route only after AUTO-002 PASS and required checks pass.
- No deployment.
- No Supabase/RLS/customer data/app repo mutation.
