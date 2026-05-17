# PROCESS_INTERFACE_HANDOFF_MATRIX

## Purpose
Define process-to-process interfaces and handoffs as a supporting process-control matrix. This is not a turtle diagram.

## Scope
MOP, COP, SOP, ADP, Clause 9, Clause 10, app onboarding, GitHub CI readiness and n8n readiness interfaces.

## Owner/agent
Process Engineer with QA Gatekeeper.

## Inputs
Completed process turtles, process maps, ADP operating model, agent assignments and WI_005_INTERFACE_MAPPING.

## Activities/method
Map sending process, receiving process, transferred input/output, control point, evidence, risk, escalation, gate impact and maturity dependency.

## Outputs/records
Process interface and handoff control matrix.

## Linked processes
MOP to COP, COP to SOP, SOP to COP, ADP to COP, Clause 9 to Clause 10, RCA/CAPA to lessons learned, lessons learned to WI/agent/process updates, app onboarding to app-repo CI readiness and app onboarding to n8n readiness.

## Linked agents/workstations
Process Engineer, QA Gatekeeper, Internal Audit Specialist, RCA/CAPA Specialist, Lessons Learned Controller, GitHub CI Controller and n8n Automation Controller.

## Linked skills/WIs
WI_005_INTERFACE_MAPPING, WI_021_INTERNAL_AUDIT, WI_023_RCA, WI_026_LESSONS_LEARNED_UPDATE, WI_029_APP_ONBOARDING_READINESS and WI_030_CI_N8N_READINESS_REVIEW.

## Linked gates
Interface gate, handoff gate, audit gate, improvement gate, app-onboarding gate, CI readiness gate and n8n readiness gate.

## Evidence required
Sender, receiver, transferred input/output, control-point evidence, gate decision and escalation record where applicable.

## KPIs/measures
Handoff completeness, interface failure count, repeat handoff findings, escalation closure time.

## Risks
Lost evidence, wrong receiver, skipped gate, premature CI/n8n, lessons not converted to updates.

## Controls
No critical handoff is complete without evidence and receiving-process acceptance.

## Interfaces
This file controls interfaces but does not replace process-specific turtles.

## Handoffs
| Sending process | Receiving process | Input/output transferred | Control point | Evidence required | Risk | Escalation | Gate impact | Maturity dependency |
|---|---|---|---|---|---|---|---|---|
| MOP context/risk | COP app intake/job card | Scope, context, risk limits | Context/risk gate | Context and risk record | Wrong scope | QA Gatekeeper | HOLD/BLOCK | M1/M2 |
| COP source lock | COP requirements | Active source, exclusions | Source gate | Source lock record | Stale source | Context Specialist | HOLD/BLOCK | M1+ |
| COP requirements | COP runtime specification | Acceptance criteria | Requirements gate | Acceptance record | Vague build | App Owner | HOLD | M1+ |
| COP runtime | COP backend/RLS | Runtime object/state/data need | Runtime gate | Runtime map | UI shell/schema drift | Runtime Architect | HOLD/BLOCK | M2+ |
| COP build | COP verification | Change set/build evidence | Build gate | Diff/build evidence | Scope drift | QA Gatekeeper | HOLD/BLOCK | M2+ |
| COP verification | COP validation/UAT | Verified build/evidence | Verification gate | Verification record | False PASS | QA Gatekeeper | HOLD/BLOCK | M2+ |
| COP validation | COP release/rollback | UAT decision and limitations | Validation gate | UAT record | Release blocker missed | Release Controller | HOLD/BLOCK | M2+ |
| COP release | COP support | Release/support pack | Support gate | Release/handover evidence | No support route | Support Owner | HOLD | M3+ |
| SOP prompt control | COP job card/build | Approved prompt packet | Prompt gate | Prompt review | Broad prompt | Prompt Auditor | HOLD/BLOCK | M1+ |
| SOP security/data | COP backend/release | Security and data controls | Security gate | Security evidence | Customer-data/RLS risk | Security Reviewer | BLOCK | M2+ |
| ADP verification | COP verification | Verification record | Evidence gate | Verification evidence | False PASS | Evidence Auditor | HOLD/BLOCK | M2+ |
| Clause 9 audit | Clause 10 improvement | Audit finding | NC gate | Finding evidence | Finding ignored | RCA/CAPA Specialist | HOLD/BLOCK | M2+ |
| RCA/CAPA | Lessons learned | Cause/action/effectiveness | Lessons gate | RCA/CAPA evidence | Lesson not embedded | Lessons Controller | HOLD | M2+ |
| Lessons learned | WI/agent/process update | Prevention rule/update need | Knowledge/update gate | Updated artefact evidence | Repeat failure | Knowledge Controller | HOLD/BLOCK | M2+ |
| App onboarding | App-repo CI readiness | Onboarding PASS evidence | CI readiness gate | Onboarding evidence | Premature CI | GitHub CI Controller | HOLD/BLOCK | M3+ |
| App onboarding | n8n readiness | Maturity/readiness evidence | n8n readiness gate | Readiness evidence | Automating immature process | n8n Controller | HOLD/BLOCK | M4/M5 candidate |

## PASS/HOLD/BLOCKED rules
PASS when handoff evidence and receiving acceptance exist. HOLD when non-critical evidence is pending. BLOCKED when critical handoff is missing for release, data/security, CI or n8n.

## Escalation
Escalate skipped gate, missing handoff evidence, security/data issue, premature app-repo CI or n8n automation.

## MLA / maturity dependency
Maturity determines required review depth and handoff evidence.

## Update trigger
Process change, new interface, audit finding, RCA/CAPA, app onboarding or automation request.
