# DEPLOYMENT_MAP

## Purpose
Map build, deploy, release, and rollback route.

## When to use
Before release, pilot, or rollback decision.

## Owner/tool
Release owner.

## Inputs
Repo, branch, CI, hosting, DB migration, tenant rollout, rollback evidence.

## Activities or fields
Commit; build; deploy; verification; tenant exposure; rollback; approval.

## Outputs/records
Deployment and rollback map.

## Gate controlled
No deployment/rollback map → no release.

## PASS/HOLD/BLOCKED rules
PASS if deploy and rollback route are proven. HOLD if incomplete. BLOCKED if rollback is unknown.

## Update trigger
Deployment platform, branch, release, or rollback change.
