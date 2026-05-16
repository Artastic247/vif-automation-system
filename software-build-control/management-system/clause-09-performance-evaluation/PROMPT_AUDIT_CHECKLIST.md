# PROMPT_AUDIT_CHECKLIST

## Purpose
Audit prompts used for build, review, repair, validation, audit or automation so they do not cause scope drift or false implementation.

## Scope
All reusable prompts, job-card prompts, Codex/Lovable/Claude/ChatGPT instructions, and automation-generation prompts.

## Owner/agent
Prompt Audit Specialist.

## Inputs
Prompt text, prompt register, job card, source basis, tool route, expected output, verification and rollback requirements.

## Activities/method
Check objective, source basis, scope in, scope out, files/modules in scope, prohibited changes, required output, verification method, rollback/stop condition, tool routing, customer-data boundary, secret-safety boundary, no fix-everything language, no implementation without approved job card, and no vague backend/schema/RLS request without runtime gate.

## Outputs/records
Prompt audit finding, prompt approval/rejection, update action, lessons learned update.

## Audit criteria
Prompt must be bounded, evidence-based and tool-appropriate. It must not authorise app code, schema/RLS, deployment, n8n or release work outside an approved job card.

## Evidence required
Prompt version, linked job card, source basis, expected output, verification/rollback instruction, review decision.

## MLA / maturity dependency
Released prompts require M3 evidence; automated prompt generation requires higher maturity and approval.

## Linked process
Prompt management and Clause 9 prompt audit.

## Linked gate
Prompt quality gate.

## PASS/HOLD/BLOCKED rules
PASS when prompt is bounded and evidence-ready. HOLD when scope/source is incomplete. BLOCKED when it enables broad, unsafe or unsupported implementation.

## Escalation
Escalate prompt drift, hallucination, false PASS, customer-data risk, or prohibited change instruction.

## Management-review input
Prompt failures and repeat drift trends feed management review.

## Update trigger
New prompt, tool change, failed output, RCA/CAPA, lessons learned.
