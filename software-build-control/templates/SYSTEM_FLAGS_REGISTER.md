# SYSTEM_FLAGS_REGISTER.md

| Flag ID | System flag | Why it matters | Required control | Required artefact | Gate rule | PASS evidence | HOLD/BLOCK condition |
|---|---|---|---|---|---|---|---|
| SFR-001 | No truncation | Prevents context loss. | Structured context pack. | APP_CONTEXT.md | No work without context. | Current context. | HOLD if scattered. |
| SFR-002 | Visual/layout completeness | Prevents partial UI. | Screen map. | SCREEN_MAP.md | No UI build without map. | Screen states defined. | HOLD. |
| SFR-003 | HTML prototype conversion | Prototype is not runtime proof. | Convert to specs. | SCREEN/TABLE/WORKFLOW/RUNTIME maps | No build from prototype alone. | Mapped elements. | BLOCK. |
| SFR-004 | Feature creep/backlog control | Prevents uncontrolled extras. | Backlog. | CHANGE_BACKLOG.md | Only job card scope builds. | Backlog separated. | HOLD. |
| SFR-005 | Multi-tenant isolation | Protects customer data. | RLS/tenant rules. | RUNTIME_MAP.md | No tenant work without proof. | Isolation evidence. | BLOCK. |
| SFR-006 | Dev/demo/real tenant separation | Prevents data mixing. | Tenant register. | TENANT_ROLLOUT_REGISTER.md | No real tenant testing without approval. | Tenant classified. | HOLD. |
| SFR-007 | Pilot before rollout | Limits blast radius. | Rollout gate. | RELEASE_REGISTER.md | No full rollout without pilot. | Pilot result. | BLOCK. |
| SFR-008 | Rollback by design | Enables recovery. | Rollback route. | RELEASE_REGISTER.md | No release without rollback. | Route defined. | BLOCK. |
| SFR-009 | Customer change control | Controls scope/UAT. | CR register. | CUSTOMER_CHANGE_REGISTER.md | No CR build without approval. | Impact approved. | HOLD. |
| SFR-010 | Good/bad coding pattern register | Prevents repeat failures. | Pattern register. | CODING_PATTERN_REGISTER.md | Known bad patterns blocked. | Rule exists. | HOLD. |
| SFR-011 | No automation before process stability | Prevents automating chaos. | Manual gate first. | VERIFICATION_REGISTER.md | No destructive automation. | Manual proof. | BLOCK. |
| SFR-012 | No module complete without runtime evidence | Prevents UI false PASS. | Runtime map. | RUNTIME_MAP.md | No module complete from UI alone. | Runtime proof. | HOLD. |
| SFR-013 | No backend claim without backend read/write proof | Prevents assumptions. | Backend evidence. | VERIFICATION_REGISTER.md | No backend PASS without proof. | Read/write evidence. | BLOCK. |
| SFR-014 | No release without verification evidence | Prevents false release. | Verification register. | VERIFICATION_REGISTER.md | No release without evidence. | Evidence pack. | HOLD. |
