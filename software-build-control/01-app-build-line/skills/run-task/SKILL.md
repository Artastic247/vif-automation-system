# SKILL: run-task

## Trigger
Use after intake + build card PASS.

## Steps
1. Build `AGENT_TASK_PACKET` using handoff contract.
2. Execute route (`dry-run` or `pr-write`) via workflow.
3. Record replay key, changed files, and evidence links.

## Outputs
- Agent task packet.
- Handoff and execution artifacts.
