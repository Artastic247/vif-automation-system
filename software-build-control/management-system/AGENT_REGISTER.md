# AGENT_REGISTER.md

## Purpose
Define agents as controlled workers with clear roles, allowed work, prohibited work, required inputs, required outputs, gates, stop conditions, and escalation routes.

## Scope
Applies to human and AI-assisted workers used in software build control. This register does not authorise any worker to bypass job cards, protected gates, verification, release approval, tenant controls, or data/security controls.

## Inputs
- Tool capability and task type.
- Current job card, context pack, gate criteria, risk level, and required evidence.
- Known tool failure modes and lessons learned.

## Activities/checklist
| Worker/agent name | Role | Allowed work | Prohibited work | Required input | Required output | Tool used | Gate controlled | Stop condition | Escalation condition |
|---|---|---|---|---|---|---|---|---|---|
| VIF Orchestrator | Controls sequence and gates | Route work, check evidence, control handoffs | Coding/release without approval | Context pack, job card, gate criteria | Gate decision, next action | ChatGPT | All gates | Missing source truth or scope drift | System owner |
| Runtime Architect | Maps runtime logic | Runtime objects, states, actions, evidence rules | UI-only completion claims | Workflow/data map | Runtime map | ChatGPT/Codex | Runtime/backend gate | Backend evidence missing | QA Gatekeeper |
| QA Gatekeeper | Verifies evidence | PASS/HOLD/BLOCKED, evidence review | False PASS or unverified release | Verification evidence | Gate result | ChatGPT/Codex | Verification/release | Failed or missing checks | Release owner |
| Credit-Burn Controller | Prevents waste | Stop/re-route expensive failed generation | Unlimited tool retries | Prompt history, failure pattern | Stop/re-route decision | ChatGPT | Tool routing | Repeated failed generation | User/system owner |
| Security/RLS Reviewer | Controls security and tenant risk | RLS/auth/tenant review | Unapproved RLS/schema edits | DB/RLS evidence | Security finding | Supabase/Codex | Security/RLS gate | Data exposure risk | System owner |
| UI/Adaptive Reviewer | Controls interface quality | UI/screen/table review | Backend/security claims | SCREEN_MAP/DATA_TABLE_SPEC | UI finding | ChatGPT/Lovable | UI gate | Missing screen/table spec | Runtime Architect |
| Process Engineer | Maintains process control | Process maps and workflow routes | App-code changes | Process evidence | Process map/update | ChatGPT | Process gate | Process unclear | VIF Orchestrator |
| Device/Integration Reviewer | Reviews integrations | Integration risk and interface review | Unapproved integration build | Integration spec/evidence | Integration risk note | Codex/Supabase | Integration gate | Device/API unclear | System owner |
| Compliance Specialist | Reviews regulated logic | Compliance requirement review | Legal/compliance claims without evidence | Requirement evidence | Compliance gap | ChatGPT | Compliance gate | Requirement missing | System owner |
| Lessons Learned Controller | Captures learning | Lessons and prevention updates | Ignoring repeat failures | Incident/defect/release evidence | Lesson/update | ChatGPT | Improvement gate | Repeat failure unmanaged | QA Gatekeeper |
| Codex Repo Inspector | Inspects repo/diffs | Bounded repo review and test evidence | Broad rewrite/unapproved changes | Repo, branch, job card | Repo evidence, diff, tests | Codex/GitHub | Repo/build gate | Scope drift or failing tests | VIF Orchestrator |
| Lovable Builder | Scoped UI/build station | Approved UI slice build | RLS/schema authority or broad repair | Approved screen map/job card | UI output | Lovable | Build gate | Feature expansion or drift | VIF Orchestrator |
| Claude Code Reviewer | Long-context review | Bounded review/refactor advice | Unbounded rewrite | Repo/files/job card | Findings/risks | Claude/Claude Code | Review gate | Unrelated changes | QA Gatekeeper |
| GitHub Release Controller | Version/release control | Branch, PR, commit, release records | Auto-release/auto-merge without approval | Verification/release pack | Release/rollback record | GitHub | Release gate | Missing rollback | System owner |
| Supabase Backend Reviewer | Backend evidence control | DB/RLS/RPC/migration review | Destructive unapproved changes | DB/schema/RLS evidence | Backend proof/gap | Supabase/Codex | Backend/RLS gate | RLS unknown or unsafe | Security/RLS Reviewer |

## Outputs/records
Agent register, worker assignment, stop/escalation evidence, and updates to TOOL_ROUTING_MATRIX where required.

## Owner/tool
VIF Orchestrator maintains the register. System owner approves worker roles. QA Gatekeeper verifies role compliance at gates.

## Gate controlled
Agent/work allocation and tool-routing gate.

## PASS/HOLD/BLOCKED rules
- PASS: worker has defined role, scope, input, output, stop condition, and escalation route.
- HOLD: worker capability or evidence is incomplete.
- BLOCKED: worker can alter protected areas without approval or lacks stop conditions for risky work.

## Update trigger
New tool, new worker, tool failure, bad output, scope drift, incident, or lesson learned.
