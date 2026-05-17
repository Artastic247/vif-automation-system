# M4 Branch and PR Discipline Rules

## Scope
These rules apply to all M4 changes under `software-build-control/01-app-build-line/`.

## Branch Rules
1. Start every M4 task from the latest `main` branch state available in this repository.
2. Use one focused branch per task.
3. Keep branch scope limited to a single objective; do not mix M3 workflow/status updates with M4 branch-rule updates.
4. Rebase or merge `main` before opening a PR if the branch is behind.

## Pull Request Rules
1. Open a new PR per focused branch.
2. PR title must clearly describe the single objective.
3. PR must include only files required for that objective.
4. If unrelated files appear, stop and clean the branch before review.
5. Do not update or merge prior PRs that mixed unrelated objectives; replace them with clean, single-purpose PRs.

## Change-Control Checks
- Verify `git status` shows only intended files before commit.
- Verify PR diff matches the declared scope.
- If scope drift is detected, halt and split work into a separate branch and PR.
