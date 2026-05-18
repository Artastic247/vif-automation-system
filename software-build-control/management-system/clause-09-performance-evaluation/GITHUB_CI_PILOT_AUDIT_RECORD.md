# GITHUB_CI_PILOT_AUDIT_RECORD

## Purpose
Document and audit the active control-system GitHub CI pilot.

## Scope
Manual/read-only/control-system-only validation workflows.

## Owner/agent
GitHub CI Controller and Internal Audit Specialist.

## Inputs
Workflow templates, validation scripts, permissions configuration and validation reports.

## Activities/method
Review workflow path, trigger type, permissions, validation command, artifact/report handling, rollback/disable route and prohibited automation boundaries.

## Outputs/records
GitHub CI pilot audit record and gate decision.

## Audit criteria
Pilot must remain manual, read-only and control-system-only. No deploy, auto-fix, auto-merge, auto-release or app-repo activation allowed.

## Evidence required
Workflow files, run evidence, permission settings and validation reports.

## MLA / maturity dependency
Pilot limited to M2 controlled-pilot behaviour.

## Linked process
Clause 9 CI pilot audit.

## Linked gate
GitHub CI pilot gate.

## PASS/HOLD/BLOCKED rules
PASS if workflow remains manual/read-only/control-system-only. HOLD if expansion requested without approval. BLOCKED if workflow can modify app repos, release, merge or deploy.

## Escalation
Any attempt to expand into app repos or enable auto actions.

## Management-review input
Pilot status and automation risk feed management review.

## Update trigger
Workflow change, validation change, automation request or finding.

## Current pilot state
- workflow path: software-build-control/github/workflows/
- trigger type: manual/read-only validation
- permissions: restricted/read-only
- validation command: python scripts/validate_control_pack.py --root .
- deployment exists: no
- auto-merge exists: no
- auto-release exists: no
- secrets required: no
- workflow modifies files: no
- artifact/report behaviour: validation reports only
- rollback/disable route: disable workflow templates/remove activation
- risks: false PASS, unsafe expansion, validator gaps
- current gate decision: HOLD for expansion, PASS for controlled manual pilot
- expansion allowed: no

## CI scope note
This pilot record is control-system only and does not authorise app-repo CI activation.

