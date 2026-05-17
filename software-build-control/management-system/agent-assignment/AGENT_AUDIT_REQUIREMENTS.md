# AGENT_AUDIT_REQUIREMENTS

## Purpose
Define audit requirements for agents and specialists to confirm they follow assigned processes, WIs, evidence rules and gate authority.

## Scope
All agents and specialists performing management-system, app-development, review, validation, release, support, improvement, CI or n8n readiness work.

## Owner/agent
Internal Audit Specialist with Agent Audit Specialist and QA Gatekeeper.

## Inputs
Master agent register, process assignments, WI assignments, gate authority matrix, evidence outputs, maturity record, audit programme and RCA/CAPA history.

## Activities/method
Audit role assignment, competence evidence, allowed/prohibited work, WI use, evidence output, gate decisions, escalation behaviour, maturity level, and repeated failure patterns.

## Outputs/records
Agent audit record, finding, NC/RCA/CAPA trigger, maturity update input and management-review input.

## Linked processes
Clause 9 agent audit, Clause 7 competence, Clause 10 RCA/CAPA and ADP process assignments.

## Linked skills/WIs
WI_001 to WI_030, especially WIs owned by the audited agent.

## Linked gates
Agent audit gate, maturity gate, competence gate, gate-authority gate and improvement gate.

## Evidence required
Sampled work output, WI use evidence, gate decisions, escalation records, competence/maturity record and audit findings.

## Risks
Agent performs prohibited work, evidence not produced, gate authority misused, specialist bypassed, false PASS, repeated errors.

## Controls
Agents must be audited according to risk, maturity and role criticality. Findings feed NC/RCA/CAPA where required.

## Interfaces
Internal Audit Specialist, Agent owner, QA Gatekeeper, MLA Assessor, RCA/CAPA Specialist, Management Review Owner.

## Audit requirements
| Agent group | Audit focus | Minimum frequency logic | Escalation trigger |
|---|---|---|---|
| Orchestrator/QA | Scope, gates, evidence, protected scope | Risk/maturity based | False PASS or scope breach |
| Coders/builders | Job-card scope, diff evidence, prohibited changes | Pilot/release sampling | Unapproved app repo/schema change |
| Reviewers/testers | Review/test evidence and negative paths | Per release/pilot | Missed critical defect |
| Runtime/RLS/security | Runtime, backend enforcement, tenant/data controls | Per high-risk change | RLS/customer-data risk |
| Release/support | Release/rollback/support evidence | Each release/pilot | Failed rollback/no support owner |
| Prompt/context/AI | Source truth, prompt drift, AI output verification | Risk-based sample | Hallucination/unsupported claim |
| CI/n8n controllers | HOLD rules, automation permission, disable route | Before any change | Premature automation |
| RCA/CAPA/CI/knowledge | Cause, action, effectiveness, knowledge update | Per major NC/repeat | Ineffective CAPA/repeat failure |

## PASS/HOLD/BLOCKED rules
PASS when agent work is evidenced and within authority. HOLD when evidence gaps exist. BLOCKED when prohibited work, false PASS, customer-data risk or automation bypass occurs.

## Escalation
Escalate agent out-of-scope action, repeated failure, authority misuse, missing critical evidence, security risk or overdue findings.

## MLA / maturity dependency
Audit frequency increases when maturity is low, risk is high, failures repeat or automation is requested. M4/M5 require trend evidence.

## Update trigger
Agent role change, audit finding, maturity change, RCA/CAPA, new WI/tool/model or automation request.
