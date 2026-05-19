# Branch Protection Guidance

## Purpose

This document records the intended protection rules for the VIF Automation System `main` branch.

The aim is simple: factory-control changes should enter `main` through a reviewed pull request with visible gate evidence.

## Target branch

`main`

## Required operating rule

`main` should be treated as a protected release lane. Normal work should be performed on a branch and submitted through a pull request.

## Recommended repository settings

In GitHub repository settings, configure `main` so that:

- A pull request is required before merge.
- At least one human approval is required.
- Pull request conversations are resolved before merge.
- Required status checks must pass before merge.
- Direct changes to `main` are avoided except for emergency owner action.

## Required status checks

Use the checks produced by `.github/workflows/vif-factory-gate.yml`:

- `VIF required-file gate`
- `Repository guard`
- `Optional Node checks`
- `Optional Python checks`

If GitHub displays workflow-prefixed names, select the matching checks from the latest VIF Factory Gate run.

## Agent rule

Agents may create branches, commits, and pull requests. Agents may not approve or merge their own work.

## Current limitation

This document records the required configuration. The actual GitHub setting must be applied in repository settings if the available tooling does not expose that setting.

## Verification

After configuration, create a small test PR and confirm that merge is blocked until the required review and VIF Factory Gate checks are satisfied.
