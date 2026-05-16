# APPROVED_CONTACT_REGISTER.md

## Purpose
Register approved real contact values and identity/contact-data use so organisational emails are used intentionally, project-specifically and with evidence.

## Scope
Applies to SNAGG, customer, supplier, user, owner, test/demo and production contact values used in control-system artefacts, prompts, templates, app onboarding records, app source reviews and future automation flows.

## Inputs
Approved project/app, approved purpose, contact value, allowed artefacts, prohibited use, owner, approval evidence, review date and contact status.

## Activities
- Add real contacts only when the project/app and purpose are known.
- Do not create blanket/global approval for organisational emails.
- Mark contacts HOLD when project or approval evidence is incomplete.
- Mark contacts BLOCKED/retired when unsafe, stale or no longer approved.
- Use placeholders where real contact identity is not required.

## Outputs
Controlled contact register and contact-use decision.

## Records
| Contact ID | Email/contact value | Organisation | Approved project/app | Approved purpose | Allowed artefacts | Prohibited use | Owner | Approval evidence | Review date | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| CONTACT-001 | khan.angus@snagg.org | SNAGG | HOLD — project/app not specified in this control-system job card | HOLD — may only be used where specifically approved for a project, role, contact point, user account, test account or owner field | HOLD — no blanket/global artefact approval | Role/security logic, frontend access logic, tenant logic, generic generated templates, production truth without project approval | VIF Orchestrator / project owner | HOLD — project-specific approval required before active use | TBD | HOLD |
| CONTACT-PLACEHOLDER-001 | `<project-owner-email>` | Placeholder | Any controlled project where a real contact is not approved | Placeholder only | Templates, examples, prompts, drafts | Production identity, auth, role/security logic | Prompt Quality Reviewer | Placeholder rule | On use | Approved placeholder |
| CONTACT-PLACEHOLDER-002 | `owner@example.com` | Placeholder | Any controlled project where an example is needed | Example only | Training/examples/non-production drafts | Production identity, auth, role/security logic | Prompt Quality Reviewer | Placeholder rule | On use | Approved placeholder |

## Owner/tool
VIF Orchestrator owns contact approval routing. Security/RLS Reviewer owns identity/security risk. Prompt Quality Reviewer owns template/prompt placeholders. QA Gatekeeper reviews validation findings.

## Linked process
SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, SOP-08 Security, tenant and data protection control, COP-08 Environment and tenant setup.

## Linked gate
Identity/contact-data gate, prompt gate, data protection gate, evidence gate.

## PDCA
- PLAN: define contact approval need, project/app, purpose, allowed artefacts and prohibited use.
- DO: register contact value or use placeholder.
- CHECK: scan for uncontrolled emails and validate against this register.
- ACT: approve, hold, retire, block or replace contact values and update lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: contact is approved for a specific project/purpose or is a controlled placeholder.
- HOLD: real contact exists but project-specific approval or review evidence is incomplete.
- BLOCKED: contact is used for role/security/access/auth/tenant/admin logic or uncontrolled production identity.

## Update trigger
New project contact, SNAGG email request, generated output containing an email, app onboarding, app scan, audit finding, validation finding, contact change, or lesson learned.
