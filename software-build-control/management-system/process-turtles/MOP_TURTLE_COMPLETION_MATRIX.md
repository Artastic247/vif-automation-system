# MOP_TURTLE_COMPLETION_MATRIX

## Purpose
Complete turtle mapping for management-oriented processes MOP-01 to MOP-07.

## Scope
Context, governance, planning/risk, management review, audit/MLA, corrective-action/improvement governance and AI/tool governance.

## Owner/agent
Process Engineer with Management Review Owner and QA Gatekeeper.

## Inputs
Management-system architecture, Clause 4-10 controls, agent assignments, WI_001 to WI_030 and audit/MLA records.

## Activities/method
Define each MOP turtle with input, source, activity, output, receiver, owner, resources, WIs, KPI, risk, control, evidence, interface, PDCA, gate and escalation.

## Outputs/records
MOP turtle completion matrix.

## Linked processes
MOP-01 to MOP-07.

## Linked agents/workstations
VIF Orchestrator, Context Specialist, Risk Specialist, Management Review Owner, Internal Audit Specialist, RCA/CAPA Specialist, AI Governance Specialist.

## Linked skills/WIs
WI_001, WI_002, WI_003, WI_004, WI_005, WI_006, WI_007, WI_021, WI_022, WI_023, WI_024, WI_025, WI_027, WI_028, WI_030.

## Linked gates
Context, leadership, planning, management review, audit, improvement and AI/tool gates.

## Evidence required
Management records, audit/MLA records, risk registers, review outputs, RCA/CAPA and knowledge updates.

## KPIs/measures
Audit completion, action closure, risk treatment, maturity level, improvement effectiveness, tool/AI findings.

## Risks
Weak governance, false maturity, unmanaged risk, audit finding not converted, AI/tool drift.

## Controls
Management gates, audit programme, MLA, RCA/CAPA, management review and escalation.

## Interfaces
MOP to COP operating processes, SOP support processes and Clause 10 improvement.

## Handoffs
Management policy/risk/objectives to COP; audit findings to Clause 10; review outputs to improvement/knowledge.

## MOP turtle matrix
| Process ID | Process name | Input/source | Activities/method | Output/receiver | Owner/agent | Resources/tools | Skills/WIs | KPI/measure | Risk | Control | Records/evidence | Interfaces/handoffs | PDCA | Gate | Escalation | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MOP-01 | Context management | Internal/external context, interested parties, standards, app portfolio | Analyse context, scope, source truth, boundaries | Context pack to COP/ADP | Context Management Specialist | Context registers, source files | WI_001, WI_003, WI_004 | Context completeness | Stale/incorrect context | Source lock and context gate | Context record | To app intake/source lock | Plan | Context gate | Source conflict | STRUCTURAL PASS |
| MOP-02 | Leadership/governance | Scope, roles, authority needs | Define authority, accountability, gates | Authority model to all processes | VIF Orchestrator | Agent matrices | WI_002, WI_021, WI_022 | Gate clarity | Undefined authority | Gate authority matrix | Authority record | To COP/SOP/ADP | Plan/Act | Governance gate | False PASS | STRUCTURAL PASS |
| MOP-03 | Planning/objectives/risk | Risk, opportunities, objectives | Define objectives, risk treatment, change plan | Risk/objective records to operation | Risk Specialist | Risk/KPI registers | WI_006, WI_007 | Risk treatment closure | Untreated risk | Risk gate | Risk records | To ADP risk/security | Plan | Planning gate | High residual risk | STRUCTURAL PASS |
| MOP-04 | Management review | Audit, KPIs, MLA, NC/CAPA, risks | Review performance and decisions | Review actions to improvement | Management Review Owner | Review register | WI_006, WI_025, WI_027 | Action closure | Decisions not acted | Review action tracking | Review actions | To Clause 10/knowledge | Check/Act | Review gate | Overdue critical action | STRUCTURAL PASS |
| MOP-05 | Internal audit and MLA | Audit programme, MLA criteria | Audit, assess maturity, classify findings | Findings/MLA to NC/CI | Internal Audit Specialist, MLA Assessor | Audit/MLA registers | WI_021, WI_022, WI_028 | Findings closure, MLA level | False PASS | Audit criteria and MLA rules | Audit/MLA evidence | To Clause 10 | Check | Audit/MLA gate | Critical finding | PASS/STRUCTURAL PASS |
| MOP-06 | Corrective action/improvement governance | NC, RCA/CAPA, repeat failure | Govern correction, RCA, CAPA, CI | Improved controls to processes | RCA/CAPA Specialist | NC/CAPA/CI registers | WI_023, WI_024, WI_025, WI_026, WI_027 | CAPA effectiveness | Recurrence | Effectiveness review | RCA/CAPA evidence | To all processes | Act | Improvement gate | Ineffective CAPA | STRUCTURAL PASS |
| MOP-07 | AI/tool governance | AI/tool use, provider risks, prompt failures | Assess AI/tool risk, routing, audit | Tool/AI decisions to support/operation | AI Governance Specialist, Tool Reviewer | Tool matrix, AI audit | WI_008, WI_009, WI_028, WI_030 | AI/tool findings | AI bad output/tool failure | Tool routing and AI audit | Tool/AI records | To prompt/build/CI/n8n | Plan/Check | AI/tool gate | Unsafe tool use | STRUCTURAL PASS |

## PASS/HOLD/BLOCKED rules
PASS requires validation and operating evidence. STRUCTURAL PASS means turtle fields exist. HOLD where evidence, validation or use records are pending.

## Escalation
Escalate missing management owner, false PASS, critical risk, unsupported claim or ineffective improvement.

## MLA / maturity dependency
MOP maturity depends on audit evidence, review records and effective improvement closure.

## Update trigger
Management review, audit finding, risk update, RCA/CAPA, tool change or app onboarding request.
