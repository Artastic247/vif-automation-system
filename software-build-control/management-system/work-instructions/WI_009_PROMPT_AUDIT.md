# WI_009_PROMPT_AUDIT

## Purpose
Audit prompts after use to confirm the tool/model output stayed aligned with scope, source truth, evidence and gates.

## Scope
All prompts used for management-system artefacts, app-development work, audits, validation scripts, code review, app repair, documentation and automation concepts.

## When to use
Use after significant AI-assisted output, after drift, after false PASS risk, after rework, or during scheduled prompt audits.

## When not to use
Do not use to approve an unsafe output retrospectively; unsafe output must be held or escalated.

## Owner/agent
Prompt Audit Specialist with AI Output Auditor and QA Gatekeeper.

## Inputs
Prompt used, tool/model used, output generated, source basis, job card, evidence link, prohibited patterns, lessons learned and resulting action.

## Method steps
1. Record prompt and tool/model.
2. Check output against objective and source basis.
3. Check scope in/out compliance.
4. Check drift and unsupported claims.
5. Check evidence links and false PASS risk.
6. Check prohibited prompt patterns.
7. Identify tool/model behaviour and model-specific limitation.
8. Record lesson learned or RCA/CAPA trigger.
9. Decide PASS/HOLD/BLOCKED for prompt effectiveness.

## Outputs/records
Prompt audit record, prompt failure register entry, lessons learned, RCA/CAPA trigger or prompt update.

## Evidence required
Prompt, output, source evidence, job card, comparison notes, finding and corrective action if required.

## Linked ADP processes
ADP-10, ADP-11, ADP-12, ADP-16 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 7 prompt management, Clause 9 prompt/AI output audit and Clause 10 RCA/CAPA/lessons learned.

## Linked gates
Prompt audit, evidence, NC/RCA/CAPA and improvement gates.

## Tools allowed
Prompt register, AI output audit checklist, job cards, evidence register and lessons learned register.

## Tools prohibited
Using AI output as truth without source verification or using audit to excuse prohibited work.

## Risks
Hallucination, drift, unsupported source, false PASS, unverified code changes, model-specific limitation ignored.

## Controls
Prompt output cannot be accepted as evidence unless independently supported. Repeated drift triggers RCA/CAPA and prompt update.

## Interfaces
Prompt Engineer, AI Output Auditor, Context Specialist, QA Gatekeeper, RCA/CAPA Specialist and Knowledge Controller.

## PASS/HOLD/BLOCKED rules
PASS when output aligned and evidence is sufficient. HOLD when verification is incomplete. BLOCKED when output creates unsafe action, false PASS, customer-data risk or prohibited change.

## Escalation
Escalate false PASS, hallucinated source, protected-scope breach, repeated drift or model/tool unsuitability.

## MLA / maturity dependency
M2+ prompt use requires audit sampling. M3 released prompts require periodic review. M4/M5 automation requires trend evidence and low drift risk.

## Update trigger
Prompt failure, AI bad output, audit schedule, RCA/CAPA, lessons learned or tool/model change.
