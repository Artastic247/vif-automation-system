# APP_DEVELOPMENT_PERFORMANCE_IMPROVEMENT_LINKAGE

## Purpose
Define how app-development performance evaluation feeds improvement and how improvement updates the ADP production line.

## Scope
Clause 9 audits, MLA, management-review inputs, audit findings, NC/RCA/CAPA, effectiveness review, continual improvement, lessons learned, organisational knowledge, maturity upgrade/downgrade, repeat-failure control, validator/check improvement and prompt/skill/agent/procedure updates.

## Owner/agent
QA Gatekeeper with Internal Audit Specialist, RCA/CAPA Specialist and Continual Improvement Owner.

## Inputs
Audit findings, MLA assessments, validation reports, NC/RCA/CAPA, effectiveness reviews, KPI trends, repeat-failure records and lessons learned.

## Activities/method
Classify finding/source, identify affected ADP process, feed Clause 9 input into Clause 10 output, assign owner, define evidence and closure rule, update maturity/knowledge/prompt/skill/agent/validator/process where needed.

## Outputs/records
Performance-improvement linkage record, NC/RCA/CAPA trigger, improvement action, knowledge update and maturity decision.

## Linked ADP processes
All ADP processes, especially ADP-16 to ADP-21.

## Linked MOP/COP/SOP processes
Clause 9 performance evaluation, Clause 10 improvement, management review and organisational knowledge.

## Linked skills/WIs
Evidence audit, internal audit, MLA assessment, RCA, CAPA, effectiveness review, continual improvement, lessons learned, organisational knowledge update, validator calibration.

## Linked gates
Audit gate, finding closure gate, NC/RCA/CAPA gate, effectiveness gate, improvement gate, maturity gate.

## Evidence required
Finding, affected ADP process, linked Clause 9 source, Clause 10 record, owner, action evidence, closure evidence and maturity impact.

## Risks
Findings not converted into action, CAPA ineffective, lessons not embedded, validator not updated, repeat failures continue.

## Controls
Every significant finding must link to NC/RCA/CAPA or improvement decision; every ineffective action must escalate.

## Interfaces
Auditor, QA, RCA/CAPA, CI owner, knowledge controller, prompt/skill/agent/process owners, management review.

## Performance/improvement matrix
| Finding/source | Affected ADP process | Clause 9 input | Clause 10 output | Owner | Evidence | Closure rule |
|---|---|---|---|---|---|---|
| Evidence gap | ADP-16 | Evidence audit | NC/correction | QA | Verification record | Evidence complete |
| False PASS | ADP-16 | Validator/audit finding | RCA/CAPA | QA/RCA | False-PASS evidence | Effectiveness proven |
| Runtime gap | ADP-06/16 | Process/app audit | NC/RCA | Runtime Architect | Runtime evidence | Governed workflow proven |
| RLS/security risk | ADP-08/09/13 | Security audit | NC/CAPA | Security/RLS | Risk/RLS evidence | Risk treated |
| Failed UAT | ADP-17 | Validation result | Improvement/CAPA | Product Owner | UAT evidence | User acceptance achieved |
| Failed release/rollback | ADP-18 | Release audit | RCA/CAPA | Release Controller | Rollback evidence | Release control effective |
| Prompt drift | ADP-10/11 | Prompt audit | NC/prompt update | Prompt Auditor | Prompt record | Revised prompt effective |
| Repeat repair failure | ADP-21 | Trend/KPI | Repeat failure/CAPA | RCA/CAPA | Linked NCs | Recurrence controlled |
| Validator miss | ADP-16/21 | Validator audit | Calibration/CAPA | Validator Owner | Test cases | FN/FP controlled |
| Tool/provider failure | ADP-10/11/20 | Supplier audit | Improvement/risk action | Tool Reviewer | Provider evidence | Suitability confirmed |

## PASS/HOLD/BLOCKED rules
PASS when findings are traced to action and closure. HOLD when actions open. BLOCKED when critical finding lacks containment, owner or escalation.

## Escalation
Escalate repeated ineffective CAPA, false PASS, data/security risk, failed rollback or overdue management action.

## Update trigger
Audit finding, MLA change, NC/RCA/CAPA, KPI trend, lessons learned, support incident or management review.
