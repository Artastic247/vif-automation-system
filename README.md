# VIF Automation System

Initial repository anchor for the Software Build Control System.

The control-system package is stored under `software-build-control/`.

## Factory agent system

The VIF factory-level agent operating method is stored under:

```text
software-build-control/factory-agent-system/
```

This area defines the reusable AI-assisted coding production line: factory agent roles, gate model, Codex/PR flow, lessons-learned feedback, and deployment templates for build repositories.

Core rule: VIF owns the factory method; each build repository still needs its own local `AGENTS.md`, CI workflow, PR template, issue template, build control notes, known issues record, and release checklist.
