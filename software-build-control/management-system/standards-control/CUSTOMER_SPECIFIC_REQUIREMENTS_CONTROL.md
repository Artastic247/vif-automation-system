# CUSTOMER_SPECIFIC_REQUIREMENTS_CONTROL

## Purpose
Control customer-specific requirements and app-specific compliance requirements so they are not invented, mixed between customers or used without source evidence.

## Scope
Customer-specific requirements, customer manuals/specifications/portal requirements, contract requirements, app-specific regulatory/compliance inputs and customer-facing claim impact.

## Owner/agent
Customer-Specific Requirement Owner and App-Specific Compliance Owner with Compliance Claim Approver.

## Inputs
Customer requirement source, customer owner/contact role, app-specific source, requirement classification, affected app/process, affected standards/guidance lens, implementation impact, evidence required, approval required and review frequency.

## Activities/method
1. Identify customer/project/app.
2. Record customer requirement source or APP SOURCE REQUIRED.
3. Record customer owner/contact role without personal email unless supplied for the specific project.
4. Classify requirement.
5. Link affected app/process and standard/guidance lens.
6. Define implementation impact and evidence required.
7. Define approval and review frequency.
8. Define claim-control impact.
9. Prevent cross-customer reuse unless explicitly authorised and revalidated.

## Outputs/records
Customer/app requirement record, source-required status, implementation impact, evidence requirement, approval record and claim-control impact.

## Linked processes
Clause 4 context/interested parties, Clause 6 planning/change, Clause 8 operation/app development, Clause 9 audit and Clause 10 improvement.

## Linked skills/WIs
WI_001_CONTEXT_LOCK, WI_003_SOURCE_OF_TRUTH_LOCK, WI_007_RISK_OPPORTUNITY_REVIEW, WI_021_INTERNAL_AUDIT, WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE and WI_029_APP_ONBOARDING_READINESS.

## Linked gates
Customer source gate, app source gate, requirements gate, app onboarding gate, release gate and claim-control gate.

## Evidence required
Customer/app source, requirement classification, affected process/app, implementation evidence, approval evidence, review date and claim-control decision.

## Risks
Invented customer requirement, wrong customer requirement reused, app-specific requirement assumed, customer-facing claim without source, personal contact data used unnecessarily.

## Controls
Customer-specific requirements require CUSTOMER SOURCE REQUIRED until supplied. App-specific requirements require APP SOURCE REQUIRED until supplied. Customer owner/contact is role-based unless personal details are supplied for the specific project.

## Interfaces
Customer-Specific Requirement Owner, App-Specific Compliance Owner, App Owner, Process Owner, Standards Specialists, Compliance Claim Approver, QA Gatekeeper.

## Requirement control fields
| Field | Required rule |
|---|---|
| Customer/project/app | Must be specific to the project |
| Requirement source | Customer-supplied or CUSTOMER SOURCE REQUIRED / APP SOURCE REQUIRED |
| Customer owner/contact role | Use role, not personal email, unless supplied for the project |
| Requirement classification | CSR, contract, specification, portal, regulatory/app-specific, internal alignment |
| Affected app/process | Must be linked to actual app/process |
| Affected standard/guidance lens | Link only as alignment lens unless source evidence exists |
| Implementation impact | Define design/build/process/evidence impact |
| Evidence required | Define objective evidence required |
| Approval required | Define owner/approver |
| Review frequency | Per customer/app change or scheduled review |
| Source-required status | CUSTOMER SOURCE REQUIRED or APP SOURCE REQUIRED until supplied |
| Claim-control impact | No customer-facing claim without source and approval |

## Requirement-control register template
| Requirement ID | Customer/project/app | Source | Owner/contact role | Classification | Affected app/process | Affected lens | Implementation impact | Evidence required | Approval required | Review frequency | Source status | Claim impact | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CSR-001 | To be assigned | CUSTOMER SOURCE REQUIRED | Role required | To be classified | To be assigned | To be assigned | To be defined | Evidence required | Approval required | Per source/change | CUSTOMER SOURCE REQUIRED | Claim HOLD | OPEN |
| APP-REQ-001 | To be assigned | APP SOURCE REQUIRED | App owner role | App-specific requirement | To be assigned | To be assigned | To be defined | Evidence required | Approval required | Per app/source change | APP SOURCE REQUIRED | Claim HOLD | OPEN |

## PASS/HOLD/BLOCKED rules
PASS when source, affected process, evidence and approval are defined. HOLD while customer/app source is missing. BLOCKED if customer/app requirement is invented, copied from another customer without approval, or used for customer-facing claim without source.

## Escalation
Escalate missing customer source, missing app source, cross-customer reuse risk, false claim risk or unclear requirement ownership.

## MLA / maturity dependency
Maturity cannot progress for customer/app-specific control unless source evidence, implementation evidence and approval evidence exist.

## Update trigger
New customer requirement, app-specific requirement, source change, customer claim request, app onboarding, audit finding or RCA/CAPA.
