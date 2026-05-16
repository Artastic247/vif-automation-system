# APP_DEVELOPMENT_CONTEXT_SCOPE_LINKAGE

## Purpose
Define how app-development work connects to context, scope, interested parties, source-of-truth and protected boundaries.

## Scope
All ADP app-development processes before build, repair, release, onboarding, CI or automation.

## Owner/agent
Context Management Specialist with VIF Orchestrator and QA Gatekeeper.

## Inputs
Internal/external context, PESTLE/SWOT where relevant, interested parties, app portfolio, customer/tenant/data context, source-of-truth artefacts, standards applicability, project boundaries and protected-scope rules.

## Activities/method
Lock context before design/build. Define source of truth, scope in/out, exclusions, interested parties, data/tenant boundaries, standards lenses and protected items. Reassess context when app type, customer need, tenant model, data class, tool route or release scope changes.

## Outputs/records
Context linkage record, source lock, scope boundary, interested-party notes, protected-scope confirmation and gate decision.

## Linked ADP processes
ADP-01, ADP-02, ADP-03, ADP-05, ADP-09, ADP-10, ADP-18, ADP-21.

## Linked MOP/COP/SOP processes
Clause 4 context, Clause 5 authority, Clause 6 risk planning, Clause 7 documented information, Clause 8 operation, Clause 9 audit and Clause 10 improvement.

## Linked skills/WIs
Context lock, source-of-truth lock, scope lock, PESTLE/SWOT, interested-party analysis, standards applicability, evidence audit.

## Linked gates
Intake gate, context gate, requirements gate, risk/security gate, build-instruction gate, release gate and improvement gate.

## Evidence required
Repo/branch/commit, current job card, context pack, app/customer/tenant/data boundary, interested-party record, standards source status and protected-scope statement.

## Risks
Stale context, wrong repo/branch, scope creep, unsupported standards claim, customer-data exposure, old drafts treated as truth, protected scope touched.

## Controls
No app work proceeds without active source lock and scope boundary. SOURCE REQUIRED and CUSTOMER SOURCE REQUIRED apply where standards/customer requirements are not supplied.

## Interfaces
App owner, process owner, context specialist, standards specialist, security/data reviewer, GitHub controller, QA gatekeeper.

## Context linkage matrix
| ADP process | Context input | Source of truth | Scope boundary | Interested party | Evidence required | Gate impact |
|---|---|---|---|---|---|---|
| ADP-01 | Opportunity/request | Request record | Initial in/out | App owner | Intake record | Intake PASS/HOLD |
| ADP-02 | Repo/source state | Repo/commit/context pack | Active truth only | Builder/reviewer | Source lock | Context PASS/HOLD/BLOCK |
| ADP-03 | Process/domain truth | Process owner evidence | Domain only | Process owner | Domain record | Domain gate |
| ADP-04 | Operator workflow | User/operator evidence | User flow | Operator/user | Workflow capture | Workflow gate |
| ADP-05 | Requirements | Acceptance criteria | Approved scope | App owner/user | Acceptance record | Requirements gate |
| ADP-06 | Runtime route | Runtime map | Module boundaries | Runtime architect | Runtime evidence | Runtime gate |
| ADP-09 | Tenant/data/security | Risk/security review | Protected data | Customer/security | Risk evidence | Risk gate |
| ADP-10 | Build instruction | Job card | Scope in/out | Builder/tool | Prompt packet | Build gate |
| ADP-18 | Release context | Release pack | Release scope | Support/customer | Release/rollback evidence | Release gate |
| ADP-21 | Failure/lesson | NC/RCA/CAPA | Improvement scope | Process/knowledge owners | Improvement record | Clause 10 gate |

## PASS/HOLD/BLOCKED rules
PASS when active context and source truth are evidenced. HOLD when context is incomplete. BLOCKED when protected scope, customer data, wrong repo/branch or unsupported claim risk exists.

## Escalation
Escalate stale source, missing customer source, protected-scope conflict or app build request without context lock.

## Update trigger
New request, source change, customer requirement, data/tenant change, tool change, release request or RCA/CAPA.
