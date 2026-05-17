---
handoff_id: issue-<id>-r<rev>
source_issue: <id>
route: codex
branch_name: issue-<id>-<slug>
replay_key: issue-<id>-r<rev>
target_paths:
  - software-build-control/01-app-build-line/**
forbidden_paths:
  - .github/workflows/**
  - supabase/**
  - n8n/**
risk_class: low
operator_merge_required: true
required_checks:
  - vif/intake
  - vif/diff-scope
  - vif/ci
  - vif/operator-approval
output_schema: null
---

# Objective
State one specific outcome for this run.

# Context
State key context and constraints needed to execute without chat memory.

# Allowed work
List exact files or directories that may change.

# Disallowed work
List forbidden changes for this run.

# Acceptance criteria
Define the checks/evidence required for completion.

# Required PR body fields
- Linked issue
- Summary
- Changed files
- Out-of-scope confirmed
- Gate status
- Replay key
