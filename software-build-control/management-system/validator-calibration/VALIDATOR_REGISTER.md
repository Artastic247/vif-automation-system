# VALIDATOR_REGISTER

## Purpose
Register all validators/checks used by the Software Build Management System so each check has defined purpose, owner, scope, severity logic, gates and maturity status.

## Scope
Control-pack validators, management-system validators, app-development validators, external-app scan profiles, GitHub Actions checks and future n8n workflow checks.

## Owner/agent
Validator/Checker Auditor with QA Gatekeeper.

## Inputs
Validation scripts, required artefact lists, template-heading rules, evidence requirements, severity rules, process controls, WIs, audit findings and calibration results.

## Activities/method
Maintain validator/check ID, validator/check name, purpose, owner, scope, input artefacts, output result, severity logic, linked gate, linked process, linked WI, maturity level and current status.

## Outputs/records
Validator register, coverage status, maturity status and validation-control evidence.

## Linked processes
Clause 9 performance evaluation, Clause 10 improvement, app-development operating model, work-instruction management, agent assignment, process-turtle control, standards control, app onboarding and automation governance.

## Linked skills/WIs
WI_017_VERIFICATION_REVIEW, WI_021_INTERNAL_AUDIT, WI_022_MLA_ASSESSMENT, WI_028_VALIDATOR_CALIBRATION, WI_029_APP_ONBOARDING_READINESS and WI_030_CI_N8N_READINESS_REVIEW.

## Linked gates
Validation gate, evidence gate, app onboarding gate, app-repo CI gate, n8n readiness gate, release gate, backend/RLS gate and external validation closure gate.

## Evidence required
Validator script/check definition, test-case evidence, report output, FP/FN record where applicable, owner approval and review status.

## Risks
Unregistered validator, unclear severity, false PASS, false negative, validation scope misunderstood, unsupported app onboarding/CI/n8n PASS.

## Controls
Every validator must have owner, scope, severity logic, maturity level and test evidence before being used for gate closure.

## Interfaces
QA Gatekeeper, Evidence Auditor, Internal Audit Specialist, RCA/CAPA Specialist, GitHub CI Controller, n8n Automation Controller and App Onboarding Owner.

