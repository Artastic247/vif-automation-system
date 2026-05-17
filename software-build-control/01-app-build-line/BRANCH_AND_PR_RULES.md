# BRANCH AND PR RULES

## 1. Purpose
This document defines branch and pull request discipline for the VIF app-build line to reduce rework, prevent mixed scope, and keep merges reviewable and safe.

## 2. One issue = one branch = one PR
Each issue must be implemented on exactly one dedicated branch and proposed in exactly one PR. Do not combine multiple issues in a single PR.

## 3. Branch naming rules
- Use clear, issue-aligned names (for example: `issue-8-branch-pr-rules`, `m3-ci-validation-gate`).
- Avoid reusing stale feature branches for new issues.
- M2 rebuild branches must be created from current `main`.

## 4. PR title rules
- PR titles must state the intent and scope precisely.
- Use imperative style (for example: `Add branch and PR discipline rules for app-build line`).
- Do not use ambiguous titles such as "updates" or "misc fixes".

## 5. Allowed changed-file expectations
- A PR should change only files required for its issue scope.
- For governance-only tasks, prefer one-file PRs.
- Any unexpected file delta must be reverted before review.

## 6. No mixed-scope PR rule
- Do not mix M1 closure work, M2 rebuild work, and unrelated governance edits.
- Do not bundle runtime/workflow/code changes with branch-governance documentation unless explicitly required by one issue.

## 7. Stale branch handling
- If a branch drifts from `main` or contains superseded work, close/retire it.
- Start a fresh branch from current `main` for new implementation cycles.

## 8. Conflict handling rules
- Broad conflicted PRs that overlap accepted baseline should be closed, not manually repaired line-by-line.
- Rebuild required scope cleanly from current `main` in a new branch.

## 9. Merge authority rules
- Codex may create and update PRs.
- Codex may not merge unless explicitly authorised for that specific PR.
- Final merge authority remains with human reviewers/owners.

## 10. CI validation requirements
- CI validation must pass before merge review.
- For app-build-line route changes, run/create-build-cards, run-task, and verify-build validation path must be green.
- Upload/report evidence should be available for reviewer inspection.

## 11. M2 HOLD rule
- M2 remains `HOLD_PENDING_CLEAN_REBUILD` until explicitly reopened.
- No incremental M2 layering is allowed on stale/conflicted branches.
- M2 rebuild must start from current `main` only.

## 12. Codex authority limitations
- Codex cannot self-authorize scope expansion.
- Codex must follow protected-scope restrictions (no Supabase/RLS, n8n, deployment, customer data, DOS FMEA, or app-repo changes unless explicitly approved).
- Codex must stop and report when baseline/branch state is unsuitable.

## 13. Example good PR flow
1. Open issue with defined scope.
2. Branch from current `main` using issue-aligned name.
3. Implement only required files for that issue.
4. Run required validation and confirm gate result.
5. Open one PR with focused title/body and evidence.
6. Address review comments without widening scope.
7. Merge only after CI pass and human approval.

## 14. Example bad PR flow
- Reusing an old branch containing multiple prior tasks.
- Mixing M1 closure, M2 rebuild, and workflow/runtime edits in one PR.
- Manually repairing a large conflicted PR instead of closing and rebuilding cleanly.
- Requesting merge while CI is red or gate is `HOLD`.

## 15. Closure and cleanup rules
- After merge/closure, delete obsolete branches.
- Close superseded/conflicted PRs with reason documented.
- Keep status records updated to reflect accepted baseline and hold states.
- `PASS_WITH_WARNINGS` requires manual review and does not auto-approve merge.
- `HOLD` blocks merge until resolved.
