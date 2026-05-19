# VIF Factory Agent System

## Purpose

This folder defines the VIF factory-level control system for AI-assisted software builds.

It does not replace the controls inside each build repository. VIF owns the standard method, gates, templates, role definitions, and lessons-learned feedback loop. Each product/build repository still needs its own local `AGENTS.md`, CI workflow, task template, PR template, and product-specific build controls.

## Operating model

```text
VIF factory standard
  ↓
Build repository local controls
  ↓
Codex / Claude / GPT workstation execution
  ↓
GitHub Actions verification
  ↓
Pull request review
  ↓
Human release authority
  ↓
Lessons learned returned to VIF
```

## Layer split

| Layer | Responsibility | Output |
| --- | --- | --- |
| VIF factory | Defines standard work, agent roles, gates, reusable templates, and feedback rules | Factory agent system files and templates |
| Build repository | Defines local product context, routes, tests, restrictions, and acceptance criteria | Repo-specific `AGENTS.md`, CI, issues, PRs, release evidence |
| Agent workstation | Executes scoped work packages inside a controlled repo | Branches, code changes, test results, PRs |
| Verification gate | Runs automated checks and exposes failures | CI results, logs, failed checks, build evidence |
| Human authority | Confirms scope fit and release readiness | Merge/release decision |

## Core rule

VIF is the factory. The build repository is the production line. The AI tool is a workstation. GitHub Actions is the inspection bay. The user remains the release authority.

No agent may treat a chat answer, screenshot, or assumption as source of truth where a repository file, issue, PR, log, test result, or release record exists.

## Minimum deployment pack for each build repo

Each build repo must receive the following local controls before agentic coding is considered controlled:

```text
repo/
├─ AGENTS.md
├─ docs/
│  ├─ BUILD_CONTROL.md
│  ├─ DECISIONS.md
│  ├─ KNOWN_ISSUES.md
│  └─ RELEASE_CHECKLIST.md
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  └─ agent-task.yml
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/
│     └─ ci.yml
└─ src/
```

## Standard workflow

1. VIF defines the work package and acceptance criteria.
2. The build repo receives the task as a GitHub Issue.
3. Codex or another coding agent works on one branch for one issue.
4. The agent opens a PR with evidence of what changed and what was verified.
5. GitHub Actions runs the inspection checks.
6. The agent fixes CI failures and review findings inside the same scoped PR.
7. The user reviews the final diff and merge readiness.
8. Lessons learned are captured back into VIF when the build reveals a reusable rule, failure mode, or template improvement.

## Prohibited patterns

- Using VIF as a loose chat prompt bank with no repo controls.
- Letting every build repo invent its own agent operating method.
- Allowing agents to make broad rewrites under a small task title.
- Treating a passing UI as release evidence when service, data, permissions, and test gates are not checked.
- Merging AI-generated work without CI evidence and human release authority.
- Storing protected strategic logic or proprietary reasoning patterns in public-facing repo files.

## Folder contents

| File | Use |
| --- | --- |
| `agent-roles.md` | Defines factory-level agent roles and boundaries |
| `gate-model.md` | Defines the coding automation gates |
| `codex-pr-flow.md` | Defines the controlled Codex / PR operating loop |
| `lessons-learned-feedback.md` | Defines how build lessons update VIF |
| `templates/AGENTS.template.md` | Local build-repo agent instruction template |
| `templates/BUILD_CONTROL.template.md` | Local build-repo build control template |
| `templates/agent-task.template.yml` | GitHub Issue template for agent tasks |
| `templates/PULL_REQUEST_TEMPLATE.template.md` | PR evidence template |
| `templates/ci.template.yml` | Minimum GitHub Actions verification template |
| `templates/RELEASE_CHECKLIST.template.md` | Human release gate checklist |
