# APP_DEVELOPMENT_PROCESS_ARCHITECTURE

## Purpose
Define the app-development production flow used to build, repair, review, validate, release and support apps without drifting into document-control work for its own sake.

## Scope
All software builds, app repairs, reviews, releases and controlled changes managed through the Software Build Management System.

## Owner/agent
VIF Orchestrator with Product/App Owner, Process Owner, QA Gatekeeper and Release Controller.

## Inputs
Opportunity/request, app context, source-of-truth evidence, domain/process-owner input, operator/user input, risks, tenant/security needs, current maturity and approved job card.

## Activities/method
Production flow: App opportunity/request -> App intake -> Context/source-of-truth lock -> Domain/process-owner truth capture -> User/operator input -> Requirements and acceptance criteria -> Runtime-first process route -> Module/runtime-object map -> UI/interface concept -> Data/backend/RLS concept -> Risk/security/tenant review -> Job card and prompt packet -> Build instruction -> Coding/build execution -> Code review -> Backend/RLS review -> UI/adaptive review -> Test execution -> Verification -> Validation/UAT -> Release/rollback review -> Handover/support -> Feedback -> Lessons learned -> NC/RCA/CAPA/continual improvement when required.

## Outputs/records
Approved app-development route, job cards, runtime maps, verification records, validation/UAT evidence, release/rollback evidence, support/feedback records and improvement triggers.

## Linked process
ADP-01 to ADP-21 app-development process flow.

## Linked skills/WIs
Context lock, scope lock, source-of-truth lock, runtime-first review, prompt quality review, DB/RLS proof, UI/interface review, verification, validation, release/rollback, RCA/CAPA and lessons learned.

## Linked gates
Intake, context lock, requirements, runtime map, risk/security, build instruction, review, verification, validation/UAT, release, support and improvement gates.

## Evidence required
Evidence must prove the current process state. Documents alone do not prove app readiness.

## Risks
Jumping from idea directly to Lovable/Codex, schema-first build, UI-route-first build, broad build prompts, CI before onboarding, n8n before maturity, release without evidence.

## Controls
Blocked: idea-to-tool jump, document-completion-as-readiness, schema-first build, UI-route-first build, broad build-the-whole-app prompts, app-repo CI before onboarding, n8n before maturity approval and release without evidence.

## Interfaces
App owner, process owner, operator/user, domain specialist, runtime architect, UI/UX, backend/RLS, coders, reviewers, testers, QA, release and support.

## PASS/HOLD/BLOCKED rules
PASS when the full route is evidenced for the defined scope. HOLD when any upstream truth/evidence is incomplete. BLOCKED when build/release/automation is attempted before the required gate.

## Escalation
Escalate protected-scope breach, source drift, runtime gap, unapproved CI/n8n, release without evidence or customer-data risk.

## Update trigger
New app, app repair, major change, failed validation, release issue, RCA/CAPA or lesson learned.
