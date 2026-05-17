# STANDARDS_SPECIALIST_ASSIGNMENT_MATRIX

## Purpose
Assign specialist ownership for standards/guidance lenses, customer-specific requirements, app-specific requirements and compliance-claim approval.

## Scope
All standards-control activities used in the Software Build Management System, app-development operating model, audit model, app onboarding, release decisions and customer-facing claim control.

## Owner/agent
Compliance Claim Approver owns the matrix. QA Gatekeeper verifies gate alignment.

## Inputs
Standards source-control register, crosswalk matrix, interpretation rules, agent assignment matrix, audit requirements, customer/app source status and claim-control needs.

## Activities/method
1. Assign a responsible specialist for each standards/guidance lens.
2. Define allowed work and prohibited work.
3. Define evidence output.
4. Define gate authority and escalation route.
5. Confirm source-required status.
6. Confirm customer-facing claims require Compliance Claim Approver.

## Outputs/records
Specialist assignment matrix, interpretation ownership, claim-approval ownership and escalation route.

## Linked processes
Standards control, Clause 4-10 process architecture, app-development operating model, audit, RCA/CAPA, management review and app onboarding.

## Linked skills/WIs
WI_003_SOURCE_OF_TRUTH_LOCK, WI_007_RISK_OPPORTUNITY_REVIEW, WI_021_INTERNAL_AUDIT, WI_022_MLA_ASSESSMENT, WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE and WI_029_APP_ONBOARDING_READINESS.

## Linked gates
Standards applicability gate, source-control gate, interpretation gate, claim-control gate, app onboarding gate and release gate.

## Evidence required
Assigned specialist, allowed/prohibited work, source status, evidence output, gate authority and escalation route.

## Risks
Wrong specialist, unsupported interpretation, invented customer requirement, unsupported customer-facing claim, standard copied or misused.

## Controls
Each standards/guidance lens has a named owner. No customer-facing compliance/certification claim may be made without Compliance Claim Approver and source evidence.

## Interfaces
Standards specialists, App Owner, Customer-Specific Requirement Owner, App-Specific Compliance Owner, QA Gatekeeper, Internal Audit Specialist and Management Review Owner.

## Specialist assignment matrix
| Specialist / owner | Assigned lens/control | Allowed work | Prohibited work | Evidence output | Gate authority | Escalation |
|---|---|---|---|---|---|---|
| ISO 9001/9002 Guidance Specialist | ISO 9001-style clause 4-10 structure and ISO/TS 9002 guidance logic | Internal alignment guidance, process/procedure clarity review | Claiming ISO 9001 compliance/certification readiness; copying standard/guidance text | Guidance interpretation note with SOURCE REQUIRED where missing | Interpretation input only | Compliance Claim Approver |
| ISO 9004 Maturity/Sustained Success Specialist | ISO 9004 maturity and sustained-success logic | Maturity/self-assessment alignment lens | Claiming ISO 9004 compliance/certification | Maturity guidance note | MLA input only | MLA Assessor / Compliance Claim Approver |
| IATF 16949 Process Discipline Specialist | Automotive process discipline, defect prevention, change control, evidence discipline | Process discipline and automotive-style control advice | Claiming IATF compliance/certification readiness; inventing CSR | Process-discipline note with SOURCE REQUIRED / CUSTOMER SOURCE REQUIRED | Process/risk input only | Compliance Claim Approver |
| ISO/IEC 27001 Security Specialist | Information-security management-system logic | Security, access, tenant/data, supplier security alignment | Claiming ISO/IEC 27001 compliance/certification readiness | Security interpretation note | Security gate input | Security/Data Reviewer / Compliance Claim Approver |
| ISO 31000/31010 Risk Specialist | Risk framework and risk-assessment technique logic | Risk criteria, treatment and technique-selection support | Claiming formal compliance or copying proprietary technique tables | Risk guidance note | Risk gate input | QA Gatekeeper |
| ISO/IEC 42001 AI Management Specialist | AI governance, AI risk, human oversight, AI lifecycle and tool/model control | AI governance alignment | Claiming ISO/IEC 42001 compliance/certification readiness | AI-management guidance note | AI/tool gate input | AI Governance Specialist / Compliance Claim Approver |
| Customer-Specific Requirement Owner | Customer-specific requirements | Control customer-supplied requirements for the specific customer/project | Inventing CSR; applying one customer’s requirement to another | Customer requirement record | Customer requirement input only | App Owner / Compliance Claim Approver |
| App-Specific Compliance Owner | App-specific regulatory/compliance requirements | Control app-specific source requirements | Assuming requirements from another app/sector | App requirement record | App onboarding/release input | App Owner / Compliance Claim Approver |
| Compliance Claim Approver | Customer-facing claim approval | Approve/reject customer-facing wording with evidence | Approve unsupported claim or certification-readiness claim | Claim approval/rejection record | Final claim-control authority | Management Review Owner / QA Gatekeeper |

## PASS/HOLD/BLOCKED rules
PASS when all required specialists are assigned and boundaries are defined. HOLD while source-required or review evidence is pending. BLOCKED when a claim or interpretation is made without authorised specialist/source control.

## Escalation
Escalate unsupported claim, missing source, customer requirement ambiguity, app requirement ambiguity, interpretation dispute or specialist bypass.

## MLA / maturity dependency
Maturity can progress only when specialist ownership and source control are evidenced. M4/M5 require audit and effectiveness evidence.

## Update trigger
New standard/guidance lens, specialist change, customer/app requirement, claim request, audit finding or RCA/CAPA.
