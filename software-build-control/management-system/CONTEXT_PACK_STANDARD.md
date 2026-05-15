# CONTEXT_PACK_STANDARD

## Purpose
Preserve context without truncation or uncontrolled expansion.

## When to use
Before any chat, tool session, Codex task, Lovable build, review, or release decision.

## Owner/tool
ChatGPT/user create; Codex/GitHub validate repo facts.

## Inputs
App context; current branch/version; current job card; source-of-truth artefacts; latest evidence; known defects; scope exclusions; tenant/environment context; rollback context.

## Activities or fields
Context summary; evidence references; open assumptions; decisions; current gate; do-not-touch areas.

## Outputs/records
Current context pack.

## Gate controlled
Context lock gate.

## PASS/HOLD/BLOCKED rules
PASS when current context is complete and bounded. HOLD if evidence is partial. BLOCKED if source/version/tenant context is unknown for risky work.

## Update trigger
Every new job card, evidence update, branch change, or defect discovery.
