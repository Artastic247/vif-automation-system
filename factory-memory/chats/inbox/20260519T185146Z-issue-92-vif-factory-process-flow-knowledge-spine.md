# Factory Memory Source

- Source type: issue
- Source ID: issue-92
- Title: VIF Factory Process-Flow Knowledge Spine
- Ingested at: 20260519T185146Z

## Source content

# VIF Factory Process-Flow Knowledge Spine

Source issue: #92

Implement the VIF Factory Process-Flow Knowledge Spine.

Scope:
- Add controlled factory-memory instruction files for app building, vibe coding, process flow, software production stack, maturity model, Six-M operation model, tool/station routing, and buy-vs-build guidance.
- Update the existing app-development operating model so OP-01 to OP-08 are the top-level route and ADP-01 to ADP-21 remain the detailed subprocess route.
- Add OP/MOP/COP/SOP/ADP crosswalk.
- Add a short .codex/AGENTS.md pointer to the knowledge spine and station-routing rule.
- Register new knowledge files in FACTORY_MEMORY_REGISTER.md.
- Harden factory-memory ingest output/state semantics for process-change recommendations and explicit knowledge states.

Protected scope:
- No Supabase/RLS changes.
- No deployment changes.
- No app repository/customer data changes.
- No auto-merge.
- Human merge required for this control-plane build.
