# Factory Memory Source

- Source type: issue
- Source ID: issue-69
- Title: AUTO-004-LIVE-001 — Factory memory label trigger test
- Ingested at: 20260519T114435Z

## Source content

# AUTO-004-LIVE-001 — Factory memory label trigger test

Source issue: #69

## Objective

Live-test the AUTO-004 GitHub-native factory memory trigger after PR #68 merged.

## Trigger under test

Add label `factory-memory-ingest` to this issue.

## Expected result

GitHub Actions should run `Factory Memory Ingest`, create deterministic factory-memory stubs from this issue, push an `auto-issue-*auto-003-factory-memory*` branch, and open a PR.

## Controls

- Deterministic v1 only.
- No LLM summarisation yet.
- No auto-merge.
- Human merge required.
- No deployment.
- No Supabase/RLS/customer data/app repo mutation.
- Expected-file scope check applies.
