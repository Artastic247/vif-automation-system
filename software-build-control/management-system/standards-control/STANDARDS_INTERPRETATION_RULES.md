# STANDARDS_INTERPRETATION_RULES

## Purpose
Define who may interpret standards/guidance, what counts as source evidence, how source gaps are marked, and how interpretation disputes are escalated.

## Scope
All standards/guidance interpretation used internally, in app-development controls, audits, app onboarding, release readiness, customer communications and claim control.

## Owner/agent
Compliance Claim Approver with assigned standards specialists.

## Inputs
Standard/guidance lens, source evidence, customer-specific source, app-specific source, interpretation request, affected process, affected claim and risk.

## Activities/method
1. Assign the correct specialist.
2. Confirm source evidence status.
3. Mark SOURCE REQUIRED, CUSTOMER SOURCE REQUIRED or APP SOURCE REQUIRED if evidence is missing.
4. Define permitted internal interpretation.
5. Define prohibited wording and claim restrictions.
6. Escalate interpretation disputes.
7. Link interpretations to audit, RCA/CAPA and management review where risk exists.
8. Record review outcome.

## Outputs/records
Interpretation record, source status, specialist decision, escalation record and claim-control decision.

## Linked processes
Standards control, Clause 4 context, Clause 6 risk planning, Clause 7 documented information, Clause 8 operation, Clause 9 audit, Clause 10 improvement and management review.

## Linked skills/WIs
WI_003_SOURCE_OF_TRUTH_LOCK, WI_007_RISK_OPPORTUNITY_REVIEW, WI_021_INTERNAL_AUDIT, WI_023_RCA, WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE and WI_029_APP_ONBOARDING_READINESS.

## Linked gates
Interpretation gate, source-control gate, claim-control gate, audit gate, RCA/CAPA gate, app onboarding gate and release gate.

## Evidence required
Source evidence, specialist assigned, interpretation decision, allowed wording, prohibited wording, escalation decision and approval status.

## Risks
Wrong interpretation, unsupported source, customer-specific requirement invented, proprietary text copied, customer-facing claim made without approval.

## Controls
Only assigned specialists may interpret. Human approval is required before customer-facing claims. Missing sources must be visibly marked.

## Interfaces
Standards specialists, Compliance Claim Approver, Customer-Specific Requirement Owner, App-Specific Compliance Owner, Process Owner, App Owner, QA Gatekeeper and Management Review Owner.

## Interpretation authority
| Interpretation area | Responsible specialist | Source evidence rule | Escalation |
|---|---|---|---|
| ISO 9001/9002-style management-system logic | ISO 9001/9002 Guidance Specialist | SOURCE REQUIRED unless official/licensed source supplied | Compliance Claim Approver |
| ISO 9004 maturity/sustained-success logic | ISO 9004 Specialist | SOURCE REQUIRED | Compliance Claim Approver |
| IATF-style automotive process discipline | IATF 16949 Specialist | SOURCE REQUIRED; CSR requires CUSTOMER SOURCE REQUIRED | Compliance Claim Approver |
| Information security logic | ISO/IEC 27001 Security Specialist | SOURCE REQUIRED | Security/Data Reviewer + Compliance Claim Approver |
| Risk framework/techniques | ISO 31000/31010 Risk Specialist | SOURCE REQUIRED | QA Gatekeeper |
| AI management logic | ISO/IEC 42001 AI Management Specialist | SOURCE REQUIRED | AI Governance Specialist + Compliance Claim Approver |
| Customer-specific requirements | Customer-Specific Requirement Owner | CUSTOMER SOURCE REQUIRED | App Owner + Compliance Claim Approver |
| App-specific compliance/regulatory requirements | App-Specific Compliance Owner | APP SOURCE REQUIRED | App Owner + Compliance Claim Approver |

## What counts as source evidence
- Official/licensed standard access record where applicable.
- Customer-supplied CSR, contract, portal requirement, manual, specification or written instruction for the specific customer/project.
- App-specific regulatory/compliance source supplied for the specific app/project.
- Approved internal interpretation record that references source status and limits use.

## What must be marked SOURCE REQUIRED
Any standard/guidance lens without official/licensed source evidence available in the project record.

## What must be marked CUSTOMER SOURCE REQUIRED
Any customer-specific requirement not supplied by the relevant customer or authorised project source.

## What must be marked APP SOURCE REQUIRED
Any app-specific legal, regulatory, customer or compliance requirement not supplied for the specific app/project.

## PASS/HOLD/BLOCKED rules
PASS when source status, specialist and allowed interpretation are recorded. HOLD when source is pending. BLOCKED when unsupported wording is used for customer-facing claim, release or app onboarding approval.

## Escalation
Escalate disputes, unsupported claims, missing source, customer-specific ambiguity, app-specific ambiguity or false claim risk.

## MLA / maturity dependency
M3+ interpretation control requires audit evidence. M4/M5 require review trends and effectiveness evidence.

## Update trigger
New source, new interpretation, dispute, audit finding, RCA/CAPA, customer-facing claim request or management-review action.
