# APP_PRODUCT_AUDIT_CHECKLIST

## Purpose
Audit whether an app/module is controlled, runtime-proven and safe for onboarding, release or support.

## Scope
Apps and modules including DOS FMEA, SPC, QMS, MSA, APQP, QCPro and future apps when onboarded.

## Owner/agent
App/Product Audit Specialist with Runtime Architect, DB/RLS Reviewer, Release Controller and Security/Data Reviewer.

## Inputs
App context, process supported, roles, runtime map, UI map, data table spec, backend/RLS evidence, tenant register, verification, validation/UAT, release/rollback and support records.

## Activities/method
Check app context, process supported, user roles, runtime objects, UI/interface controls, database/backend/RLS controls, tenant/data controls, verification, validation/UAT, release/rollback, support/maintenance, customer change control, demo vs production data boundary and backend read/write governed workflow evidence.

## Outputs/records
App/product audit report, onboarding readiness result, release/support findings.

## Audit criteria
App/module is not complete unless runtime, backend read/write, tenant/data, verification and release/rollback evidence exist.

## Evidence required
Repo/commit, build/test output, backend/RLS proof, tenant evidence, UAT, release/rollback record, support plan.

## MLA / maturity dependency
App onboarding requires maturity evidence. App-repo CI remains HOLD until onboarding readiness passes.

## Linked process
App onboarding, runtime-first operation, release/support.

## Linked gate
App onboarding and product audit gate.

## PASS/HOLD/BLOCKED rules
PASS when governed workflow and evidence are proven. HOLD when evidence is partial. BLOCKED when customer data, RLS, release, rollback or runtime proof is missing for production-impacting use.

## Escalation
Escalate unsafe customer exposure, false backend claim, missing rollback, demo-data-as-PASS or protected-action failure.

## Management-review input
App readiness, repeated defects and release risks feed management review.

## Update trigger
App onboarding, release, major defect, customer change, audit finding.
