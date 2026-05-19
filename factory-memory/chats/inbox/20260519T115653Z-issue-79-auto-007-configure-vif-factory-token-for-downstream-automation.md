# Factory Memory Source

- Source type: issue
- Source ID: issue-79
- Title: AUTO-007 — Configure VIF_FACTORY_TOKEN for downstream automation
- Ingested at: 20260519T115653Z

## Source content

# AUTO-007 — Configure VIF_FACTORY_TOKEN for downstream automation

Source issue: #79

## Objective

Close the remaining full-automation limitation where PRs created with the default `GITHUB_TOKEN` do not trigger downstream pull-request workflows.

## Required repository setting

Create repository secret `VIF_FACTORY_TOKEN` using a fine-grained GitHub token with access to `Artastic247/vif-automation-system`.

## Required permissions

- Contents: Read and write
- Pull requests: Read and write
- Issues: Read and write
- Actions: Read and write or read where write is not available
- Metadata: Read

## Acceptance criteria

- Factory Memory Ingest uses `secrets.VIF_FACTORY_TOKEN` instead of falling back to `github.token`.
- Generated factory-memory PRs trigger downstream required PR checks.
- Guarded auto-merge can complete after AUTO-002 PASS and required checks pass.

## Scope

Documentation/control record only until the secret is manually created in GitHub repository settings.
