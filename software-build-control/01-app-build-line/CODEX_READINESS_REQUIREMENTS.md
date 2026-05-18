# CODEX_READINESS_REQUIREMENTS

## Purpose

This document defines the readiness requirements for using Codex as a build-station interface within the VIF app-build-line.

Codex must not be treated as automatically ready.

Readiness must be verified before task assignment.

## Classification

- Codex = tool / build-station interface.
- OpenAI = interested party/provider.

## Core rule

If Codex readiness cannot be confirmed:

```text
STOP
```

Do not continue using stale or partially connected workspaces.

## Required readiness checks

### 1. GitHub connectivity

Verify:

- GitHub repository linked,
- correct repository selected,
- repository visibility/access confirmed,
- branch visibility confirmed.

Evidence:

- repo visible in Codex UI,
- branch list available,
- current default branch identifiable.

Blocking conditions:

- repo not visible,
- no branch visibility,
- no GitHub integration.

Fallback:

- use GitHub control plane directly,
- re-establish integration,
- use manual branch creation.

### 2. Control-plane confirmation

Verify:

- `main` or approved base branch exists,
- workspace aligns to current accepted baseline,
- origin/remote available where terminal execution is expected.

Blocking conditions:

- no `main`,
- no origin,
- detached workspace,
- stale branch only.

Mandatory response:

```text
STOP AND REPORT
```

### 3. Branch capability

Verify:

- branch creation possible,
- branch naming rules understood,
- branch scope isolated.

Blocking conditions:

- cannot create branch,
- stale branch reuse required,
- mixed-scope branch.

### 4. Push capability

Verify:

- push permitted,
- auth/token scope valid,
- private repo write access confirmed.

Blocking conditions:

- push denied,
- 403/auth failure,
- workspace cannot access remote.

Fallback:

- GitHub control-plane branch creation,
- manual operator push,
- dry-run only.

### 5. Pull request capability

Verify:

- PR creation permitted,
- repo integration active,
- target branch visible.

Blocking conditions:

- cannot create PR,
- repo not recognised,
- merge target unavailable.

Fallback:

- operator creates PR manually,
- GitHub control-plane route.

### 6. Scope-control capability

Verify:

- changed-file preflight available,
- task scope understood,
- protected paths identifiable.

Blocking conditions:

- changed files exceed approved scope,
- generated artifacts appear unexpectedly,
- protected paths appear.

Mandatory response:

```text
STOP AND REPORT
```

### 7. Capability/plan awareness

The VIF process must not assume all Codex environments have equal capability.

Verify:

- current plan/tier understood,
- model/runtime limitations understood,
- task size appropriate for environment.

Examples:

- Plus vs Pro vs Enterprise,
- runtime differences,
- task execution limits,
- context-size limits,
- branch/PR capability variance.

Blocking conditions:

- required feature unavailable,
- execution mode unsupported,
- workspace cannot perform required operation.

Fallback:

- GitHub Actions dry-run,
- manual control-plane operation,
- alternate review route.

## Human-factor control

The operator must not become the hidden integration layer.

If the operator is repeatedly:

- manually copying prompts,
- repairing stale branches,
- manually relaying outputs,
- manually reconstructing context,

then the process is not sufficiently automated or controlled.

This condition must trigger:

- corrective action,
- route redesign,
- improved interface automation.

## Current approved operating mode

Current approved state:

```text
Controlled semi-automation
```

Codex is currently approved for:

- dry-run support,
- controlled PR generation,
- narrow-scope changes,
- controlled branch operations.

Codex is not yet approved for:

- autonomous merge,
- uncontrolled branch recovery,
- broad conflict repair,
- unrestricted runtime mutation.
