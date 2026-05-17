# SOP_TURTLE_COMPLETION_MATRIX

## Purpose
Complete turtle mapping for support processes SOP-01 to SOP-12.

## Scope
Support processes that enable controlled software-build and app-development work.

## Owner/agent
Process Engineer with Organisational Knowledge Controller and QA Gatekeeper.

## Inputs
Support process requirements, WI_001 to WI_030, agent assignment matrices, evidence rules and management-system support controls.

## Activities/method
Define each SOP turtle with input, source, activity, output, receiver, owner, resources, WIs, KPI, risk, control, evidence, interface, handoff, PDCA, gate and escalation.

## Outputs/records
SOP turtle completion matrix.

## Linked processes
SOP-01 to SOP-12.

## Linked agents/workstations
Knowledge Controller, Skill/WI Auditor, Tool/Supplier Reviewer, Prompt Audit Specialist, Evidence Auditor, Security/Data Reviewer, Release Controller and Lessons Learned Controller.

## Linked skills/WIs
WI_001 to WI_030 as applicable by support process.

## Linked gates
Support, competence, prompt, evidence, security, configuration, contingency, supplier and knowledge gates.

## Evidence required
Support records, knowledge updates, competence/WI records, tool reviews, prompt/context audit records, security/data evidence and lessons learned.

## KPIs/measures
Support-record completeness, WI ownership, prompt drift, evidence gap rate, tool findings, security/data findings, knowledge adoption and repeat lessons.

## Risks
Support process exists only as document, stale knowledge, wrong tool route, prompt drift, evidence gaps, security/data breach.

## Controls
Support processes must define owner, records, interfaces, evidence and escalation.

## Interfaces
SOP to COP/ADP operations, Clause 9 audit and Clause 10 improvement.

## Handoffs
Support controls feed operating processes; findings and lessons feed RCA/CAPA and knowledge updates.

## SOP turtle matrix
| Process ID | Process name | Input/source | Activities/method | Output/receiver | Owner/agent | Resources/tools | Skills/WIs | KPI/measure | Risk | Control | Records/evidence | Interfaces/handoffs | PDCA | Gate | Escalation | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SOP-01 | Documented information | Artefacts/records | Control storage, revision, approval state | Controlled records to users/auditors | Knowledge Controller | Repo/registers | WI_003, WI_027 | Record completeness | Uncontrolled doc | Source/record control | Document records | To all processes | Plan/Act | Document gate | Conflicting record | STRUCTURAL PASS |
| SOP-02 | Organisational knowledge | Lessons/audits/RCA | Update knowledge and adoption | Knowledge updates to agents/processes | Knowledge Controller | Knowledge register | WI_027 | Adoption evidence | Stale knowledge | Knowledge update flow | Knowledge records | To COP/ADP | Act | Knowledge gate | Unsafe old guidance | STRUCTURAL PASS |
| SOP-03 | Competence/skills | Role/WI needs | Assign WIs and competence | Competent agents to processes | Skill/WI Auditor | WI matrix | WI_022, WI_028 | WI coverage | Untrained agent | Competence/maturity matrix | Competence evidence | To process owners | Plan/Check | Competence gate | Agent misuse | STRUCTURAL PASS |
| SOP-04 | Agent/worker control | Role needs | Assign allowed/prohibited work | Agent assignment to processes | VIF Orchestrator | Agent matrices | WI_021, WI_022 | Assignment coverage | Undefined authority | Agent register/gate matrix | Agent evidence | To all processes | Plan/Check | Agent gate | False PASS | STRUCTURAL PASS |
| SOP-05 | Tool routing/qualification | Tool need/risk | Select and review tools | Tool route to job card | Tool/Supplier Reviewer | Tool matrix | WI_008, WI_030 | Tool issues | Wrong/unsafe tool | Tool review | Tool evidence | To prompt/build | Plan | Tool gate | Provider failure | STRUCTURAL PASS |
| SOP-06 | Prompt control | Prompt need | Review/audit prompt | Approved prompt packet | Prompt Audit Specialist | Prompt register | WI_008, WI_009 | Prompt drift rate | Broad prompt | Prompt quality gate | Prompt evidence | To ADP-10/11 | Plan/Check | Prompt gate | Unsafe prompt | STRUCTURAL PASS |
| SOP-07 | Evidence/record control | Work output | Verify record completeness | Evidence record to gate | Evidence Auditor | Evidence register | WI_017, WI_021 | Evidence gaps | False PASS | Evidence audit | Verification evidence | To QA/release | Check | Evidence gate | Missing critical evidence | STRUCTURAL PASS |
| SOP-08 | Security/tenant/data protection | Data/security need | Review data/tenant/security | Security decision to operation | Security/Data Reviewer | Security checklist | WI_014, WI_015, WI_020 | Security findings | Customer-data risk | Security/data gate | Security evidence | To backend/release | Check | Security gate | Data exposure | STRUCTURAL PASS |
| SOP-09 | Configuration/version control | Version/change | Control commits/versions | Config record to release | Release/Configuration Controller | GitHub/release regs | WI_016, WI_019 | Version drift | Wrong version | Config control | Commit/version evidence | To release/support | Do/Check | Config gate | Wrong commit | STRUCTURAL PASS |
| SOP-10 | Contingency/continuity | Support/release risk | Define contingency route | Continuity actions to support | Support Owner | Support/continuity regs | WI_019, WI_025 | Recovery readiness | No fallback | Contingency control | Continuity evidence | To support/MR | Act | Continuity gate | Failed recovery | STRUCTURAL PASS |
| SOP-11 | Supplier/tool-provider control | Provider/tool risk | Review provider suitability | Provider decision to tool routing | Tool/Supplier Reviewer | Supplier audit | WI_021, WI_030 | Provider findings | Tool outage/risk | Supplier review | Supplier evidence | To SOP-05 | Check | Supplier gate | Provider failure | STRUCTURAL PASS |
| SOP-12 | Lessons learned/knowledge reuse | Event/failure/improvement | Capture and embed lessons | Updated controls to processes | Lessons Learned Controller | Lessons register | WI_026, WI_027 | Recurrence rate | Lesson not used | Effectiveness review | Lesson evidence | To knowledge/WI/process | Act | Lessons gate | Repeat failure | STRUCTURAL PASS |

## PASS/HOLD/BLOCKED rules
PASS requires validation/use evidence. STRUCTURAL PASS means support turtle fields exist. HOLD where validation/use evidence is pending. BLOCKED if support failure creates protected-scope/security/release risk.

## Escalation
Escalate stale knowledge, security risk, unowned WI, prompt/tool failure, missing evidence or repeated failure.

## MLA / maturity dependency
Support-process maturity requires competence evidence, audits, use records and improvement actions.

## Update trigger
Support process change, audit finding, RCA/CAPA, tool change, knowledge update or app onboarding request.
