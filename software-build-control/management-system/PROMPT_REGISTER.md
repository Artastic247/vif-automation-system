# PROMPT_REGISTER

## Purpose
Control prompts used for build, repair, review, audit, and automation.

## When to use
Before using a reusable prompt or after prompt failure/drift.

## Owner/tool
Prompt owner; ChatGPT maintains; tool outputs verified by user/Codex.

## Inputs
Prompt text, target tool, job card, scope, risks.

## Activities or fields
| Prompt ID | Purpose | Target tool | Mode | Scope | Owner | Status | Linked job card | Last reviewed date | Known risks |
|---|---|---|---|---|---|---|---|---|---|

## Outputs/records
Approved prompt register.

## Gate controlled
Prompt-control gate.

## PASS/HOLD/BLOCKED rules
PASS if prompt has scope, stop condition, verification, and rollback. HOLD if unreviewed. BLOCKED if it authorises uncontrolled work.

## Update trigger
New prompt, model/tool change, failed output, or lessons learned.
