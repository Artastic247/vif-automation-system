# APP BUILD SPEC

- runtime object: thin app-build execution cell
- user role: build controller / automation operator
- start event: explicit invocation of app_build_line.py command route
- state model: intake -> spec -> build-card -> task-packet -> verification -> gate decision
- allowed action: generate dry-run packets and verification evidence under software-build-control only
- protected action: any app code changes, Supabase/RLS/deployment/customer-data change, CI activation, n8n, release
- UI/interface expectation: CLI with explicit subcommands and deterministic report outputs
- backend/data expectation: local JSON/Markdown report generation only
- verification rule: all required fields present and all required reports generated after command route
- validation rule: command sequence create-build-cards, run-task, verify-build executes successfully
- rollback expectation: remove generated dry-run artifacts and hold gate if verification fails
