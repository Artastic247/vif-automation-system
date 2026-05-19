# M7 Product-Line Dry Run Internal Audit

## Control header

- Audit ID: M7-DRYRUN-001
- Linked issue: #59
- Source branch: main
- Source commit: 0456234374908e330ef3950df87ae6b4019a6a7f
- Working branch: auto-issue-59-m7-product-line-dry-run
- Date: 2026-05-19
- Status: Intake evidence and controlled dry-run route definition
- Maturity state before this record: Level 3.2 governed semi-automation
- Maturity target under test: M7 controlled product-line dry-run

This record does not approve Level 4 maturity, auto-merge, deployment, app repository mutation, Supabase/RLS changes, customer data handling, or full autonomous factory operation.

## Objective

Establish the first controlled evidence pack for the M7 product-line factory dry run and internal audit. The objective is to confirm whether the management system is ready to route a real product-line dry run through issue, branch, PR, validation, AUTO-002 review, Codex review, and human merge.

## Scope

In scope:

- Management-system alignment check for M7 readiness.
- MLA readiness assessment for moving from Level 3.2 toward Level 4 evidence.
- Factory skill and plugin architecture recommendation.
- Evidence inventory for current controlled automation records.
- Dry-run route, bottlenecks, protected boundaries, and next actions.

Out of scope unless separately approved:

- Auto-merge.
- Direct push to main.
- Broad autonomous repair.
- Runtime deployment.
- App repository mutation.
- Supabase, RLS, edge function, or customer-data changes.
- n8n orchestration changes.
- Generated report commits as source payloads.

## Method

This intake follows the deep-dive evidence review method:

1. Build evidence inventory.
2. Tag material statements as FACT, INFERENCE, or UNKNOWN.
3. Identify missing evidence and protected boundaries.
4. Map the system controls that must govern the dry run.
5. Set gate status before execution.

The VIF Skill OS method is used to assess skills as controlled work instructions with scope, evidence, handoff contracts, platform adapters, and release gates.

## Evidence inventory

| Evidence | Observation | Control relevance |
|---|---|---|
| `.codex/AGENTS.md` | Codex station operating contract exists after CODEX-PLUGIN-001. | Codex can load a repeatable factory-station contract. |
| `.codex/skills/auto-issue-to-pr/SKILL.md` | AUTO-001 skill pack exists. | Issue-to-branch-to-PR route is documented for Codex. |
| `.codex/skills/auto-pr-review/SKILL.md` | AUTO-002 review skill exists. | PR review and HOLD/PASS routing are documented. |
| `.codex/skills/repair-loop/SKILL.md` | Repair loop skill exists. | HOLD results have a documented repair route. |
| `.codex-plugin/plugin.json` | Codex plugin metadata exists. | The pack is discoverable as a Codex plugin/instruction pack. |
| `.github/workflows/auto-pr-review.yml` | AUTO-002 now covers `auto-issue-*` and `codex-plugin-*` branches. | Plugin-pack and controlled automation branches can be reviewed. |
| `software-build-control/scripts/auto_pr_review.py` | AUTO-002 includes scoped review profiles. | Changed-file scope checks are profile-aware. |
| `software-build-control/management-system/AUTOMATION_MATURITY_REGISTER.md` | Current verified maturity remains Level 3.2 with M7 as next gate. | Prevents false claims of full autonomy. |
| `software-build-control/management-system/MANAGEMENT_SYSTEM_TO_FACTORY_TRACEABILITY.md` | Management system remains upstream of factory control, automation control, tool execution, and output. | Confirms reverse control is not permitted. |
| `software-build-control/management-system/TOOLCHAIN_CAPABILITY_MATRIX.md` | Tool and provider capability limits are registered as management-system controls. | Supports LLM/platform selection and limitation tracking. |
| `software-build-control/management-system/agent-assignment/MASTER_AGENT_REGISTER.md` | Controlled human, AI, and tool roles are registered. | Supports agent assignment and accountability. |
| `software-build-control/management-system/AGENT_REGISTER.md` | Factory worker/station roles are documented. | Supports split-work routing across Codex, Claude, Copilot, and future LLM stations. |
| `software-build-control/management-system/app-development-operating-model/APP_DEVELOPMENT_ROLE_WORKSTATION_MODEL.md` | Workstation boundaries and prohibited work are defined. | Prevents uncontrolled app mutation. |
| `software-build-control/01-app-build-line/OPERATOR_PANEL.md` | Operator panel records current mode, maturity, restrictions, and M7 as next gate. | Gives operator-facing gate state. |
| `.github/workflows/app-build-line-validation.yml` | App-build-line validation exists for controlled sample execution and report upload. | Provides validation mechanism for dry-run evidence. |

