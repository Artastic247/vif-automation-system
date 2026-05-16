# AUTOMATION_BOUNDARY_MATRIX.md

## Purpose
Define exactly what automation is allowed, prohibited or maturity-gated within the Software Build Control System.

## Scope
Applies to GitHub Actions, validators, future n8n flows, AI-assisted workflows, release routes, app onboarding routes and future orchestration tooling.

## Owner/agent
VIF Orchestrator owns automation routing. QA Gatekeeper reviews enforcement boundaries. System owner approves maturity expansion.

## Inputs
Validator maturity, AI governance rules, CI governance, audit findings, CAPA status, management-review decisions and automation-readiness assessments.

## Activities/checklist
| Automation area | Allowed | Prohibited | Required maturity | Human approval required | Rollback required |
|---|---|---|---|---|---|
| Validation reporting | Yes | No destructive actions | M3 | Yes | Yes |
| Workflow gating | Limited | Auto-release/auto-merge | M4 | Yes | Yes |
| Auto-fix | No | All autonomous fixes | BLOCKED | N/A | N/A |
| Deployment automation | No | Automatic deployment | BLOCKED | N/A | N/A |
| Schema/RLS automation | No | Automatic schema/RLS changes | BLOCKED | N/A | N/A |
| Customer-data automation | No | Any customer-data routing without approval | BLOCKED | N/A | N/A |
| n8n orchestration | Future pilot only | Production orchestration | M4+ pilot | Yes | Yes |
| Release automation | No | Autonomous release | BLOCKED | N/A | N/A |

## Outputs/records
Automation approval, maturity evidence, rollback evidence and management-review input.

## Maturity level
Automation boundaries are controlled using M0–M5 maturity rules.

## Evidence required
Validator maturity, audit evidence, management approval, rollback route and monitored execution evidence.

## Linked process
MOP-04 AI governance, SOP-05 Tool routing and tool qualification, MOP-06 Management review.

## Linked agent/skill/procedure/module
VIF Orchestrator, QA Gatekeeper, GitHub Release Controller, Validator Control Procedure and CI Activation Governance.

## Interface/control point
Interfaces with validators, workflows, future n8n routes, release governance and app onboarding.

## PASS/HOLD/BLOCKED rules
- PASS: automation stays within approved boundary and maturity.
- HOLD: automation candidate requires more evidence or review.
- BLOCKED: automation attempts autonomous protected action.

## PDCA
- PLAN: define automation boundary.
- DO: execute limited approved automation.
- CHECK: monitor behaviour and findings.
- ACT: tighten or expand boundaries based on evidence.

## Audit frequency
Reviewed during management review, validator review and automation-readiness review.

## Automation allowance
This document itself governs automation allowance.

## Escalation
Escalate overreach, false PASS, unsafe automation, missing rollback or maturity overstatement.

## Update trigger
Workflow change, validator change, audit finding, automation pilot or management-review decision.
