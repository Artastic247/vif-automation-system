# SKILL.md

id: auto-pr-review
name: AUTO PR Review Station

trigger:
- AUTO-generated PR opened
- AUTO-generated PR synchronized
- PR branch starts with auto-issue-

purpose:
Perform deterministic inspection of AUTO-generated PRs before human merge.

inputs:
- PR title
- PR body
- head branch
- changed files

method:
1. Confirm auto branch pattern.
2. Confirm changed-file allowlist.
3. Reject forbidden paths.
4. Confirm PR metadata contains issue traceability.
5. Confirm PR body contains workflow and human merge controls.
6. Produce PASS/HOLD result.
7. Post result to PR.

outputs:
- AUTO-002 Review Result comment
- changed-file assessment
- pass/fail checklist
- recommendation

human approval point:
Human merge remains mandatory. Skill may recommend only.

failure modes:
- non-AUTO PR ignored
- forbidden files changed
- missing PR metadata
- generated report paths present
- workflow/runtime changes present
- no issue traceability
