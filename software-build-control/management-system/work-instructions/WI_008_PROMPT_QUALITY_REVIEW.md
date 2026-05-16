# WI_008_PROMPT_QUALITY_REVIEW

## Purpose
Review prompts before use so AI-assisted work stays bounded, source-based, tool-appropriate and evidence-driven.

## Scope
Prompts for ChatGPT, Codex, Claude, Lovable, Gemini/local LLMs, Copilot, n8n concepts and any AI-assisted build, review, audit or repair work.

## When to use
Use before sending a prompt that can create, modify, review, validate, repair, plan or release management-system or app artefacts.

## When not to use
Do not use as approval to implement without an approved job card or gate.

## Owner/agent
Prompt Audit Specialist with VIF Orchestrator and QA Gatekeeper.

## Inputs
Prompt draft, objective, source basis, scope in/out, allowed changes, prohibited changes, tool route, required output, evidence required, stop condition, rollback route and job card.

## Method steps
1. Confirm objective and source basis.
2. Confirm scope in and scope out.
3. Define allowed and prohibited changes.
4. Confirm tool/model route and limitations.
5. Confirm required output format and evidence.
6. Confirm stop condition and rollback route.
7. Remove vague wording like "fix everything" or "complete backend".
8. Confirm no implementation without approved job card.
9. Confirm protected scope, customer data and secret-safety boundaries.
10. Approve, hold or reject prompt.

## Outputs/records
Prompt quality review record, approved prompt packet, rejection/hold note or escalation.

## Evidence required
Prompt version, job card, source basis, tool route, scope/prohibition list, expected output and approval record.

## Linked ADP processes
ADP-02, ADP-05, ADP-10, ADP-11, ADP-12, ADP-16 and ADP-21.

## Linked MOP/COP/SOP processes
Clause 7 prompt/tool support, Clause 8 operation, Clause 9 prompt audit and Clause 10 improvement.

## Linked gates
Prompt, job-card, build, review, evidence and improvement gates.

## Tools allowed
ChatGPT for architecture/review, Codex for scoped code work, Lovable for bounded app/UI generation, Claude for code review, Gemini/local LLM for review where safe, GitHub for evidence.

## Tools prohibited
Tools used to bypass job-card gates, touch protected scope, expose customer data/secrets, activate app-repo CI/n8n or auto-fix/merge/release.

## Risks
Prompt drift, hallucination, broad implementation, wrong tool, false PASS, customer-data exposure, unapproved schema/RLS change.

## Controls
No prompt is approved without objective, source basis, scope, prohibited changes, evidence rule, stop condition and tool route.

## Interfaces
Prompt Engineer, Context Specialist, GitHub Controller, QA Gatekeeper, Tool/Supplier Reviewer and AI Output Auditor.

## PASS/HOLD/BLOCKED rules
PASS when prompt is bounded and evidence-ready. HOLD when source/scope/output is incomplete. BLOCKED when prompt authorises unsafe or prohibited work.

## Escalation
Escalate broad prompts, protected-scope requests, no evidence rule, customer-data exposure or repeated prompt drift.

## MLA / maturity dependency
M1 prompts require human review. M2 pilot prompts require evidence. M3 released prompts require register control. M4/M5 may allow limited automation only after maturity permission.

## Update trigger
New prompt, tool change, failed output, RCA/CAPA, lessons learned or audit finding.
