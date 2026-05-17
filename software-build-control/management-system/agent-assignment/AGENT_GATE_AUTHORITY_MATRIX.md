# AGENT_GATE_AUTHORITY_MATRIX

## Purpose
Define who may make PASS/HOLD/BLOCKED gate decisions and who may approve high-risk decisions.

## Scope
All management-system gates, ADP gates, release/rollback, app onboarding, app-repo CI, n8n, backend/RLS/security changes, standards/compliance interpretations and customer-facing claims.

## Owner/agent
QA Gatekeeper controls the matrix with VIF Orchestrator and Management Review Owner.

## Inputs
Master agent register, RACI authority matrix, ADP gates, WI gates, risk level, maturity level and protected-scope rules.

## Activities/method
Assign decision authority per gate, define allowed decision scope, required evidence, second approval if needed and prohibited approvals.

## Outputs/records
Gate authority matrix, approval evidence and escalation route.

## Linked processes
Clause 4-10, ADP-01 to ADP-21, app onboarding and automation governance.

## Linked skills/WIs
WI_001 to WI_030.

## Linked gates
All PASS/HOLD/BLOCKED gates.

## Evidence required
Gate decision record, authority owner, evidence reviewed, approval status and escalation if blocked.

## Risks
Wrong approver, false PASS, customer-facing claim without source, release without rollback, automation before maturity.

## Controls
Only named gate authorities may move gates. App-repo CI/n8n remain HOLD until separate readiness gate passes. Auto-fix, auto-merge and auto-release remain BLOCKED.

## Interfaces
QA, VIF Orchestrator, Release Controller, Security/Data Reviewer, Standards Specialists, CI/n8n Controllers, App Owner.

## Gate authority matrix
| Gate/decision | PASS authority | HOLD authority | BLOCK authority | Evidence required | Notes |
|---|---|---|---|---|---|
| Context/source lock | QA Gatekeeper | Context Specialist | QA Gatekeeper | Context/source record | Wrong repo/source = BLOCK |
| Scope/job card | VIF Orchestrator | QA Gatekeeper | QA Gatekeeper | Job card/scope | Broad prompt = HOLD/BLOCK |
| Requirements | App Owner + QA | App Owner | QA Gatekeeper | Acceptance criteria | Process owner consulted |
| Runtime-first | QA Gatekeeper | Runtime Architect | QA Gatekeeper | Runtime map/proof | UI shell not PASS |
| UI/interface | App Owner | UI/UX Reviewer | QA Gatekeeper | UI review | No backend claims |
| Backend/RLS/security | Supabase/RLS Engineer + Security Reviewer | Security Reviewer | QA Gatekeeper | RLS/security proof | Frontend-only blocked |
| Build execution | VIF Orchestrator | QA Gatekeeper | QA Gatekeeper | Approved job card | Scoped only |
| Verification | QA Gatekeeper | Evidence Auditor | QA Gatekeeper | Build/test/scan evidence | False PASS blocked |
| Validation/UAT | App Owner + Process Owner | UAT Coordinator | QA Gatekeeper | UAT evidence | User/process fit required |
| Release/rollback | Release Controller + App Owner | Release Controller | QA Gatekeeper | V&V + rollback proof | No evidence = BLOCK |
| App onboarding | QA Gatekeeper | VIF Orchestrator | QA Gatekeeper | Onboarding readiness | Separate job card required |
| App-repo CI | QA Gatekeeper + GitHub CI Controller | GitHub CI Controller | QA Gatekeeper | Onboarding PASS + calibration | Currently HOLD |
| n8n | QA Gatekeeper + n8n Controller + MLA Assessor | n8n Controller | QA Gatekeeper | Automation maturity evidence | Currently HOLD |
| Backend/RLS changes | Supabase/RLS Engineer + Security Reviewer | Security Reviewer | QA Gatekeeper | Runtime/rollback proof | Production changes blocked without gate |
| Standards interpretation | Relevant Standards Specialist | Standards Specialist | Compliance Claim Approver | SOURCE REQUIRED | No compliance claim |
| Customer-facing claim | Compliance Claim Approver + App Owner | Compliance Claim Approver | QA Gatekeeper | Source/customer evidence | No certification claim |
| Auto-fix | None | QA Gatekeeper | QA Gatekeeper | Not applicable | BLOCKED |
| Auto-merge | None | QA Gatekeeper | QA Gatekeeper | Not applicable | BLOCKED |
| Auto-release | None | QA Gatekeeper | QA Gatekeeper | Not applicable | BLOCKED |

## PASS/HOLD/BLOCKED rules
PASS when authorised owner approves with evidence. HOLD when evidence or authority is incomplete. BLOCKED when prohibited approval is attempted or critical evidence is missing.

## Escalation
Escalate false PASS, missing evidence, unauthorised release, app-repo CI/n8n activation or unsupported compliance claim.

## MLA / maturity dependency
Higher-risk gates require M2+ pilot evidence; release/onboarding/CI/n8n require defined maturity thresholds and explicit approval.

## Update trigger
Gate change, authority change, audit finding, release issue, automation request or management-review action.
