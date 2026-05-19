# MLA_AUTOMATION_PERMISSION_MATRIX

## Purpose
Define automation permission by maturity level.

## Scope
Control-system CI, app-repo CI, n8n, validators, agents, app onboarding, release readiness, and external app scan orchestration.

## Owner/agent
MLA Assessor, GitHub CI Controller, n8n Automation Controller, QA Gatekeeper.

## Inputs
Maturity level, audit status, risk, rollback/disable route, owner approval.

## Activities/method
| Maturity | Permission | Human approval | Allowed example | Prohibited example |
|---|---|---|---|---|
| M0 | None | Required | Exploration | Enforcement |
| M1 | None | Required | Draft review | Automation |
| M2 | Sandbox/manual | Required | Controlled pilot | App-repo enforcement |
| M3 | Controlled manual use | Required | Manual workflow | Auto-fix/release |
| M4 | Limited automation | Required | Report routing | Auto-merge/release |
| M5 | Automation candidate | Governance approval | Mature orchestration | Uncontrolled change |

## Outputs/records
Automation permission decision, approval record, rollback route and blocked-permission record where applicable.

## Audit criteria
Automation must never exceed maturity permission.

## Evidence required
MLA record, audit record, rollback/disable route, risk review, approval.

## MLA / maturity dependency
Automation permission is directly controlled by MLA level and risk.

## Linked process
Automation governance and Clause 9 MLA.

## Linked gate
Automation permission gate.

## PASS/HOLD/BLOCKED rules
PASS if automation is within permitted maturity and audited. HOLD if evidence is incomplete. BLOCKED if automation exceeds maturity or can modify app/Supabase/customer data without approval.

## Escalation
Escalate any automation that can auto-fix, auto-merge, auto-release, or alter protected data.

## Management-review input
Automation permission changes and blocks feed management review.

## Update trigger
Maturity change, CI/n8n request, tool change, audit finding.
