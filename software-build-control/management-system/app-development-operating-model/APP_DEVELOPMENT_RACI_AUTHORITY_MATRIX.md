# APP_DEVELOPMENT_RACI_AUTHORITY_MATRIX

## Purpose
Define responsibility, accountability, consultation and information flow for app-development authority decisions.

## Scope
Authority decisions from intake through release, onboarding, CI, n8n and customer-facing claims.

## Owner/agent
VIF Orchestrator and QA Gatekeeper.

## Inputs
ADP process register, specialist matrix, maturity level, risk level and job card.

## Activities/method
Assign RACI for each decision and define authority limits.

## Outputs/records
RACI/authority record and approval evidence.

## Linked process
ADP-01 to ADP-21.

## Linked skills/WIs
Gate review, source lock, runtime-first, DB/RLS proof, validation/UAT, release/rollback, app onboarding readiness.

## Linked gates
All approval gates.

## Evidence required
Named decision, R/A/C/I parties, approval record, gate result.

## Risks
Wrong approver, unapproved release, unsupported customer claim, app-repo CI/n8n activated too early.

## Controls
Only accountable authority can release gate. App-repo CI and n8n remain HOLD until later approved job card.

## Interfaces
Authority connects app owner, process owner, QA, release, security, specialists and customer-facing approver.

## RACI matrix
| Decision | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Intake approval | VIF Orchestrator | Product/App Owner | QA Gatekeeper | Support Owner |
| Context/source lock | Context Specialist | QA Gatekeeper | GitHub Controller | VIF Orchestrator |
| Domain truth approval | Process Owner | Product/App Owner | Domain Specialist | QA Gatekeeper |
| User/operator workflow approval | Operator Workflow Specialist | Process Owner | UI/UX Specialist | Product/App Owner |
| Requirements approval | Product/App Owner | QA Gatekeeper | Process Owner, Compliance Specialist | Builder |
| Runtime map approval | Runtime Architect | QA Gatekeeper | Process Engineer | UI/Backend leads |
| UI approval | UI/UX Specialist | Product/App Owner | Operator/User Tester | Frontend Coder |
| Backend/RLS approval | Supabase/RLS Engineer | Security/Data Specialist | Backend Coder | QA Gatekeeper |
| Security/data approval | Security/Data Specialist | QA Gatekeeper | Supabase/RLS Engineer | Product/App Owner |
| Build execution | Builder/Coder | VIF Orchestrator | Prompt Engineer | QA Gatekeeper |
| Code review | Code Reviewer | QA Gatekeeper | GitHub Controller | Builder |
| Test approval | Test Owner | QA Gatekeeper | Integration Test Owner | Product/App Owner |
| Verification approval | QA Gatekeeper | QA Gatekeeper | Evidence Auditor | Release Controller |
| UAT approval | UAT Coordinator | Product/App Owner | Process Owner/User | Release Controller |
| Release approval | Release Controller | Product/App Owner | QA Gatekeeper, Config Controller | Support Owner |
| Rollback approval | Release Controller | QA Gatekeeper | Configuration Controller | Product/App Owner |
| App onboarding approval | VIF Orchestrator | QA Gatekeeper | App/Product Auditor | GitHub CI Controller |
| App-repo CI approval | GitHub CI Controller | QA Gatekeeper | Release Controller | VIF Orchestrator |
| n8n approval | n8n Automation Controller | QA Gatekeeper | MLA Assessor | Management Review Owner |
| Compliance/customer-facing claim approval | Compliance Claim Approver | Product/App Owner | Standards Specialist | VIF Orchestrator |

## PASS/HOLD/BLOCKED rules
PASS when RACI is defined and accountable approval exists. HOLD when consulted/informed roles incomplete. BLOCKED when accountable authority is missing or prohibited decision is attempted.

## Escalation
Escalate unapproved release, unsupported claim, app-repo CI activation or n8n automation attempt.

## Update trigger
Role change, process change, audit finding, app onboarding or management decision.
