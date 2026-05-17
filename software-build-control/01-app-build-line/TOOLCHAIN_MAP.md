# TOOLCHAIN_MAP

| Tool | Owns | Trigger in | Output | Auth | Failure domain |
|---|---|---|---|---|---|
| GitHub Issues | Work order intake | Issue form submission | Durable structured task | GitHub user | Underspecified issue |
| GitHub Actions | Event routing and execution | `issues`, `issue_comment`, `workflow_dispatch`, `pull_request` | Checks, artifacts, PR operations | `GITHUB_TOKEN` / GitHub App token | Workflow misrouting or permission gaps |
| Codex (`codex exec` or action) | AI task execution | Routed workflow job | Patch, summary, JSONL trace | `OPENAI_API_KEY` | Prompt contamination, out-of-scope edits |
| CI checks | Technical validation | PR/update events | Pass/fail statuses and logs | Native repo CI auth | Broken build/test or flaky checks |
| Operator | Final approval and merge | Review gate state | Merge, reroute, or close | GitHub user | Human process delay/error |
