# VALIDATOR_DISABLE_ROLLBACK_ROUTE

## Purpose
Define controlled conditions for disabling, bypassing, rolling back or replacing a validator/check without creating false PASS risk.

## Scope
All validators/checks, CI checks, external app scan profiles and future n8n workflow checks.

## Owner/agent
QA Gatekeeper with Validator/Checker Auditor.

## Inputs
Disable request, reason, affected validator, affected gate, risk assessment, temporary control, rollback route, approver, escalation and record requirement.

## Activities/method
Assess whether disabling is allowed, define temporary control, block affected gates where needed, approve disablement, record action, roll back validator or restore previous version, and review false PASS risk.

## Outputs/records
Disable/rollback decision, temporary control, affected gate status, rollback evidence and management-review input where significant.

## Linked processes
Clause 9 validation/audit, Clause 10 improvement, app onboarding, CI readiness and n8n readiness.

## Linked skills/WIs
WI_021_INTERNAL_AUDIT, WI_024_CAPA_EFFECTIVENESS_REVIEW, WI_028_VALIDATOR_CALIBRATION and WI_030_CI_N8N_READINESS_REVIEW.

## Linked gates
Validator gate, evidence gate, app onboarding gate, CI/n8n gate, release gate and external validation closure gate.

## Evidence required
Disable reason, approval, temporary manual control, affected gates, rollback route, restore evidence and closure review.

## Risks
Validator disabled to bypass gate, false PASS, untracked manual workaround, no rollback, automation proceeds without check.

## Controls
A validator may only be disabled with QA approval, documented reason, temporary control and affected-gate HOLD/BLOCK decision.

## Interfaces
Validator Owner, QA Gatekeeper, Internal Audit Specialist, RCA/CAPA Specialist, GitHub CI Controller, n8n Controller and Management Review Owner.

## Disable/rollback rules
- Critical validators must not be disabled to enable PASS.
- If a critical validator is unavailable, affected gates remain HOLD or BLOCKED.
- Temporary manual review must be assigned and evidenced.
- Rollback restores previous known-good validator or disables affected automation path.
- False PASS risk must be explicitly contained.
- Disablement of security, secret, protected-scope, CI/n8n or release validators requires escalation.

## Approval authority
| Validator type | Disable approval | Temporary control | Gate effect |
|---|---|---|---|
| Critical security/secret/customer-data | QA Gatekeeper + Security/Data Reviewer | Manual security/data audit | BLOCK/HOLD |
| Release/rollback | QA Gatekeeper + Release Controller | Manual release audit | HOLD/BLOCK |
| App onboarding | QA Gatekeeper + App Onboarding Owner | Manual readiness review | HOLD |
| GitHub CI/n8n | QA Gatekeeper + CI/n8n Controller | Keep automation disabled | HOLD/BLOCK |
| Non-critical warning check | QA Gatekeeper | Manual review note | PASS_WITH_WARNINGS possible |

## PASS/HOLD/BLOCKED rules
PASS only when validator is restored or temporary control is effective for non-critical scope. HOLD when validator is disabled and gate evidence is incomplete. BLOCKED when disabling creates unsafe false PASS risk.

## Escalation
Escalate critical validator disablement, unapproved bypass, failed rollback, repeated validator failure or automation request without validator.

## MLA / maturity dependency
M4/M5 automation cannot rely on disabled critical validators. M2/M3 require manual review if validator is unavailable.

## Update trigger
Validator failure, false positive/negative, script change, CI/n8n readiness request, audit finding or management-review decision.
