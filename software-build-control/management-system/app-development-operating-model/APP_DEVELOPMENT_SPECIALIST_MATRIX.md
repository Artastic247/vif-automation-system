# APP_DEVELOPMENT_SPECIALIST_MATRIX

## Purpose
Define when specialists are activated during app development without activating every specialist by default.

## Scope
Specialist activation for ADP-01 to ADP-21 based on app type, risk, technology, customer/regulatory need, data/security impact, process stage, maturity, device/integration need and tenant/RLS impact.

## Owner/agent
VIF Orchestrator with QA Gatekeeper.

## Inputs
App type, risk review, technology stack, data classification, tenant model, customer requirements, maturity level and process stage.

## Activities/method
Activate specialists only when trigger criteria are met. Record trigger, specialist, scope, evidence expected and gate impact.

## Outputs/records
Specialist activation decision and review evidence.

## Linked process
ADP-03 to ADP-21.

## Linked skills/WIs
Risk review, UI review, runtime-first review, DB/RLS proof, security review, integration review, release/rollback review, RCA/CAPA.

## Linked gates
Domain, runtime, UI, backend, security, release, improvement and onboarding gates.

## Evidence required
Activation reason, specialist output and gate decision.

## Risks
Overloading every job with specialists, missing critical expertise, false compliance claim, data/security miss.

## Controls
Specialist activation is risk- and stage-based; no customer-facing compliance claim without approval and source evidence.

## Interfaces
Specialists interface with primary ADP workstation and QA Gatekeeper.

## Specialist activation matrix
| Specialist | Activation trigger | Typical ADP stage | Required output | Gate impact | Maturity dependency |
|---|---|---|---|---|---|
| Runtime Architect | New module, workflow, state, protected action | ADP-06 | Runtime map | Runtime gate | M2+ for build |
| UI/UX Specialist | New screen, operator workflow, responsive concern | ADP-07/14 | UI/interface review | UI gate | M1+ |
| Frontend Coder | UI implementation required | ADP-11 | Frontend diff | Build gate | M2+ |
| Backend Coder | Service/data logic required | ADP-08/11 | Backend diff | Backend gate | M2+ |
| Supabase/RLS Engineer | Tables, RLS, tenant/role logic, migration | ADP-08/13 | RLS/backend proof | Backend/RLS gate | M2+ |
| Security/Data Protection Specialist | Customer data, secrets, auth, tenant risk | ADP-09/13 | Security review | Security gate | M2+ |
| Compliance Specialist | Regulated/customer requirement | ADP-03/05/09 | Compliance lens note | Requirements/risk gate | SOURCE REQUIRED |
| ISO/IATF Specialist | Automotive/process/customer-specific discipline | ADP-03/05/09 | Process discipline review | Domain/risk gate | CUSTOMER SOURCE REQUIRED if CSR |
| AI Governance Specialist | AI use, AI output, AI tool/provider | ADP-09/10/16 | AI risk/oversight review | AI gate | M1+ |
| Operator/User Tester | Operator-facing flow or UAT | ADP-04/14/17 | User test evidence | Validation gate | M1+ |
| Device/Integration Specialist | Device, API, CSV, external interface | ADP-08/11/15 | Integration route/proof | Integration gate | M2+ |
| Release Controller | Release/rollback/pilot request | ADP-18 | Release decision | Release gate | M3+ |
| RCA/CAPA Specialist | NC, repeat failure, false PASS, failed release | ADP-21 | RCA/CAPA record | Improvement gate | M2+ |

## PASS/HOLD/BLOCKED rules
PASS when required specialists are activated and outputs exist. HOLD when activation decision is incomplete. BLOCKED when a critical specialist is bypassed for data/security/release/customer-risk work.

## Escalation
Escalate missed specialist trigger, unsupported compliance claim or high-risk build without specialist approval.

## Update trigger
New app type, tool, technology, customer requirement, risk change or audit finding.
