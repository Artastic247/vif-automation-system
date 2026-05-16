# HUMAN_OVERSIGHT_MATRIX.md

## Purpose
Define required human approval points for AI-assisted software development, release support, data use, compliance claims and automation activation.

## Scope
Applies to all AI-assisted outputs and actions that may affect app code, schema/RLS, tenants, customer data, production release, rollback, compliance/audit evidence, customer-facing content or automation.

## Owner/tool
System owner owns final oversight. VIF Orchestrator controls workflow routing. QA Gatekeeper controls verification approval. Security/RLS Reviewer controls data/security approvals.

## Inputs
Job card, context pack, AI impact assessment, AI output, data classification, verification evidence, tenant/release records and risk rating.

## Activities/fields
| Decision/action | Required human approval | Required evidence | AI may recommend? | AI may execute? | Linked gate |
|---|---|---|---|---|---|
| Job card approval | VIF Orchestrator / process owner | Scope, evidence, gates | Yes | No | Job-card gate |
| App code change | Assigned owner + QA Gatekeeper | Job card, diff, tests | Yes | Only via approved tool route | Build/verification gate |
| Schema/RLS change | Security/RLS Reviewer | Runtime map, DB/RLS proof | Yes | No automatic change | DB/RLS gate |
| Customer-data use | Security/RLS Reviewer + project owner | Data approval/masking | No unless approved | No | Data protection gate |
| Tenant rollout | Release Controller + Security/RLS Reviewer | Tenant register, rollback | Yes | No automatic rollout | Tenant rollout gate |
| Production release | System owner / Release Controller | Verification, UAT, rollback | Yes | No automatic release | Release gate |
| Rollback | Release Controller / System owner | Rollback trigger and route | Yes | No automatic rollback | Rollback gate |
| Compliance claim | Compliance Specialist / system owner | Source evidence | Draft only | No | Compliance/evidence gate |
| Customer-facing content | Product/customer owner | Review and approval | Draft only | No | Content gate |
| AI automation activation | System owner + QA Gatekeeper | Readiness and risk approval | Yes | No | Automation-readiness gate |
| n8n workflow activation | System owner + Automation Controller | Workflow, trigger, risk, rollback | Yes | No | Automation-readiness gate |

## Outputs/records
Human approval record, approval/rejection decision, reviewer, evidence and gate status.

## Linked process
MOP-04 AI governance, COP-09 Job card approval, COP-11 Verification, COP-13 Tenant rollout, COP-14 Release/rollback, SOP-08 Security/data protection.

## Linked gate
Human oversight gate, job-card gate, DB/RLS gate, tenant gate, release gate, data protection gate, automation-readiness gate.

## Human approval
Required before protected changes, release, rollback, tenant exposure, customer-data use, compliance claim or automation activation.

## Data boundary
Approvers must verify data classification and AI_DATA_GOVERNANCE before approving AI-supported work.

## PASS/HOLD/BLOCKED rules
- PASS: correct human approver, evidence and gate decision are recorded.
- HOLD: approval is pending or evidence incomplete.
- BLOCKED: AI attempts protected action without required human approval.

## PDCA
- PLAN: define approval points and required evidence.
- DO: obtain approval before controlled action.
- CHECK: review approval records and evidence quality.
- ACT: update matrix after failures, audit findings or process changes.

## Update trigger
New AI route, new protected action, approval failure, audit finding, release issue, data incident, automation change or lesson learned.
