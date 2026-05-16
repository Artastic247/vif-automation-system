# MATURITY_LEVEL_MODEL.md

## Purpose
Define the maturity-level model used to control process use, audit depth, automation permission, release confidence and escalation within the Software Build Control System.

## Scope
Applies to every MOP, COP and SOP process; every agent/worker; every skill/work instruction; every procedure; every workflow; every prompt family; every validation script/check; every tool/integration profile; and every app/module onboarded later.

## Owner/agent
VIF Orchestrator owns maturity routing. QA Gatekeeper verifies evidence. Process owners own maturity claims for their processes. System owner approves M4/M5 automation permissions.

## Inputs
Process records, evidence records, audit results, validation reports, RCA/CAPA records, KPI results, lessons learned, interface/control-point evidence and management-review decisions.

## Activities/checklist
| Maturity level | Definition | Minimum evidence | Gate status | Automation allowance |
|---|---|---|---|---|
| M0 — Not defined | No approved process/control exists; work is ad hoc. | None or uncontrolled notes only. | BLOCKED for use beyond exploration. | No automation. |
| M1 — Draft | Initial template/procedure exists but is not proven. | Draft artefact and owner identified. | HOLD unless used only for controlled drafting. | Drafting assistance only. |
| M2 — Pilot | Used in controlled sandbox or pilot; evidence is being collected. | Pilot record, review evidence and human approval. | HOLD/PASS depending evidence and scope. | Human-controlled pilot assistance only. |
| M3 — Released | Approved for controlled use within defined scope. | Approved artefact, records, verification and periodic audit plan. | PASS for defined scope only. | Controlled operational use; no autonomous release. |
| M4 — Managed | KPIs, audits, RCA/CAPA and effectiveness review active. | KPI trend, audit result, CAPA/effectiveness evidence. | PASS with monitoring. | Limited governed automation with monitoring. |
| M5 — Optimised | Measured, audited, improved, reusable and automation-ready. | Optimisation evidence, lessons learned loop, monitoring and rollback. | PASS for automation candidate. | Automation candidate with audit, monitoring and rollback. |

## Outputs/records
Maturity rating, evidence basis, gate decision, automation allowance, audit frequency, owner, risks and next action.

## Maturity level
M0 to M5 as defined above.

## Evidence required
Evidence must prove current use, effectiveness, repeatability, controls, audit result, RCA/CAPA status and interface/control-point performance before maturity is increased.

## Linked process
MOP-03 Planning/risk/opportunity, MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action/improvement, SOP-07 Evidence and record control.

## Linked agent/skill/procedure/module
All agents, skills, procedures, workflows, validators and app modules are subject to this maturity model.

## Interface/control point
Maturity claims must include affected interfaces and control points. Interface failures prevent maturity increase.

## PASS/HOLD/BLOCKED rules
- PASS: maturity level is supported by evidence and used only within permitted scope.
- HOLD: maturity claim is plausible but evidence, audit or effectiveness proof is incomplete.
- BLOCKED: maturity is overstated, automation is attempted too early, or critical evidence/control is missing.

## PDCA
- PLAN: define maturity criteria and expected evidence.
- DO: apply maturity level to controlled items.
- CHECK: audit maturity evidence and interface/control-point performance.
- ACT: raise/lower maturity, update controls and escalate overstatements.

## Audit frequency
M0/M1 readiness review only; M2 after each pilot/use; M3 scheduled periodic audit; M4 KPI/effectiveness audit; M5 optimisation and automation-readiness audit.

## Automation allowance
Automation follows maturity rules only: M0 none, M1 drafting only, M2 human-controlled pilot assistance, M3 controlled operational use without autonomous release, M4 limited governed automation, M5 automation candidate.

## Escalation
Escalate maturity overstatement, automation attempted before permitted maturity, failed interface/control point, false PASS or ineffective CAPA.

## Update trigger
New process, agent, skill, validator, workflow, module, audit finding, maturity change, automation request, CAPA result, management review decision or lesson learned.
