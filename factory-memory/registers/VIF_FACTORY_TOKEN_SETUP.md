# VIF Factory Token Setup

## Purpose

`VIF_FACTORY_TOKEN` allows trusted VIF factory workflows to create branches and pull requests with a user-scoped or app-scoped token instead of the default GitHub Actions `GITHUB_TOKEN`.

This is required for the full automation loop because pull requests created with the default `GITHUB_TOKEN` do not reliably trigger downstream pull-request workflows.

## Secret name

Repository secret:

`VIF_FACTORY_TOKEN`

## Required repository

`Artastic247/vif-automation-system`

## Recommended token type

Use a fine-grained GitHub personal access token or GitHub App token scoped only to the VIF automation repository.

## Required permissions

- Contents: Read and write
- Pull requests: Read and write
- Issues: Read and write
- Actions: Read and write where available, otherwise read
- Metadata: Read

## Where it is used

Factory workflows should prefer:

`secrets.VIF_FACTORY_TOKEN || github.token`

This keeps the workflow runnable before the secret exists, but enables downstream workflow chaining after the secret is configured.

## Acceptance test

1. Create or label a factory-memory ingest issue.
2. Confirm Factory Memory Ingest opens a generated memory PR.
3. Confirm downstream pull-request checks start on that generated PR.
4. Confirm AUTO-002 returns PASS for generated memory scope.
5. Confirm guarded auto-merge can be enabled after required checks pass.

## Controls

- Do not store token values in the repository.
- Do not print token values in workflow logs.
- Rotate the token if exposed.
- Keep token scope limited to this repository.
- Control-plane workflow edits remain human-gated.
