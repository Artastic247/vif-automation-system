# AI_OUTPUT_AUDIT_CHECKLIST

## Purpose
Audit AI-generated outputs before they are treated as evidence, implementation input or release support.

## Scope
All AI-generated analysis, code suggestions, procedures, prompts, audits, reports and automation outputs.

## Owner/agent
AI Output Auditor with Prompt Audit Specialist.

## Inputs
Prompt source basis, model/tool used, generated output, verification evidence and linked job card.

## Activities/method
Audit prompt source basis, tool/model used, output claim verification, evidence backing the output, hallucination risk, code/security impact, customer-data boundary, human review, implementation impact, verification evidence and whether the output triggered rework or false confidence.

## Outputs/records
AI output audit result, verification status, findings and lessons-learned linkage.

## Audit criteria
AI output cannot be treated as truth without evidence verification.

## Evidence required
Prompt, output, validation evidence, review approval and linked RCA/CAPA if failed.

## MLA / maturity dependency
Higher automation maturity requires stronger verification evidence.

## Linked process
AI governance, validation and Clause 9 AI output audit.

## Linked gate
AI output verification gate.

## PASS/HOLD/BLOCKED rules
PASS when evidence verifies the output. HOLD when verification is incomplete. BLOCKED when false confidence, hallucination or unsafe implementation risk exists.

## Escalation
Escalate hallucinated outputs, false PASS, customer-data risk or unsafe code suggestions.

## Management-review input
AI output failure trends and repeat hallucination issues feed management review.

## Update trigger
Output failure, RCA/CAPA, audit finding, provider/tool change.
