# Factory Memory Source

- Source type: issue
- Source ID: issue-87
- Title: AUTO-006 factory automation corrective controls
- Ingested at: 20260519T124250Z

## Source content

# AUTO-006 factory automation corrective controls

Source issue: #87

Corrective action for factory automation audit findings.

Scope:
- Make AUTO-002 able to fail workflow status when HOLD is produced.
- Make factory-memory ingest idempotent when an issue was already processed.
- Make guarded auto-merge handle clean/mergeable PRs without false failure.
- Add deterministic regression validation for the corrective controls.

Controls:
- GitHub main is source of truth.
- One issue = one branch = one PR.
- No direct push to main.
- No generated report commits.
- Human-gated control-plane change; generated memory PR auto-merge route remains scoped.
