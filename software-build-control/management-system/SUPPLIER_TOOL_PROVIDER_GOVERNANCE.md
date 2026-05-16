# SUPPLIER_TOOL_PROVIDER_GOVERNANCE.md

## Purpose
Define governance for external AI/tool providers, cloud services, platforms and suppliers used within the Software Build Control System.

## Scope
Applies to ChatGPT, Codex, Claude, Lovable, Gemini, Copilot, GitHub, Supabase, Vercel, local LLM tooling, future n8n routes and other external software/service providers.

## Owner/agent
System owner governs supplier/tool-provider approval. VIF Orchestrator governs operational routing. Security/RLS Reviewer governs supplier data/security impact.

## Inputs
Provider inventory, AI system inventory, pricing/credit changes, outages, SLA information, security concerns, dependency risks, operational incidents and management-review decisions.

## Activities/checklist
1. Register supplier/tool provider.
2. Define intended use and prohibited use.
3. Assess dependency risk and operational criticality.
4. Assess data/security exposure.
5. Monitor outages, pricing, credit limits and behavioural changes.
6. Define fallback/contingency route.
7. Review provider suitability and maturity periodically.
8. Escalate supplier/tool instability or governance concerns.

## Outputs/records
Supplier/tool register, dependency review, outage review, pricing/credit review, contingency review and supplier assessment.

## Maturity level
M3 requires governed provider review. M4/M5 require trend analysis, fallback validation and strategic dependency management.

## Evidence required
Provider inventory, dependency assessment, contingency evidence, pricing/credit review, outage evidence and approval status.

## Linked process
MOP-03 Strategic planning risk and opportunity, MOP-04 AI governance and tool-use policy, SOP-05 Tool routing and tool qualification, SOP-10 Contingency and continuity control.

## Linked agent/skill/procedure/module
System owner, VIF Orchestrator, Security/RLS Reviewer, Credit-Burn Controller, AI governance controls and contingency planning.

## Interface/control point
Interfaces with AI governance, contingency planning, operational capacity governance, onboarding governance and portfolio governance.

## PASS/HOLD/BLOCKED rules
- PASS: provider/tool risk, dependency and contingency controls are acceptable.
- HOLD: provider instability, pricing risk or contingency gaps require review.
- BLOCKED: uncontrolled dependency, unacceptable data/security exposure or unsupported operational reliance.

## PDCA
- PLAN: define provider strategy and fallback routes.
- DO: operate using approved providers.
- CHECK: review outages, pricing, behaviour and incidents.
- ACT: change route, add controls or reduce dependency.

## Audit frequency
During management review, after outages/incidents and during dependency-risk review.

## Automation allowance
No provider/tool may receive customer or protected data outside approved governance boundaries.

## Escalation
Escalate outages, uncontrolled dependency, pricing spikes, provider drift, security concerns or unsupported operational reliance.

## Update trigger
Provider change, outage, pricing change, capability change, security concern, audit finding or lesson learned.
