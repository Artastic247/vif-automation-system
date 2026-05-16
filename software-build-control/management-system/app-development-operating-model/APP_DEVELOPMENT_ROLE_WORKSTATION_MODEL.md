# APP_DEVELOPMENT_ROLE_WORKSTATION_MODEL

## Purpose
Define software-factory workstations used to build and control apps.

## Scope
Management/control, build, specialist, test/assurance and support stations.

## Owner/agent
VIF Orchestrator.

## Inputs
ADP process register, maturity level, job card, risk profile, tool route and required evidence.

## Activities/method
Assign workstations by process stage and risk. Do not activate every specialist by default.

## Outputs/records
Workstation assignment record, evidence outputs and gate responsibilities.

## Linked process
ADP process architecture.

## Linked skills/WIs
Role-specific WIs in linkage matrix.

## Linked gates
Process gates and release gates.

## Evidence required
Assignment matrix, output evidence and gate decision.

## Risks
Wrong workstation, unsupported tool route, coder bypasses reviewer, specialist missing.

## Controls
Each workstation has allowed work, prohibited work, input, output, evidence, gate responsibility, escalation and maturity requirement.

## Interfaces
Workstation handoffs in handoff/interface maps.

## Workstation model
| Station family | Workstation | Purpose | Allowed work | Prohibited work | Required input | Required output | Evidence produced | Gate responsibility | Escalation trigger | Maturity requirement |
|---|---|---|---|---|---|---|---|---|---|---|
| Management/control | VIF Orchestrator | Route/control work | Job cards, gates | Code changes | Request/context | Approved route | Job card | Intake/context | Scope drift | M1+ |
| Management/control | Product/App Owner | Own app value | Acceptance | Unapproved release | Request | Acceptance | Requirements | Requirements | Value conflict | M1+ |
| Management/control | Process Owner | Own process truth | Process approval | Code edits | Domain data | Process truth | Approval | Domain gate | Truth gap | M1+ |
| Management/control | QA Gatekeeper | Evidence gate | PASS/HOLD/BLOCK | Release without proof | Evidence | Gate decision | Verification | Verification | False PASS | M2+ |
| Management/control | Release Controller | Release/rollback | Release review | Unsafe release | UAT/release pack | Release decision | Release record | Release | Rollback gap | M3+ |
| Management/control | Configuration Controller | Version/config | Version control | Untracked config | Commit/version | Config record | Config evidence | Release | Version drift | M2+ |
| Management/control | Credit-Burn Controller | Cost discipline | Tool spend review | Block safety work blindly | Tool plan | Cost risk | Cost note | Tool route | Credit waste | M1+ |
| Build | App Architect | App structure | Architecture | Skip runtime | Requirements | Architecture | Architecture map | Design | Architecture drift | M2+ |
| Build | Runtime Architect | Runtime depth | Runtime object/state | UI-only PASS | Requirements | Runtime map | Runtime evidence | Runtime | No runtime object | M2+ |
| Build | Frontend Coder | UI build | Frontend change | Backend/RLS claims | Job card | UI diff | Code diff | Build | Scope drift | M2+ |
| Build | Backend Coder | Backend logic | Service/data logic | Unsafe RLS | Job card | Backend diff | Code diff | Build | Data risk | M2+ |
| Build | Supabase/RLS Engineer | DB/RLS | RLS/design review | Blind migration | Data concept | RLS evidence | RLS proof | Backend | RLS risk | M2+ |
| Build | Integration Engineer | Integrations | Integration design | Unapproved provider | Interface map | Integration proof | Integration evidence | Integration | Provider risk | M2+ |
| Build | Prompt Engineer | Prompt packets | Bound prompts | Broad prompts | Job card | Prompt packet | Prompt evidence | Prompt | Prompt drift | M1+ |
| Build | Lovable Builder | UI/app scaffold | Scoped build | Whole-app jump | Prompt packet | Build output | Lovable output | Build | Scope drift | M2+ |
| Build | Codex Implementer | Code implementation | Scoped code changes | App repo without gate | Job card | Patch/PR | Diff evidence | Build | Unsafe diff | M2+ |
| Build | Claude Code Reviewer | Review/code reasoning | Review | Direct release | Diff | Review findings | Review record | Review | Missed risk | M2+ |
| Build | GitHub Controller | Repo ops | Branch/commit ops | App CI activation | Approved route | Repo evidence | Commit evidence | Config | Wrong branch | M2+ |
| Specialist | Domain Specialist | Domain truth | Domain review | Code release | Process input | Domain note | Truth evidence | Domain | Domain gap | M1+ |
| Specialist | Compliance/ISO/IATF Specialist | Standards lens | Guidance | Compliance claim | Source | Gap note | Review note | Risk | SOURCE REQUIRED | M1+ |
| Specialist | AI Governance Specialist | AI controls | AI review | Approve unsafe AI | AI use | AI decision | AI evidence | AI gate | AI risk | M1+ |
| Specialist | Security/Data Protection Specialist | Data/security | Security review | Ignore data risk | Data map | Security finding | Risk evidence | Security | Data exposure | M2+ |
| Specialist | UI/UX Specialist | Usability | UI review | Backend proof | UI concept | UI decision | UI evidence | UI gate | Usability risk | M1+ |
| Specialist | Operator Workflow Specialist | Operator flow | Workflow capture | Assume workflow | User input | Workflow evidence | Workflow record | Workflow | Operator mismatch | M1+ |
| Specialist | Device/Integration Specialist | Device flow | Device/integration review | Unsupported integration | Device need | Integration route | Device evidence | Integration | Device risk | M2+ |
| Test/assurance | Unit Test Owner | Unit tests | Test design | Skip tests | Code | Test output | Test report | Test | Failed tests | M2+ |
| Test/assurance | Integration Test Owner | Integration tests | Test execution | Claim integration | Build | Integration result | Test evidence | Test | Integration fail | M2+ |
| Test/assurance | UAT Coordinator | UAT | Coordinate UAT | Sign off alone | Verified build | UAT record | UAT evidence | Validation | UAT fail | M2+ |
| Test/assurance | Process-Owner Validator | Process fit | Validate fit | Code edit | UAT build | Signoff | Validation evidence | Validation | Process misfit | M2+ |
| Test/assurance | Operator/User Tester | Usability | User testing | Release approval alone | UAT build | Feedback | UAT notes | Validation | User rejection | M1+ |
| Test/assurance | Evidence Auditor | Evidence quality | Audit evidence | Invent evidence | Records | Finding | Audit record | Evidence | False PASS | M2+ |
| Test/assurance | Release Auditor | Release audit | Release evidence review | Deploy | Release pack | Finding | Audit record | Release | Rollback gap | M2+ |
| Test/assurance | RCA/CAPA Specialist | Problem solving | RCA/CAPA | Guess causes | NC | RCA/CAPA | RCA evidence | Improvement | Repeat failure | M2+ |
| Test/assurance | Lessons Learned Controller | Learning | Update lessons | Ignore recurrence | RCA/CAPA | Lesson update | LL evidence | Improvement | Repeat issue | M2+ |
| Support | Support Owner | Support route | Support handling | Release change | Handover | Support record | Support evidence | Support | No support | M2+ |
| Support | Incident Owner | Incident control | Incident classify | Uncontrolled fix | Support issue | Incident record | Incident evidence | Incident | Critical incident | M2+ |
| Support | Maintenance Owner | Maintenance | Maintenance plan | Feature creep | Support data | Maintenance record | Maintenance evidence | Maintenance | Drift | M2+ |
| Support | Customer Change Owner | Customer changes | Change intake | Direct build | Request | Change record | Change evidence | Change | Uncontrolled change | M2+ |
| Support | Knowledge Controller | Knowledge | Update knowledge | Stale docs | Lesson | Knowledge record | Knowledge evidence | Knowledge | Stale guidance | M2+ |

## PASS/HOLD/BLOCKED rules
PASS when station is assigned and evidence produced. HOLD when role/evidence is incomplete. BLOCKED when prohibited work is attempted.

## Escalation
Escalate wrong workstation, unapproved tool use, protected-scope breach or missing evidence.

## Update trigger
New tool, role, app type, process change or audit finding.
