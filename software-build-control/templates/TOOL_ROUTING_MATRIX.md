# TOOL_ROUTING_MATRIX

| Tool | Correct use | Prohibited use | Required input | Required output | Stop condition |
|---|---|---|---|---|---|
| ChatGPT | Gate logic, context, job cards | Coding without evidence | Context pack | Artefacts | Missing evidence |
| Codex | Repo inspection, bounded patches | Broad rewrite | Job card | Diff/evidence | Scope drift |
| Lovable | Locked UI build station | Source-of-truth decisions | Screen/table specs | UI changes | Expands scope |
| GitHub | Version control, PR, rollback anchor | Secrets or uncontrolled main | Branch/job card | Commit/PR evidence | Direct unsafe push |
| Supabase | DB/RLS evidence | Untested destructive changes | Project/schema | Backend proof | RLS unknown |
| n8n | Orchestration only | Auto-fix/release | Approved workflow | Routing/evidence | Destructive action |