## Fact, inference, and unknown register

| Type | Statement | Impact |
|---|---|---|
| FACT | PR #55 added the VIF Codex plugin pack and was merged before this intake. | Codex has a repeatable station pack baseline. |
| FACT | PR #58 updated AUTO-002 coverage and was merged before this intake. | AUTO-002 can now review plugin-pack branches and the controlled coverage repair route. |
| FACT | Current main for this intake is `0456234374908e330ef3950df87ae6b4019a6a7f`. | Branch baseline is traceable. |
| FACT | The approved maturity state before this record is Level 3.2, not full autonomy. | Prevents maturity overstatement. |
| FACT | Human merge authority remains mandatory. | Auto-merge remains prohibited. |
| FACT | Protected scope includes app repo mutation, Supabase/RLS, deployment, customer data, and broad repair unless separately approved. | Dry run must stay artifact and evidence focused. |
| INFERENCE | The factory is ready to start M7 as a controlled intake and evidence route. | M7 can proceed as a dry run, not as an autonomy upgrade. |
| INFERENCE | VIF Skill OS should be merged into the factory as the governed skill-system layer. | Skills become managed factory assets instead of ad hoc local prompts. |
| INFERENCE | Codex, Claude, Copilot, ChatGPT, and future LLM stations should use thin adapters over the same neutral factory skill contracts. | Multi-LLM collaboration becomes auditable and replaceable. |
| INFERENCE | Usage caps, free-tier limits, context windows, runtime limits, and tool permissions should be treated as provider constraints in the toolchain matrix and agent assignment route. | The factory can route work based on capability and bottleneck risk. |
| UNKNOWN | Actual current plan limits and usage caps for each connected LLM provider were not measured in this intake. | Provider routing remains a HOLD item before claiming autonomous load balancing. |
| UNKNOWN | Exact product-line sample for M7 execution has not been selected in this record. | Dry-run execution cannot start until the sample is named. |
| UNKNOWN | Available connector tools did not expose a direct workflow_dispatch trigger during intake. | Manual trigger or repo-attached GitHub CLI may be needed for the first execution. |
| UNKNOWN | Latest app-build-line artifacts from the post-merge baseline were not downloaded into this evidence pack. | Artifact review remains pending. |

## Management-system alignment

| Control area | Current state | M7 readiness |
|---|---|---|
| Governance hierarchy | Management system controls factory, automation, tools, and outputs. | PASS for intake. |
| Issue-to-PR route | AUTO-001 and Codex pack define issue, branch, change, validate, PR, review, human merge. | PASS for intake. |
| PR review route | AUTO-002 coverage now includes Codex plugin branches and controlled automation profile checks. | PASS for intake. |
| Repair route | Repair loop skill exists for HOLD results. | PASS for intake. |
| Maturity control | Level 3.2 remains source-of-truth state. | PASS for preventing false autonomy claims. |
| Product-line dry run | Route is defined, but a real product-line sample has not completed through the factory. | HOLD for Level 4 upgrade. |
| Multi-LLM orchestration | Roles and tool matrix exist, but provider caps and live handoff behavior are not measured. | HOLD for autonomous collaboration claims. |
| Protected scope | Restrictions are documented. | PASS for intake; BLOCKED for unapproved mutation. |

## VIF Skill OS and plugin architecture recommendation

VIF Skill OS should be merged into the factory as a governed factory skill-system layer, not as a single all-purpose prompt. The factory should own the following controlled assets:

- Skill registry.
- Plugin registry.
- Agent registry.
- Provider and tool capability matrix.
- Handoff contracts.
- Evidence requirements.
- Release and maturity gates.
- Lessons-learned loop.
- Platform adapters.

Individual skills and plugins should remain modular. Codex, Claude, Copilot, ChatGPT, Cursor, Gemini, Ollama, and future stations should load the same neutral factory contracts through thin platform adapters. This keeps the factory portable and prevents one LLM vendor or editor from becoming the uncontrolled source of truth.

The factory should not merge every available skill by default. A skill or plugin should be accepted only when it has:

- A clear factory purpose.
- Declared inputs and outputs.
- Scope and non-goals.
- Evidence it must inspect or produce.
- Handoff rules.
- Failure modes.
- Validation method.
- Owner or responsible station.
- Release state.

Candidate required packs for the next factory stage:

