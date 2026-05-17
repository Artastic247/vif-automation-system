# PROCESS_KPI_RISK_CONTROL_EVIDENCE_MATRIX

## Purpose
Define KPI, risk, control and evidence expectations as a supporting process-control matrix. This is not a turtle diagram.

## Scope
MOP, COP, SOP and ADP process families and selected critical processes.

## Owner/agent
QA Gatekeeper with Process Engineer and Management Review Owner.

## Inputs
Process turtles, risk registers, KPI registers, audit criteria, evidence records and process owners.

## Activities/method
For each process or process family define KPI/measure, risk, control, evidence, record, review frequency, owner and escalation trigger.

## Outputs/records
Process KPI/risk/control/evidence matrix and management-review input.

## Linked processes
MOP-01 to MOP-07, COP-01 to COP-16, SOP-01 to SOP-12 and ADP-01 to ADP-21.

## Linked agents/workstations
Process Owners, QA Gatekeeper, Risk Specialist, Evidence Auditor, Internal Audit Specialist and Management Review Owner.

## Linked skills/WIs
WI_006_PDCA_REVIEW, WI_007_RISK_OPPORTUNITY_REVIEW, WI_017_VERIFICATION_REVIEW, WI_021_INTERNAL_AUDIT, WI_022_MLA_ASSESSMENT and WI_025_CONTINUAL_IMPROVEMENT.

## Linked gates
KPI review gate, risk gate, evidence gate, audit gate and management-review gate.

## Evidence required
KPI result, risk/control record, evidence record, review decision and escalation record if triggered.

## KPIs/measures
Defined per process family and selected process row.

## Risks
KPI missing, risk not linked to control, evidence not current, review frequency not defined.

## Controls
Every process family has minimum KPI/risk/control/evidence expectations. Gaps are captured in the turtle gap register.

## Interfaces
Process owners, Evidence Auditor, Risk Specialist, Internal Audit Specialist, RCA/CAPA Specialist and Management Review Owner.

## Handoffs
KPI/risk/evidence trends hand off to management review and Clause 10 improvement.

## Matrix
| Process ID | KPI/measure | Risk | Control | Evidence required | Record | Review frequency | Owner | Escalation trigger |
|---|---|---|---|---|---|---|---|---|
| MOP family | Audit closure, risk treatment, maturity status | Weak governance | Management review, audit and MLA | Audit, MLA and review actions | MR/audit/MLA registers | Monthly/quarterly or risk-based | Management Review Owner | Critical overdue action |
| COP family | Gate pass rate, rework, release readiness | Unsafe app operation | Job card, V&V and release controls | Job cards, verification, UAT and release records | COP evidence pack | Per job/release | QA Gatekeeper | False PASS or release blocker |
| SOP family | Support-control completeness | Support failure or stale knowledge | Support process audit | WI, knowledge, evidence and tool records | SOP registers | Risk-based | Knowledge Controller | Critical support gap |
| ADP family | Runtime gaps, test/UAT issues, release blockers | UI shell/runtime failure | Runtime-first and V&V controls | Runtime, test, UAT and release evidence | ADP evidence pack | Per build/pilot | Runtime Architect/QA | Runtime false PASS |
| COP-07 | RLS/security proof gaps | Tenant/data breach | DB/RLS proof | Read/write/role/tenant/negative proof | RLS evidence record | Per backend/RLS change | Supabase/RLS Engineer | Denied path succeeds |
| COP-11 | Verification evidence gaps | False PASS | Verification review | Build/lint/test/scan/current evidence | Verification register | Per job card | QA Gatekeeper | Stale or failed evidence |
| COP-13 | Rollback readiness | Failed release/rollback | Release/rollback review | Release and rollback evidence | Release register | Per release | Release Controller | Rollback route missing |
| COP-16 | Onboarding readiness gaps | Premature onboarding/CI/n8n | Onboarding readiness review | App context/source/runtime/security evidence | Onboarding register | Per app | VIF Orchestrator | CI/n8n request before PASS |
| ADP-06 | Runtime map completeness | UI shell | Runtime-first review | Runtime object/state/action evidence | Runtime map | Per module | Runtime Architect | No runtime object |
| ADP-16 | Verification PASS quality | False PASS | Evidence audit | Current evidence pack | Verification record | Per job | QA Gatekeeper | Evidence missing |
| ADP-21 | Improvement closure | Repeat failure | RCA/CAPA/CI route | Improvement evidence | Improvement register | Per NC/repeat | RCA/CAPA Specialist | Repeat failure |

## PASS/HOLD/BLOCKED rules
PASS when KPI, risk, control and evidence are defined and reviewed. HOLD when review evidence is pending. BLOCKED when critical risk has no control or evidence.

## Escalation
Escalate missing critical KPI/control, worsening trend, false PASS, security/data risk, failed rollback or repeated failure.

## MLA / maturity dependency
M4/M5 require trend and effectiveness evidence. Lower maturity may remain structural only.

## Update trigger
New KPI, risk change, audit finding, RCA/CAPA, management review or app onboarding request.
