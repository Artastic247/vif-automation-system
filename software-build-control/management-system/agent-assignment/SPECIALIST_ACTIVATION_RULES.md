# SPECIALIST_ACTIVATION_RULES

## Purpose
Define when specialists must be activated so the right expertise is used without overloading every job with unnecessary specialists.

## Scope
All management-system and app-development work where risk, technology, customer/regulatory need, data/security impact, maturity, device/integration, tenant/RLS, release impact, audit finding or RCA/CAPA trigger requires specialist review.

## Owner/agent
VIF Orchestrator with QA Gatekeeper and relevant specialist leads.

## Inputs
App type, process stage, risk level, data classification, tenant model, technology stack, customer/regulatory requirement, maturity level, release impact, audit finding and RCA/CAPA trigger.

## Activities/method
Assess activation criteria, appoint specialist only where trigger applies, define scope of review, required evidence, gate impact and escalation route. Do not activate every specialist by default.

## Outputs/records
Specialist activation record, review evidence, gate decision and escalation if specialist is bypassed.

## Linked processes
ADP-01 to ADP-21, Clause 6 risk planning, Clause 8 operation/design, Clause 9 audit and Clause 10 improvement.

## Linked skills/WIs
WI_007, WI_011, WI_012, WI_014, WI_015, WI_016, WI_017, WI_018, WI_019, WI_020, WI_021, WI_022, WI_023, WI_028, WI_029 and WI_030.

## Linked gates
Risk, runtime, UI, backend/RLS, security, release, audit, RCA/CAPA, app onboarding, CI and n8n gates.

## Evidence required
Activation trigger, specialist assigned, review output, evidence reviewed, decision and gate impact.

## Risks
Specialist overload, missing critical specialist, unsupported compliance claim, security/data gap, device/integration failure, premature automation.

## Controls
Specialist activation is triggered by risk and scope. High-risk data/security/release/RLS work cannot bypass required specialist.

## Interfaces
VIF Orchestrator, QA Gatekeeper, specialists, App Owner, Process Owner, builders, auditors and release/support owners.

## Activation rules
| Specialist | Activate when | Evidence output | Gate impact |
|---|---|---|---|
| Runtime Architect | Runtime object, state, workflow or protected action exists | Runtime review | Runtime gate |
| UI/UX Interface Reviewer | New/changed screen, operator view or usability issue | UI review | UI/UAT gate |
| Frontend Coder | UI implementation required | Frontend diff | Build gate |
| Backend Coder | Service/data/backend logic required | Backend diff | Build/backend gate |
| Supabase/RLS Engineer | Schema, RLS, tenant, role or migration change | DB/RLS proof | Backend/RLS gate |
| Security/Data Protection Reviewer | Customer data, secrets, tenant isolation, auth or privacy risk | Security/data review | Security gate |
| Compliance/Standards Specialist | Standards/customer/regulatory interpretation required | Interpretation note | Requirements/claim gate |
| ISO/IATF Specialist | Automotive process discipline, CSR or defect-prevention concern | Discipline review | Process/risk gate |
| AI Governance Specialist | AI tool/output affects decision or data boundary | AI risk review | AI gate |
| Operator/User Tester | Operator/user path, UAT or usability validation required | User test evidence | Validation gate |
| Device/Integration Specialist | Device, API, CSV, external integration or hardware flow involved | Integration review | Integration gate |
| Release Controller | Pilot/release/rollback decision required | Release review | Release gate |
| RCA/CAPA Specialist | NC, repeat failure, false PASS, failed release or ineffective action | RCA/CAPA record | Improvement gate |
| GitHub CI Controller | Control-system/app-repo CI readiness question exists | CI readiness record | CI gate |
| n8n Automation Controller | n8n notification/issue/evidence/route requested | n8n readiness record | n8n gate |

## PASS/HOLD/BLOCKED rules
PASS when required specialist is activated and output exists. HOLD when activation evidence is incomplete. BLOCKED when critical specialist is bypassed for high-risk work.

## Escalation
Escalate specialist bypass, unsupported customer-facing claim, data/security risk, RLS risk, release risk or premature automation.

## MLA / maturity dependency
M1 may request advisory review. M2 requires specialist review for pilot risk. M3+ requires released role evidence. M4/M5 require specialist performance/audit trends.

## Update trigger
New technology, app type, risk, standard/customer requirement, audit finding, RCA/CAPA or maturity change.
