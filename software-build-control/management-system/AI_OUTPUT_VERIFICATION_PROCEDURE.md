# AI_OUTPUT_VERIFICATION_PROCEDURE.md

## Purpose
Ensure AI outputs are verified against source evidence, repo/files, security/data rules, tenant/RLS controls, build/test evidence and human review before they influence decisions or implementation.

## Scope
Applies to AI-generated or AI-assisted outputs for architecture, code, UI, database/backend/RLS, documentation, verification, validation, release support, rollback, audit evidence, customer-facing content and continual improvement.

## Owner/tool
QA Gatekeeper owns output verification. VIF Orchestrator controls gate routing. Security/RLS Reviewer verifies security/data/tenant impact. Relevant specialist owners verify technical outputs.

## Inputs
AI output, prompt, context pack, source-of-truth evidence, job card, files affected, risk/impact assessment, data classification, verification method and human reviewer.

## Activities/fields
Verification shall include:
- Source basis check.
- Evidence check.
- File/repo check.
- Security/data check.
- Role/tenant/RLS check where relevant.
- Build/lint/test evidence where relevant.
- Human review.
- PASS/HOLD/BLOCKED decision.
- Lessons learned if failure occurs.

| Verification step | Required evidence | PASS condition | HOLD/BLOCKED trigger |
|---|---|---|---|
| Source basis | Context pack/source lock | Output matches current source | Stale or missing source |
| Scope | Job card | Output within scope | Out-of-scope change |
| Files/repo | Diff/file evidence | Correct files only | Wrong repo/branch/file |
| Security/data | Data classification/security review | No prohibited data/security risk | Secret/customer-data risk |
| Role/tenant/RLS | RLS/tenant evidence where relevant | Backend-controlled proof exists | Frontend-only security claim |
| Build/lint/test | Test/build logs where relevant | Required checks pass | Failed or missing critical checks |
| Human review | Reviewer record | Reviewer accepts evidence | Review missing or rejects |

## Outputs/records
AI output verification record, PASS/HOLD/BLOCKED decision, evidence links, correction/rework route and lessons learned where needed.

## Linked process
COP-11 Verification, MOP-04 AI governance and tool-use policy, SOP-07 Evidence and record control, SOP-08 Security/data protection, MOP-07 Corrective action/improvement.

## Linked gate
AI output verification gate, evidence gate, build gate, DB/RLS gate, data protection gate, release gate.

## Human approval
Required before any AI output is accepted for implementation, release support, customer-facing content, compliance/audit evidence or protected technical changes.

## Data boundary
AI outputs that include or imply customer, confidential, secret or production data must be verified against AI_DATA_GOVERNANCE before use.

## PASS/HOLD/BLOCKED rules
- PASS: AI output is source-grounded, in scope, evidence-linked, human-reviewed and verification checks pass.
- HOLD: output may be useful but source, evidence, test or approval is incomplete.
- BLOCKED: output is ungrounded, unsafe, out-of-scope, data-risky, role/security-risky or claims PASS without evidence.

## PDCA
- PLAN: define verification checks before AI use.
- DO: verify AI output against required evidence.
- CHECK: review verification results and failures.
- ACT: correct/reject output and update risks, prompts, skills, tool routes and lessons learned.

## Update trigger
Bad AI output, failed verification, release issue, app defect, audit finding, CI finding, tool/model change or lesson learned.
