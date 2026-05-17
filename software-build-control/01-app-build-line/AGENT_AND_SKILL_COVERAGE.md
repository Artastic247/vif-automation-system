# AGENT_AND_SKILL_COVERAGE

## Purpose
Define the required agent and skill for each app-build-line process step so execution is not ambiguous and can be automated without ad-hoc prompting.

## Step-to-agent coverage

| Step | Process artifact | Primary agent/workstation | Required skill/WI | Automation status |
|---|---|---|---|---|
| Intake | `00-intake/APP_BUILD_INTAKE.md` | `vif-orchestrator` | `skills/intake-triage/SKILL.md` | Implemented |
| Build card generation | `02-build-cards/BUILD_CARD.md` | `process-engineer` | `skills/create-build-cards/SKILL.md` | Implemented |
| Agent task handoff | `03-agent-task/AGENT_TASK_PACKET.md` | `codex-runtime-workstation` | `skills/run-task/SKILL.md` + `CODEX_TASK_HANDOFF.md` | Implemented |
| Verification | `04-verification/BUILD_VERIFICATION_PACKET.md` | `qa-gatekeeper` | `skills/verify-build/SKILL.md` | Implemented |
| PR and release gate | `05-pr-release/PR_RELEASE_PACKET.md` | `release-controller` | `skills/pr-release-gate/SKILL.md` | Implemented |

## Required execution rules
- One issue maps to one branch and one PR.
- All steps must emit evidence into `reports/`.
- `vif/intake`, `vif/diff-scope`, and `vif/ci` are mandatory check contexts.
- Merge requires explicit operator/release authority approval until autonomous merge policy is approved.
