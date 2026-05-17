# BUILD CARD

- build card ID: BC-SAMPLE-APP-0001
- app name: sample-app
- module: 01-app-build-line
- objective: produce minimum viable execution-cell artifacts for controlled app-build routing
- scope in: files under software-build-control/01-app-build-line and script under software-build-control/scripts/app_build_line
- scope out: app repositories, infra/deployment, database/security policies, external CI and release flows
- files allowed: software-build-control/01-app-build-line/**, software-build-control/scripts/app_build_line/app_build_line.py
- files prohibited: app repo code, Supabase/RLS, edge functions, deployment configs, customer data
- task steps: scaffold structure; create packet templates; run CLI route; generate reports; verify gate
- evidence required: generated reports + command logs
- verification method: verify-build subcommand checks required artifacts and protected-scope assertions
- stop condition: missing required fields/reports or protected-scope breach
- gate decision: PASS_WITH_WARNINGS for dry-run MVP with shallow scanner depth when all checks pass
