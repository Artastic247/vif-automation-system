# SKILL_TEMPLATE.md

## Purpose
Define the standard format for any controlled skill/work instruction used by app-development workers and agents.

## Scope
Applies when creating, revising, approving, or retiring skills used for context control, scope control, gate checks, evidence mapping, UI review, database/RLS review, tenant rollout, contingency review, verification, release, and lessons learned.

## Inputs
- Skill need or trigger.
- Related gate, process, agent/worker, templates, evidence requirements, and known failure modes.

## Activities/checklist
Every skill must define:

- Skill ID and name.
- Trigger.
- Purpose.
- When to use.
- When not to use.
- Required inputs.
- Method steps.
- Output format.
- Quality checks.
- Common failure modes.
- Escalation triggers.
- Gate controlled.
- Records/evidence produced.
- Human approval point where required.
- Revision history.

## Outputs/records
Approved skill definition, skill register update, linked gate/process/template, and revision history.

## Owner/tool
Skill owner maintains the skill. Lessons Learned Controller and VIF Orchestrator review updates. Specialist reviewers own technical skill content.

## Gate controlled
Skill definition and controlled-method gate.

## PASS/HOLD/BLOCKED rules
- PASS: skill has all required fields, clear limits, evidence requirements, and gate linkage.
- HOLD: skill is useful but missing minor owner/revision/evidence detail.
- BLOCKED: skill authorises uncontrolled app-code, schema/RLS, release, customer-data, or automation work.

## Update trigger
New skill, repeated failure, tool change, process change, audit finding, or lessons-learned action.
