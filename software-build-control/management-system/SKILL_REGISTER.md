# SKILL_REGISTER.md

## Purpose
Register controlled skills as repeatable work instructions/methods used by agents and workers during app development, recovery, review, verification, release, and improvement.

## Scope
Applies to reusable methods used across software build control. Skills do not replace job cards, evidence, human approval, or gate decisions.

## Inputs
- App context, job card, gate criteria, evidence, risk, tool route, and lesson learned.
- Worker/agent assignment and required output.

## Activities/checklist
| Skill | Trigger | Purpose | When to use | When not to use | Required inputs | Method steps | Output | Quality checks | Failure modes | Gate controlled |
|---|---|---|---|---|---|---|---|---|---|---|
| Context lock | New work/chat | Prevent truncation | Before planning/build | After context already current | App/repo/evidence | Build one-page context, mark missing evidence | APP_CONTEXT | Evidence current | Old source truth | Context gate |
| Scope lock | Job-card prep | Prevent feature creep | Before build/review | Vague request with no evidence | Objective, scope, exclusions | Define in/out/prohibited work | CURRENT_JOB_CARD | Scope bounded | Extra features | Job-card gate |
| Gate check | Any formal gate | Decide PASS/HOLD/BLOCKED | Every gate | No criteria | Gate checklist/evidence | Compare evidence to criteria | Gate decision | Evidence cited | False PASS | All gates |
| Evidence map | Verification | Link claims to proof | Before PASS | No claim made | Logs, files, DB, screenshots | Map claim to evidence | VERIFICATION_REGISTER | Traceable proof | Missing proof | Verification gate |
| Runtime-first review | Module review | Prevent UI-only completion | Before backend/module claim | Pure visual concept | Workflow/data/schema | Map object/state/action/evidence | RUNTIME_MAP | Backend proof | UI false PASS | Runtime gate |
| UI/interface review | UI work | Ensure screen/layout completeness | Before UI build | No UI impact | SCREEN_MAP/DATA_TABLE_SPEC | Review routes, states, actions | UI findings | States/roles clear | Partial UI | UI gate |
| Database/RLS review | Backend work | Protect data and tenant isolation | Before schema/RLS/protected action | No backend impact | Runtime/data/tenant evidence | Review DB/RLS/migration/proof | Backend finding | Read/write proof | Frontend-only security | DB/RLS gate |
| Tenant rollout review | Pilot/release | Control exposure | Before pilot/release | No tenant impact | Tenant register, release scope | Check tenant type, flags, rollback | Rollout decision | Rollback ready | Data mix | Tenant gate |
| Contingency review | Risky work/release | Plan recovery | Before high-risk work | Low-risk docs only | Risk, change, rollback | Check triggers and response | Contingency note | Owner/route clear | No rollback | Contingency gate |
| Prompt quality review | AI instruction | Prevent prompt drift | Before tool execution | No tool use | Job card/evidence | Check objective, scope, stop, verify, rollback | Approved prompt | No broad prompt | Tool drift | Prompt gate |
| Code-pattern review | Repo review | Reuse good/block bad patterns | Before refactor/repair | No code impact | Diff/pattern register | Check bad/good patterns | Pattern finding | Rule applied | Repeat defect | Coding standard gate |
| Verification review | After build | Prove result | Before release/PASS | No change | Build/lint/test/backend/manual evidence | Review checks | Verification decision | Commands/proof clear | Missing tests | Verification gate |
| Release check | Release prep | Control release | Before deployment/rollout | No release | Verification, UAT, rollback, tenant exposure | Check release criteria | Release decision | Rollback ready | False release | Release gate |
| Lessons learned | Closure/failure | Prevent repeat | After defect/release/tool drift | No event | Incident/defect evidence | Capture cause and control update | LESSONS_LEARNED | Prevention added | Repeat failure | Improvement gate |

## Outputs/records
Skill register, linked skill templates, gate outputs, updated lessons learned, and process knowledge updates.

## Owner/tool
Lessons Learned Controller and VIF Orchestrator maintain. Specialist reviewers own technical method content for UI, backend/RLS, verification, and release skills.

## Gate controlled
Skill/method governance gate.

## PASS/HOLD/BLOCKED rules
- PASS: skill has trigger, purpose, use limits, inputs, method, output, quality checks, failure modes, and gate.
- HOLD: skill exists but lacks evidence, owner, or quality checks.
- BLOCKED: skill authorises uncontrolled app/code/schema/release/customer-data work.

## Update trigger
New skill, repeated failure, agent/tool change, process update, audit finding, or lesson learned.
