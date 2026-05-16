# WI_020_MOCK_DEMO_DATA_BOUNDARY

## Purpose
Separate mock UI data, seeded demo tenant data and real production/customer data so evidence and privacy boundaries are not mixed.

## Scope
All demo apps, app previews, seeded tenants, mock data, test data, UAT data and customer/production data.

## When to use
Use during design preview, demo setup, UAT preparation, evidence review, tenant onboarding, app repair and release validation.

## When not to use
Do not use to authorise customer data in unapproved tools or to treat demo/mock data as production PASS evidence.

## Owner/agent
Security/Data Protection Reviewer with QA Gatekeeper and Product/App Owner.

## Inputs
Data source, tenant type, mock/demo labels, seed records, evidence claim, tool route, privacy boundary, production/customer data status and approval record.

## Method steps
1. Identify data type: mock UI/design-preview, seeded demo tenant, test/UAT, or real production/customer.
2. Label demo and mock data clearly.
3. Confirm seeded demo tenant records are identified.
4. Check evidence claim type.
5. Confirm mock/demo data is not used as production PASS evidence.
6. Confirm customer data is not used in unapproved tools.
7. Check tenant boundary.
8. Escalate mixing or privacy risk.
9. Record gate decision.

## Outputs/records
Data-boundary decision, demo/mock label record, tenant data note, evidence-use decision and escalation if mixed.

## Evidence required
Data source record, tenant label, seed evidence, evidence claim, approval record and privacy/tool boundary confirmation.

## Linked ADP processes
ADP-02, ADP-04, ADP-07, ADP-09, ADP-15, ADP-16, ADP-17, ADP-18 and ADP-20.

## Linked MOP/COP/SOP processes
Clause 7 information control, Clause 8 operation, Clause 9 security/data audit and Clause 10 NC/RCA/CAPA.

## Linked gates
Context gate, data/security gate, evidence gate, validation/UAT gate and release gate.

## Tools allowed
Mock data in design previews, labelled demo tenants, controlled test data, approved UAT records.

## Tools prohibited
Customer data in unapproved AI/tools, unlabelled demo data, mock/demo evidence as production PASS, mixed demo/production truth.

## Risks
Privacy breach, false PASS, demo truth confused with production, tenant mixing, unsupported customer-data handling.

## Controls
Demo data must be labelled. Mock/demo data cannot be production PASS evidence. Customer data needs approved boundary.

## Interfaces
Product/App Owner, Security/Data Reviewer, Tenant Owner, QA Gatekeeper, UAT Coordinator, Evidence Auditor.

## PASS/HOLD/BLOCKED rules
PASS when data type, label and evidence use are clear. HOLD when labelling is incomplete but no customer risk exists. BLOCKED when customer data risk, tenant mixing or false production evidence exists.

## Escalation
Escalate customer-data exposure, tenant mixing, unlabelled demo data or mock/demo PASS claim.

## MLA / maturity dependency
M1 allows labelled mock. M2 allows controlled demo/UAT. M3 requires released data-boundary records. M4/M5 require monitoring and audit trends.

## Update trigger
New demo tenant, UAT, data import, evidence review, app onboarding, audit finding or security incident.
