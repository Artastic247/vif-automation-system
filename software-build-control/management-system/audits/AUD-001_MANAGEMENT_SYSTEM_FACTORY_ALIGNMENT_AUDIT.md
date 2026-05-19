# AUD-001 Management System / Factory Alignment Audit

## 1. Audit identification

- Audit ID: AUD-001
- Audit title: Management-system governance over VIF factory build process
- Audit type: Internal system audit
- Audit trigger: Operator concern that the factory/tooling layer became muddled and moved ahead of the management-system layer
- Linked issue: #26
- Audit date: 2026-05-18
- Audit status: Completed for current evidence snapshot

## 2. Audit objective

Determine whether the VIF management system is effectively governing the factory build process, or whether the factory, automation, and AI toolchain layers are operating ahead of management-system control.

## 3. Audit scope

The audit covered the relationship between:

1. Management system layer
2. Factory control layer
3. App-build-line execution layer
4. Toolchain interfaces including Codex, ChatGPT, Claude, GitHub Actions and GitHub
5. Corrective actions CA-001 and CA-002
6. Recent PR / branch evidence from the app-build-line build sequence

## 4. Audit criteria

Audit criteria used:

- Management system must govern the factory.
- Factory must govern automation.
- Automation must govern tools.
- Tools must execute work.
- Context and interested-party requirements must be defined before reliance on tools.
- Internal and external issues must be considered.
- Risks and opportunities must be controlled.
- Process interfaces must be defined.
- Evidence must support gate decisions.
- Corrective actions must address root cause, not only symptoms.
- Generated artifacts must not drive source-control conflicts.
- Human-factor dependency must be visible and controlled.

## 5. Audit method

Audit method:

- Review of recent PR history and merge outcomes.
- Review of conflict recovery history involving PR #19, PR #20 and PR #21.
- Review of CA-001 issue and PR #23.
- Review of CA-002 issue and PR #25 status.
- Review of current GitHub control-plane evidence.
- Review of app-build-line operating logic, router behaviour and workflow maturity.
- Assessment against management-system/process-approach expectations.

## 6. Evidence reviewed

Evidence reviewed included:

- PR #2: initial thin app-build-line execution cell.
- PR #5: M1 closure status.
- PR #7: CI validation gate.
- PR #11: branch and PR discipline rules.
- PR #13: GitOps issue template, router/workflows, docs and routing script.
- PR #15: router hardening for manual dry-run pilot.
- PR #16: operator panel and automation acceleration updates.
- PR #17: agent guardrails.
- PR #18: smoke CI, automation acceleration plan and operator panel updates.
- PR #19, PR #20, PR #21: overlapping conflict-prone recovery PRs, all closed/not merged.
- PR #23: CA-001 generated-artifact and conflict-recovery governance, merged.
- PR #25: CA-002 context and Codex readiness controls, open/mergeable at time of audit.
- Issue #22: CA-001 corrective action.
- Issue #24: CA-002 corrective action.
- Issue #26: AUD-001 audit trigger.

## 7. Positive findings / conformities

### C-001: Control-plane direction is correct

GitHub has been established as the practical control plane for issues, PRs, branch records, audit trail and CI inspection.

This supports a durable system-of-record model and reduces reliance on transient AI workspaces.

### C-002: Corrective action process is functioning

The system detected a recurring failure mode, contained overlapping PRs, identified root cause, raised CA-001 and produced a corrective PR.

This demonstrates that the management system can identify and act on nonconformity.

### C-003: Generated artifact conflict risk is now formally controlled

CA-001 introduced controls separating mergeable source/configuration assets from generated evidence artifacts.

This directly addresses the conflict-loop mechanism observed in PR #19, PR #20 and PR #21.

### C-004: Human release authority remains retained

No evidence was found that autonomous merge authority has been approved. Human merge authority remains the release gate.

### C-005: Router has been hardened to dry-run mode

The app-build router has been constrained to manual/dry-run behaviour, which is appropriate while the management-system controls remain immature.

## 8. Nonconformities

### NC-001: Management system did not fully govern the factory before execution expansion

Evidence shows that app-build-line automation, routing, smoke workflows and operator-panel tooling were expanded before context, interested-party, provider-capability and toolchain-readiness controls were fully defined.

This caused the build sequence to become reactive rather than management-system-led.

Requirement intent affected:

- Context must be understood before process reliance.
- Interested-party requirements must be known before dependence on provider-controlled tools.
- Operational controls must be established before execution expansion.

Risk:

- Tooling decisions may outrun governance.
- Factory behaviour may be shaped by Codex/GitHub execution limitations rather than management-system requirements.

Required action:

- Complete CA-002 and link context/interested-party controls into factory operating controls before increasing automation autonomy.

### NC-002: Codex/toolchain readiness was assumed rather than verified before use

Codex workspace limitations, missing origin/default-branch access, push/PR capability and plan/tier constraints were discovered during operation instead of controlled as readiness criteria before task assignment.

Risk:

- Codex may be assigned work it cannot execute.
- Human operator becomes hidden integration layer.
- Stale workspaces can generate invalid PRs or conflict loops.

Required action:

- Implement and enforce Codex readiness checks before Codex receives build tasks.
- Treat OpenAI as provider/interested party and Codex as a tool/process interface.

### NC-003: Human operator became the hidden automation layer

The operating route relied on the human operator to copy prompts, interpret conflicts, trigger Codex, push/merge PRs and reconstruct context.

This means the process was not yet sufficiently systematised.

Risk:

- Loss of repeatability.
- Increased error probability.
- Operator fatigue.
- Process knowledge retained in chat memory rather than controlled documentation.

Required action:

