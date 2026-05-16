# AI_USE_POLICY.md

## Purpose
Define controlled, responsible and evidence-based use of AI tools in software design, development, review, verification, release support and continual improvement.

## Scope
Applies to ChatGPT, Codex, Claude/Claude Code, Lovable, Gemini, Copilot, local LLMs, GitHub automation, future n8n flows and any other AI-assisted tool used in the Software Build Control System.

## Owner/tool
AI Governance Owner owns this policy. VIF Orchestrator controls tool routing. QA Gatekeeper controls AI-output evidence. Security/RLS Reviewer controls data, identity and tenant risk.

## Inputs
Context pack, current job card, tool route, prompt approval, data classification, risk register, impact assessment, human-approval matrix, evidence records and lessons learned.

## Activities/fields
### Allowed AI uses
- Architecture review, gap analysis and controlled planning.
- Read-only repo inspection and evidence mapping.
- Bounded code suggestions under approved job card.
- UI/layout planning where screen/data/runtime maps exist.
- Verification support, contradiction review and test-evidence review.
- Documentation drafting under documented-information control.
- Lessons learned, RCA support and process improvement suggestions.

### Prohibited AI uses
- No automatic release.
- No automatic RLS, schema, destructive migration or tenant-impacting change.
- No AI-generated PASS without evidence.
- No uncontrolled app-code changes.
- No use of real customer data in unapproved tools.
- No use of credentials, secrets or production data in AI prompts.
- No invented emails, contacts, customer facts, standards claims or compliance claims.
- No app-wide repair, feature expansion or broad refactor without approved job card.
- No production/customer-facing content without human review.

### Human approval points
Human approval is required before app-code change, schema/RLS change, customer-data use, tenant rollout, release, rollback, compliance claim, customer-facing content, AI automation activation and n8n workflow activation.

### Tool-specific boundaries
Tool-specific AI boundaries are defined in AI_SYSTEM_INVENTORY, TOOL_SPECIFIC_PROMPT_INSTRUCTIONS and TOOL_ROUTING_MATRIX.

### Data boundary
AI tools may only receive data permitted by AI_DATA_GOVERNANCE. Customer, confidential, secret and production data require explicit approval or masking/anonymisation.

## Outputs/records
AI-use decision, approved/rejected AI route, risk/impact record, prompt record, AI traceability record, verification record, lessons learned and tool/provider review.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-05 Tool routing and tool qualification, SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, SOP-08 Security, tenant and data protection control.

## Linked gate
AI governance gate, prompt gate, tool-routing gate, data protection gate, verification gate, release gate, automation-readiness gate.

## Human approval
Mandatory for all high-risk AI-supported outputs, protected changes, customer-data exposure, compliance claims, releases, rollbacks and automation activation.

## Data boundary
No secrets, credentials, production data or real customer data may be sent to AI tools unless explicitly approved and controlled by AI_DATA_GOVERNANCE.

## PASS/HOLD/BLOCKED rules
- PASS: AI use is allowed, tool-routed, data-safe, human-reviewed where required and evidence-linked.
- HOLD: AI use is potentially valid but risk, data, context, approval or evidence is incomplete.
- BLOCKED: AI use requests prohibited actions, unapproved data, automatic release, uncontrolled code/schema/RLS changes, invented facts or AI-only PASS decisions.

## PDCA
- PLAN: define allowed AI use, tool route, data boundary, oversight and evidence requirements.
- DO: use AI only within approved prompt, tool route and job-card scope.
- CHECK: verify AI output against source evidence, tests, security/data rules and human review.
- ACT: update policy, risks, prompts, tool routes, skills, lessons and validation after failures or changes.

## Update trigger
New AI tool, model change, AI failure, audit finding, CI finding, bad output, data incident, credit burn, customer concern, release issue or lesson learned.