| Pack | Factory role | Current gate |
|---|---|---|
| VIF Skill OS | Governs skill lifecycle, adapters, evals, and release gates. | Merge into factory knowledge system as controlled method. |
| Codex Plugin Pack | Codex station execution and review instructions. | Baseline exists after CODEX-PLUGIN-001. |
| Deep Dive Evidence Review | Audit and internal-review intake method. | Use for M7 and management-system audits. |
| AUTO-001 Issue-to-PR | Controlled execution route. | Use for scoped issue-to-PR work. |
| AUTO-002 PR Review | Automated PR gate and HOLD/PASS route. | Use on every eligible PR. |
| Repair Loop | Controlled response to HOLD/failing checks. | Use only after failed gate. |
| ChatGPT App Submission | ChatGPT App packaging and review. | Not required unless the repo contains an MCP ChatGPT App server. |
| Security scan/threat-model skills | Protected-scope and customer-data checks. | Required before touching protected data or deployment. |
| Provider capability adapter | Captures LLM caps, costs, context limits, rate limits, and work routing. | Required before claiming multi-LLM autonomous collaboration. |

## Multi-LLM collaboration control concept

The factory should support many LLM stations, but collaboration must be controlled by the factory rather than negotiated ad hoc by the models.

Required routing data:

- Provider name and platform.
- Model family and version where visible.
- Available tools and permissions.
- Usage cap or quota type.
- Context and file limits.
- Runtime or session limits.
- Cost class.
- Strength profile.
- Known failure modes.
- Allowed work classes.
- Prohibited work classes.
- Handoff format.
- Evidence requirements.

Suggested station split:

| Station | Good fit | Factory limit |
|---|---|---|
| Codex | Repo inspection, scoped edits, PR creation, workflow repair. | Must prove repo/connector boundary and never auto-merge. |
| Claude Code | Long-form code review, refactor reasoning, alternate implementation critique. | Must not become approval authority. |
| Copilot | In-editor completion and small local changes. | Requires human/editor control and scope guard. |
| ChatGPT | Planning, evidence synthesis, product/design reasoning, app submission checks. | Must not be treated as repo truth unless connected to evidence. |
| Future LLM station | Assigned by capability, cap, and tool access. | Must register before receiving work. |

## Dry-run route

1. Create or confirm issue for M7 dry run.
2. Start from current GitHub main.
3. Create `auto-issue-*` branch.
4. Add or update only declared evidence files.
5. Open PR with expected-file scope check, workflow_dispatch only, no auto-merge, and human merge required.
6. Allow AUTO-002 and app-build-line validation to run.
7. Perform Codex review of PR evidence.
8. Human decides merge or HOLD.
9. After merge, select one product-line sample and run it through the factory as artifact-only evidence.
10. Record MLA result and management-review action.

## Bottlenecks and operator load

| Bottleneck | Current impact | Required control |
|---|---|---|
| Local workspace is not a Git checkout | Local repo proof and local workflow commands cannot be used from the current folder. | Use GitHub connector or repo-attached Codespace/task before repo claims. |
| Workflow dispatch not exposed through current connector tools | Full dry-run trigger may require manual GitHub UI, GitHub CLI in a real checkout, or a workflow rerun path. | Record trigger method in evidence. |
| Provider usage caps not measured | Multi-LLM load routing cannot be proven yet. | Add provider-capability register before autonomous routing. |
| Human merge remains mandatory | Operator is still the final release authority. | Keep maturity at Level 3.2 until M7 evidence passes review. |
| Product-line sample not selected | M7 execution cannot be completed from intake alone. | Select PFMEA, SPC, Control Plan, APQP, or other approved sample. |

## Protected-scope confirmation

This intake does not modify:

- App repository source.
- Supabase configuration.
- RLS policies.
- Edge functions.
- Deployment configuration.
- Customer data.
- n8n orchestration.
- Runtime production paths.

## Gate decision

| Gate | Decision | Reason |
|---|---|---|
| M7 intake readiness | PASS | Management-system controls, plugin pack, AUTO-002 coverage, and maturity register support starting a controlled dry-run intake. |
| Level 4 maturity upgrade | HOLD | No completed product-line dry-run evidence has been reviewed yet. |
| Full autonomous factory | BLOCKED | Human authority, provider limits, protected scope, rollback, monitoring, and live multi-LLM routing are not yet proven. |
| Auto-merge | BLOCKED | Explicitly prohibited by the operating contract. |

## Next action

Open the M7 intake PR and let AUTO-002 plus app-build-line validation run. If the PR passes, human merge may approve the intake record only. The next separate issue should select the first product-line sample and run the controlled artifact-only M7 dry run.
