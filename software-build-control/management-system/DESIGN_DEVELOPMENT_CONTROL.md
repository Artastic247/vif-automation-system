# DESIGN_DEVELOPMENT_CONTROL

## Purpose
Control full software design, development, modification, validation, release, and lessons learned.

## When to use
For new apps, new modules, major modifications, repairs affecting workflow/backend/data, or customer-impacting changes.

## Owner/tool
Product owner with ChatGPT for gate logic; Codex/GitHub for repo evidence.

## Inputs
Request, context, impact, maps, current job card, risks, tenant/environment data.

## Activities or fields
Request → Context check → Impact assessment → Design/update plan → Risk review → Job card → Build/modification → Verification → Validation/UAT → Tenant rollout decision → Release → Lessons learned.

## Outputs/records
Design plan, job card, verification register, release record, lessons learned.

## Gate controlled
Design and development gate.

## PASS/HOLD/BLOCKED rules
PASS when each route step has evidence. HOLD if review is incomplete. BLOCKED if build/release starts without job card or verification.

## Update trigger
Any new design, modification, defect repair, or release.
