# Tool Routing Matrix

| Tool | Correct use | Prohibited use | Stop condition |
|---|---|---|---|
| ChatGPT | Strategy, gates, artefacts | Unapproved coding | Missing evidence |
| Codex | Repo inspection, bounded patches | Broad redesign | Scope drift/failing tests |
| Claude/Claude Code | Long-context review | Unbounded rewrite | Touches unrelated modules |
| Lovable | Scoped UI/prototype station | Backend/RLS authority | Expands features |
| GitHub | Version control, issues, PRs | Secrets/direct prod changes | Unreviewed main push |
| Supabase | DB/RLS evidence | Untested destructive changes | RLS/data risk |
| n8n | Routing/evidence orchestration | Auto-fix/release | Destructive action |
| Gemini/local LLM | Second opinion | Source-of-truth authority | Unsupported claims |
| Copilot | Inline completion | Architecture/schema/release | Out-of-scope changes |
