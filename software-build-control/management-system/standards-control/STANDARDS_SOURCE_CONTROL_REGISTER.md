# STANDARDS_SOURCE_CONTROL_REGISTER

## Purpose
Record source status, ownership, allowed use, prohibited use and gap status for all standards, guidance lenses, customer-specific requirements and app-specific compliance requirements.

## Scope
All standards/guidance references used by the Software Build Management System and app-development operating model.

## Owner/agent
Compliance Claim Approver owns this register. Each standards specialist owns their assigned source entries.

## Inputs
Standard/guidance name, official/licensed source status, customer source evidence, app-specific source evidence, owner, linked process, linked specialist, intended use and gap status.

## Activities/method
1. Register each standards/guidance lens.
2. Record source status: available, SOURCE REQUIRED, CUSTOMER SOURCE REQUIRED or APP SOURCE REQUIRED.
3. Assign source owner and linked specialist.
4. Define allowed use and prohibited use.
5. Link process and gate impact.
6. Define review date and gap status.
7. Escalate unsupported claims or missing source evidence.

## Outputs/records
Standards source register, source-required list, customer-source-required list, app-source-required list and claim-control input.

## Linked processes
Clause 4 to Clause 10, app-development operating model, standards-control, audit, RCA/CAPA, app onboarding and release control.

## Linked skills/WIs
WI_003_SOURCE_OF_TRUTH_LOCK, WI_007_RISK_OPPORTUNITY_REVIEW, WI_021_INTERNAL_AUDIT, WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE and WI_029_APP_ONBOARDING_READINESS.

## Linked gates
Source-control gate, standards applicability gate, customer-facing claim gate, app onboarding gate, release gate and management-review gate.

## Evidence required
Source status, source owner, allowed/prohibited use, specialist, linked process, gap status and review date.

## Risks
Source evidence missing, unsupported interpretation, customer requirement invented, app requirement assumed, customer-facing claim made without approval.

## Controls
If source is missing, mark SOURCE REQUIRED, CUSTOMER SOURCE REQUIRED or APP SOURCE REQUIRED. No source-required item may support a customer-facing compliance claim.

## Interfaces
Standards specialists, Customer-Specific Requirement Owner, App-Specific Compliance Owner, Compliance Claim Approver, QA Gatekeeper, App Owner and Process Owner.

## Source-control register
| Standard/guidance name | Source status | Source owner | Allowed use | Prohibited use | Review date | Linked process | Linked specialist | Gap status |
|---|---|---|---|---|---|---|---|---|
| ISO 9001-style clause 4-10 management-system structure | SOURCE REQUIRED | ISO 9001/9002 Guidance Specialist | Internal alignment lens for context, leadership, planning, support, operation, performance and improvement | Claiming ISO 9001 compliance/certification readiness | TBD | Clause 4-10 architecture | ISO 9001/9002 Guidance Specialist | Open source-required control |
| ISO/TS 9002 guidance logic | SOURCE REQUIRED | ISO 9001/9002 Guidance Specialist | Practical implementation guidance lens | Copying guidance text or implying added requirements | TBD | Procedure/WI clarity | ISO 9001/9002 Guidance Specialist | Open source-required control |
| ISO 9004 maturity and sustained-success logic | SOURCE REQUIRED | ISO 9004 Specialist | Maturity/self-assessment/sustained improvement lens | Claiming ISO 9004 compliance/certification | TBD | MLA and management review | ISO 9004 Maturity/Sustained Success Specialist | Open source-required control |
| IATF 16949-style automotive process discipline | SOURCE REQUIRED | IATF 16949 Specialist | Automotive process discipline, defect-prevention and change-control lens | Claiming IATF compliance/certification readiness or inventing CSR | TBD | Process discipline/change/evidence | IATF 16949 Process Discipline Specialist | Open source-required control |
| ISO/IEC 27001 information-security management-system logic | SOURCE REQUIRED | ISO/IEC 27001 Security Specialist | Security risk/access/customer data/tenant isolation lens | Claiming ISO 27001 compliance/certification readiness | TBD | Security/data control | ISO/IEC 27001 Security Specialist | Open source-required control |
| ISO 31000 risk-management framework logic | SOURCE REQUIRED | ISO 31000/31010 Risk Specialist | Risk framework lens | Claiming formal compliance | TBD | Risk planning | ISO 31000/31010 Risk Specialist | Open source-required control |
| ISO 31010 risk-assessment technique logic | SOURCE REQUIRED | ISO 31000/31010 Risk Specialist | Technique-selection lens for risk assessment | Copying proprietary technique tables or claiming formal compliance | TBD | Risk analysis/evaluation | ISO 31000/31010 Risk Specialist | Open source-required control |
| ISO/IEC 42001 AI management-system logic | SOURCE REQUIRED | ISO/IEC 42001 AI Management Specialist | AI governance, oversight, lifecycle, output verification lens | Claiming ISO/IEC 42001 compliance/certification readiness | TBD | AI/tool governance | ISO/IEC 42001 AI Management Specialist | Open source-required control |
| Customer-specific requirements | CUSTOMER SOURCE REQUIRED | Customer-Specific Requirement Owner | Apply only when supplied by customer or authorised project source | Inventing CSR or applying one customer requirement to another customer | Per project | App/process/customer requirement control | Customer-Specific Requirement Owner | Customer source required |
| App-specific regulatory/compliance requirements | APP SOURCE REQUIRED | App-Specific Compliance Owner | Apply only when supplied for the specific app/product/project | Assuming requirements from another app/sector | Per app | App onboarding/release | App-Specific Compliance Owner | App source required |

## PASS/HOLD/BLOCKED rules
PASS when source status and use boundaries are defined. HOLD while source-required gaps remain. BLOCKED if unsupported source is used for customer-facing claim, app onboarding approval or release claim.

## Escalation
Escalate source dispute, missing customer source, missing app source, unsupported wording or false claim risk.

## MLA / maturity dependency
Maturity cannot advance to M3+ claim-control use unless source tracking, specialist ownership and audit evidence exist.

## Update trigger
New standard/guidance lens, source update, customer source receipt, app requirement receipt, audit finding, RCA/CAPA or claim request.
