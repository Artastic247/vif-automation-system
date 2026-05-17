# PROCESS_TURTLE_SCOPE_AND_USE_RULES

## Purpose
Define the correct scope and use rules for process turtle artefacts so turtles remain process-specific and are not misused as generic completion matrices.

## Scope
This applies to all process-turtle artefacts under the Software Build Management System.

## Owner/agent
Process Engineer with QA Gatekeeper.

## Inputs
Process architecture, MOP/COP/SOP/ADP process definitions, app-development operating model, agent assignment matrices and work instructions.

## Activities/method
Use turtle diagrams only for defined processes. Use supporting matrices for interfaces, KPIs, agents, WIs, validators, prompts and evidence controls. Do not call supporting artefacts turtles unless they describe an actual process turtle.

## Outputs/records
Process-turtle scope rule, turtle-use decision and misclassification correction record.

## Linked processes
MOP, COP, SOP and ADP process families only.

## Linked agents/workstations
Process Engineer, QA Gatekeeper, VIF Orchestrator and Internal Audit Specialist.

## Linked skills/WIs
WI_004_PROCESS_MAPPING and WI_005_INTERFACE_MAPPING.

## Linked gates
Process-definition gate, turtle-completion gate, process-audit gate and app-onboarding HOLD gate.

## Evidence required
Defined process ID, process name, turtle row and evidence that the target is an actual process.

## KPIs/measures
Number of true process turtles completed, number of misclassified turtle artefacts corrected, number of SOURCE REQUIRED process names.

## Risks
Generic artefacts being treated as process turtles, false process-approach maturity, app onboarding before process proof, audit confusion.

## Controls
Turtles are process-specific. Supporting artefacts must be clearly labelled as supporting process-control matrices.

## Interfaces
Process architecture, interface matrix, KPI matrix, WI matrix, agent matrix, validator controls and audit controls.

## Handoffs
Process turtle gaps feed the turtle gap register, process audit and validation alignment.

## Turtle scope rules
- Turtles apply only to defined processes.
- Valid turtle families are MOP, COP, SOP and ADP.
- ADP turtles are allowed only because ADP-01 to ADP-21 are defined as app-development process steps in the operating model.
- Work instructions are not turtle diagrams.
- Agents and specialists are not turtle diagrams.
- Validators and validation scripts are not turtle diagrams.
- Prompts and prompt files are not turtle diagrams.
- Checklists, registers, evidence records, README and MANIFEST are not turtle diagrams.
- Interface maps, KPI matrices, agent matrices and WI matrices are linked controls, not turtle diagrams.
- Supporting artefacts must not be named as turtle artefacts unless they are process-specific turtle matrices.

## PASS/HOLD/BLOCKED rules
PASS when turtle scope is process-specific and supporting controls are correctly labelled. HOLD when process names or evidence remain SOURCE REQUIRED. BLOCKED when non-process artefacts are treated as process turtles for gate approval.

## Escalation
Escalate turtle misuse, false process completion, unclear process definitions or app onboarding attempted from structural turtle evidence only.

## MLA / maturity dependency
Structural turtle completion may support M1/M2 only. M3+ requires operational use evidence, audit and validation.

## Update trigger
Process register update, turtle audit finding, validation alignment, app onboarding request or RCA/CAPA.
