# PERFORMANCE_EVALUATION_PROCEDURE.md

## Purpose
Define the Clause 9-style performance-evaluation process for the Software Build Control System so process effectiveness, gate performance, audit results, maturity level, validation results, AI outputs, prompt control, evidence quality, release readiness and improvement needs are reviewed in a controlled way.

## Scope
Applies to all MOP, COP and SOP processes, app onboarding later, validation scripts, prompts, AI tools, agents/workers, skills, evidence records, release/rollback records, tenant rollout controls and management-system artefacts.

## Owner/agent
QA Gatekeeper owns performance evaluation. VIF Orchestrator coordinates process inputs. Process owners provide KPI and evidence. System owner reviews management-level performance. AI Governance Owner reviews AI-related performance.

## Inputs
Process KPIs, audit programme/results, maturity-level assessment, validation reports, gate decisions, RCA/CAPA records, lessons learned, AI bad-output records, prompt failure records, customer feedback, release/rollback records and support/maintenance records.

## Activities/checklist
1. Define performance indicators and review frequency.
2. Collect process, gate, validation, AI, prompt, evidence and maturity data.
3. Review whether processes are performing as intended.
4. Review whether outputs are evidence-backed and gate decisions are reliable.
5. Review maturity level and automation permission.
6. Identify trends, repeated failures, false PASS risk and weak controls.
7. Raise audit findings, RCA/CAPA or improvement actions where required.
8. Feed significant results into management review.

## Outputs/records
Performance evaluation record, KPI review, audit inputs, maturity review, management-review inputs, improvement actions and escalation records.

## Maturity level
Minimum M3 required for routine operational performance evaluation. M0/M1 receive readiness review only. M2 receives pilot-focused evaluation. M4/M5 require trend and effectiveness review.

## Evidence required
KPI source records, gate records, validation reports, audit records, maturity evidence, AI/prompt monitoring records and lessons-learned links.

## Linked process
MOP-05 Internal audit, MOP-06 Management review, MOP-07 Corrective action and continual improvement, MOP-03 Planning/risk/opportunity, SOP-07 Evidence and record control.

## Linked agent/skill/procedure/module
QA Gatekeeper, Process Engineer, AI Governance Owner, Lessons Learned Controller, gate-check skill, evidence-map skill, audit skill and maturity-level assessment.

## Interface/control point
Interfaces with audit, management review, RCA/CAPA, maturity assessment, validation scripts, prompt monitoring, AI monitoring, release/rollback, tenant rollout and lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: performance evidence is current, reviewed, linked to KPIs/gates and actions are assigned where needed.
- HOLD: evidence is partial or trends are unclear, but no unsafe automation/release is authorised.
- BLOCKED: performance data indicates false PASS risk, uncontrolled process failure, repeated defect, missing evidence, or maturity overstatement without containment.

## PDCA
- PLAN: define performance measures, evidence sources and review cadence.
- DO: collect and review performance evidence.
- CHECK: evaluate effectiveness, maturity, trends and gaps.
- ACT: raise audit findings, RCA/CAPA, management-review actions, process updates and lessons learned.

## Audit frequency
Risk and maturity based: M0/M1 readiness only, M2 per pilot/use, M3 periodic, M4 trend/effectiveness, M5 optimisation and automation-readiness review.

## Automation allowance
No CI/n8n/automation expansion may be authorised from performance evaluation alone. Automation requires maturity permission, audit evidence, validation evidence, human approval and management-review decision.

## Escalation
Escalate false PASS, repeated failed verification, uncontrolled AI bad output, critical prompt failure, evidence gap, overdue CAPA, maturity overstatement or failed release/rollback signal.

## Update trigger
New process KPI, audit result, failed gate, validation failure, AI/prompt issue, app onboarding, release issue, management review or lesson learned.