- Add explicit human-factor control and reduce memory-dependent handoffs.
- Use issue templates, handoff contracts and operator-panel checks as mandatory process inputs.

### NC-004: Process interfaces are not yet fully mapped and traceable

Although GitHub, Codex, ChatGPT, Claude and GitHub Actions are referenced, the process interface map is not yet complete enough to show all inputs, outputs, authorities, constraints and fallback routes.

Risk:

- Tool boundaries remain ambiguous.
- Review/support/build roles may overlap.
- Agents may execute outside intended authority.

Required action:

- Add a toolchain interface-control document and capability matrix.
- Define station authority levels and handoff evidence.

## 9. Risk observations

### RO-001: Automation maturity exceeded governance maturity

The factory reached semi-automated GitOps routing before readiness, interested-party and provider capability controls were mature.

### RO-002: Generated evidence can still re-enter source control unless enforced technically

CA-001 defines policy. Further technical controls may be needed later, such as changed-file preflight checks or CI warnings when generated reports are included without authorisation.

### RO-003: Provider plan and model variance is a real operational constraint

ChatGPT/Codex/Claude capabilities vary by provider, plan, tier, model, runtime and integration method.

The factory must not assume Pro/Enterprise capability where the current operating context is Plus-level or otherwise constrained.

### RO-004: Tool providers are interested parties; tools are resources/interfaces

The audit confirms the distinction:

- OpenAI, Anthropic, GitHub/Microsoft and other providers are interested parties.
- Codex, ChatGPT, Claude, GitHub Actions and related systems are tools, resources and process interfaces.

This distinction must be embedded into management-system controls.

## 10. Opportunities for improvement

### OFI-001: Add a formal VIF process map

Create a process map showing:

```text
Management system
→ factory control
→ automation control
→ tool execution
→ product-line output
```

### OFI-002: Add turtle diagrams for key processes

Priority turtles:

- management-system governance process,
- app-build-line process,
- corrective action process,
- toolchain readiness process,
- PR/release process.

### OFI-003: Add a toolchain capability matrix

Matrix should include:

- provider,
- tool/platform,
- plan/tier,
- capability,
- limitation,
- readiness evidence,
- failure mode,
- fallback route.

### OFI-004: Add management-review inputs

Management review should include:

- automation incidents,
- failed PR/conflict loops,
- provider/tool capability changes,
- CI gate performance,
- operator burden,
- corrective action effectiveness.

### OFI-005: Add technical enforcement for generated-artifact policy

Later improvement may include CI checks that warn or fail when generated report files are changed without explicit authorisation.

## 11. Corrective action effectiveness review

### CA-001 effectiveness

CA-001 is considered effective for containment and initial recurrence prevention because:

- overlapping PRs were closed,
- generated-artifact conflict loop was identified,
- policy was created,
- conflict-recovery rules were created,
- a clean PR merged without conflict.

Remaining risk:

- policy needs technical enforcement in future.

### CA-002 effectiveness

CA-002 is not yet fully effective because PR #25 is open at the time of audit.

Expected effect after merge:

- context and interested-party controls defined,
- Codex readiness criteria established,
- provider/tool distinction captured,
- human-factor dependency recognised.

Further action likely required:

- toolchain interface control,
- capability matrix,
- human-factor dependency control document.

## 12. Management-system vs factory alignment verdict

Verdict:

```text
PARTIALLY ALIGNED / NOT YET MATURE
```

Rationale:

The management system is now beginning to govern the factory through corrective actions, policies and audit triggers. However, the build history shows that the factory execution layer initially advanced faster than the management-system controls.

The system is recoverable and improving, but further automation should be held until CA-002 is merged and the remaining interface/capability controls are completed.

## 13. Required next actions before further automation

### Action 1: Merge CA-002 after review
nPR #25 should be reviewed and merged if it remains clean and scope-controlled.

### Action 2: Open CA-003 or OFI task for toolchain capability matrix

Required file:

`software-build-control/management-system/TOOLCHAIN_CAPABILITY_MATRIX.md`

### Action 3: Add toolchain interface-control document

Required file:

`software-build-control/01-app-build-line/TOOLCHAIN_INTERFACE_CONTROL.md`

### Action 4: Add human-factor/operator dependency control

Required file:

`software-build-control/management-system/HUMAN_FACTOR_AND_OPERATOR_DEPENDENCY_CONTROL.md`

### Action 5: Hold full automation expansion

Do not progress to Codex PR-write/full-auto mode until:

- context/interested-party controls are merged,
- toolchain readiness checks exist,
- interface map exists,
- human-factor dependency is controlled,
- generated artifact policy is enforceable.

## 14. Audit conclusion

The operator concern is valid.

The VIF factory and management system became partially muddled during rapid build activity. The factory began to develop tooling, routing and smoke automation before the management-system context, interested-party, readiness and interface controls were fully established.

The corrective response is now moving in the right direction.

The immediate priority is not more automation. The immediate priority is to complete management-system alignment so the factory is built around controlled processes rather than around tool behaviour.

## 15. Post-audit effectiveness addendum

Original audit verdict:

```text
PARTIALLY ALIGNED / NOT YET MATURE
```

Post-corrective-action status:

```text
Management-system governance is now effective for Level 3.2 governed controlled automation.
```

Corrective actions completed:

- CA-001
- CA-002
- CA-003
- CA-004

Verification completed:

- VER-001
- M5A
- VER-002
- M6A
- M6B

Current remaining limitation:

The factory has not yet completed a real product-line dry-run.

Updated maturity:

```text
Level 3.2 — Governed Controlled Automation
```

Next required gate:

```text
M7 — first product-line dry-run
```

The original audit findings remain valid as historical evidence. This addendum records post-audit effectiveness and the current aligned maturity state after corrective actions and verifications were completed.
