# AGENT TASK PACKET

- assigned agent/workstation: codex-runtime-workstation
- required specialist: build-control integrator
- required WI: local execution guard + SBC-JC-0006U instruction set
- tool route: python app_build_line.py create-build-cards -> run-task -> verify-build
- coding boundary: software-build-control/01-app-build-line and software-build-control/scripts/app_build_line only
- prohibited actions: app repo edits, Supabase/RLS/deployment/customer data changes, CI activation, n8n, auto-fix/merge, release
- output expected: build-card-output.json, agent-task-packet.json, build-verification-report.json/.md, gate-decision.json
- verification evidence required: successful command execution and generated report presence/content
