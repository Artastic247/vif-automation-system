# PROCESS_ARCHITECTURE.md

## Purpose
Convert the Software Build Control System from a document/control pack into a process-led management system for controlled AI-assisted app development.

## Scope
Covers management processes (MOP), core operational processes (COP), and support processes (SOP) used to control app intake, design, build, verification, validation, release, rollback, support, improvement, AI/tool use, evidence, prompts, skills, and organisational knowledge.

## Process architecture principle
The system is process-led, not document-led. Documents, templates, scripts, prompts, agents, and skills are controlled outputs/resources of processes.

## Process families

| Family | Purpose | Direction of control |
|---|---|---|
| MOP — Management-oriented processes | Set direction, governance, context, risk, AI policy, audit, review, and improvement. | Set requirements for COP and SOP; review effectiveness. |
| COP — Core operational processes | Produce and control app-development outputs from intake to support. | Convert requests into controlled, verified, validated, released or rejected work. |
| SOP — Support-oriented processes | Provide documented information, knowledge, competence, tooling, evidence, security, configuration, contingency, and lessons. | Support and protect COP execution. |

## Controlled process list

### Management processes
- MOP-01 Context and interested-party management
- MOP-02 Leadership and governance
- MOP-03 Strategic planning, objectives, risk and opportunity
- MOP-04 AI governance and tool-use policy
- MOP-05 Internal audit
- MOP-06 Management review
- MOP-07 Corrective action and continual improvement

### Core operational processes
- COP-01 App intake and classification
- COP-02 Source-of-truth and context lock
- COP-03 Requirements and acceptance criteria
- COP-04 UI/interface design control
- COP-05 Data table/grid specification
- COP-06 Workflow/runtime specification
- COP-07 Database/backend/RLS design control
- COP-08 Environment and tenant setup
- COP-09 Job card creation and approval
- COP-10 Build/modification control
- COP-11 Verification
- COP-12 Validation/UAT
- COP-13 Tenant rollout
- COP-14 Release and rollback
- COP-15 App support and maintenance
- COP-16 Customer change control

### Support processes
- SOP-01 Documented information control
- SOP-02 Organisational knowledge control
- SOP-03 Competence and skill control
- SOP-04 Agent/worker control
- SOP-05 Tool routing and tool qualification
- SOP-06 Prompt control and prompt quality
- SOP-07 Evidence and record control
- SOP-08 Security, tenant, and data protection control
- SOP-09 Configuration and version control
- SOP-10 Contingency and continuity control
- SOP-11 Supplier/tool-provider control
- SOP-12 Lessons learned and knowledge reuse

## Mandatory process definition fields
Every process shall define: process ID, name, type, purpose, owner/agent, inputs, activities, outputs, linked artefacts/templates, linked skills/work instructions, records/evidence, gates, KPI, risks, controls, interfaces, PDCA, and PASS/HOLD/BLOCKED rules.

## PDCA rule
Every process must explicitly define PLAN, DO, CHECK, and ACT. If any PDCA stage is only implied, the process is incomplete.

## Process approach rule
A document, script, prompt, checklist, agent, or skill is not a process by itself. It must be linked to a process owner, input, activity, output, record, measure, risk, control, gate, and improvement route.

## Interface rule
Lessons learned, corrective action, audit findings, prompt failures, tool failures, CI findings, release defects, and customer feedback must feed back into context, risk, skills, prompts, tools, processes, templates, and validation rules.

## Outputs/records
PROCESS_REGISTER, PROCESS_INTERACTION_MAP, PDCA_PROCESS_MODEL, PROCESS_OWNER_MATRIX, PROCESS_KPI_REGISTER, PROCESS_RISK_CONTROL_REGISTER, PROCESS_RECORDS_MATRIX, PROCESS_GATE_MATRIX, and process-level turtle records.

## Owner/tool
VIF Orchestrator owns process architecture. Process Engineer maintains process maps. QA Gatekeeper verifies process evidence. Specialist workers own process-specific technical controls.

## Gate controlled
Process architecture gate, PDCA gate, management-system completeness gate.

## PASS/HOLD/BLOCKED rules
- PASS: all MOP/COP/SOP processes have owner, inputs, activities, outputs, records, KPI, risk, control, gate, interfaces, and explicit PDCA.
- HOLD: process exists but some measures, interfaces, or work instructions are incomplete.
- BLOCKED: process is missing, ownerless, document-only, or lacks PDCA for controlled app-development work.

## Update trigger
New process, process failure, audit finding, tool failure, app failure, customer change, release issue, CI change, or lesson learned.
