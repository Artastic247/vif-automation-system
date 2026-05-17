# STANDARDS_APPLICABILITY_PROCEDURE

## Purpose
Control how standards and guidance lenses are identified, assessed, sourced, interpreted and used inside the Software Build Management System without making unsupported compliance or certification claims.

## Scope
This procedure applies to all standards/guidance references used in the control system, app-development operating model, work instructions, audits, validators, app onboarding readiness, release decisions and customer-facing claim control.

## Owner/agent
Standards-control owner: Compliance Claim Approver.

Supporting specialists:
- ISO 9001/9002 Guidance Specialist
- ISO 9004 Maturity/Sustained Success Specialist
- IATF 16949 Process Discipline Specialist
- ISO/IEC 27001 Security Specialist
- ISO 31000/31010 Risk Specialist
- ISO/IEC 42001 AI Management Specialist
- Customer-Specific Requirement Owner
- App-Specific Compliance Owner
- QA Gatekeeper

## Inputs
Standards/guidance lens, customer-specific requirement, app-specific compliance input, source evidence, customer source evidence, app source evidence, process affected, risk affected, claim request, audit finding and management-review action.

## Activities/method
1. Identify the standard, guidance lens, customer-specific requirement or app-specific requirement being referenced.
2. Define intended use: internal alignment, audit lens, risk lens, customer requirement, app-specific requirement or customer-facing claim support.
3. Record source status as available, SOURCE REQUIRED, CUSTOMER SOURCE REQUIRED or APP SOURCE REQUIRED.
4. Assign the responsible specialist.
5. Link the standard/guidance lens to affected processes, WIs, gates, risks and evidence.
6. Confirm the use is an alignment lens unless licensed/source evidence and approved claim evidence are available.
7. Mark gaps and unresolved source items.
8. Escalate unclear interpretation, missing customer source, missing app source or claim risk.
9. Review changes to standards/guidance when source evidence changes, customer requirements change, app scope changes or audit findings require review.
10. Route false or unsupported claim risk to NC/RCA/CAPA and management review.

## Outputs/records
Applicability decision, source-control register entry, crosswalk entry, interpretation note, specialist review, claim-control decision, source-required gap and management-review input where applicable.

## Linked processes
Clause 4 context and scope, Clause 5 authority, Clause 6 risk and change planning, Clause 7 support/documented information/competence, Clause 8 operational control, Clause 9 audit/MLA, Clause 10 NC/RCA/CAPA/continual improvement, app-development operating model and app onboarding readiness.

## Linked skills/WIs
WI_001_CONTEXT_LOCK, WI_003_SOURCE_OF_TRUTH_LOCK, WI_007_RISK_OPPORTUNITY_REVIEW, WI_021_INTERNAL_AUDIT, WI_022_MLA_ASSESSMENT, WI_023_RCA, WI_024_CAPA_EFFECTIVENESS_REVIEW, WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE and WI_029_APP_ONBOARDING_READINESS.

## Linked gates
Standards applicability gate, source-control gate, interpretation gate, customer-facing claim gate, app onboarding gate, release gate, audit gate, RCA/CAPA gate and management-review gate.

## Evidence required
Source status record, responsible specialist, allowed/prohibited use, affected process, affected artefact, claim-control decision, source-required status and review date.

## Risks
Unsupported compliance claim, copied proprietary standard content, invented customer requirement, incorrect interpretation, customer-facing claim without approval, standards crosswalk treated as implementation evidence.

## Controls
Standards are used as alignment lenses unless source evidence and approval are available. Official standard text, proprietary tables, thresholds, examples or handbook content must not be copied. Customer-specific requirements cannot be invented. App-specific requirements require APP SOURCE REQUIRED until supplied.

## Interfaces
Standards-control owner, specialist owners, process owners, audit, RCA/CAPA, app onboarding, release, security/data, AI governance and management review.

## PASS/HOLD/BLOCKED rules
PASS when applicability, source status, specialist owner, allowed use and gate impact are defined. HOLD when source-required items, validation-script updates or review evidence remain pending. BLOCKED when a compliance/certification claim is made without approved evidence or protected scope is touched.

## Escalation
Escalate missing official source evidence, missing customer source evidence, missing app source evidence, interpretation dispute, false claim risk or customer-facing wording request.

## MLA / maturity dependency
M1 permits draft internal alignment only. M2 permits controlled pilot alignment. M3 permits released internal control use with source tracking. M4/M5 require audit, review, improvement and claim-control effectiveness evidence.

## Update trigger
New standard/guidance lens, source update, customer requirement, app-specific requirement, audit finding, RCA/CAPA, management-review action or customer-facing claim request.
