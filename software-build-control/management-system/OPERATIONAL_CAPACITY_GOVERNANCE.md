# OPERATIONAL_CAPACITY_GOVERNANCE.md

## Purpose
Define governance for operational capacity, resource planning and workload sustainability across the Software Build Control System.

## Scope
Applies to software-build control operations, app onboarding, audits, RCA/CAPA, release support, validator review, AI/tool usage, pilot execution, portfolio governance and future customer/project work.

## Owner/agent
System owner owns capacity governance. VIF Orchestrator owns workload routing. QA Gatekeeper reviews capacity impact on quality and gate reliability.

## Inputs
Job cards, app onboarding pipeline, audit programme, CAPA backlog, release schedule, tool availability, credit-burn records, process KPIs, maturity assessments and management-review priorities.

## Activities/checklist
1. Identify current workload and active job cards.
2. Classify work by risk, maturity, urgency and resource demand.
3. Confirm available human, tool, model, review and validation capacity.
4. Prioritise work by safety, customer impact, release risk and maturity need.
5. Block or defer work where capacity creates quality risk.
6. Track overload, bottlenecks and repeated rework.
7. Feed capacity risks into management review and improvement planning.

## Outputs/records
Capacity review, workload priority, bottleneck record, resourcing decision, deferral decision and improvement action.

## Maturity level
M3 requires controlled capacity planning for operational use. M4/M5 require trend review and proactive capacity optimisation.

## Evidence required
Workload list, owner capacity, tool capacity, review capacity, backlog status, bottleneck evidence and management-review decision where needed.

## Linked process
MOP-03 Strategic planning risk and opportunity, MOP-06 Management review, MOP-07 Corrective action and continual improvement, SOP-05 Tool routing and tool qualification.

## Linked agent/skill/procedure/module
System owner, VIF Orchestrator, QA Gatekeeper, Credit-Burn Controller, audit programme, CAPA register and pilot KPI register.

## Interface/control point
Interfaces with job-card control, app onboarding, audit programme, release governance, validator governance, AI credit-burn control and portfolio governance.

## PASS/HOLD/BLOCKED rules
- PASS: capacity is adequate for controlled execution and review.
- HOLD: capacity constrained; work must be prioritised or deferred.
- BLOCKED: workload pressure risks false PASS, skipped review, unsafe release, uncontrolled automation or unresolved critical CAPA.

## PDCA
- PLAN: define workload and capacity needs.
- DO: route and resource work.
- CHECK: review bottlenecks, delays and quality impact.
- ACT: reprioritise, improve process, add capacity or reduce scope.

## Audit frequency
During management review, portfolio review and when capacity bottlenecks appear.

## Automation allowance
Automation may not be used to mask inadequate capacity unless governance, maturity and validation evidence support it.

## Escalation
Escalate overload, critical bottleneck, repeated rework, review capacity shortfall, tool unavailability or credit/resource burn risk.

## Update trigger
New project/app, capacity overload, release pressure, audit backlog, CAPA backlog, tool outage, credit-burn spike or management-review decision.
