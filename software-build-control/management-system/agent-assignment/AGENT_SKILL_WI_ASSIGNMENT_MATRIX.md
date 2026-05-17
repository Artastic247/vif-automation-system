# AGENT_SKILL_WI_ASSIGNMENT_MATRIX

## Purpose
Map agents and specialists to WI_001 to WI_030 so every skill/work instruction has accountable ownership and execution support.

## Scope
All released or structurally complete work instructions under management-system/work-instructions/.

## Owner/agent
Skill/WI Audit Specialist with VIF Orchestrator.

## Inputs
WI_001 to WI_030, master agent register, process assignments, maturity levels and audit findings.

## Activities/method
Assign primary owner, supporting agent, evidence output and gate link to each WI. If WI ownership is missing, the WI remains HOLD for operational use.

## Outputs/records
Agent-to-WI assignment matrix and WI ownership record.

## Linked processes
All MOP/COP/SOP and ADP processes that use WI_001 to WI_030.

## Linked skills/WIs
WI_001 through WI_030.

## Linked gates
Skill/WI release gate, execution gate, audit gate and maturity gate.

## Evidence required
WI assignment, owner competence, use evidence and audit evidence.

## Risks
WI exists but no owner, untrained agent executes WI, WI not audited, inconsistent method use.

## Controls
Each WI has primary owner and supporting reviewer. Operational use requires maturity and evidence.

## Interfaces
Skill/WI owner, Process Owner, QA Gatekeeper, Internal Audit Specialist and Knowledge Controller.

## WI assignment matrix
| WI | Primary owner/agent | Supporting agent/specialist | Evidence output | Gate link |
|---|---|---|---|---|
| WI_001_CONTEXT_LOCK | Context Management Specialist | VIF Orchestrator | Context lock record | Context gate |
| WI_002_SCOPE_LOCK | VIF Orchestrator | QA Gatekeeper | Scope lock record | Scope gate |
| WI_003_SOURCE_OF_TRUTH_LOCK | Context Management Specialist | GitHub Controller | Source lock record | Source gate |
| WI_004_PROCESS_MAPPING | Process Engineer | Process Owner | Process map/turtle | Process gate |
| WI_005_INTERFACE_MAPPING | Process Engineer | QA Gatekeeper | Interface map | Interface gate |
| WI_006_PDCA_REVIEW | Process Engineer | CI Owner | PDCA review | PDCA gate |
| WI_007_RISK_OPPORTUNITY_REVIEW | Risk Specialist | Security/Data Reviewer | Risk record | Risk gate |
| WI_008_PROMPT_QUALITY_REVIEW | Prompt Audit Specialist | VIF Orchestrator | Prompt review | Prompt gate |
| WI_009_PROMPT_AUDIT | Prompt Audit Specialist | AI Output Auditor | Prompt audit | Audit/NC gate |
| WI_010_CONTEXT_PACK_AUDIT | Context Management Specialist | Evidence Auditor | Context audit | Context audit gate |
| WI_011_RUNTIME_FIRST_REVIEW | Runtime Architect | Process Owner | Runtime review | Runtime gate |
| WI_012_UI_INTERFACE_REVIEW | UI/UX Interface Reviewer | Operator/User Tester | UI review | UI gate |
| WI_013_DATA_TABLE_GRID_REVIEW | UI/UX Interface Reviewer | Database/RLS Reviewer | Table/grid review | UI/backend gate |
| WI_014_DATABASE_RLS_PROOF | Supabase/RLS Engineer | Security/Data Reviewer | DB/RLS proof | Backend/RLS gate |
| WI_015_PROTECTED_ACTION_BACKEND_ENFORCEMENT | Runtime Architect | Supabase/RLS Engineer | Protected-action proof | Security gate |
| WI_016_MIGRATION_REPLAY_ROLLBACK_SAFETY | Supabase/RLS Engineer | Release Controller | Migration safety record | Migration/release gate |
| WI_017_VERIFICATION_REVIEW | QA Gatekeeper | Evidence Auditor | Verification review | Verification gate |
| WI_018_VALIDATION_UAT_REVIEW | Operator/User Tester | App Owner | UAT record | Validation gate |
| WI_019_RELEASE_ROLLBACK_REVIEW | Release/Configuration Controller | QA Gatekeeper | Release/rollback review | Release gate |
| WI_020_MOCK_DEMO_DATA_BOUNDARY | Security/Data Reviewer | App Owner | Data-boundary record | Data/evidence gate |
| WI_021_INTERNAL_AUDIT | Internal Audit Specialist | Specialist Auditors | Audit report | Audit gate |
| WI_022_MLA_ASSESSMENT | MLA Assessor | QA Gatekeeper | MLA assessment | Maturity gate |
| WI_023_RCA | RCA/CAPA Specialist | Process Owner | RCA record | RCA gate |
| WI_024_CAPA_EFFECTIVENESS_REVIEW | RCA/CAPA Specialist | CI Owner | Effectiveness record | CAPA gate |
| WI_025_CONTINUAL_IMPROVEMENT | Continual Improvement Owner | Management Review Owner | Improvement action | CI gate |
| WI_026_LESSONS_LEARNED_UPDATE | Lessons Learned Controller | Knowledge Controller | Lesson record | Lessons gate |
| WI_027_ORGANISATIONAL_KNOWLEDGE_UPDATE | Organisational Knowledge Controller | Standards/Tool owners | Knowledge update | Knowledge gate |
| WI_028_VALIDATOR_CALIBRATION | Validator/Checker Auditor | QA Gatekeeper | Calibration record | Validator gate |
| WI_029_APP_ONBOARDING_READINESS | VIF Orchestrator | App/Product Auditor | Onboarding readiness record | App onboarding gate |
| WI_030_CI_N8N_READINESS_REVIEW | GitHub CI Controller / n8n Controller | MLA Assessor, QA Gatekeeper | CI/n8n readiness record | Automation gate |

## PASS/HOLD/BLOCKED rules
PASS when every WI has owner, support and evidence output. HOLD when use/competence evidence is incomplete. BLOCKED when critical WI lacks owner for active work.

## Escalation
Escalate unowned WI, repeated WI failure, agent misuse, false PASS or missing evidence.

## MLA / maturity dependency
M1 draft WI; M2 pilot WI; M3 released WI; M4 managed WI with audit/KPI; M5 optimised WI eligible for limited automation.

## Update trigger
New WI, WI revision, role change, audit finding, RCA/CAPA or maturity change.
