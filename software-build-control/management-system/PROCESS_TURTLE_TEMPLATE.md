# PROCESS_TURTLE_TEMPLATE.md

## Purpose
Provide a reusable turtle diagram format for every Software Build Control System process so process inputs, outputs, resources, methods, measures, risks, controls, records, interfaces and PDCA links are visible before execution.

## Scope
Applies to each MOP, COP and SOP process. A process is incomplete if it cannot be represented using this turtle template.

## Inputs
PROCESS_REGISTER, PDCA_PROCESS_MODEL, PROCESS_OWNER_MATRIX, PROCESS_KPI_REGISTER, PROCESS_RISK_CONTROL_REGISTER, PROCESS_RECORDS_MATRIX and PROCESS_GATE_MATRIX.

## Activities/checklist
For every process, complete the turtle fields below.

## Turtle diagram template

| Turtle element | Required content |
|---|---|
| Process ID and name | Unique process identifier and process name |
| Purpose | Why the process exists |
| Inputs | What triggers or feeds the process |
| Outputs | What the process produces |
| Owner | Accountable process owner/agent |
| Resources/tools | Tools, platforms, systems, repositories, templates or data needed |
| Methods/skills | Skills, work instructions, procedures or checklists used |
| Measures/KPIs | How performance/effectiveness is measured |
| Risks | What could go wrong |
| Controls | Controls that prevent or detect risk |
| Records/evidence | Records proving the process was executed |
| Interfaces | Upstream/downstream processes and handoffs |
| PLAN | What is planned before execution |
| DO | What is executed or controlled |
| CHECK | What is reviewed, tested, audited or verified |
| ACT | What is corrected, updated or improved |
| PASS/HOLD/BLOCKED | Gate rules for the process |

## Example structure

```text
Process ID:
Process name:
Process type:
Purpose:
Owner:
Inputs:
Activities:
Outputs:
Resources/tools:
Methods/skills:
Measures/KPIs:
Risks:
Controls:
Records/evidence:
Interfaces:
PLAN:
DO:
CHECK:
ACT:
PASS/HOLD/BLOCKED rule:
```

## Outputs/records
Completed process turtle diagrams and linked process evidence.

## Owner/tool
Process Engineer maintains the template. Process owners complete process-specific turtles. QA Gatekeeper reviews completeness.

## Gate controlled
Turtle diagram and process-definition gate.

## PASS/HOLD/BLOCKED rules
- PASS: all turtle elements are completed and linked to process register evidence.
- HOLD: minor field gaps exist but the process is not active for risky work.
- BLOCKED: process lacks owner, inputs, outputs, records, controls, interfaces or PDCA.

## Update trigger
New process, process revision, process audit, gate failure, or lessons-learned update.
