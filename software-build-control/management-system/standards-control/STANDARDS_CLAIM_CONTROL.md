# STANDARDS_CLAIM_CONTROL

## Purpose
Control internal and customer-facing wording so the Software Build Management System does not make unsupported compliance, certification-readiness, customer-specific or app-specific claims.

## Scope
All internal reports, app onboarding records, release packs, proposals, customer-facing statements, audit outputs, README/MANIFEST wording, job cards and automation outputs that reference standards, compliance, certification, customer requirements or regulatory requirements.

## Owner/agent
Compliance Claim Approver with QA Gatekeeper.

## Inputs
Claim request, intended audience, source evidence, customer source evidence, app source evidence, standards crosswalk, specialist interpretation, implementation evidence, audit evidence and approval request.

## Activities/method
1. Classify wording as internal alignment, internal status, customer-facing claim or prohibited claim.
2. Confirm source evidence and implementation evidence.
3. Confirm specialist interpretation where needed.
4. Confirm customer-specific and app-specific source status.
5. Approve, revise, hold or reject wording.
6. Record claim decision.
7. Withdraw or correct unsupported claims.
8. Trigger NC/RCA/CAPA for false or unsupported claims.
9. Feed significant claim risk to management review.

## Outputs/records
Claim review record, approved wording, rejected wording, withdrawal/correction record, NC/RCA/CAPA trigger and management-review input.

## Linked processes
Standards control, Clause 4 context, Clause 5 authority, Clause 7 documented information, Clause 8 operation/release, Clause 9 audit and Clause 10 NC/RCA/CAPA.

## Linked skills/WIs
WI_001_CONTEXT_LOCK, WI_003_SOURCE_OF_TRUTH_LOCK, WI_021_INTERNAL_AUDIT, WI_023_RCA, WI_024_CAPA_EFFECTIVENESS_REVIEW, WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE and WI_029_APP_ONBOARDING_READINESS.

## Linked gates
Claim-control gate, standards source gate, app onboarding gate, release gate, management-review gate and NC/RCA/CAPA gate.

## Evidence required
Claim text, source evidence, implementation evidence, specialist review, approval decision, review date, withdrawal/correction evidence where applicable.

## Risks
Unsupported compliance claim, certification-readiness claim, copied proprietary text, customer-specific requirement invented, app-specific requirement assumed, crosswalk used as implementation proof.

## Controls
Human approval is required before customer-facing compliance wording. Crosswalk evidence does not equal implementation evidence. Source-required items cannot support a claim.

## Interfaces
Compliance Claim Approver, App Owner, Customer-Specific Requirement Owner, App-Specific Compliance Owner, Standards Specialists, QA Gatekeeper, Management Review Owner.

## Allowed internal wording
- “Aligned as an internal management-system lens where source status is controlled.”
- “SOURCE REQUIRED pending official/licensed source evidence.”
- “CUSTOMER SOURCE REQUIRED pending customer-supplied requirement.”
- “APP SOURCE REQUIRED pending app-specific source evidence.”
- “Structural control present; validation/use evidence pending.”

## Prohibited wording
- “Certified.”
- “Certification ready.”
- “Compliant with ISO/IATF/IEC standard.”
- “Meets all requirements.”
- “Customer-specific requirements satisfied” unless customer source and implementation evidence are approved.
- “App regulatory requirements satisfied” unless app source and implementation evidence are approved.
- Any copied proprietary standard text, tables, thresholds, examples or handbook text.

## Customer-facing claim approval
Customer-facing claims require:
1. Defined claim text.
2. Source evidence.
3. Implementation evidence.
4. Specialist review.
5. Compliance Claim Approver approval.
6. App Owner approval where app/customer-facing.
7. Record in claim review register.

## Claim withdrawal/correction route
If an unsupported claim is detected:
1. Stop reuse of the claim.
2. Record claim finding.
3. Notify responsible owner.
4. Correct or withdraw wording.
5. Open NC/RCA/CAPA if customer-facing, repeated or high risk.
6. Update standards-control/knowledge records.
7. Feed significant issue to management review.

## App onboarding impact
App onboarding remains HOLD if customer/app requirements are source-required, claim-control evidence is missing, or wording implies readiness/compliance without evidence.

## Release impact
Release remains HOLD/BLOCKED if release wording claims compliance/certification/customer requirement fulfilment without source and implementation evidence.

## PASS/HOLD/BLOCKED rules
PASS when claim wording is approved with evidence. HOLD when source or implementation evidence is incomplete. BLOCKED when unsupported customer-facing compliance/certification claim is made or protected scope is touched.

## Escalation
Escalate unsupported claim, certification-readiness wording, customer-specific ambiguity, app-specific ambiguity, copied proprietary content or repeated claim failure.

## MLA / maturity dependency
M3+ claim-control maturity requires audit evidence. M4/M5 require trend monitoring and effective correction of false-claim risks.

## Update trigger
Claim request, proposal/release wording, standards/source change, customer requirement, app requirement, audit finding, RCA/CAPA or management review.
