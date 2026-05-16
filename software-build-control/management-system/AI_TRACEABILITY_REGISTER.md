# AI_TRACEABILITY_REGISTER.md

## Purpose
Link AI-assisted work from job card to prompt, tool/model, output, affected files, evidence, human reviewer, decision, verification result and lessons learned.

## Scope
Applies to all AI-assisted architecture, review, planning, app-code support, schema/RLS review, verification, validation, release support, customer-facing content, audit/compliance evidence, automation-readiness and continual-improvement work.

## Owner/tool
QA Gatekeeper owns traceability integrity. VIF Orchestrator owns job-card linkage. Prompt Quality Reviewer owns prompt linkage. AI Governance Owner reviews systemic AI traceability. Relevant specialist owners review technical evidence.

## Inputs
Job card, prompt, tool/model, AI output, affected files/systems, evidence records, human reviewer, gate decision, verification result and lessons learned.

## Activities/fields
| Trace ID | Job card | Prompt ID/summary | Tool/model | AI output summary | Files/systems affected | Evidence | Human reviewer | Decision | Verification result | Linked lesson learned | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AIT-001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | PASS/HOLD/BLOCKED | TBD | TBD | Open |

## Outputs/records
AI traceability record, evidence linkage, decision history, verification linkage and lessons learned linkage.

## Linked process
MOP-04 AI governance and tool-use policy, SOP-06 Prompt control and prompt quality, SOP-07 Evidence and record control, COP-11 Verification, MOP-07 Corrective action and continual improvement.

## Linked gate
AI traceability gate, prompt gate, evidence gate, verification gate, release gate, lessons-learned gate.

## Human approval
Required for traceability records supporting protected work, release support, compliance/audit evidence, customer-facing content or automation activation.

## Data boundary
Traceability records must avoid secrets, credentials, uncontrolled customer data, production data and uncontrolled identity/contact values. Use references and placeholders where needed.

## PASS/HOLD/BLOCKED rules
- PASS: job card, prompt, tool/model, output, affected files, evidence, reviewer, decision and verification result are linked.
- HOLD: traceability is incomplete and no protected action proceeds.
- BLOCKED: AI output affects protected work without traceability, evidence, reviewer or decision record.

## PDCA
- PLAN: define traceability requirements before AI use.
- DO: record prompt, tool, output and evidence link.
- CHECK: review traceability before decision/release/closure.
- ACT: correct traceability gaps and update prompts, processes, risks and lessons learned.

## Update trigger
AI-assisted work item, verification failure, release support, customer-facing content, audit evidence, app defect, bad output, audit finding, CI finding or lesson learned.
