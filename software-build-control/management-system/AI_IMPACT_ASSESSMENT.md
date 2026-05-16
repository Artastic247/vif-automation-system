# AI_IMPACT_ASSESSMENT.md

## Purpose
Assess the impact of AI-assisted work before AI output is used for app code, schema/RLS, tenant/customer data, release support, customer-facing content, compliance/audit evidence, automation activation or external-tool integration.

## Scope
Applies before high-risk AI use across app design, development, review, verification, validation, tenant rollout, release, customer communication, audit evidence and automation.

## Owner/tool
AI Governance Owner owns this template. VIF Orchestrator controls routing. QA Gatekeeper verifies evidence impact. Security/RLS Reviewer reviews data/security/tenant impact.

## Inputs
Current job card, context pack, AI tool route, prompt, output, affected files/data/tenants, data classification, risk register, human-approval requirement and verification method.

## Activities/fields
| Field | Required assessment |
|---|---|
| Assessment ID | Unique ID |
| Linked job card | Required for implementation/release/data-impacting use |
| AI tool/model | Tool and model/version if known |
| Use case | Review, code, schema/RLS, release, tenant, content, audit evidence, automation |
| Impact trigger | Code change, schema/RLS, customer data, tenant data, release, customer-facing content, compliance evidence, automation, external connection |
| Data involved | Public/internal/confidential/customer/secret/production/demo/synthetic |
| Files/systems affected | Repo/files/tables/workflows/integrations |
| Human approval required | Yes/No and approver |
| Verification evidence required | Build/test/security/RLS/manual review/evidence map |
| Risk rating | Low/Medium/High/Critical |
| Decision | PASS/HOLD/BLOCKED |
| Conditions | Required controls before proceeding |

## Outputs/records
AI impact assessment record, risk decision, human approval evidence, verification requirements and blocked/approved route.

## Linked process
MOP-04 AI governance and tool-use policy, MOP-03 Planning/risk/opportunity, COP-10 Build/modification control, COP-11 Verification, COP-14 Release/rollback, SOP-08 Security/data protection.

## Linked gate
AI impact gate, prompt gate, build gate, DB/RLS gate, data protection gate, release gate, automation-readiness gate.

## Human approval
Required before AI modifies app code, changes schema/RLS, affects tenant/customer data, supports release decisions, creates customer-facing content, generates compliance/audit evidence, activates automation or connects to external tools/repositories.

## Data boundary
Customer, confidential, secret and production data are HOLD/BLOCKED unless approved by AI_DATA_GOVERNANCE with masking/anonymisation and evidence.

## PASS/HOLD/BLOCKED rules
- PASS: impact is assessed, risk is acceptable, data boundary is safe, approval is recorded and verification is defined.
- HOLD: impact is plausible but evidence, approval, risk or verification is incomplete.
- BLOCKED: impact involves protected data, schema/RLS, release, tenant exposure, automation or compliance claims without approval/evidence.

## PDCA
- PLAN: assess impact before high-risk AI use.
- DO: execute only approved AI route.
- CHECK: verify AI output and impact controls.
- ACT: update risks, prompts, tools, lessons and controls after impact findings.

## Update trigger
High-risk AI use, new tool integration, app-code change, schema/RLS suggestion, tenant/customer data impact, release support, automation activation, audit finding or lesson learned.
