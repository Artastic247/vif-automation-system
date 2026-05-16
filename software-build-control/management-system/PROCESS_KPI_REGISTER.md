# PROCESS_KPI_REGISTER.md

## Purpose
Define process-level KPIs and performance measures so the Software Build Control System can evaluate effectiveness, not only file presence.

## Scope
All MOP, COP and SOP processes.

## Inputs
PROCESS_REGISTER, PROCESS_OWNER_MATRIX, GATE_CHECKLISTS, VERIFICATION_REGISTER, RELEASE_REGISTER, audit findings, incidents and lessons learned.

## Activities/checklist
Maintain at least one KPI or performance measure per process. KPIs must be reviewed during management review and used for corrective action where needed.

| Process ID | Process name | KPI/performance measure | Target or review rule | Evidence source | Owner | Review cadence | Escalation trigger |
|---|---|---|---|---|---|---|---|
| MOP-01 | Context and interested-party management | Context review current % | Review after major app/tool/customer change | Context record | VIF Orchestrator | Quarterly/triggered | Context missing for risky work |
| MOP-02 | Leadership and governance | Processes with accountable owner % | 100% | Owner matrix | System owner | Quarterly | Owner missing |
| MOP-03 | Strategic planning, objectives, risk and opportunity | Risk actions closed on time % | Review trend | Risk register | System owner | Monthly/quarterly | Critical risk overdue |
| MOP-04 | AI governance and tool-use policy | AI/tool failure and rework rate | Trend down | Lessons/tool records | AI Governance Owner | Monthly | Data/tool misuse |
| MOP-05 | Internal audit | Audit plan completion and findings closure % | Review trend | Audit records | QA Gatekeeper | Per programme | Critical finding open |
| MOP-06 | Management review | Management-review action closure % | Review trend | Review actions | System owner | Scheduled | Overdue strategic action |
| MOP-07 | Corrective action and continual improvement | Repeat defect rate | Trend down | CA/lessons records | QA Gatekeeper | Monthly | Repeat critical defect |
| COP-01 | App intake and classification | Intake completeness % | 100% before build | Intake checklist | VIF Orchestrator | Per request | Build requested with incomplete intake |
| COP-02 | Source-of-truth and context lock | Wrong repo/branch/context events | Zero | Baseline evidence | Codex Repo Inspector | Per job card | Source mismatch |
| COP-03 | Requirements and acceptance criteria | Requirements rework rate | Trend down | Job card/UAT | Product owner | Per job card | Acceptance unclear |
| COP-04 | UI/interface design control | UI rework due to missing screen map | Trend down/zero | SCREEN_MAP review | UI Reviewer | Per UI change | UI build without screen map |
| COP-05 | Data table/grid specification | Table/grid defect rate | Trend down | DATA_TABLE_SPEC/test results | Runtime Architect | Per table change | Missing column/source mapping |
| COP-06 | Workflow/runtime specification | Runtime defect rate | Trend down | RUNTIME_MAP/verification | Runtime Architect | Per workflow | Runtime object/state undefined |
| COP-07 | Database/backend/RLS design control | Backend/RLS findings | Zero critical | DB/RLS evidence | Supabase Reviewer | Per backend change | RLS/security defect |
| COP-08 | Environment and tenant setup | Data-mix or tenant-exposure events | Zero | Tenant register | Security/RLS Reviewer | Per rollout | Real data risk |
| COP-09 | Job card creation and approval | Scope drift rate | Trend down/zero | Job card/diff review | VIF Orchestrator | Per job card | Out-of-scope work |
| COP-10 | Build/modification control | Build pass rate and out-of-scope diff count | Build pass; zero prohibited diff | Build/diff records | Assigned worker | Per build | Prohibited file change |
| COP-11 | Verification | Verification evidence completeness % | 100% before release | VERIFICATION_REGISTER | QA Gatekeeper | Per change | Missing critical evidence |
| COP-12 | Validation/UAT | UAT rejection rate and unresolved UAT issues | Review trend | UAT record | Product/customer owner | Per release | UAT rejected |
| COP-13 | Tenant rollout | Rollback/incident rate during rollout | Trend down; zero critical | Tenant rollout record | Release Controller | Per rollout | Tenant exposure incident |
| COP-14 | Release and rollback | Release success rate and rollback readiness % | 100% rollback readiness | RELEASE_REGISTER | GitHub Release Controller | Per release | Rollback route missing |
| COP-15 | App support and maintenance | Open issue ageing and maintenance action closure | Review trend | Maintenance records | App owner | Monthly | Critical support item overdue |
| COP-16 | Customer change control | Change cycle time and UAT closure | Review trend | Change register | Change owner | Per change/monthly | Customer approval missing |
| SOP-01 | Documented information control | Obsolete/uncontrolled document count | Zero critical | Document records | System owner | Quarterly | Wrong document used |
| SOP-02 | Organisational knowledge control | Reusable knowledge reviewed % | Review cadence met | Knowledge register | Process Engineer | Quarterly | Knowledge unreviewed |
| SOP-03 | Competence and skill control | Competence gap count | Critical gaps closed | Skill/competence records | System owner | Quarterly | Worker lacks required skill |
| SOP-04 | Agent/worker control | Agent scope-drift events | Zero critical | Agent/tool records | VIF Orchestrator | Monthly | Worker bypasses gate |
| SOP-05 | Tool routing and tool qualification | Tool failure/re-route rate | Review trend | Tool routing records | VIF Orchestrator | Monthly | Wrong tool used |
| SOP-06 | Prompt control and prompt quality | Prompt failure rate | Trend down | Prompt records | Prompt Reviewer | Monthly | Prompt drift causes rework |
| SOP-07 | Evidence and record control | Evidence gap rate | Zero before release | Evidence records | QA Gatekeeper | Per gate | False PASS risk |
| SOP-08 | Security, tenant and data protection control | Data/security incident count | Zero critical | Security records | Security/RLS Reviewer | Per change/monthly | Data exposure risk |
| SOP-09 | Configuration and version control | Wrong version/baseline events | Zero | Git/release records | GitHub Release Controller | Per job/release | Version unknown |
| SOP-10 | Contingency and continuity control | Recovery time and unresolved contingency actions | Review trend | Contingency records | VIF Orchestrator | Per incident/quarterly | No recovery route |
| SOP-11 | Supplier/tool-provider control | Tool/provider outage impact events | Review trend | Provider records | System owner | Quarterly | Critical provider dependency unmanaged |
| SOP-12 | Lessons learned and knowledge reuse | Lessons converted into controls % | 100% for critical lessons | Lessons register | Lessons Controller | Monthly | Repeat failure without control update |

## Outputs/records
KPI register, performance review input, escalation records and management review input.

## Owner/tool
System owner maintains. Process owners update measures. QA Gatekeeper verifies evidence quality.

## Gate controlled
Performance evaluation and management review gate.

## PASS/HOLD/BLOCKED rules
- PASS: every process has a measure, owner, evidence source and review rule.
- HOLD: measure exists but target/cadence/evidence is incomplete.
- BLOCKED: critical process has no performance measure or no escalation route.

## Update trigger
New process, KPI change, management review, audit finding, recurring defect, CI activation or lesson learned.
