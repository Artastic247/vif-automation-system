# CONTINGENCY_PLAN.md

## Purpose
Define practical recovery routes for app-development disruptions before they become uncontrolled rework, customer impact, data exposure, or false release confidence.

## Scope
Applies to AI-assisted app development, repair, verification, validation, release, tenant rollout, support, and maintenance. This document does not authorise app-code, Supabase, RLS, deployment, customer-data, or n8n changes by itself.

## Inputs
- Approved request, defect, release, pilot, or incident.
- Current app context, repo, branch, version, environment, tenant, and rollback evidence.
- Tool output, logs, build/test evidence, user/customer feedback, or incident evidence.

## Activities/checklist
For each contingency record: trigger, risk, immediate containment, owner/tool, decision gate, recovery route, rollback route, evidence required, and lesson learned update.

| Contingency | Trigger | Risk | Immediate containment | Owner/tool | Decision gate | Recovery route | Rollback route | Evidence required | Lesson learned update required |
|---|---|---|---|---|---|---|---|---|---|
| Lovable credit burn / failed generation | Repeated failed generations or broad drift | Cost, scope, partial code | Stop Lovable; freeze scope | Credit-Burn Controller | Tool routing | Move to Codex/review | Revert generated diff | Prompt/history/diff | Yes |
| Codex/Claude/GPT/Gemini tool failure | Tool unavailable, wrong output, hallucination | Wrong repair or delay | Stop and re-route | VIF Orchestrator | Tool routing | Use alternate tool with same job card | Revert if files changed | Tool output | Yes |
| Model context loss / truncation | Missing scope/history/source truth | Wrong assumptions | Rebuild context pack | VIF Orchestrator | Context lock | Restore from artefacts | None if no code changed | APP_CONTEXT/job card | Yes |
| Wrong repo or wrong branch | Repo/branch mismatch | Wrong baseline modified | Stop immediately | GitHub Release Controller | Baseline | Confirm correct repo/branch | Revert wrong branch commit | Git evidence | Yes |
| Failed build | Build command fails | Broken package | Hold build gate | QA Gatekeeper | Build | Create bounded fix card | Revert failed diff | Build log | Yes |
| Failed test | Regression/unit/UAT test fails | Unsafe release | Hold verification | QA Gatekeeper | Verification | Fix under new job card | Revert if needed | Test log | Yes |
| Failed deployment | Deploy fails or wrong deploy target | Outage/release block | Hold release | GitHub Release Controller | Release | Restore last stable deploy | Previous deployment | Deploy log | Yes |
| Broken migration | Migration fails or corrupts model | Data loss/outage | Stop migration; backup state | Supabase Backend Reviewer | DB/RLS | Corrective migration | Restore/PITR only if authorised | Migration logs | Yes |
| RLS/security defect | Unauthorised or cross-tenant access | Data exposure | Disable feature/access | Security/RLS Reviewer | Runtime/backend | Patch RLS under job card | Feature flag/deploy rollback | RLS test evidence | Yes |
| Tenant data exposure risk | Tenant boundary unclear or breached | Customer data leakage | Stop access; quarantine evidence | Security/RLS Reviewer | Tenant/data | Re-verify RLS and tenant IDs | Disable exposure | Tenant/RLS proof | Yes |
| Customer data accidentally used in dev | Real data detected in dev/demo | Data protection risk | Quarantine/remove data | Security/RLS Reviewer | Environment | Sanitise/reseed | Restore clean dev | Data handling record | Yes |
| Supabase unavailable | DB/auth/functions unavailable | Testing/release blocked | Stop release | Supabase Backend Reviewer | Environment | Wait/failover/manual evidence | Disable feature exposure | Status/logs | Yes |
| GitHub unavailable | Repo/PR/CI unavailable | No version-control evidence | Stop build/release | GitHub Release Controller | Baseline/release | Resume after access restored | None | Access/status evidence | Yes |
| Lost rollback route | Previous version unknown | Unsafe release | Block release | QA Gatekeeper | Rollback | Reconstruct version path | No release | Commit/deploy evidence | Yes |
| App feature rejected in pilot | Pilot user/customer rejects | Failed validation | Disable pilot exposure | Release Controller | Validation/UAT | Return to backlog/problem solving | Feature flag/deploy rollback | UAT feedback | Yes |
| Urgent production defect | High-risk live defect | Customer impact | Contain and classify emergency | VIF Orchestrator | Emergency | COMMANDER job card | Last stable version | Incident evidence | Yes |
| Prompt drift / bad instruction | Tool works outside scope | Uncontrolled change | Stop tool | Prompt Quality Reviewer | Job-card | Rewrite instruction | Revert diff | Prompt/diff | Yes |
| AI tool modifies out-of-scope files | Diff includes prohibited files | Regression/security risk | Reject change | Codex Repo Inspector | PR/review | New bounded patch | Revert file/commit | Diff evidence | Yes |
| Release blocked by missing evidence | Verification incomplete | False PASS | Hold release | QA Gatekeeper | Release | Collect missing evidence | No release | Verification register | Yes |
| User/customer UAT rejection | UAT rejects outcome | Failed validation | Hold rollout | Product owner | Validation/UAT | Return to job card/backlog | Disable feature exposure | UAT record | Yes |

## Outputs/records
Contingency record, containment evidence, rollback evidence, incident/change/job-card link, and lessons-learned update.

## Owner/tool
VIF Orchestrator owns routing. QA Gatekeeper owns verification/release holds. Security/RLS Reviewer owns data/RLS contingencies. GitHub Release Controller owns version and rollback evidence. Supabase Backend Reviewer owns database/backend evidence.

## Gate controlled
Contingency, rollback, release, tenant rollout, security/RLS, and emergency gates.

## PASS/HOLD/BLOCKED rules
- PASS: trigger, owner, containment, recovery, rollback, evidence, and lesson update are clear.
- HOLD: evidence or owner is incomplete but no unsafe action is underway.
- BLOCKED: data exposure, destructive change, missing rollback, wrong repo/branch, or release without evidence.

## Update trigger
Any incident, failed generation, failed build/test/deploy, RLS issue, tenant/data concern, pilot rejection, urgent defect, tool drift, or release hold.
