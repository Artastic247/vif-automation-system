# VALIDATOR_COVERAGE_MATRIX

## Purpose
Map validators/checks to artefacts, processes, gaps detected, affected gates, severity, owners, test evidence and maturity dependency.

## Scope
All validator coverage required before external validation execution and later app onboarding/automation readiness.

## Owner/agent
Validator/Checker Auditor with QA Gatekeeper.

## Inputs
Validator register, artefact inventory, process architecture, WI set, agent assignments, corrected process-turtle scope, standards-control files, prompt/context files, security/data rules and automation hold rules.

## Activities/method
Map each validator/check to artefact/process covered, gap detected, gate affected, severity, owner, test evidence and maturity dependency. Ensure process-turtle validator respects corrected turtle scope.

## Outputs/records
Validator coverage matrix and gap basis for validation-script alignment.

## Linked processes
Clause 9, Clause 10, app-development operating model, skills/WIs, agent assignment, process turtles, standards control, prompt/context, app onboarding, GitHub CI and n8n readiness.

## Linked skills/WIs
WI_001 to WI_030, especially WI_028_VALIDATOR_CALIBRATION.

## Linked gates
Validation, app onboarding, app-repo CI, n8n, release, backend/RLS, customer-facing claim and external validation closure gates.

## Evidence required
Coverage row, owner, test evidence, severity decision, maturity dependency and validation status.

## Risks
Coverage gap, validator misses corrected turtle-scope rule, app onboarding released early, CI/n8n enabled before maturity, unsupported compliance claim.

## Controls
Coverage must include all required validator categories. Process-turtle validator must check only MOP/COP/SOP/ADP process turtles and correctly named supporting matrices.

## Interfaces
Validator Owner, Process Engineer, Standards Specialist, Prompt Auditor, Security/Data Reviewer, CI/n8n Controllers and QA Gatekeeper.

## Coverage matrix
| Validator/check | Artefact/process covered | Gap detected | Gate affected | Severity | Owner | Test evidence | Maturity dependency |
|---|---|---|---|---|---|---|---|
| Required artefact checker | Core control files/folders | Missing required artefact | Validation/app onboarding | HOLD/BLOCKED | Validator Auditor | TC-001/003 | M2+ |
| Template field checker | Markdown procedures/WIs/registers | Missing required heading | Validation | HOLD | Validator Auditor | TC-001/004 | M2+ |
| Evidence completeness checker | Evidence records/reports | Missing evidence | Verification/release/onboarding | HOLD/BLOCKED | Evidence Auditor | TC-005/006 | M2+ |
| Process architecture checker | MOP/COP/SOP/ADP architecture | Missing owner/interface/gate | Process gate | HOLD | Process Engineer | TC-001/003 | M2+ |
| Clause 9 checker | Audit/MLA/performance files | Missing Clause 9 control | Clause 9 gate | HOLD | Internal Audit Specialist | TC-001/003 | M3 context |
| Clause 10 checker | NC/RCA/CAPA/CI files | Missing improvement control | Clause 10 gate | HOLD | RCA/CAPA Specialist | TC-001/003 | M2+ |
| App-development operating-model checker | ADP operating-model files | Missing ADP/control linkage | Operating-model gate | HOLD | Process Engineer | TC-001/003 | M2+ |
| Work-instruction checker | WI_001 to WI_030 | Missing WI/heading | Skill/WI gate | HOLD | Skill/WI Auditor | TC-001/004 | M2+ |
| Agent-assignment checker | Agent assignment files | Missing owner/authority/escalation | Agent gate | HOLD | VIF Orchestrator | TC-001/003 | M2+ |
| Corrected process-turtle checker | MOP/COP/SOP/ADP turtles and supporting matrices | Misclassified non-process turtle; missing process turtle | Turtle gate | HOLD/BLOCKED | Process Engineer | TC-017/018 | M2+ |
| Standards-control checker | Standards/crosswalk/claim files | Unsupported claim/source missing | Claim/app onboarding | HOLD/BLOCKED | Standards Specialist | TC-020 | M2+ |
| Prompt/context checker | Prompt/context/source controls | Broad prompt/source drift | Prompt/job-card gate | HOLD/BLOCKED | Prompt/Context Specialists | TC-006/007 | M2+ |
| Identity/contact checker | Identity/contact-data controls | Missing privacy/data boundary | Data gate | HOLD/BLOCKED | Security/Data Reviewer | TC-014 | M2+ |
| AI-management checker | AI governance/tool-output files | Unsafe AI/data use | AI gate | BLOCKED | AI Governance Specialist | TC-014/020 | M2+ |
| Secret detector | Secrets/.env/service-role risk | Secret exposure | Security/release | BLOCKED | Security/Data Reviewer | TC-015 | M3 for automation |
| Large-file detector | Large maintainability-risk files | Oversized files | Maintainability/review | WARNING/HOLD | QA Gatekeeper | TC-002 | M2+ |
| Forbidden-pattern detector | Unsafe code/config patterns | Unsafe pattern | Security/release | HOLD/BLOCKED | Security/Data Reviewer | TC-006/019 | M2+ |
| External-app scan profile | Future app repo read-only scan | App risk/protected scope | App onboarding | HOLD/BLOCKED | App/Product Auditor | TC-007/008/014 | M2+ before onboarding |
| GitHub Actions workflow check | Control-system/app-repo workflows | Deploy/auto-merge/auto-release/premature CI | CI readiness | BLOCKED | GitHub CI Controller | TC-009/011/012/013 | M3+ for expansion |
| Future n8n workflow check | n8n workflow design/export | Premature automation/privacy/auto-action | n8n readiness | BLOCKED | n8n Controller | TC-010/011/012/013/014 | M4/M5 candidate only |

## Process-turtle validator special note
The corrected process-turtle validator must respect this scope: MOP, COP, SOP and ADP process turtles are valid. Interface/handoff and KPI/risk/control/evidence are supporting process-control matrices. Work instructions, agents, validators, prompts, checklists and records are not turtle targets.

## PASS/HOLD/BLOCKED rules
PASS when all required categories have mapped coverage and test evidence. HOLD when validation-script alignment or test execution is pending. BLOCKED when a critical coverage gap can permit unsafe PASS.

## Escalation
Escalate coverage gaps affecting app onboarding, app-repo CI, n8n, release, customer-facing claims, backend/RLS changes or external validation closure.

## MLA / maturity dependency
Coverage can be structural at M2; M3+ requires executed validation evidence; M4/M5 require review trends and low FP/FN risk.

## Update trigger
New validator, artefact class, app onboarding request, CI/n8n request, audit finding, FP/FN or validation-script update.
