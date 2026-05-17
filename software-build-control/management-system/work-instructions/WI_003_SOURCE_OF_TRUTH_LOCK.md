# WI_003_SOURCE_OF_TRUTH_LOCK

## Purpose
Identify and control the active source of truth so obsolete drafts, pasted history or unsupported assumptions do not drive app-development decisions.

## Scope
All artefacts, job cards, repo files, uploaded evidence, standards references, customer requirements and validation reports.

## When to use
Use whenever multiple versions, drafts, commits, uploaded files or conflicting instructions exist.

## When not to use
Do not use as a replacement for customer approval, runtime validation or official standards-source verification.

## Owner/agent
Context Management Specialist with GitHub Controller and Evidence Auditor.

## Inputs
Repo/branch/commit, current evidence pack, active artefact list, superseded artefacts, source-required items, customer-source-required items, old drafts and validation reports.

## Method steps
1. Identify active artefact and owner.
2. Identify superseded artefacts.
3. Mark SOURCE REQUIRED where official source is missing.
4. Mark CUSTOMER SOURCE REQUIRED where customer requirement is needed.
5. Confirm repo/branch/commit evidence.
6. Confirm current evidence pack.
7. Demote old drafts unless reapproved.
8. Record conflicts and unresolved gaps.
9. Issue source-of-truth gate decision.

## Outputs/records
Source-of-truth register, superseded artefact list, source-required list, evidence pack reference and conflict log.

## Evidence required
Commit/tree SHA, file path, uploaded evidence citation, validation report, customer source or official source status.

## Linked ADP processes
ADP-02, ADP-03, ADP-05, ADP-09, ADP-10, ADP-16, ADP-18 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 4 context, Clause 7 documented information/knowledge, Clause 8 operation, Clause 9 audit and Clause 10 improvement.

## Linked gates
Source lock, context, requirements, standards, verification and release gates.

## Tools allowed
GitHub file/commit evidence, uploaded file search, local checkout validation, evidence register.

## Tools prohibited
Using memory, old drafts, unverified pasted text or AI output as final source truth without source lock.

## Risks
Wrong source used, superseded draft drives work, unsupported claim, stale validation, conflicting instructions.

## Controls
Active truth must be explicit. Unsupported standards/customer requirements must not become customer-facing claims.

## Interfaces
Standards Specialist, Customer Requirement Owner, GitHub Controller, Evidence Auditor, QA Gatekeeper.

## PASS/HOLD/BLOCKED rules
PASS when active source and evidence are clear. HOLD when non-critical source evidence is pending. BLOCKED when critical source truth or customer/official source is missing for risky work.

## Escalation
Escalate source conflict, missing customer source, unsupported compliance claim or release based on stale evidence.

## MLA / maturity dependency
M1 allows draft source control. M2 requires pilot evidence. M3+ requires controlled source records. M4/M5 require audit trend and automation readiness.

## Update trigger
New source, commit change, uploaded file, conflicting evidence, customer requirement or audit finding.
