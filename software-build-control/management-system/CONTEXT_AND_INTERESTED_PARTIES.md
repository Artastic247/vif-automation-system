# CONTEXT_AND_INTERESTED_PARTIES

## Purpose

This document defines the context and interested-party controls for the VIF software-build control system.

It supports CA-002 and ensures the app-build factory is governed by the management system before automation is expanded.

## Core principle

The management system governs the factory.

The factory governs automation.

Automation governs tools.

Tools execute work.

The reverse is not permitted.

## Scope

This context analysis applies to:

- VIF app-build-line,
- AI-assisted software production,
- GitHub control-plane workflows,
- Codex/ChatGPT/Claude-supported work,
- future orchestration tools,
- future product-line builds.

## Tool vs interested party distinction

Tools and platforms are resources or process interfaces.

Provider organisations are interested parties.

Examples:

| Provider / interested party | Tool / platform | Classification |
|---|---|---|
| OpenAI | ChatGPT, Codex, OpenAI API | Provider controls access, plans, models, usage rules and capability limits |
| Anthropic | Claude, Claude Code | Provider controls model behaviour, usage rules, tooling, limits and documentation |
| GitHub / Microsoft | GitHub, GitHub Actions, GitHub Apps | Provider controls repository permissions, workflow rules, API behaviour and branch protections |
| Supabase | Supabase platform | Provider controls hosted database, auth, RLS, edge function and plan limitations |
| n8n | n8n workflow platform | Provider controls workflow execution, webhook behaviour and hosting constraints |
| Vercel | Vercel deployment platform | Provider controls deployment, runtime, limits and availability |
| Lovable | Lovable app-building platform | Provider controls generation environment, integration limits and plan capability |

## Interested parties

### 1. Human operator / release authority

Needs:

- clear operating route,
- visible queue,
- evidence before merge,
- controlled escalation,
- low reliance on memory,
- clear stop/go rules.

System expects:

- final release authority,
- review of PR scope,
- approval of generated-artifact exceptions,
- escalation when gates fail.

Readiness evidence:

- operator panel available,
- branch/PR rules defined,
- handoff template available,
- conflict recovery rules available.

Blocking conditions:

- operator cannot identify current baseline,
- PR scope unclear,
- evidence unavailable,
- merge authority unclear.

Fallback:

- hold PR,
- return to issue/control-plane route,
- create corrective action if repeated.

### 2. OpenAI as provider

Tools supplied:

- ChatGPT,
- Codex,
- OpenAI API,
- model/runtime access.

Needs/expectations from VIF:

- compliant use of provider rules,
- secure handling of prompts and secrets,
- realistic assumption of plan and model limits,
- no overstatement of capability.

VIF expects:

- documented model/tool behaviour,
- stable enough execution interface,
- usable task execution where plan permits,
- predictable API or product limits where documented.

Key constraints:

- capability varies by plan,
- model variants may behave differently,
- Codex workspace may not always align with GitHub control plane,
- task limits and execution behaviour may differ between Plus, Pro, Team, Enterprise or API contexts.

Readiness evidence:

- current plan/tier identified,
- Codex access confirmed,
- GitHub integration confirmed,
- ability to access repo/default branch confirmed,
- push/PR capability confirmed where required.

Blocking conditions:

- no confirmed access to `main`,
- no origin/remote in workspace,
- insufficient token/auth scope,
- plan does not support required action,
- provider/runtime limit blocks execution.

Fallback:

- use GitHub control plane directly,
- use artifact-only dry-run,
- use manual branch creation,
- defer automation mode.

### 3. GitHub / Microsoft as provider

Tools supplied:

- GitHub repositories,
- GitHub Actions,
- GitHub Apps,
- branch protection,
- pull requests,
- issues,
- API.

Needs/expectations from VIF:

- secure token use,
- correct repository permissions,
- controlled branch/PR workflows,
- compliance with API and workflow constraints.

VIF expects:

- reliable source of truth,
- durable audit trail,
- issue/PR routing,
- CI inspection,
- branch protection and release controls.

Readiness evidence:

- repo default branch confirmed,
- permissions confirmed,
- actions enabled,
- required workflows present,
- branch protection/required checks reviewed.

Blocking conditions:

- private repo access failure,
- token or GitHub App missing permissions,
- workflow permissions too restrictive,
- Actions unavailable,
- branch protection misconfigured.

Fallback:

- manual GitHub UI intervention,
- direct control-plane change by authorised operator,
- corrective action.

### 4. Anthropic as provider

Tools supplied:

- Claude,
- Claude Code,
- MCP/tool integrations where used.

Needs/expectations from VIF:

- controlled prompt/context inputs,
- safe tool access,
- clear review-only or execution authority boundary.

VIF expects:

- review support,
- reasoning support,
- optional coding support when authorised,
- tool-use behaviour within defined constraints.

Readiness evidence:

- access confirmed,
- role defined,
- repository access route controlled,
- review/output expectations defined.

Blocking conditions:

- no repo access,
- unclear authority,
- context drift,
- unsupported action.

Fallback:

- ChatGPT planning review,
- GitHub issue evidence review,
- manual review.

### 5. GitHub Actions inspection station

Classification:

- tool/process interface supplied by GitHub/Microsoft.

Needs:

- correct workflow files,
- required permissions,
- stable inputs,
- controlled artifacts.

System expects:

- repeatable validation,
- evidence upload,
- status checks,
- no hidden source mutation unless authorised.

Blocking conditions:

- workflow not triggered,
- missing secrets,
- required report missing,
- status HOLD,
- artifact upload failure.

Fallback:

- manual dispatch,
- local evidence marked as non-release evidence,
- corrective action.

### 6. Future orchestration providers

Examples:

- n8n,
- Temporal,
- Vercel,
- Supabase,
- other automation hosts.

These become interested parties when used.

Readiness must be assessed before process reliance.

## Internal issues

The following internal issues affect VIF factory performance:

- operator memory dependency,
- manual prompt relay,
- branch scope drift,
- stale workspace reuse,
- generated artifacts treated as source,
- unclear merge authority in some flows,
- incomplete readiness checks for execution stations,
- duplicate PR creation by agents,
- unclear escalation when tools cannot access `main`.

## External issues

The following external issues affect VIF factory performance:

- provider plan limitations,
- model/capability variance,
- workspace/runtime instability,
- GitHub access or permission failures,
- private repo integration limits,
- network and transport failures,
- provider feature changes,
- API rate or task limits,
- pricing/tier changes,
- vendor policy changes.

## Risks and opportunities

### Risks

- automation attempted beyond tool capability,
- human operator remains hidden control point,
- provider limitations block execution,
- generated evidence conflicts recur,
- false confidence in AI autonomy,
- branch/PR drift.

### Opportunities

- GitHub as durable control plane,
- issue templates as structured work orders,
- CI artifacts as evidence records,
- Codex as controlled build station,
- ChatGPT/Claude as review and audit stations,
- phased autonomy with human release authority.

## Context conclusion

The VIF factory must not assume AI tools are always capable, connected or authorised.

Every toolchain station must have readiness criteria, capability limits, provider constraints, and fallback routes before it is used as part of the operating process.
