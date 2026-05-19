---
name: AUTO-002 PR Review Gate
description: Use when a pull request needs deterministic AUTO-002 review for scoped changes, protected-scope checks, validation evidence, and PASS or HOLD routing before human merge.
---

# AUTO-002 PR Review Gate

## Metadata
- id: auto-pr-review
- triggers: pull request opened, pull request ready for review, operator requests AUTO-002 review, PR branch updated after repair

## Purpose
Use AUTO-002 or equivalent Codex review to verify that a PR is scoped, validated, safe to merge by a human, and free of protected-scope changes.

## Inputs
- PR number or PR URL
- expected changed files
- issue number
- task class
- validation evidence
- declared protected-scope status

## Core rules
- GitHub main is source of truth.
- Do not work from stale local main.
- Do not push directly to main.
- One issue = one branch = one PR.
- Human merge authority remains mandatory.
- Auto-merge prohibited.
- Generated reports are artifacts, not source payloads.
- If workspace cannot confirm origin/main, STOP.
- If changed files exceed declared scope, STOP.
- If AUTO-002 returns HOLD, run repair-loop skill.

## Method
1. Confirm the PR targets `main`.
2. Confirm the branch contains current `origin/main` or has been refreshed against it.
3. List changed files and compare them with expected files.
4. Reject forbidden paths, generated report commits, broad repair, and protected-scope changes.
5. Review validation output and rerun deterministic checks when practical.
6. Return `PASS` only when scope, validation, and route are clean.
7. Return `HOLD` with specific repair instructions when anything is unclear or failing.
8. Do not merge.

## HOLD conditions
- unexpected changed files
- missing or weak validation evidence
- forbidden paths
- protected scope without explicit approval
- generated report commits
- PR does not target `main`
- issue number missing
- branch does not contain current `origin/main`
- broad or unrelated repair
- no rollback path

## Outputs
- PASS/HOLD state
- reviewed changed-file list
- validation evidence reviewed
- findings or repair instructions
- next action
