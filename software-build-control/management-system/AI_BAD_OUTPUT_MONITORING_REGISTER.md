# AI_BAD_OUTPUT_MONITORING_REGISTER.md

## Purpose
Monitor AI bad outputs so failures are detected, corrected, analysed, prevented and linked to prompt failures, lessons learned, risk updates, tool routing and process improvement.

## Scope
Applies to hallucinations, wrong code, false PASS statements, unsafe schema/RLS suggestions, missing evidence, wrong repo/branch assumptions, prompt drift, repeated failed repairs, identity/contact errors and compliance overclaims from any AI tool.

## Owner/tool
QA Gatekeeper owns bad-output monitoring. Prompt Quality Reviewer owns prompt-related failures. AI Governance Owner owns systemic AI-risk updates. Lessons Learned Controller owns learning capture.

## Inputs
AI output, prompt/input summary, tool/model, verification findings, review comments, incidents, failed builds/tests, release issues, prompt failure records and user/customer feedback.

## Activities/fields
| Bad output ID | Tool/model | Prompt/input summary | Failure type | Effect | Detection method | Correction | Corrective action | Recurrence risk | Linked prompt failure | Linked lesson learned | Effectiveness check | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AIBO-001 | TBD | TBD | Hallucination / false PASS / wrong code / unsafe suggestion / missing evidence / prompt drift | TBD | Human review / test / audit / user finding | TBD | TBD | Low/Medium/High | TBD | TBD | TBD | Open |

## Outputs/records
Bad-output record, correction, corrective action, recurrence risk, linked lesson, prompt/tool/process update and effectiveness check.

## Linked process
MOP-04 AI governance, MOP-07 Corrective action and continual improvement, SOP-06 Prompt control, SOP-12 Lessons learned, COP-11 Verification.

## Linked gate
AI monitoring gate, prompt gate, verification gate, improvement gate, lessons-learned gate.

## Human approval
Required to close high or critical bad-output records and to accept effectiveness evidence.

## Data boundary
Bad-output records must not include secrets, credentials, uncontrolled customer data or unapproved identity/contact data. Use placeholders where needed.

## PASS/HOLD/BLOCKED rules
- PASS: bad output is corrected, root cause/corrective action is defined, lesson is linked and effectiveness is checked.
- HOLD: bad output is logged but correction or effectiveness evidence is pending.
- BLOCKED: bad output caused or could cause protected action, data exposure, false release, schema/RLS risk or repeated failure without containment.

## PDCA
- PLAN: define bad-output categories and monitoring sources.
- DO: log and correct bad outputs.
- CHECK: verify recurrence risk and effectiveness.
- ACT: update risks, prompts, skills, tool routes, procedures and validation rules.

## Update trigger
AI output failure, prompt failure, failed verification, app defect, release issue, data/security concern, audit finding, CI finding or lesson learned.
