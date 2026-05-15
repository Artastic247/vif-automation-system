# PROMPT_QUALITY_STANDARD

## Purpose
Set minimum requirements for build/repair/review prompts.

## When to use
Before giving any tool a build, repair, audit, or implementation instruction.

## Owner/tool
Prompt owner and approving user.

## Inputs
Job card, source evidence, target tool, risk limits.

## Activities or fields
Every build/repair prompt must include: objective; scope in; scope out; files/modules in scope; prohibited changes; inputs; outputs; verification; rollback; stop condition; gate decision.

## Outputs/records
Approved prompt or rejected prompt.

## Gate controlled
Prompt quality gate.

## PASS/HOLD/BLOCKED rules
PASS if all minimum fields exist. HOLD if evidence is incomplete. BLOCKED if prompt allows uncontrolled code/schema/release changes.

## Update trigger
Prompt review, tool failure, or process improvement.
