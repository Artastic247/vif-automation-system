# VALIDATOR_SEVERITY_AND_GATE_RULES

## Purpose
Define validation severity levels and gate effects so findings consistently produce PASS, PASS_WITH_WARNINGS, HOLD or BLOCKED decisions.

## Scope
All validators/checks, scan profiles, workflow checks and future n8n checks.

## Owner/agent
QA Gatekeeper with Validator/Checker Auditor.

## Inputs
Finding type, risk, affected gate, protected scope, evidence status, maturity level, validator output and severity policy.

## Activities/method
Classify findings as INFO, WARNING, HOLD, BLOCKED, PASS or PASS_WITH_WARNINGS. Link each severity to gate impact and escalation rules.

## Outputs/records
Severity decision, gate result, escalation where required and management-review input for high-risk trends.

## Linked processes
Clause 9 validation/audit, Clause 10 improvement, app onboarding, release, backend/RLS change control, GitHub CI readiness and n8n readiness.

## Linked skills/WIs
WI_017_VERIFICATION_REVIEW, WI_019_RELEASE_ROLLBACK_REVIEW, WI_020_MOCK_DEMO_DATA_BOUNDARY, WI_028_VALIDATOR_CALIBRATION, WI_029_APP_ONBOARDING_READINESS and WI_030_CI_N8N_READINESS_REVIEW.

## Linked gates
Validation, app onboarding, app-repo CI, n8n, release, customer-facing claim, backend/RLS change and external validation closure gates.

## Evidence required
Finding evidence, severity rationale, gate impact, owner and closure route.

## Risks
Severity under-classified, warning used to bypass critical HOLD/BLOCK, PASS claimed without runtime evidence.

## Controls
Critical missing evidence, protected-scope breach, secrets/customer-data risk, premature CI/n8n, auto-fix/auto-merge/auto-release and unsupported customer claim are BLOCKED.

## Interfaces
QA Gatekeeper, Validator Auditor, Security/Data Reviewer, Release Controller, App Onboarding Owner, GitHub CI Controller and n8n Controller.

## Severity definitions
| Severity/result | Meaning | Gate effect |
|---|---|---|
| INFO | Non-blocking informational note | No gate block, record only |
| WARNING | Non-critical risk or maintainability concern | PASS_WITH_WARNINGS possible if no critical gate affected |
| HOLD | Evidence incomplete, required item missing, validation pending or non-critical control gap | Gate cannot close until resolved or accepted under controlled HOLD |
| BLOCKED | Unsafe/prohibited condition, critical evidence missing, protected-scope breach or forbidden action | Gate blocked; escalation required |
| PASS | Required checks satisfied with evidence | Gate may close for defined scope only |
| PASS_WITH_WARNINGS | Checks passed but non-critical warnings remain | Gate may close only if warnings are classified non-critical |

## Gate blocking rules
| Finding type | App onboarding | App-repo CI | n8n | Release | Customer-facing claims | Backend/RLS changes | External validation closure |
|---|---|---|---|---|---|---|---|
| Missing required critical artefact | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD |
| Missing validation execution | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD |
| Secret/customer-data exposure | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| Protected-scope breach | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| App onboarding attempted early | BLOCKED | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD |
| App-repo CI attempted early | BLOCKED | BLOCKED | HOLD | HOLD | HOLD | HOLD | HOLD |
| n8n attempted early | BLOCKED | HOLD | BLOCKED | HOLD | HOLD | HOLD | HOLD |
| Auto-fix/auto-merge/auto-release | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| Unsupported compliance/customer claim | BLOCKED | HOLD | HOLD | HOLD | BLOCKED | HOLD | HOLD |
| Backend/RLS proof missing | HOLD | HOLD | HOLD | BLOCKED if release | HOLD | BLOCKED | HOLD |
| Runtime validation unavailable | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD | HOLD |

## PASS/HOLD/BLOCKED rules
PASS only when evidence supports scope. HOLD when evidence/validation remains incomplete. BLOCKED when prohibited or unsafe condition exists.

## Escalation
Escalate BLOCKED findings, repeated HOLD without action, severity downgrade requests, and any false PASS risk.

## MLA / maturity dependency
Low maturity increases severity sensitivity. M4/M5 may allow warnings only where trend evidence proves control effectiveness.

## Update trigger
New validator, new risk class, FP/FN finding, audit finding, automation request or management-review decision.
