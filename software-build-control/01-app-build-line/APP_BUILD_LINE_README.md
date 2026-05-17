# APP BUILD LINE README

This directory defines a thin execution cell for controlled app-build routing.

## Command route
1. `create-build-cards`
2. `run-task`
3. `verify-build`

## Output reports
Generated in `software-build-control/01-app-build-line/reports/`.

## Safety
The execution cell is constrained to software-build-control artifacts and must not touch app repos or protected systems.


## Agent and skill coverage
- See `AGENT_AND_SKILL_COVERAGE.md` for per-step required agent/workstation and skill mappings.
