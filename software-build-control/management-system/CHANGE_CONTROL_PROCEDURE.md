# CHANGE_CONTROL_PROCEDURE

## Purpose
Control all internal, customer, defect, urgent, maintenance, design, backend/schema/RLS, tenant rollout, and rollback changes.

## When to use
For every change request or repair.

## Owner/tool
Change owner; ChatGPT structures; Codex validates repo evidence.

## Inputs
Change request, defect, customer request, incident, impact evidence.

## Activities or fields
Internal change; customer change; defect repair; urgent fix; app maintenance change; design change; schema/backend/RLS change; tenant rollout change; release rollback; impact; approval; verification; closure.

## Outputs/records
Approved/rejected change record and linked job card.

## Gate controlled
Change-control gate.

## PASS/HOLD/BLOCKED rules
PASS when impact/approval/rollback are clear. HOLD if evidence is partial. BLOCKED if change bypasses approval or touches protected areas without evidence.

## Update trigger
Every change event.
