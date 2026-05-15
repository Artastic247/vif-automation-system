# GATE_MODEL

| Gate | Entry evidence | PASS condition | HOLD condition | BLOCKED condition |
|---|---|---|---|---|
| Intake | Request/evidence | Scope known | Missing info | Unsafe/unclear |
| Baseline | Repo/version/env | Source locked | Partial evidence | Wrong source |
| Screen/layout | Screen map | Visual complete | Gaps | UI build attempted |
| Data table/grid | Table spec | Columns/rules defined | Missing mapping | Build attempted |
| Workflow | Workflow map | States/actions defined | Exceptions unclear | Protected action unclear |
| Runtime/backend | Runtime map | Backend/RLS proof defined | Missing proof | Security risk |
| Job card | Approved maps | Scope locked | Inputs missing | Scope creep |
| Build | Job card | Build done in scope | Checks pending | Out-of-scope change |
| Verification | Test evidence | PASS evidence | Partial evidence | Failed critical check |
| Tenant rollout | Tenant register | Pilot/rollout controlled | Tenant unknown | Data exposure risk |
| Release | Release register | Evidence+rollback | Missing evidence | Unsafe release |
| Lessons learned | Event/defect | Prevention captured | Pending | Repeat defect unaddressed |
