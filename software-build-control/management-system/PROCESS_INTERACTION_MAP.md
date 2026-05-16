# PROCESS_INTERACTION_MAP.md

## Purpose
Show how Software Build Control System processes interact so the system operates as a process-led management system rather than isolated documents or tool actions.

## Scope
Covers interactions between MOP, COP and SOP processes for controlled AI-assisted app development.

## Inputs
PROCESS_ARCHITECTURE, PROCESS_REGISTER, PDCA_PROCESS_MODEL, risk/records/gate matrices, app-development lifecycle controls and lessons learned.

## Activities/checklist
Use this interaction map before changing the process architecture, activating CI, onboarding an app repo, or approving a new tool/workflow.

## High-level interaction model

```text
MOP-01 Context and interested parties
        ↓
MOP-03 Planning, objectives, risks/opportunities ← MOP-07 Corrective action/improvement
        ↓                                      ↑
MOP-02 Leadership and governance              ↑
        ↓                                      ↑
MOP-04 AI governance/tool-use policy           ↑
        ↓                                      ↑
COP-01 Intake → COP-02 Source/context lock → COP-03 Requirements
        ↓                                      ↑
COP-04 UI → COP-05 Data tables → COP-06 Runtime → COP-07 DB/RLS
        ↓                                      ↑
COP-08 Environment/tenant → COP-09 Job card → COP-10 Build/modification
        ↓                                      ↑
COP-11 Verification → COP-12 Validation/UAT → COP-13 Tenant rollout
        ↓                                      ↑
COP-14 Release/rollback → COP-15 Support/maintenance → COP-16 Customer change
        ↓                                      ↑
MOP-05 Internal audit → MOP-06 Management review → MOP-07 Improvement
```

## MOP interaction rules

| MOP process | Sets direction for | Receives feedback from | Required feedback route |
|---|---|---|---|
| MOP-01 Context/interested parties | COP-01, COP-03, SOP-02 | Customer feedback, incidents, audit, market/tool changes | Update context, scope and risks |
| MOP-02 Leadership/governance | All processes | Gate failures, escalation, unclear ownership | Update owner/authority matrix |
| MOP-03 Planning/risk/opportunity | COP and SOP priorities | Contingencies, incidents, audits, metrics | Update risk, objectives and controls |
| MOP-04 AI governance/tool-use policy | SOP-04, SOP-05, SOP-06, COP-10 | AI/tool failures, prompt drift, credit burn | Update AI/tool/prompt rules |
| MOP-05 Internal audit | All processes | Process records and evidence | Findings to MOP-07 and MOP-06 |
| MOP-06 Management review | Strategy, objectives, resources | KPIs, audit, risks, incidents, lessons | Decisions/actions to process owners |
| MOP-07 Corrective action/improvement | All processes | Defects, escapes, failures, findings | Process, skill, prompt, template and validation updates |

## COP interaction rules

| COP flow | Required support | Required management interface | Output handoff |
|---|---|---|---|
| COP-01 to COP-03 | SOP-01, SOP-02, SOP-06 | MOP-01, MOP-03 | Approved intake/requirements |
| COP-04 to COP-07 | SOP-03, SOP-04, SOP-05, SOP-08 | MOP-04 | Approved screen/data/runtime/backend maps |
| COP-08 to COP-10 | SOP-08, SOP-09, SOP-10 | MOP-02, MOP-03 | Approved job card and controlled build |
| COP-11 to COP-14 | SOP-07, SOP-09, SOP-10 | MOP-05, MOP-06 as needed | Verification, UAT, rollout and release records |
| COP-15 to COP-16 | SOP-02, SOP-12, MOP-07 | MOP-06 | Maintenance/change/improvement records |

## SOP support rules

| SOP process group | Supports | Protects against |
|---|---|---|
| SOP-01/SOP-07 | All records and evidence | Uncontrolled documentation and false PASS |
| SOP-02/SOP-12 | Knowledge and improvement | Repeat failures and lost learning |
| SOP-03/SOP-04/SOP-05/SOP-06 | Skills, agents, tools and prompts | Wrong worker/tool/prompt drift |
| SOP-08/SOP-09/SOP-10/SOP-11 | Data, config, contingency, providers | Data exposure, wrong version, outage, no rollback |

## Feedback loops
Lessons learned and corrective action must feed back into: context, risks, objectives, process maps, skills/work instructions, prompt controls, tool routing, agent limits, validation scripts, templates, and app-specific registers.

## Outputs/records
Process interaction decisions, updated process interfaces, improvement actions, and gate decisions.

## Owner/tool
Process Engineer maintains. VIF Orchestrator approves interactions. QA Gatekeeper verifies process evidence.

## Gate controlled
Process interaction and systems-thinking gate.

## PASS/HOLD/BLOCKED rules
- PASS: every process has defined upstream/downstream interfaces and feedback route.
- HOLD: interface exists but owner/evidence is incomplete.
- BLOCKED: a process produces controlled output without support, gate, record, or feedback route.

## Update trigger
New process, process failure, tool change, app onboarding, audit finding, customer feedback, or lesson learned.
