# AI_DATA_GOVERNANCE.md

## Purpose
Define data-governance rules for AI tool use so prompts, outputs, reviews and automation do not expose customer data, confidential information, credentials, secrets, production data or uncontrolled identity/contact data.

## Scope
Applies to all AI-assisted work using ChatGPT, Codex, Claude/Claude Code, Lovable, Gemini, Copilot, local LLMs, GitHub automation, future n8n flows and future AI-connected services.

## Owner/tool
Security/RLS Reviewer owns data governance. AI Governance Owner owns AI-use alignment. VIF Orchestrator controls routing. QA Gatekeeper verifies evidence.

## Inputs
Data classification, project approval, context pack, prompt, tool route, impact assessment, customer-data approval, masking/anonymisation evidence and exception approval.

## Activities/fields
| Data class | Meaning | AI tool use rule | Evidence required |
|---|---|---|---|
| Public data | Publicly available non-sensitive information | Allowed if source-cited where relevant | Source/context record |
| Internal data | Non-public internal control-system data | Allowed in approved tools with context controls | Job card/context pack |
| Confidential data | Sensitive business, IP, client or regulated data | HOLD unless approved and minimised | Approval and masking decision |
| Customer data | Data belonging to customer or customer tenant | BLOCKED unless specific project approval and masking/anonymisation exists | Customer/project approval and data rule |
| Credentials/secrets | Passwords, tokens, API keys, env files, service-role keys | BLOCKED | Must not be sent to AI |
| Production data | Live operational/customer data | BLOCKED unless formally approved exception | Exception approval and masking |
| Demo/synthetic data | Non-real seeded/demo data | Allowed when clearly synthetic and not copied from customer data | Seed/demo evidence |
| Identity/contact data | Real emails/names/contact values | Use only if approved in contact register | APPROVED_CONTACT_REGISTER |

## Masking/anonymisation rules
- Replace real names, emails, company identifiers, tenant IDs, tokens and sensitive values with placeholders unless approved.
- Use synthetic examples where possible.
- Do not paste `.env`, API keys, Supabase service-role keys, production exports or customer records into AI tools.
- Record approval evidence for exceptions.

## Prohibited data use
No AI prompt may include credentials, secrets, unapproved customer data, production data, uncontrolled SNAGG/customer emails, or confidential data beyond the approved minimum necessary.

## Outputs/records
Data classification decision, AI-use approval, masking/anonymisation evidence, exception record and verification finding.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-08 Security, tenant and data protection control, SOP-06 Prompt control, SOP-07 Evidence and record control, COP-08 Environment and tenant setup.

## Linked gate
Data protection gate, prompt gate, identity/contact-data gate, AI governance gate, tenant gate, evidence gate.

## Human approval
Required for confidential, customer, production or identity/contact data exceptions.

## Data boundary
Credentials/secrets are always blocked. Customer and production data are blocked unless explicitly approved and masked/anonymised where appropriate.

## PASS/HOLD/BLOCKED rules
- PASS: data class is allowed, minimised, approved where needed and evidence is recorded.
- HOLD: data class or approval is unclear.
- BLOCKED: credentials, secrets, unapproved customer data, production data or uncontrolled identity/contact data are present.

## PDCA
- PLAN: classify data and define approved AI route before use.
- DO: use only allowed/masked/minimised data.
- CHECK: scan/review prompts and outputs for prohibited data.
- ACT: contain exposure, update controls and lessons learned after findings.

## Update trigger
New data class, customer-data request, identity/contact finding, tool change, prompt failure, security incident, audit finding or lesson learned.
