# SYSTEM_FLAGS_REGISTER

| Flag ID | System flag | Why it matters | Required control | Required artefact | Gate rule | PASS evidence | HOLD/BLOCK condition |
|---|---|---|---|---|---|---|---|
| SFR-001 | No truncation | Prevent context loss | Structured context pack | APP_CONTEXT | No build without current context | Current context pack | HOLD if scattered only |
| SFR-002 | Visual/layout completeness | Prevent partial UI | Screen map | SCREEN_MAP | No UI build without screen map | Approved map | HOLD |
| SFR-003 | HTML prototype conversion | Prototype is not runtime proof | Convert to specs | SCREEN/DATA/WORKFLOW/RUNTIME | No code from prototype alone | Mapped elements | BLOCK |
| SFR-004 | Feature creep/backlog control | Prevent scope drift | Backlog | CHANGE_BACKLOG | Only job card enters build | Backlog separated | HOLD |
| SFR-005 | Multi-tenant isolation | Protect data | Tenant/RLS evidence | RUNTIME/TENANT | No pilot without proof | Isolation evidence | BLOCK |
| SFR-006 | Dev/demo/real tenant separation | Prevent data mixing | Tenant classification | TENANT_ROLLOUT | No real-data dev | Tenant list | HOLD |
| SFR-007 | Pilot before rollout | Avoid global defects | Feature/tenant rollout | TENANT/RELEASE | No full rollout first | Pilot evidence | BLOCK |
| SFR-008 | Rollback by design | Enable safe recovery | Rollback route | RELEASE | No release without rollback | Rollback proof | BLOCK |
| SFR-009 | Customer change control | Control external changes | Change register | CUSTOMER_CHANGE | No customer build without CR | Approved CR | HOLD |
| SFR-010 | Good/bad coding pattern register | Stop repeat defects | Pattern register | CODING_PATTERN | No repeat bad pattern | Rules applied | HOLD |
| SFR-011 | No automation before process stability | Avoid automating chaos | Manual gate first | VERIFICATION | No automation until proven | Manual evidence | BLOCK |
| SFR-012 | No module complete without runtime evidence | UI is not completion | Runtime map | RUNTIME | No module PASS from UI only | Backend/evidence | HOLD |
| SFR-013 | No backend claim without backend read/write proof | Prevent false backend claims | Backend evidence | VERIFICATION | No backend PASS without proof | Read/write proof | BLOCK |
| SFR-014 | No release without verification evidence | Prevent false PASS | Verification register | VERIFICATION/RELEASE | No release without evidence | Evidence pack | HOLD |
