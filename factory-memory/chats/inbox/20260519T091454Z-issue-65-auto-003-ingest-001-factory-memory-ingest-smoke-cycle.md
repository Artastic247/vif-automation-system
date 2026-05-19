# Factory Memory Source

- Source type: issue
- Source ID: issue-65
- Title: AUTO-003-INGEST-001 - Factory memory ingest smoke cycle
- Ingested at: 20260519T091454Z

## Source content

# AUTO-003-INGEST-001 - Factory memory ingest smoke cycle

Source issue: #65

## Objective

Run the first controlled factory-memory ingest smoke cycle after AUTO-003 merged.

## Source

Use this issue as the source evidence.

## Expected outputs

- Stored issue evidence in `factory-memory/chats/inbox/`.
- Summary stub in `factory-memory/chats/summaries/`.
- Decision record stub in `factory-memory/decisions/`.
- Lesson learned stub in `factory-memory/lessons-learned/`.
- Skill update recommendation stub in `factory-memory/skills/`.

## Controls

- Deterministic v1 only.
- No LLM summarisation yet.
- No auto-merge.
- Human merge required.
- No deployment.
- No Supabase/RLS/customer data/app repo mutation.
- Expected-file scope check applies.

## Acceptance

AUTO-002, VIF Factory Gate, App Build Line Validation, and Codex review must PASS before human merge.
