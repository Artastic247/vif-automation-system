# AGENT_MATURITY_AND_COMPETENCE_MATRIX

## Purpose
Define competence and maturity expectations for agents and specialists before they perform controlled work or make gate decisions.

## Scope
All agents, specialists, coders, reviewers, testers, owners, controllers and auditors in the Software Build Management System.

## Owner/agent
MLA Assessor with Skill/WI Audit Specialist and QA Gatekeeper.

## Inputs
Master agent register, work instructions, role assignments, audit findings, training/competence evidence, use evidence, KPI trends, RCA/CAPA and maturity records.

## Activities/method
Assess each role against competence needs, maturity level, evidence requirements, allowed work, prohibited work, audit frequency and automation permission.

## Outputs/records
Agent competence/maturity record, training gap, audit schedule and gate restriction.

## Linked processes
Clause 7 competence/support, Clause 9 MLA/audit, Clause 10 improvement and ADP process assignments.

## Linked skills/WIs
WI_001 to WI_030.

## Linked gates
Competence gate, MLA gate, skill/WI release gate, app onboarding gate, release gate, CI/n8n readiness gate.

## Evidence required
Competence evidence, WI familiarity, supervised use evidence, audit findings, maturity record and improvement actions.

## Risks
Untrained agent, tool misuse, AI/tool overreach, gate decision without competence, automation before maturity, repeated errors.

## Controls
Agent maturity restricts allowed work. Low maturity requires supervision/human review. Gate authority requires defined competence.

## Interfaces
Agent owner, Skill/WI owner, MLA Assessor, Internal Audit Specialist, QA Gatekeeper and Management Review Owner.

## Maturity and competence matrix
| Maturity | Agent capability | Evidence required | Allowed work | Automation permission |
|---|---|---|---|---|
| M0 | Not defined | None | Exploration only | None |
| M1 | Draft role/skill | Role/WI draft | Controlled drafting with review | None |
| M2 | Pilot capable | Supervised use evidence | Controlled pilot work | Manual/read-only only |
| M3 | Released | Approved WI and audit record | Defined operational scope | Limited CI consideration only |
| M4 | Managed | KPIs, audits, effective CAPA | Repeatable controlled work | Limited automation candidate |
| M5 | Optimised | Trend/effectiveness evidence | Scalable controlled work | Automation candidate with approval |

## Role competence focus
| Role group | Minimum competence focus | Minimum maturity for unsupervised gate work |
|---|---|---|
| Orchestration/QA | Scope, gates, evidence, protected scope | M2/M3 |
| Coders/builders | Scoped implementation, code evidence, rollback awareness | M2 |
| Reviewers/testers | Verification, negative paths, evidence quality | M2 |
| Runtime/backend/RLS/security | Runtime state, RLS, role/tenant proof | M2/M3 |
| Release/support | Release/rollback/support monitoring | M3 |
| Audit/RCA/CAPA/improvement | Evidence, findings, cause, effectiveness | M2/M3 |
| CI/n8n controllers | Automation governance, disable route, privacy | M3+ for expansion |

## PASS/HOLD/BLOCKED rules
PASS when competence and maturity support assigned work. HOLD when training/evidence is incomplete. BLOCKED when agent attempts prohibited or high-risk work beyond maturity.

## Escalation
Escalate repeated agent error, gate misuse, untrained agent, maturity overstatement or automation bypass.

## MLA / maturity dependency
This matrix is an input to MLA assessment and automation permission decisions.

## Update trigger
Role change, WI change, audit finding, RCA/CAPA, repeated failure, new tool/model or automation request.
