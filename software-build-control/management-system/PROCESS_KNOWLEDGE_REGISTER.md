# PROCESS_KNOWLEDGE_REGISTER.md

## Purpose
Capture reusable process knowledge for app modules, development controls, tool routing, known failure modes, approved methods, skills, agents, and lessons learned.

## Scope
Applies to app-development process knowledge across DOS FMEA, SPC, QMS, MSA, APQP, QCPro, future apps, and the Software Build Control System. This register stores controlled knowledge only; it must not store customer secrets, credentials, or uncontrolled customer data.

## Inputs
- Process maps, workflow catalogue, lessons learned, incidents, gate reviews, app baseline records, customer feedback, and tool-review findings.

## Activities/checklist
Capture and review knowledge using this structure:

| Process name | App/module affected | Source of knowledge | Current approved method | Related templates | Related skills | Related agents | Known failure modes | Lessons learned | Last review date | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| App intake | All apps | Gate reviews and recovery findings | Use APP_INTAKE_CHECKLIST before planning | APP_CONTEXT, CURRENT_JOB_CARD | Context lock, scope lock | VIF Orchestrator | Missing repo/branch/source truth | No build before intake | TBD | System owner |
| UI/interface control | UI modules | Prior UI truncation and partial builds | Use SCREEN_MAP and DATA_TABLE_SPEC before UI build | SCREEN_MAP, DATA_TABLE_SPEC | UI/interface review | UI/Adaptive Reviewer | Dashboard-first, missing states | No UI build without screen map | TBD | UI reviewer |
| Backend/RLS control | Supabase apps | Tenant/RLS risk findings | Use RUNTIME_MAP and DATABASE_BACKEND_CONTROL before backend work | RUNTIME_MAP | Database/RLS review | Supabase Backend Reviewer | Frontend-only security, missing read/write proof | No backend claim without proof | TBD | Backend reviewer |
| Tenant rollout | Multi-tenant apps | Pilot/rollback concerns | Use TENANT_ROLLOUT_REGISTER before exposure | TENANT_ROLLOUT_REGISTER | Tenant rollout review | GitHub Release Controller | Real/demo/dev data mixing | Pilot before rollout | TBD | Release owner |
| Verification/release | All apps | False PASS risks | Use VERIFICATION_REGISTER and RELEASE_REGISTER before release | VERIFICATION_REGISTER, RELEASE_REGISTER | Verification review, release check | QA Gatekeeper | Missing build/test/backend evidence | No release without evidence | TBD | QA Gatekeeper |

## Outputs/records
Approved process knowledge, linked templates, skills, agents, known failure modes, and lessons learned updates.

## Owner/tool
Process Engineer owns structure. Lessons Learned Controller updates failure modes. Specialist owners update app/module knowledge. VIF Orchestrator ensures reuse before future work.

## Gate controlled
Process knowledge and reuse gate.

## PASS/HOLD/BLOCKED rules
- PASS: process knowledge has owner, approved method, related templates/skills/agents, known failure modes, and review status.
- HOLD: knowledge exists but owner or review date is missing.
- BLOCKED: knowledge contains secrets/customer data or authorises uncontrolled code/schema/release work.

## Update trigger
New app, new module, repeated failure, incident, successful recovery, release, customer feedback, tool drift, or lesson learned.
