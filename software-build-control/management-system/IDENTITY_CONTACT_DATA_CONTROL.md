# IDENTITY_CONTACT_DATA_CONTROL.md

## Purpose
Control the use of organisational identities, contact details and email addresses so generated documents, prompts, templates and app-development artefacts do not accidentally insert, approve, hardcode or misuse real people, company emails, SNAGG domains or production identity values.

## Scope
Applies to the Software Build Control System, prompts, templates, job cards, registers, validation scripts, examples, app onboarding packs, app source reviews, test/demo data guidance, customer-facing artefacts and future automation flows. It applies to SNAGG, customer, supplier, user, owner, test and demo contact data.

## Approved identity/contact-data use
- Approved project contact in an APPROVED_CONTACT_REGISTER row with status Approved.
- Named owner/responsible person only where the project, purpose, artefact and approval evidence are recorded.
- Test/demo account only where clearly marked as non-production and not a real company identity unless approved.
- Placeholder/example contact only when clearly non-real, such as `owner@example.com`, `user@example.test`, `<approved-contact@example.com>` or `<project-owner-email>`.

## Prohibited identity/contact-data use
- Do not invent company emails.
- Do not insert SNAGG emails generically.
- Do not insert customer, supplier or user emails without project approval.
- Do not use email addresses as frontend role, permission, admin, super_admin, tenant, auth, access or security logic.
- Do not treat any email address as production truth without project approval.
- Do not use real customer data for test/demo examples unless explicitly approved and controlled.
- Do not use real emails in prompts where a placeholder is sufficient.

## Project-specific contact approval rule
Every real email/contact value must be tied to a specific project/app, approved purpose, allowed artefacts, owner, approval evidence, review date and status. No contact has blanket/global approval unless explicitly approved by the system owner and recorded.

## SNAGG email usage rule
SNAGG emails must not be inserted generically. Other SNAGG emails must only be added where explicitly directed and registered for the specific project/app and purpose.

## khan.angus@snagg.org usage rule
`khan.angus@snagg.org` may only be used where specifically approved for a specific project, role, contact point, user account, test account or owner field. It is not globally approved. If the project/app and purpose are unknown, the contact status must remain HOLD and the value must not be used in generated artefacts or app logic.

## Test/demo email rule
Use placeholders for examples unless a specific test/demo account is approved. Preferred placeholder domains are `example.com`, `example.org`, `example.net`, `example.test` or explicit angle-bracket placeholders. Test/demo emails must not be used as production users, real owners or security logic.

## Production email rule
Production email/contact values require project approval, evidence and review. They must be recorded in APPROVED_CONTACT_REGISTER before use and must be removed or replaced if approval expires or the project context changes.

## Role/security logic rule
No email address may be used as role, permission, admin, super_admin, auth, tenant, access, owner, or security logic in frontend or backend code. Role/security logic must use controlled role/permission models, tenant membership, claims, RLS, policy tables or approved backend authorisation mechanisms.

## Prompt/template/email boundary
Prompts and templates must not invent or inject real company emails. Use placeholders unless the contact register confirms a project-specific approved contact. Prompt outputs containing real emails must be reviewed before use.

## Evidence required
- Contact register entry.
- Approved project/app and approved purpose.
- Allowed artefacts and prohibited use.
- Owner and approval evidence.
- Review date and status.
- Evidence that the email is not used for role/security logic.

## Owner/tool
Security/RLS Reviewer owns identity/security risk. VIF Orchestrator controls project-specific approval. Prompt Quality Reviewer controls prompt/template use. QA Gatekeeper checks validation findings.

## Linked processes
SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, SOP-08 Security, tenant and data protection control, SOP-09 Configuration and version control, COP-08 Environment and tenant setup, COP-10 Build/modification control, MOP-04 AI governance and tool-use policy.

## Linked gates
Identity/contact-data gate, prompt gate, data protection gate, security gate, evidence gate, build gate, tenant gate and release gate.

## PDCA
- PLAN: define approved contacts, placeholders, project-specific purpose, allowed artefacts and prohibited uses.
- DO: use only approved or placeholder contact values in prompts, templates, records and app artefacts.
- CHECK: scan files for email-like patterns, SNAGG domains, unknown real emails and email-based role/security logic.
- ACT: remove or replace uncontrolled emails, update contact register, update prompt/template controls, log failures and update lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: all contact/email occurrences are approved, placeholders or controlled policy/register references and not used as role/security logic.
- HOLD: SNAGG emails or real emails exist but require project-specific approval, classification or replacement before use.
- BLOCKED: any email is used in role/security/access/auth/tenant/admin logic, app access logic or uncontrolled production identity logic.

## Update trigger
New email/contact value, SNAGG identity request, project onboarding, generated template output, prompt failure, app scan finding, customer-data concern, audit finding, validation finding, or lesson learned.
