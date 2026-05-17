# AUDIT_OBJECT_REGISTER

## Purpose
Define every auditable object class in the factory.

## Scope
Repository files, markdown controls, templates, scripts, validation reports, prompts, prompt generator rules, workflow definitions, process maps, turtles, agents, WIs, validators, standards-control, app intake, backend, UI, database/RLS, release, customer change, lessons and RCA/CAPA records.

## Audit owner/agent
Evidence Auditor with Internal Audit Specialist.

## Audit object
Auditable object classes and evidence expectations.

## Audit criteria
Each object type must have owner, source location, audit method, evidence, linked process, linked gate and finding trigger.

## Evidence required
File path, commit SHA, source record, linked process, linked agent, linked WI, linked validator, linked gate, audit result and finding record where applicable.

## Audit method
Review the controlled artefact, verify linkage to process/agent/WI/validator/gate, sample evidence, classify findings, and record PASS/HOLD/BLOCKED.

## Sampling method
Risk-based sample. High-risk, low-maturity, automation-related, customer-facing, security/RLS, prompt-generation and release-impact items require deeper sampling.

## Linked processes
MOP/COP/SOP process set, ADP-01 to ADP-21 app-development process set, Clause 9 performance evaluation and Clause 10 improvement.

## Linked agents
VIF Orchestrator, QA Gatekeeper, Internal Audit Specialist, MLA Assessor, Prompt Audit Specialist, Workflow Manager Auditor, Process Engineer, Runtime Architect, Security/Data Reviewer, RCA/CAPA Specialist.

## Linked skills/WIs
WI_001 to WI_030 as applicable.

## Linked validators
Required artefact checker, template checker, evidence checker, process checker, WI checker, agent checker, prompt/context checker, workflow checker, standards checker and factory-runtime audit runner when released.

## Linked gates
Context gate, scope gate, source gate, process gate, audit gate, MLA gate, validation gate, app-onboarding gate, app-repo CI gate, n8n gate and release gate.

## PASS/HOLD/BLOCKED rules
PASS when the audited object is defined, owned, linked, evidenced and within approved scope. HOLD when evidence, linkage, source or validation is incomplete. BLOCKED when protected scope is touched, false PASS risk exists, customer data/secrets are exposed, app-repo CI is activated early, n8n is implemented early, or unsupported compliance/certification claims are made.

## Findings classification
Observation, minor finding, major finding, blocked-gate finding, false-PASS finding, source-required finding, customer-source-required finding, app-source-required finding, security/RLS finding, customer-data finding, prompt-drift finding, workflow-drift finding, validator-failure finding and automation-maturity finding.

## Escalation
Escalate major, blocked-gate, false-PASS, security/RLS, customer-data, unsupported-claim, app-repo CI, n8n or repeated findings to QA Gatekeeper and RCA/CAPA Specialist.

## NC/RCA/CAPA trigger
Trigger NC/RCA/CAPA for major findings, repeated findings, false PASS, protected-scope breach, customer-data exposure, security/RLS risk, unsupported claim, ineffective correction or repeated workflow/prompt drift.

## MLA / maturity dependency
M0/M1 areas require close monitoring and limited automation. M2 permits controlled pilot evidence. M3 requires released control with audit evidence. M4/M5 require trend, effectiveness and continual-improvement evidence.

## Management-review input
Major findings, repeat findings, maturity downgrade, automation-readiness issues, source-required risks and false-PASS events feed management review.

## Update trigger
Update after audit finding, RCA/CAPA, process change, workflow change, prompt change, validator change, standards/source change, app onboarding request, CI/n8n readiness request or management-review action.
