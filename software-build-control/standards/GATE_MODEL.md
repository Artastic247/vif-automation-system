# Gate Model

| Gate | Entry evidence | PASS condition | HOLD condition | BLOCKED condition |
|---|---|---|---|---|
| Intake | Request/evidence | Context clear | Missing detail | Unsafe/unclear target |
| Baseline | Repo/branch/version | Source locked | Partial evidence | Wrong/unknown baseline |
| Screen/layout | Screen map | Layout complete | Gaps | Build requested without map |
| Data table/grid | Data table spec | Columns/sources clear | Partial | Table build without spec |
| Workflow | Workflow map | Actors/states/actions clear | Partial | Protected action undefined |
| Runtime/backend | Runtime map | Backend/RLS proof defined | Missing proof | Frontend-only claim |
| Job card | Approved maps | Scope bounded | Inputs missing | Scope creep |
| Build | Approved job card | Build within scope | Failed build | Unapproved changes |
| Verification | Evidence pack | Checks pass | Partial evidence | Failed critical checks |
| Tenant rollout | Tenant register | Exposure controlled | Missing tenant evidence | Real tenant risk |
| Release | Release register | Verified and rollback-ready | Missing evidence | Unsafe release |
| Lessons learned | Event/defect | Prevention captured | Pending | Repeat failure unmanaged |
