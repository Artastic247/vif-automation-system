# STANDARDS_CROSSWALK_MATRIX

## Purpose
Map standards/guidance lenses to software-build controls, artefacts, specialists, evidence, source status, gaps and gate impact.

## Scope
All standards/guidance lenses used by the Software Build Management System.

## Owner/agent
Compliance Claim Approver with assigned standards specialists.

## Inputs
Standards source-control register, standards applicability decisions, process architecture, work instructions, audit criteria, app-development operating model and app onboarding controls.

## Activities/method
1. Map the standard/guidance lens to clause/theme.
2. Define the software-build control.
3. Link artefact/procedure.
4. Assign specialist.
5. Define evidence required.
6. Record source status and gap.
7. Define gate impact.
8. Maintain without copying standard text or making compliance claims.

## Outputs/records
Standards crosswalk matrix and source/gap register input.

## Linked processes
Clause 4 context, Clause 5 leadership, Clause 6 planning, Clause 7 support, Clause 8 operation, Clause 9 performance evaluation, Clause 10 improvement, AI governance, security, risk, maturity and customer requirements.

## Linked skills/WIs
WI_001, WI_003, WI_004, WI_006, WI_007, WI_021, WI_022, WI_023, WI_024, WI_025, WI_027, WI_029 and WI_030.

## Linked gates
Context, leadership, risk, support, operation, audit, improvement, standards, claim-control, app onboarding and release gates.

## Evidence required
Artefact/procedure link, specialist review, source status, evidence type and gate impact.

## Risks
Crosswalk treated as implementation evidence, copied standard text, unsupported claim, missing customer/app source.

## Controls
The crosswalk supports alignment only. It does not prove implementation, compliance, certification readiness, customer acceptance or release readiness.

## Interfaces
Process owners, standards specialists, audit, RCA/CAPA, app onboarding and release control.

## Crosswalk matrix
| Standard/guidance lens | Clause/theme | Software-build control | Artefact/procedure | Specialist | Evidence required | Source status | Gap | Gate impact |
|---|---|---|---|---|---|---|---|---|
| ISO 9001-style structure | Clause 4 context | Context, scope, interested parties, process architecture | Context/source-lock, process architecture, process turtles | ISO 9001/9002 Guidance Specialist | Context pack, process map, source status | SOURCE REQUIRED | Official source not supplied | Context/app onboarding HOLD if unsupported |
| ISO 9001-style structure | Clause 5 leadership | Authority, accountability, gate ownership | Agent/gate authority matrices | ISO 9001/9002 Guidance Specialist | Authority records, gate decisions | SOURCE REQUIRED | Source required | Governance gate |
| ISO 9001-style structure | Clause 6 planning | Risk, objectives, change planning | Risk/change planning artefacts, WI_007 | ISO 9001/9002 Guidance Specialist + Risk Specialist | Risk/objective/change records | SOURCE REQUIRED | Source required | Risk/change gate |
| ISO 9001-style structure | Clause 7 support | Competence, knowledge, documented information, tools/resources | WI set, agent competence, knowledge control, tool routing | ISO 9001/9002 Guidance Specialist | Competence/WI/knowledge/tool records | SOURCE REQUIRED | Source required | Support gate |
| ISO 9001-style structure | Clause 8 operation | App-development, release/rollback, customer change | ADP operating model, WI_011-WI_020 | ISO 9001/9002 Guidance Specialist | Job card, V&V, release/rollback evidence | SOURCE REQUIRED | Source required | Operation/release gate |
| ISO 9001-style structure | Clause 9 performance evaluation | Audit, MLA, monitoring, management review | Clause 9 artefacts, WI_021/WI_022 | Internal Audit Specialist | Audit/MLA reports | SOURCE REQUIRED | Clause 9 validated internally but source still required | Audit/MLA gate |
| ISO 9001-style structure | Clause 10 improvement | NC, RCA/CAPA, CI, lessons, knowledge | Clause 10 artefacts, WI_023-WI_027 | RCA/CAPA Specialist | NC/RCA/CAPA/effectiveness evidence | SOURCE REQUIRED | External validation pending | Improvement gate |
| ISO/TS 9002 guidance logic | Procedure clarity | Practical implementation intent and evidence examples | Work instructions and procedures | ISO 9001/9002 Guidance Specialist | WI/procedure review evidence | SOURCE REQUIRED | Source required | WI/procedure gate |
| ISO 9004 maturity/sustained success | Maturity and sustained improvement | MLA, trends, effectiveness, stakeholder confidence | MLA files, validator review, management review | ISO 9004 Specialist | MLA/effectiveness/KPI trend evidence | SOURCE REQUIRED | Source required | MLA/CI gate |
| IATF 16949-style discipline | Automotive process discipline | Process approach, defect prevention, change control, evidence discipline | Process turtles, WI_004-WI_007, WI_023-WI_026 | IATF 16949 Specialist | Process/evidence/change/RCA records | SOURCE REQUIRED | CSR cannot be invented | Process/change gate |
| ISO/IEC 27001 logic | Information security | Access control, secrets, tenant isolation, customer data, audit logs | WI_014, WI_015, WI_020, validators | ISO/IEC 27001 Security Specialist | Security/data/tenant proof | SOURCE REQUIRED | Source required | Security/app onboarding gate |
| ISO 31000 logic | Risk framework | Risk criteria, ownership, treatment, monitoring | WI_007, risk matrices | ISO 31000/31010 Risk Specialist | Risk register/treatment evidence | SOURCE REQUIRED | Source required | Risk gate |
| ISO 31010 logic | Risk-assessment techniques | Technique selection and risk analysis support | Risk review records | ISO 31000/31010 Risk Specialist | Selected technique rationale | SOURCE REQUIRED | Source required | Risk analysis gate |
| ISO/IEC 42001 logic | AI governance | AI use policy, human oversight, AI output verification, model/tool control | AI governance, prompt audit, tool audit | ISO/IEC 42001 AI Management Specialist | AI/tool/output audit evidence | SOURCE REQUIRED | Source required | AI/tool gate |
| Customer-specific requirements | Customer requirements | Customer-specific controls | CUSTOMER_SPECIFIC_REQUIREMENTS_CONTROL.md | Customer-Specific Requirement Owner | Customer-supplied source | CUSTOMER SOURCE REQUIRED | Customer source required | Customer/app onboarding/release HOLD until supplied |
| App-specific requirements | App/product requirements | App-specific regulatory/compliance controls | App onboarding/readiness artefacts | App-Specific Compliance Owner | App-specific source | APP SOURCE REQUIRED | App source required | App onboarding/release HOLD until supplied |

## PASS/HOLD/BLOCKED rules
PASS when mapping, specialist, evidence and source status are defined. HOLD while source-required gaps remain. BLOCKED if crosswalk is used as compliance, certification or implementation proof.

## Escalation
Escalate unsupported crosswalk claim, missing customer source, missing app source, interpretation dispute or customer-facing wording request.

## MLA / maturity dependency
Maturity upgrade requires evidence of use, audit and source-control discipline; crosswalk alone supports structural alignment only.

## Update trigger
New source, standard/guidance change, customer requirement, app requirement, audit finding, RCA/CAPA or management-review action.
