# INSPECTION_STATIONS

## 1) Intake shape
Validate issue template completeness, route label, and objective clarity.

## 2) Handoff integrity
Validate handoff identifiers (`handoff_id`, `replay_key`), target/forbidden paths, and required check list.

## 3) Diff-scope check
Fail if changed files exceed allowlist or touch forbidden paths.

## 4) Build and test
Run required CI jobs and capture artifact links for operator review.

## 5) Security and prompt hygiene
Check for secret leakage, unsafe prompt content, and missing log masking.

## 6) Merge gate
Require all statuses green plus explicit operator approval before merge.
