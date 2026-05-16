# Software Build Control System

Purpose: prevent context drift, truncation, uncontrolled scope, false PASS decisions, unsafe tenant rollout, uncontrolled identity/contact-data use, uncontrolled AI use, and unverified AI-assisted software changes.

This package is foundation/control-system only. It does not authorise app-code changes, Supabase changes, RLS changes, deployments, n8n flows, customer-data access, auto-fixes, auto-merges, CI activation, or releases.

## Process-led management-system structure

The system is process-led, not document-led. Documents, scripts, prompts, workers, skills and templates are controlled resources/records of processes.

Process architecture is defined through:

- MOP — management-oriented processes
- COP — core operational app-development processes
- SOP — support-oriented processes
- process register
- process interaction map
- explicit PDCA per process
- turtle diagram template
- owner matrix
- KPI register
- risk/control register
- records matrix
- gate matrix

## Prompt and context-control structure

Prompt engineering is treated as a managed process, not a loose prompt template. The prompt/context-control layer includes source basis, context pack, current job card, tool routing, forbidden prompt patterns, secret/customer-data boundaries, verification, rollback, stop conditions, and prompt-to-job-card linkage.

## Identity and contact-data control

Real emails and contact identities are controlled by:

- IDENTITY_CONTACT_DATA_CONTROL
- APPROVED_CONTACT_REGISTER
- check_identity_contact_data.py

Rules:

- SNAGG emails must not be inserted generically.
- `khan.angus@snagg.org` is not globally approved and may only be used for project-specific approved purposes.
- Other SNAGG emails require explicit direction and register approval.
- Placeholders must be used for examples where real contact data is not approved.
- No email address may be used as role, permission, admin, tenant, auth, access or security decision logic.

## AI management-system controls

AI use is controlled through:

- AI_USE_POLICY
- AI_SYSTEM_INVENTORY
- AI_RISK_REGISTER
- AI_IMPACT_ASSESSMENT
- AI_OUTPUT_VERIFICATION_PROCEDURE
- HUMAN_OVERSIGHT_MATRIX
- AI_DATA_GOVERNANCE
- AI_TOOL_PROVIDER_REVIEW
- AI_LIFECYCLE_CONTROL
- AI_BAD_OUTPUT_MONITORING_REGISTER
- AI_MODEL_TOOL_CHANGE_CONTROL
- AI_CREDIT_BURN_REGISTER
- AI_TRACEABILITY_REGISTER
- check_ai_management.py

Rules:

- No automatic release.
- No automatic RLS/schema/destructive migration changes.
- No AI-generated PASS without evidence.
- No uncontrolled app-code changes.
- No real customer data in unapproved AI tools.
- No credentials, secrets or production data in AI prompts.
- No invented emails, customer facts, standards claims or compliance claims.
- Human approval is required for protected decisions and actions.

## App-development control coverage

The management-system layer covers:

- app intake
- context lock and source-of-truth lock
- requirements and acceptance criteria
- UI/interface design control
- data table/grid definition
- workflow/runtime mapping
- database/backend/RLS setup control
- environment and tenant strategy
- risk and contingency planning
- gate checklists
- agents/workers
- controlled skills/methods
- process knowledge reuse
- prompt engineering and context control
- identity/contact-data control
- AI management-system controls
- verification and validation/UAT
- tenant rollout and release
- rollback
- support/maintenance
- problem solving and lessons learned
- automation readiness

## Local validation

```bash
python scripts/validate_control_pack.py --root . --mode control-pack
```

## Gate language

- PASS: sufficient evidence to proceed.
- HOLD: evidence missing or incomplete.
- BLOCKED: unsafe to proceed.

## Current automation boundary

Automation may inspect files and write reports under `reports/`. It must not edit source files, call external services, deploy, merge, release, access customer data, modify Supabase/RLS, activate CI, or implement n8n without an approved job card.
