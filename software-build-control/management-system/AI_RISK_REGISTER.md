# AI_RISK_REGISTER.md

## Purpose
Identify, assess and control AI-related risks in AI-assisted software development and management-system work.

## Scope
Applies to all AI tools and AI-supported outputs used for design, coding, review, verification, release support, automation, documentation and continual improvement.

## Owner/tool
AI Governance Owner owns the register. QA Gatekeeper owns false-PASS and evidence risk. Security/RLS Reviewer owns data, tenant and security risk. VIF Orchestrator owns tool-route control.

## Inputs
AI tool inventory, prompt failures, bad-output records, incidents, verification findings, audit findings, tool/model changes, data classification and lessons learned.

## Activities/fields
| Risk ID | AI risk | Cause | Effect | Severity | Likelihood | Detection | Current control | Required action | Owner | Status | Linked lesson learned |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AIR-001 | Hallucination | Model invents facts/code/standards | Wrong decision or false evidence | High | Medium | Human review/evidence check | Prompt quality and verification | Strengthen source-basis checks | QA Gatekeeper | Open | TBD |
| AIR-002 | False PASS | AI states work is complete without proof | Unsafe release/build confidence | High | Medium | Verification register | No AI-generated PASS without evidence | Enforce output verification | QA Gatekeeper | Open | TBD |
| AIR-003 | Context loss/truncation | Long chat/tool handoff | Wrong scope or stale decision | High | Medium | Context pack review | No-truncation WI | Improve context pack validation | VIF Orchestrator | Open | TBD |
| AIR-004 | Wrong repo/branch | Poor source lock | Patch/review wrong baseline | High | Low/Medium | Source-of-truth lock | Baseline gate | Require repo/branch evidence | Codex Repo Inspector | Open | TBD |
| AIR-005 | Uncontrolled code change | Broad prompt/tool overreach | Regression/security defect | High | Medium | Diff review/job card | Build gate | Block broad prompts | VIF Orchestrator | Open | TBD |
| AIR-006 | Unsafe schema/RLS suggestion | AI lacks full DB context | Data exposure/broken backend | Critical | Medium | DB/RLS gate | Database/backend control | Require RLS evidence | Security/RLS Reviewer | Open | TBD |
| AIR-007 | Customer-data exposure | Real data in prompt/tool | Confidentiality breach | Critical | Low/Medium | Data governance review | Customer-data restriction | Mask/anonymise or block | Security/RLS Reviewer | Open | TBD |
| AIR-008 | Prompt drift | Prompt expands beyond objective | Scope creep/rework | Medium | Medium | Prompt checklist | Forbidden patterns | Log prompt failures | Prompt Reviewer | Open | TBD |
| AIR-009 | Tool overreach | Tool used outside capability | Unsafe output/action | High | Medium | Tool routing | Agent/tool limits | Strengthen provider review | VIF Orchestrator | Open | TBD |
| AIR-010 | Model/tool change | Provider changes behaviour | Old prompts no longer safe | Medium | Medium | Tool change review | AI model/tool change control | Revalidate prompts/tools | AI Governance Owner | Open | TBD |
| AIR-011 | Missing evidence | AI output lacks proof | False confidence | High | Medium | Evidence map | Verification register | Require traceability | QA Gatekeeper | Open | TBD |
| AIR-012 | Credit burn | Repeated failed generations | Waste and low-quality churn | Medium | Medium | Credit-burn register | Stop triggers | Re-route earlier | Credit-Burn Controller | Open | TBD |
| AIR-013 | Repeated failed repairs | Same defect repeatedly patched | More defects/rework | High | Medium | Bad-output monitoring | RCA/lessons learned | Stop and re-baseline | QA Gatekeeper | Open | TBD |
| AIR-014 | Source-truth contamination | Old drafts treated as current | Wrong build/release decisions | High | Medium | Source lock/context pack | Archive rules | Mark reference-only sources | VIF Orchestrator | Open | TBD |
| AIR-015 | Standards/compliance overclaim | AI claims compliance without evidence | Legal/audit credibility risk | High | Medium | Human compliance review | No compliance claims without evidence | Add compliance approval gate | Compliance Specialist | Open | TBD |

## Outputs/records
AI risk register, required actions, owners, status, linked lessons and management review input.

## Linked process
MOP-04 AI governance and tool-use policy, MOP-03 Planning/risk/opportunity, MOP-07 Corrective action/improvement, SOP-12 Lessons learned.

## Linked gate
AI governance gate, risk gate, prompt gate, verification gate, data protection gate, release gate.

## Human approval
Required for high and critical risks, data-impacting AI use, protected changes, release support and compliance/customer-facing claims.

## Data boundary
Risks involving customer, confidential, secret or production data must follow AI_DATA_GOVERNANCE and remain HOLD/BLOCKED until approved.

## PASS/HOLD/BLOCKED rules
- PASS: risk has cause, effect, rating, control, owner and required action.
- HOLD: risk is known but action, owner or evidence is incomplete.
- BLOCKED: critical AI risk is uncontrolled or allows protected work without human approval/evidence.

## PDCA
- PLAN: identify AI risks and controls before use.
- DO: apply controls during prompt/tool/output lifecycle.
- CHECK: monitor bad outputs, evidence gaps and incidents.
- ACT: update risks, controls, prompts, skills, tool routes and lessons learned.

## Update trigger
AI failure, prompt failure, tool/model change, incident, audit finding, CI finding, customer concern, release issue, credit burn or lesson learned.
