# MASTER_AGENT_REGISTER

## Purpose
Define the approved agents, workers and specialists used by the Software Build Management System and app-development operating model.

## Scope
All management-system, app-development, audit, validation, release, support, improvement and automation-readiness work.

## Owner/agent
VIF Orchestrator owns the register. QA Gatekeeper controls gate authority consistency.

## Inputs
ADP process register, WI_001 to WI_030, Clause 9/10 controls, operating-model workstations, risk profile, MLA status and protected-scope rules.

## Activities/method
Maintain each agent role, purpose, required competence, allowed work, prohibited work, evidence output, linked gates, escalation triggers and MLA maturity dependency. Roles may be human, AI-assisted, tool-based or specialist review stations, but accountability remains assigned to the responsible owner.

## Outputs/records
Master agent register, role boundaries, competence expectations, evidence outputs and audit triggers.

## Linked processes
MOP governance, Clause 4-10 management processes, ADP-01 to ADP-21 app-development processes, support and improvement loops.

## Linked skills/WIs
WI_001 to WI_030.

## Linked gates
Context, scope, source, risk, job-card, build, review, verification, validation, release, NC/RCA/CAPA, MLA, app onboarding, GitHub CI and n8n readiness gates.

## Evidence required
Role assignment, competence/maturity record, work output evidence, gate decision evidence and audit record where applicable.

## Risks
Undefined accountability, specialist bypass, AI/tool overreach, false PASS, customer-facing claim without approval, protected-scope breach.

## Controls
Every controlled activity must have a named owner/agent and gate authority. AI/tools assist work but do not own accountability.

## Interfaces
Process owners, skill/WI owners, QA, audit, RCA/CAPA, release, security/data, app owner, users/operators, CI/n8n controllers.

## Agent register
| Agent/specialist | Purpose | Allowed work | Prohibited work | Evidence output | MLA baseline |
|---|---|---|---|---|---|
| VIF Orchestrator | Route and coordinate controlled work | Job cards, routing, scope control | Direct app code changes without approved job card | Job card/gate record | M2 |
| QA Gatekeeper | Decide evidence gates | PASS/HOLD/BLOCK decisions | PASS without evidence | Gate decision | M2 |
| Credit-Burn Controller | Control tool/cost waste | Cost/routing review | Block required safety work blindly | Credit-risk note | M1 |
| Process Engineer | Process/turtle/interface design | Process maps, turtles, interfaces | Release approval alone | Process evidence | M2 |
| Runtime Architect | Runtime-first control | Runtime objects/states/actions | UI-only PASS | Runtime map | M2 |
| Internal Audit Specialist | Audit controls | Audit findings and reports | Implement audited changes | Audit record | M2 |
| RCA/CAPA Specialist | Problem solving | RCA/CAPA/effectiveness review | Guess root cause | RCA/CAPA evidence | M2 |
| Management Review Owner | Management review actions | Review decisions/actions | Ignore critical findings | MR action record | M2 |
| MLA Assessor | Maturity decisions | M0-M5 assessment | Overstate maturity | MLA record | M2 |
| ISO 9001/9002 Guidance Specialist | QMS guidance lens | Interpretation support | Compliance claim without source | Guidance note | M1 |
| ISO 9004 Maturity/Sustained Success Specialist | Maturity lens | Maturity/self-assessment advice | Certification claim | Maturity note | M1 |
| IATF 16949 Process Discipline Specialist | Automotive discipline lens | Process/change/defect-prevention guidance | Use customer-specific rules without source | Process discipline note | M1 |
| ISO/IEC 27001 Security Specialist | Security lens | Security risk guidance | Security claim without evidence | Security note | M1 |
| ISO 31000/31010 Risk Specialist | Risk method lens | Risk criteria/technique guidance | Risk acceptance alone | Risk method note | M1 |
| ISO/IEC 42001 AI Management Specialist | AI management lens | AI risk/oversight guidance | AI compliance claim | AI risk note | M1 |
| AI Model/Tool Auditor | Audit AI tools/models | Tool suitability reviews | Approve unsafe data use | AI tool audit | M2 |
| AI Output Auditor | Verify AI outputs | Output verification | Treat AI output as truth | AI output audit | M2 |
| Prompt Audit Specialist | Prompt quality/audit | Prompt review, drift findings | Broad implementation approval | Prompt audit | M2 |
| Context Management Specialist | Context/source lock | Context packs/source truth | Release approval alone | Context record | M2 |
| UI/UX Interface Reviewer | UI/process-fit review | UI usability/layout review | Backend/RLS approval | UI review | M1 |
| Database/RLS/Supabase Reviewer | DB/RLS proof | Backend/RLS evidence review | UI-only security claim | RLS proof | M2 |
| Security/Data Protection Reviewer | Data/security boundary | Security/data review | Customer data in unapproved tools | Security evidence | M2 |
| Release/Configuration Controller | Release/version control | Release/rollback/config control | Release without evidence | Release record | M3 |
| GitHub CI Controller | CI governance | Manual/read-only CI review | App-repo CI before onboarding | CI readiness record | M2 |
| n8n Automation Controller | n8n readiness | Design/readiness only until approved | Auto-fix/auto-merge/auto-release | n8n readiness record | M1 |
| Tool/Supplier Reviewer | Tool/provider control | Provider/tool risk review | Unapproved provider use | Supplier/tool audit | M2 |
| Organisational Knowledge Controller | Knowledge control | Knowledge updates | Store unverified claims | Knowledge record | M2 |
| Lessons Learned Controller | Lessons/effectiveness | Lesson updates | Note-only lessons | Lesson record | M2 |
| App Owner | Own app value | Acceptance/release input | Technical PASS alone | Acceptance record | M1 |
| Process Owner | Own process truth | Domain/process approval | Code release alone | Process truth evidence | M1 |
| Operator/User Tester | User workflow evidence | UAT/user feedback | Release approval alone | UAT evidence | M1 |
| Frontend Coder | UI implementation | Scoped frontend build | Backend/RLS claims | Code diff | M2 |
| Backend Coder | Backend logic | Scoped backend build | Unapproved RLS/schema change | Backend diff | M2 |
| Supabase/RLS Engineer | DB/RLS implementation/review | RLS/schema proof | Production change without gate | DB/RLS evidence | M2 |
| Device/Integration Specialist | Device/integration flow | Integration review/proof | Unsupported integration claim | Integration evidence | M2 |

## PASS/HOLD/BLOCKED rules
PASS when agent role, boundaries, evidence output and maturity expectation are defined. HOLD when competence/evidence is incomplete. BLOCKED when uncontrolled work is attempted without assigned agent or authority.

## Escalation
Escalate false PASS, missing evidence, scope drift, security/RLS risk, customer-data risk, failed validation, tool/provider failure, repeated repair failure or prohibited automation.

## MLA / maturity dependency
M0 unassigned; M1 draft role; M2 pilot/controlled role; M3 released role; M4 managed with KPIs/audit; M5 optimised and automation candidate where permitted.

## Update trigger
New role, process change, tool change, audit finding, RCA/CAPA, maturity change or app onboarding request.
