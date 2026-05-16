# PROMPT_FAILURE_REGISTER.md

## Purpose
Record prompt failures, tool drift, context loss, hallucination, unsafe instruction patterns, and AI output failures so they are corrected through lessons learned, RCA, skill updates, agent updates, tool-routing updates and process updates.

## Scope
Applies to all AI-assisted software-build work, including ChatGPT, Lovable, Codex, Claude/Claude Code, Gemini/local LLM, Copilot and future n8n routing.

## Inputs
Failed prompt or prompt summary, tool/model, output, observed drift, affected app/project, impact, evidence, job card, gate, correction and corrective action needs.

## Activities
- Log every significant prompt failure.
- Classify the failure type.
- Identify drift observed and impact.
- Determine root cause: weak source basis, missing context pack, poor scope, wrong tool, missing job card, unsafe prompt pattern, model limitation or evidence gap.
- Define immediate correction.
- Define corrective action and effectiveness check.
- Link to lesson learned, skill/procedure update, agent/tool-route update and validation update where required.

## Outputs
Prompt failure record, corrective action, lessons learned update and effectiveness check.

## Records
| Failure ID | Date | App/project | Tool/model | Prompt used or summary | Failure type | Drift observed | Impact | Root cause | Correction | Corrective action | Linked lesson learned | Linked skill/procedure update | Effectiveness check | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PF-001 | TBD | TBD | TBD | TBD | Context loss / drift / unsafe scope / wrong tool / hallucination | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Open |

## Owner/tool
Prompt Quality Reviewer owns the register. Lessons Learned Controller verifies learning capture. QA Gatekeeper checks effectiveness evidence.

## Linked process
SOP-06 Prompt control and prompt quality, MOP-07 Corrective action and continual improvement, SOP-12 Lessons learned and knowledge reuse, SOP-05 Tool routing and tool qualification.

## Linked gate
Prompt gate, lessons-learned gate, improvement gate, tool-routing gate.

## PDCA
- PLAN: define failure categories, required evidence and escalation route.
- DO: log the failure and apply correction.
- CHECK: verify whether the corrective action prevents recurrence.
- ACT: update prompt library, skills, agent limits, procedures, validation scripts and lessons learned.

## PASS/HOLD/BLOCKED rules
- PASS: failure is logged with cause, correction, corrective action, linked lesson and effectiveness check.
- HOLD: failure is logged but root cause or effectiveness evidence is pending.
- BLOCKED: critical prompt failure caused unsafe output, data risk, schema/RLS risk, release risk or repeat defect without containment.

## Update trigger
Any prompt drift, hallucination, bad repair, wrong tool route, context loss, credit burn, out-of-scope edit, failed build/test caused by prompt, or audit/CI finding.
