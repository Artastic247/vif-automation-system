# AGENT_REGISTER

## Purpose
Define agent roles, guardrails, allowed tasks, prohibited tasks, and stop conditions.

## When to use
Before assigning work to Codex, Lovable, Claude, ChatGPT, n8n, or other agents.

## Owner/tool
System owner.

## Inputs
Tool capability, task type, risk, evidence needs.

## Activities or fields
| Agent name | Purpose | Allowed tasks | Prohibited tasks | Required inputs | Required outputs | Stop condition | Owner/tool |
|---|---|---|---|---|---|---|---|

## Outputs/records
Agent register and guardrails.

## Gate controlled
Agent routing gate.

## PASS/HOLD/BLOCKED rules
PASS if agent is matched to task and stop rules. HOLD if capability is uncertain. BLOCKED if agent can alter protected areas without approval.

## Update trigger
New tool, agent failure, or process change.
