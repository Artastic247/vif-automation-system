# INFORMATION_SECURITY_DATA_AUDIT_CHECKLIST

## Purpose
Audit information security and data-protection controls across the software-build system.

## Scope
Secrets, .env handling, customer data, tenant isolation, RLS, access control, backups, external tools/providers and AI-tool data boundaries.

## Owner/agent
Information Security/Data Auditor with ISO/IEC 27001 Security Specialist.

## Inputs
Security procedures, access records, validator outputs, tenant rules, backup evidence and provider/tool approvals.

## Activities/method
Audit secrets handling, .env exposure risk, customer-data boundary, tenant-data boundary, RLS/role evidence, access control, audit logs, backup/rollback evidence, data classification, external provider access, AI tool data boundary, security-risk treatment and breach/escalation triggers.

## Outputs/records
Security/data audit report, findings, containment trigger and RCA/CAPA linkage.

## Audit criteria
Customer data and secrets must remain protected. SOURCE REQUIRED where formal security evidence is unavailable.

## Evidence required
Access records, backup evidence, validator reports, tenant/RLS proof and incident records.

## MLA / maturity dependency
Production-impacting data use requires higher maturity and audited controls.

## Linked process
Information security and Clause 9 security audit.

## Linked gate
Security/data protection gate.

## PASS/HOLD/BLOCKED rules
PASS when controls and evidence exist. HOLD when evidence is incomplete. BLOCKED when secrets, customer data or tenant isolation are uncontrolled.

## Escalation
Escalate breach risk, exposed secrets, tenant leakage or unsupported access.

## Management-review input
Security trends, incidents and unresolved risks feed management review.

## Update trigger
Security incident, provider change, audit finding, onboarding or release.
