# APP_DEVELOPMENT_PROCESS_REGISTER

## Purpose
Register the app-development production processes ADP-01 to ADP-21.

## Scope
All controlled app-development work from request to feedback and improvement.

## Owner/agent
VIF Orchestrator.

## Inputs
App request, job card, source evidence, role assignments, process requirements and maturity status.

## Activities/method
Each process defines purpose, owner/agent, inputs, activities, outputs, required specialist, required skill/WI, evidence, gate, KPI, risk, control, interface, handoff and MLA maturity dependency.

## Outputs/records
Process register used for routing work and audit.

## Linked process
App-development operating model.

## Linked skills/WIs
All app-development skills/WIs referenced in the linkage matrix.

## Linked gates
ADP gate sequence from intake to improvement.

## Evidence required
Completed records for each process when used.

## Risks
Process steps skipped, wrong agent used, missing specialist, no handoff evidence, false PASS.

## Controls
No ADP process may be marked complete without owner, input, output, evidence and next handoff.

## Interfaces
All ADP process handoffs and specialist interfaces.

## ADP process list
| ID | Process | Owner/agent | Required specialist | Required skill/WI | Evidence | Gate | KPI | Risk/control/interface/handoff | MLA dependency |
|---|---|---|---|---|---|---|---|---|---|
| ADP-01 | App intake and classification | VIF Orchestrator | Product/App Owner | Scope lock | Intake record | Intake gate | Intake cycle time | Wrong classification / classify by risk and type / handoff to source lock | M1+ |
| ADP-02 | Context/source-of-truth lock | Context Specialist | GitHub Controller | Context lock, source-of-truth lock | Repo/branch/source record | Context gate | Source gaps | Source drift / lock current truth / handoff to domain capture | M1+ |
| ADP-03 | Domain truth and process-owner capture | Process Owner | Domain Specialist | Process mapping | Domain truth record | Domain gate | Truth gaps | Assumed domain / process owner approval / handoff to user workflow | M1+ |
| ADP-04 | User/operator workflow capture | Operator Workflow Specialist | Operator/User Tester | User workflow capture | Workflow evidence | Workflow gate | Workflow defects | Desk design / operator validation / handoff to requirements | M1+ |
| ADP-05 | Requirements and acceptance criteria | Product/App Owner | QA Gatekeeper | Requirements review | Acceptance criteria | Requirements gate | Rework rate | Vague requirements / acceptance defined / handoff to runtime map | M1+ |
| ADP-06 | Runtime-first process route and module map | Runtime Architect | Process Engineer | Runtime-first review | Runtime/module map | Runtime gate | Runtime gaps | UI shell / runtime object/state/control / handoff to UI/backend concept | M2+ |
| ADP-07 | UI/interface design control | UI/UX Specialist | Process Owner | UI/interface review | Screen/interface concept | UI gate | UI defects | Visual mismatch / review with workflow / handoff to job card | M1+ |
| ADP-08 | Data/backend/RLS design control | Backend Coder | Supabase/RLS Engineer | DB/RLS proof | Data/backend/RLS concept | Backend design gate | RLS gaps | Unsafe data model / review RLS/roles / handoff to risk review | M2+ |
| ADP-09 | Risk/security/tenant review | Security/Data Reviewer | Tenant Owner | Risk/security review | Risk/tenant evidence | Risk gate | High risks open | Customer-data risk / define controls / handoff to job card | M2+ |
| ADP-10 | Job card and prompt packet creation | VIF Orchestrator | Prompt Engineer | Prompt quality review | Job card/prompt packet | Job card gate | Prompt drift | Broad prompt / bounded instruction / handoff to builder | M1+ |
| ADP-11 | Coding/build execution | Codex Implementer or Lovable Builder | Frontend/Backend Coder | Build execution WI | Change evidence | Build gate | Build failures | Scope drift / implement only job card / handoff to code review | M2+ |
| ADP-12 | Code review | Claude Code Reviewer | GitHub Controller | Code review | Review record | Review gate | Review findings | Unsafe diff / review against scope / handoff to backend review/test | M2+ |
| ADP-13 | Backend/RLS review | Supabase/RLS Engineer | Security Reviewer | DB/RLS proof | Backend/RLS evidence | Backend review gate | RLS defects | Frontend-only control / prove backend guard / handoff to UI/test | M2+ |
| ADP-14 | UI/adaptive review | UI/UX Specialist | Operator/User Tester | UI review | UI review evidence | UI review gate | Usability defects | Bad layout / operator review / handoff to testing | M2+ |
| ADP-15 | Test planning and execution | Test Owner | QA Gatekeeper | Test planning | Test results | Test gate | Test pass rate | Untested changes / execute planned tests / handoff to verification | M2+ |
| ADP-16 | Verification | QA Gatekeeper | Evidence Auditor | Verification review | Verification register | Verification gate | Evidence gaps | False PASS / evidence review / handoff to validation | M2+ |
| ADP-17 | Validation/UAT | UAT Coordinator | Process Owner/User | Validation/UAT review | UAT signoff | Validation gate | UAT defects | Misfit process / user confirms / handoff to release review | M2+ |
| ADP-18 | Release/rollback review | Release Controller | Configuration Controller | Release/rollback review | Release and rollback record | Release gate | Rollback readiness | Unsafe release / rollback proven / handoff to support | M3+ |
| ADP-19 | Handover/support readiness | Support Owner | Knowledge Controller | Handover WI | Support pack | Support gate | Support gaps | No owner / support route set / handoff to monitoring | M2+ |
| ADP-20 | Post-release monitoring and feedback | Support Owner | Incident Owner | Feedback review | Monitoring/feedback record | Monitoring gate | Incidents | Untracked feedback / classify / handoff to NC or backlog | M3+ |
| ADP-21 | Lessons learned / NC / RCA / CAPA trigger | RCA/CAPA Specialist | Lessons Learned Controller | RCA, CAPA, lessons learned | Improvement trigger | Improvement gate | Recurrence | Repeat failure / trigger Clause 10 / handoff to CI | M2+ |

## PASS/HOLD/BLOCKED rules
PASS when each used ADP process has evidence and handoff. HOLD when process evidence is incomplete. BLOCKED when protected work starts without upstream gate.

## Escalation
Escalate skipped ADP gates, missing owner, unapproved build, or runtime/release evidence gap.

## Update trigger
Process change, audit finding, app onboarding, RCA/CAPA or lesson learned.
