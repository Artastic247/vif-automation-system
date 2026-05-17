# AGENT_ESCALATION_MATRIX

## Purpose
Define escalation triggers, escalation owner and required response for agent, specialist, process and app-development failures.

## Scope
All agents, specialists, MOP/COP/SOP processes, ADP processes, WIs, validation checks, app onboarding, GitHub CI readiness and n8n readiness.

## Owner/agent
QA Gatekeeper owns escalation control with VIF Orchestrator, RCA/CAPA Specialist and Management Review Owner.

## Inputs
Finding, failed gate, missing evidence, scope drift, security/RLS risk, customer-data risk, failed validation, failed release/rollback, tool/provider failure, repeated repair failure, false PASS or automation request.

## Activities/method
Classify trigger, assign escalation owner, define containment, block unsafe gates, route to NC/RCA/CAPA where needed, define management-review input, and close only with evidence.

## Outputs/records
Escalation record, containment action, gate decision, NC/RCA/CAPA link, management-review input and closure evidence.

## Linked processes
Clause 9 audit/MLA, Clause 10 NC/RCA/CAPA, ADP-16 to ADP-21 and all affected MOP/COP/SOP processes.

## Linked skills/WIs
WI_001 to WI_030, especially WI_017, WI_021, WI_023, WI_024, WI_028, WI_029 and WI_030.

## Linked gates
Escalation, NC, RCA/CAPA, evidence, release, app onboarding, CI/n8n and management-review gates.

## Evidence required
Trigger evidence, owner, containment, decision, action evidence, closure evidence and recurrence check if required.

## Risks
Critical finding ignored, false PASS repeated, customer-data/security risk untreated, app-repo CI/n8n bypass, release without evidence.

## Controls
High-risk escalation blocks affected gates until containment and owner are assigned. Repeat failures trigger RCA/CAPA and management review.

## Interfaces
QA Gatekeeper, VIF Orchestrator, Security/Data Reviewer, Release Controller, RCA/CAPA Specialist, Management Review Owner, CI/n8n Controllers.

## Escalation matrix
| Trigger | Escalation owner | Required response | Gate impact |
|---|---|---|---|
| False PASS | QA Gatekeeper | Contain claim, audit evidence, open NC/RCA | BLOCK affected PASS |
| Missing critical evidence | Evidence Auditor | Hold gate, request evidence | HOLD/BLOCK |
| Scope drift | VIF Orchestrator | Scope lock, backlog/change routing | HOLD |
| Security/RLS risk | Security/Data Reviewer | Contain risk, backend/RLS proof, NC if needed | BLOCK if high risk |
| Customer-data risk | Security/Data Reviewer | Stop data use, contain, escalate | BLOCK |
| Failed validation | QA Gatekeeper | Hold release/onboarding, RCA if systemic | HOLD/BLOCK |
| Failed release/rollback | Release Controller | Stop rollout, rollback/contain, RCA/CAPA | BLOCK |
| Tool/provider failure | Tool/Supplier Reviewer | Assess suitability, route fallback | HOLD |
| Repeated repair failure | RCA/CAPA Specialist | RCA/CAPA and improvement action | HOLD/BLOCK |
| Agent out-of-scope action | QA Gatekeeper | Stop action, review authority, NC if required | HOLD/BLOCK |
| Skill/WI failure | Skill/WI Auditor | Review WI, update/calibrate, RCA if repeat | HOLD |
| Validator false negative | Validator Auditor | Calibrate validator, RCA/CAPA | BLOCK if safety critical |
| App-repo CI attempt before readiness | GitHub CI Controller | Stop, hold, escalate to QA | BLOCK |
| n8n attempt before maturity | n8n Controller | Stop, hold, escalate to QA/MLA | BLOCK |
| Auto-fix/auto-merge/auto-release request | QA Gatekeeper | Reject and record prohibited request | BLOCK |

## PASS/HOLD/BLOCKED rules
PASS when escalation is closed with evidence. HOLD when action is open. BLOCKED when critical risk lacks containment or prohibited automation/release is attempted.

## Escalation
This file defines escalation; unresolved critical escalation goes to Management Review Owner.

## MLA / maturity dependency
Repeated escalation can downgrade maturity and block automation, onboarding, release or specialist approval.

## Update trigger
New escalation trigger, audit finding, RCA/CAPA, management-review action, tool change or automation request.