## Validator register
| Validator/check ID | Validator/check name | Purpose | Owner | Scope | Input artefacts | Output result | Severity logic | Linked gate | Linked process | Linked WI | Maturity level | Current status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VAL-001 | Required artefact checker | Confirms required files/folders exist | Validator Auditor | Control pack and management system | Required file list | PASS/HOLD/BLOCKED | Missing critical file = HOLD/BLOCKED | Validation | Documented information | WI_028 | M2 | Structural definition |
| VAL-002 | Template field checker | Confirms required headings/fields | Validator Auditor | Templates and procedures | Markdown files | PASS/HOLD | Missing required heading = HOLD | Validation | Documented information | WI_028 | M2 | Structural definition |
| VAL-003 | Evidence completeness checker | Checks required evidence status | Evidence Auditor | Registers/reports | Evidence records | PASS/HOLD/BLOCKED | Missing critical evidence = HOLD/BLOCKED | Evidence | Clause 9 | WI_017 | M2 | Structural definition |
| VAL-004 | Process architecture checker | Checks MOP/COP/SOP/ADP architecture | Process Engineer | Process architecture | Process files | PASS/HOLD | Missing owner/interface/gate = HOLD | Process | Clause 4/8 | WI_004 | M2 | Structural definition |
| VAL-005 | Clause 9 checker | Checks audit/MLA artefacts | Internal Audit Specialist | Clause 9 | Clause 9 files | PASS/HOLD | Missing audit/MLA = HOLD | Audit/MLA | Clause 9 | WI_021/022 | M3 | Clause 9 validated previously |
| VAL-006 | Clause 10 checker | Checks NC/RCA/CAPA/CI artefacts | RCA/CAPA Specialist | Clause 10 | Clause 10 files | PASS/HOLD | Missing improvement control = HOLD | Improvement | Clause 10 | WI_023-025 | M2 | External validation pending |
| VAL-007 | App-development operating-model checker | Checks ADP operating-model files | Process Engineer | App-development operating model | ADP files | PASS/HOLD | Missing ADP/control = HOLD | Operating model | Clause 8 | WI_011/029 | M2 | External validation pending |
| VAL-008 | Work-instruction checker | Checks WI_001 to WI_030 | Skill/WI Auditor | Work instructions | WI files | PASS/HOLD | Missing WI/heading = HOLD | Skill/WI | Clause 7 | WI_028 | M2 | External validation pending |
| VAL-009 | Agent-assignment checker | Checks agent/process/WI/gate matrices | VIF Orchestrator | Agent assignment | Agent files | PASS/HOLD | Missing authority/owner = HOLD | Agent gate | Clause 5/7 | WI_021/022 | M2 | External validation pending |
| VAL-010 | Corrected process-turtle checker | Checks only process-specific turtles and support-matrix naming | Process Engineer | Process turtles | Turtle/scope files | PASS/HOLD/BLOCKED | Misclassified non-process turtle = HOLD/BLOCKED | Process turtle | Clause 4 | WI_004/005 | M2 | External validation pending |
| VAL-011 | Standards-control checker | Checks standards source/claim controls | Standards Specialist | Standards control | Standards files | PASS/HOLD/BLOCKED | Unsupported claim = BLOCKED | Standards | Clause 4/7 | WI_021/027 | M2 | Structural definition |
| VAL-012 | Prompt/context checker | Checks prompt/context controls | Prompt Auditor | Prompts/context packs | Prompt/context files | PASS/HOLD/BLOCKED | Broad prompt/source gap = HOLD/BLOCKED | Prompt/context | Clause 7/8 | WI_008-010 | M2 | Structural definition |
| VAL-013 | Identity/contact checker | Checks identity/contact data control | Security/Data Reviewer | Identity/contact artefacts | Identity/contact files | PASS/HOLD | Missing boundary = HOLD | Data control | Clause 7/8 | WI_020 | M2 | Structural definition |
| VAL-014 | AI-management checker | Checks AI governance/control artefacts | AI Governance Specialist | AI management | AI files | PASS/HOLD/BLOCKED | Unsafe AI/data use = BLOCKED | AI gate | Clause 7/9 | WI_009/021 | M2 | Structural definition |
| VAL-015 | Secret detector | Detects secrets and .env risk | Security/Data Reviewer | Repo scan | Files/source | PASS/BLOCKED | Secret found = BLOCKED | Security | Clause 7/8 | WI_020 | M3 | Existing checker concept |
| VAL-016 | Large-file detector | Detects large risky files | QA Gatekeeper | Repo scan | Source/control files | PASS_WITH_WARNINGS/HOLD | Excessive size = warning/HOLD | Maintainability | Clause 8 | WI_017 | M2 | Existing checker concept |
| VAL-017 | Forbidden-pattern detector | Detects unsafe patterns | Security/Data Reviewer | Repo scan | Source/code | PASS/HOLD/BLOCKED | Unsafe critical pattern = BLOCKED | Security/release | Clause 8/9 | WI_014/015 | M2 | Existing checker concept |
| VAL-018 | External-app scan profile | Scans app repos read-only | App/Product Auditor | External app repos | App source | PASS/HOLD/BLOCKED | Customer-data/protected risk = BLOCKED | App onboarding | Clause 8/9 | WI_029 | M1 | HOLD until onboarding |
| VAL-019 | GitHub Actions workflow check | Checks workflow safety | GitHub CI Controller | CI workflows | Workflow files | PASS/HOLD/BLOCKED | Deploy/auto-merge/auto-release = BLOCKED | CI readiness | Automation governance | WI_030 | M2 | Control-system only |
| VAL-020 | Future n8n workflow check | Checks future n8n workflow safety | n8n Automation Controller | n8n workflows | n8n design/export | PASS/HOLD/BLOCKED | Auto action/privacy risk = BLOCKED | n8n readiness | Automation governance | WI_030 | M0/M1 | Future/HOLD |

## PASS/HOLD/BLOCKED rules
PASS when validator is registered, scoped, tested and severity-controlled. HOLD when calibration or evidence is pending. BLOCKED when validator can cause false PASS or protected-scope breach.

## Escalation
Escalate unregistered validator use, false negative, false PASS, blocked-risk bypass, app onboarding/CI/n8n approval attempt without validator maturity.

## MLA / maturity dependency
M0 not defined; M1 draft; M2 pilot/manual review; M3 released; M4 managed with metrics; M5 optimised and automation candidate.

## Update trigger
New validator, script update, false positive, false negative, audit finding, external validation requirement, app onboarding or automation request.
