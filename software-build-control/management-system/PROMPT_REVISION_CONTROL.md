# PROMPT_REVISION_CONTROL.md

## Purpose
Control the lifecycle of prompts from draft to approved, revised, deprecated or retired so prompt changes are traceable and bad prompts do not remain in use.

## Scope
Applies to reusable prompts, tool-specific prompts, job-card prompts, review prompts, build/repair prompts, verification prompts, release prompts and automation-routing prompts.

## Inputs
Prompt register entry, prompt quality checklist, prompt failure register, lessons learned, tool/model changes, job-card changes and audit/validation findings.

## Activities
- Assign prompt ID and version.
- Classify status: Draft, Under Review, Approved, Active, Revised, Deprecated, Retired, Blocked.
- Record owner, purpose, linked process, linked gate and allowed use.
- Review prompt after failure, tool/model change, process change or lesson learned.
- Retire prompts with repeated drift, unsafe scope, missing evidence logic or outdated tool assumptions.
- Update APPROVED_PROMPT_LIBRARY and PROMPT_REGISTER after approval or retirement.

## Outputs
Prompt revision record, approved/revised/retired prompt status and linked lessons or corrective actions.

## Records
| Prompt ID | Version | Status | Change reason | Owner/tool | Review evidence | Approval decision | Effective date | Retired/replaced by |
|---|---|---|---|---|---|---|---|---|
| PRM-001 | v0.1 | Draft | Initial prompt control baseline | Prompt Quality Reviewer | Checklist pending | HOLD | TBD | TBD |

## Owner/tool
Prompt Quality Reviewer owns prompt revision control. VIF Orchestrator approves process/tool route changes. QA Gatekeeper checks evidence for prompt changes that affect verification/release.

## Linked process
SOP-06 Prompt control and prompt quality, SOP-12 Lessons learned and knowledge reuse, MOP-04 AI governance and tool-use policy, MOP-07 Corrective action and continual improvement.

## Linked gate
Prompt gate, document-control gate, lessons-learned gate, AI governance gate.

## PDCA
- PLAN: define prompt version, intended use, review criteria and change trigger.
- DO: revise or retire prompt under controlled status.
- CHECK: check output quality, drift history, evidence linkage and gate fit.
- ACT: approve, reject, deprecate, retire or update related process/skill/tool controls.

## PASS/HOLD/BLOCKED rules
- PASS: prompt version, owner, status, review evidence and approval decision are clear.
- HOLD: prompt is useful but pending review, owner confirmation or evidence.
- BLOCKED: prompt is unversioned, unsafe, repeatedly failed, or still active after causing critical drift or data/release risk.

## Update trigger
Prompt change, prompt failure, tool/model change, job-card template change, process change, audit finding, CI finding or lesson learned.
